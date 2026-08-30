# STRUCTURE.md

Static, client-side personal site for Ayyazul Hassan. No backend. Currently in
the **visual-language design phase** — no application code exists yet, only
docs and throwaway HTML mockups.

## State

Branch `build/editable-site`. The site is one file, `index.html`, which carries
its own content editor: Ayyaz writes into the page and it persists to the
browser, with export/import to move the writing off one machine. The design
fragments are frozen and kept only for reference (and are viewable from the
archive section at the bottom of `index.html`). The v0 output from an earlier
tool was rejected wholesale and is retained only as a counter-example.

## Filemap

| Path | Role |
|---|---|
| `CLAUDE.md` | Project instructions for Claude: goal, engineering practices (Ousterhout), git workflow, and a pointer to the locked visual language. |
| `DESIGN.md` | The locked visual system — ground, type roles, colour rules, depth convention, copy policy, honesty grammar. Authoritative for anything visual. |
| `FEATURES.md` | Ayyaz's own brief: background, hiring thesis, required features, style references. The source of intent; not edited by Claude. |
| `STRUCTURE.md` | This file. Architecture summary and filemap. |
| `content.js` | The words, links and framed pictures that **ship** with the page, as `window.SITE_CONTENT`. The editor writes to the browser, which no visitor has; the drawer's *Publish copy* button rewrites this file, and committing it is what publishes a draft. A script rather than JSON because a page opened from the filesystem cannot `fetch()` a sibling. |
| `index.html` | **The site**, and the instrument that writes it. A served page is the finished thing - no desk, no placeholder brief, no working files, and the browsers draft is not read at all, so a visitor sees exactly what `content.js` ships. The editor appears when the page is opened off the disk, from localhost, or with `#edit` on the URL. One file: fold with the left-rail demo slot, pitch, work grid (six panels, one two or three across so the slab is never gap-toothed; lids open at 65ms toward the viewer), calm pocket, contact, and a reference archive. Also the content editor - every prose block is an `.ed` element that wears placeholder grammar while empty, carries bold/italic/underline through storage behind a five-tag whitelist, and persists with links, resume and panel images to localStorage - layered over `content.js`, section by section, so the shipped copy shows through wherever the local draft is silent - with JSON export and import; a panel picture is stored whole and framed by a scale and an offset that the edit-mode stage lets you drag and zoom, so cropping stays reversible; addresses are typed beside the link they belong to, panels included, and the two type faces are custom-property tokens chosen from the desk - body is IBM Plex Mono, the face the empty placeholders already wore. The resume is downloaded under a name Ayyaz is asked for on upload, never the one it had on disk. Demo 01 runs here: the SO-100 chain, a damped-least-squares solver and a flat WebGL renderer of the URDF's own meshes, driven by the cursor. |
| `assets/so100-mesh.js` | Generated. The SO-100's thirteen visual meshes, welded and quantised, as one base64 payload on `window.SO100_MESH`. A script file rather than a binary because a page opened from the filesystem cannot `fetch()` a sibling. |
| `tools/edit-server.mjs` | The desk with a floor under it: serves the repo on `localhost:5173` (`node tools/edit-server.mjs`) and accepts one `PUT /content.js`, so Publish copy writes the file in place instead of downloading it. Loopback only, one writable path, and the body is checked for `window.SITE_CONTENT` before the file is replaced. Never deployed. |
| `tools/export_so100_mesh.py` | Builds the above from the robot repo's URDF and STLs. Run it again if the arm's geometry changes. |
| `mockups/fragment-06-demo01.html` | Five placements of the six Demo 01 boxes behind a cycler. Layout 2 (left rail) was chosen and is what `index.html` uses. |
| `mockups/fragment-05-poster.html` | Superseded by `index.html`. The mockup the layout came from. The arm demo as the fold, kraft ground, Bodoni masthead in ink, shared-contour work slab. This is the live direction. |
| `mockups/fragment-07-flaps.html` | Opening probe for the work panels. Lids swing out of the page toward the viewer, bound to whichever grid edge is nearest free (measured at runtime, so no arrangement is hardcoded); hover is an instant shade change rather than a movement. Five ways of opening behind a cycler, all of them sharp - no eased tail, since the tail is what reads as soft. Snap at 60ms is the chosen one and is now the file's default; its travel time stays on a slider (50-150ms) for re-judging. See DESIGN.md, *How a panel opens*. |
| `mockups/fragment-01-specimens.html` | Specimen sheet: ground candidates, pigments sampled from the gouache, masthead typeface comparison, button behaviours. How the palette and display face were chosen. |
| `mockups/fragment-04-devices.html` | Six spatial probes. Devices 04 (self-drawing load) and 06 (ambiguous depth) survived review; the rest were rejected for repainting the reference images. Kept as a record of what was ruled out. |
| `mockup.html` | Rejected v0 single-file mockup. Kept as a reference for what to avoid; not linked from anything. |
| `iterations/` | Rejected v0 exploratory fragments (`iter1-88.html` … `iter5-06.html`) plus an index. Superseded. |
| `iterations-clean/` | Rejected v0 second-round fragments (`iter1-editorial.html` … `iter5-plain.html`) plus an index. Superseded. |
| `Cool Pics/` | Reference artwork by other artists (Fomenko, a gouache concert scene, a one-line figure study, the *Der Mensch* plate). Git-ignored — not ours to redistribute. Drives the palette and register defined in DESIGN.md. |
| `.github/workflows/pages.yml` | Publishes the site on every push to `main`. Assembles `index.html`, `content.js` and `assets/` into the artifact rather than the whole checkout, because the repo also holds the design notes, the mockups and the mesh exporter and none of that is the site. Fails loudly if `content.js` is missing. |
| `.gitignore` | Excludes build output, environment files, and the reference artwork. |

