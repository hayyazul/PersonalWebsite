"""Turn the SO-100 URDF's visual meshes into something a web page can draw.

The arm's geometry lives in the robot repo as thirteen binary STLs, one per
visual, in triangle-soup form: every triangle carries its own three vertices,
so a flat face of two hundred triangles stores six hundred copies of the same
few corners. That is the right format for a printer and the wrong one for a
browser, where it is the number of vertices pushed per frame that costs.

So each visual is welded on (position, normal) rather than position alone.
Welding on position would average the normals at a hard edge and round off
exactly the machined corners that make the part legible when it is drawn flat;
welding on the pair keeps every crease and still collapses the interiors of
flat faces, which is where the duplication actually is.

Positions are quantised to int16 across one bounding box for the whole model
and normals to int8, because a millimetre of positional error is invisible at
the size this is drawn and the alternative is four bytes a channel.

Output is a JavaScript file rather than a binary one on purpose: a page opened
from the filesystem cannot fetch() a sibling file, but it can always load a
script tag.
"""

from __future__ import annotations

import base64
import json
import struct
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import numpy as np

# Which material the URDF names for a visual decides how it is drawn: the
# printed shells are the body, the servos are the joints.
MATERIAL_ROLE = {"3d_printed": "body", "sts3215": "motor"}


def read_binary_stl(path: Path) -> tuple[np.ndarray, np.ndarray]:
    raw = path.read_bytes()
    count = struct.unpack("<I", raw[80:84])[0]
    if len(raw) < 84 + 50 * count:
        raise ValueError(f"{path.name}: header claims {count} triangles, file is too short")
    block = np.frombuffer(raw, dtype=np.uint8, count=50 * count, offset=84).reshape(count, 50)
    floats = block[:, :48].copy().view("<f4").reshape(count, 4, 3)
    normals = np.repeat(floats[:, 0, :], 3, axis=0)
    positions = floats[:, 1:, :].reshape(count * 3, 3)
    return positions.astype(np.float64), normals.astype(np.float64)


SMOOTH_LIMIT = np.cos(np.deg2rad(40.0))


def weld(positions: np.ndarray, normals: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Collapse triangle soup to indexed vertices, keeping the creases.

    Welding on position alone would average the normals across a machined edge
    and round it off; welding on (position, normal) barely collapses anything,
    because an STL gives every face its own normal and so no two faces agree.
    What works is the middle: average the normals at each position, then let a
    corner keep the face's own normal wherever the two disagree by more than
    forty degrees. Flat and gently curved regions merge, edges stay edges.
    """
    # 1e-6 m is a thousandth of the smallest feature on the arm, so rounding
    # here only merges corners that were meant to be the same corner.
    unique_positions, inverse = np.unique(np.round(positions, 6), axis=0, return_inverse=True)
    corners = inverse.reshape(-1, 3)

    face_normals = normals.reshape(-1, 3, 3)[:, 0, :]
    edge_a = positions.reshape(-1, 3, 3)[:, 1, :] - positions.reshape(-1, 3, 3)[:, 0, :]
    edge_b = positions.reshape(-1, 3, 3)[:, 2, :] - positions.reshape(-1, 3, 3)[:, 0, :]
    # Area weighting, so a sliver does not pull the average as hard as a face.
    areas = 0.5 * np.linalg.norm(np.cross(edge_a, edge_b), axis=1)
    face_normals = _unit_rows(face_normals)

    averaged = np.zeros_like(unique_positions)
    for corner in range(3):
        np.add.at(averaged, corners[:, corner], face_normals * areas[:, None])
    averaged = _unit_rows(averaged)

    per_corner = np.repeat(face_normals, 3, axis=0)
    smooth = np.repeat(averaged[corners].reshape(-1, 3, 3)[:, 0, :] * 0, 1, axis=0)
    smooth = averaged[corners.reshape(-1)]
    agrees = np.sum(smooth * per_corner, axis=1) >= SMOOTH_LIMIT
    chosen = np.where(agrees[:, None], smooth, per_corner)

    key = np.hstack([corners.reshape(-1, 1).astype(np.float64), np.round(chosen, 3)])
    _, first, index = np.unique(key, axis=0, return_index=True, return_inverse=True)
    return positions[first], chosen[first], index.astype(np.uint32)


def _unit_rows(vectors: np.ndarray) -> np.ndarray:
    lengths = np.linalg.norm(vectors, axis=1, keepdims=True)
    return np.divide(vectors, lengths, out=np.zeros_like(vectors), where=lengths > 1e-12)


def main() -> int:
    root_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "../RobotProjects/so100-mediapipe-control"
    )
    urdf_path = root_dir / "models" / "so100.urdf"
    urdf = ET.parse(urdf_path).getroot()

    parts: list[dict] = []
    chunks: list[tuple[np.ndarray, np.ndarray, np.ndarray]] = []
    for link in urdf.findall("link"):
        for visual in link.findall("visual"):
            mesh = visual.find("geometry/mesh")
            material = visual.find("material")
            if mesh is None or material is None:
                continue
            role = MATERIAL_ROLE.get(material.get("name", ""))
            if role is None:
                raise ValueError(f"unknown material {material.get('name')!r} on {link.get('name')}")
            stl = (urdf_path.parent / mesh.get("filename")).resolve()
            positions, normals = read_binary_stl(stl)
            v, n, idx = weld(positions, normals)
            parts.append(
                {
                    "link": link.get("name"),
                    "role": role,
                    "verts": int(len(v)),
                    "tris": int(len(idx) // 3),
                    "source": stl.name,
                }
            )
            chunks.append((v, n, idx))

    every_vertex = np.vstack([c[0] for c in chunks])
    low = every_vertex.min(axis=0)
    high = every_vertex.max(axis=0)
    span = np.maximum(high - low, 1e-9)

    position_bytes, normal_bytes, index_bytes = bytearray(), bytearray(), bytearray()
    for part, (v, n, idx) in zip(parts, chunks, strict=True):
        quantised = np.clip(np.rint((v - low) / span * 65535.0), 0, 65535).astype("<u2")
        position_bytes += quantised.tobytes()
        normal_bytes += np.clip(np.rint(n * 127.0), -127, 127).astype("<i1").tobytes()
        # Indices are per part, so each part's own vertex count decides the width.
        part["wide"] = bool(part["verts"] > 65535)
        index_bytes += idx.astype("<u4" if part["wide"] else "<u2").tobytes()

    payload = bytes(position_bytes) + bytes(normal_bytes) + bytes(index_bytes)
    header = {
        "low": low.tolist(),
        "span": span.tolist(),
        "positionBytes": len(position_bytes),
        "normalBytes": len(normal_bytes),
        "parts": parts,
    }
    out = Path("assets/so100-mesh.js")
    out.parent.mkdir(exist_ok=True)
    out.write_text(
        "/* Generated by tools/export_so100_mesh.py from the SO-100 URDF. Do not edit. */\n"
        f"window.SO100_MESH={json.dumps(header, separators=(',', ':'))};\n"
        f'window.SO100_MESH.data="{base64.b64encode(payload).decode()}";\n'
    )

    triangles = sum(p["tris"] for p in parts)
    vertices = sum(p["verts"] for p in parts)
    raw = sum((p["tris"] * 3) for p in parts)
    print(f"{len(parts)} visuals  {triangles} triangles")
    print(f"vertices {raw} soup -> {vertices} welded ({100 * vertices / raw:.1f}%)")
    print(f"{out}  {out.stat().st_size / 1024:.0f} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
