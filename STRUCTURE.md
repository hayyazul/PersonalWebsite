# STRUCTURE.md

Static, client-side personal site for Ayyazul Hassan. No backend. Currently in
the **visual-language design phase** — no application code exists yet, only
docs and throwaway HTML mockups.

## State

Branch `design/visual-language`. Nothing is implemented. The v0 output from an
earlier tool was rejected wholesale and is retained only as a counter-example.

## Filemap

| Path | Role |
|---|---|
| `CLAUDE.md` | Project instructions for Claude: goal, engineering practices (Ousterhout), git workflow, and a pointer to the locked visual language. |
| `DESIGN.md` | The locked visual system — ground, type roles, colour rules, depth convention, copy policy, honesty grammar. Authoritative for anything visual. |
| `FEATURES.md` | Ayyaz's own brief: background, hiring thesis, required features, style references. The source of intent; not edited by Claude. |
| `STRUCTURE.md` | This file. Architecture summary and filemap. |
| `mockups/fragment-05-poster.html` | Current working mockup. The arm demo as the fold, kraft ground, Bodoni masthead in ink, shared-contour work slab. This is the live direction. |
| `mockups/fragment-07-flaps.html` | Opening probe for the work panels. Lids swing out of the page toward the viewer, bound to whichever grid edge is nearest free (measured at runtime, so no arrangement is hardcoded); hover is an instant shade change rather than a movement. Five ways of opening behind a cycler, all of them sharp - no eased tail, since the tail is what reads as soft. Snap at 60ms is the chosen one and is now the file's default; its travel time stays on a slider (50-150ms) for re-judging. See DESIGN.md, *How a panel opens*. |
| `mockups/fragment-01-specimens.html` | Specimen sheet: ground candidates, pigments sampled from the gouache, masthead typeface comparison, button behaviours. How the palette and display face were chosen. |
| `mockups/fragment-04-devices.html` | Six spatial probes. Devices 04 (self-drawing load) and 06 (ambiguous depth) survived review; the rest were rejected for repainting the reference images. Kept as a record of what was ruled out. |
| `mockup.html` | Rejected v0 single-file mockup. Kept as a reference for what to avoid; not linked from anything. |
| `iterations/` | Rejected v0 exploratory fragments (`iter1-88.html` … `iter5-06.html`) plus an index. Superseded. |
| `iterations-clean/` | Rejected v0 second-round fragments (`iter1-editorial.html` … `iter5-plain.html`) plus an index. Superseded. |
| `Cool Pics/` | Reference artwork by other artists (Fomenko, a gouache concert scene, a one-line figure study, the *Der Mensch* plate). Git-ignored — not ours to redistribute. Drives the palette and register defined in DESIGN.md. |
| `.gitignore` | Excludes build output, environment files, and the reference artwork. |

## Not yet present

No `src/`, no build tooling, no tests, no linter config. These arrive once the
visual language is settled and the first real module (the robot-arm demo) is
specified.