## Not yet present

No `src/`, no bundler, no tests, no linter config. The only server anywhere is `tools/edit-server.mjs`, which is authoring furniture and not part of the site. Sound and mobile are
deliberately deferred, as is the camera half of Demo 01 - its controls are out of
the page entirely rather than sitting there disabled, and go back when there is
something behind them.

## Demo 01

Ported from `../RobotProjects/so100-mediapipe-control`, chiefly
`demo/follow_cursor.py`. That version drives a meshcat viewer from Python over a
websocket; the site has no backend, so the chain, the solver and the drawing all
live in `index.html`. The joint frames are the SO-100 URDF's own, and the forward
kinematics was checked against `Kinematics.tool_pose` at five poses spanning the
workspace (agreement under a micrometre). The geometry is the URDF's own visual
meshes, exported by `tools/export_so100_mesh.py`.

Drawing is raw WebGL, no library: what this needs from a 3D pipeline is a depth
buffer and one draw call per part. Shading is quantised to three steps of one
pigment rather than a gradient - the printed shells chalk, the servos chrome -
and the outline is the same geometry pushed along its normals and drawn
inside-out, which costs a second pass and no edge extraction. The ground plane
and the drop line sit on a 2D canvas under the arm, the target marker on one
over it.

Inverse kinematics is damped least squares on position only, warm-started from
the previous pose, with a restart that aims the pan joint at the target when a
descent stalls. What it aims is `GRASP`, the empty air between the two fingers
rather than the URDF's tool frame at the root of the fixed one, so the cursor
sits where a held block would sit. Unreachable targets
are never clamped: the marker turns red and the arm holds, because a hand leaving
the workspace is the normal case during teleoperation rather than a fault.

The marker is drawn only while the pointer is over the viewport. Otherwise the
last one drawn stays frozen against whichever edge the pointer left by and reads
as paint the canvas failed to wipe. The two 2D layers also clear in device
pixels with the transform reset, because the backing store is
`round(css * dpr)` and clearing under the dpr transform leaves the last
sub-pixel row uncleared at a fractional device ratio.

The three layers all frame the picture from `view.cx/cy`, the WebGL clip matrix
included. They did not always: the matrix used the middle of the canvas while
`project` frames a little low, so the arm was drawn about thirty pixels above the
marker, the drop line and the ground, and the arm appeared to aim past the cursor.

The gestures are: the cursor aims, holding the left button closes the hand, the
wheel turns the wrist, shift+wheel zooms, shift-drag orbits, and alt-drag slides
the cursor plane along the view direction. They are listed under the viewport in
the state panel rather than over the picture.
The viewport therefore keeps the wheel to itself; ctrl passes through so the
browser's own zoom still works over it. The wrist roll is commanded rather than
solved, which is free rather than a compromise: the grasp point sits almost on
the roll axis, so that joint's column in the Jacobian is near zero and the solver
was not using it.
