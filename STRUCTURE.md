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
| `mockup.html` | Rejected v0 single-file mockup. Kept as a reference for what to avoid; not linked from anything. |
| `iterations/` | Rejected v0 exploratory fragments (`iter1-88.html` … `iter5-06.html`) plus an index. Superseded. |
| `iterations-clean/` | Rejected v0 second-round fragments (`iter1-editorial.html` … `iter5-plain.html`) plus an index. Superseded. |
| `Cool Pics/` | Reference artwork by other artists (Fomenko, a gouache concert scene, a one-line figure study, the *Der Mensch* plate). Git-ignored — not ours to redistribute. Drives the palette and register defined in DESIGN.md. |
| `.gitignore` | Excludes build output, environment files, and the reference artwork. |

## Not yet present

No `src/`, no build tooling, no tests, no linter config. These arrive once the
visual language is settled and the first real module (the robot-arm demo) is
specified.
