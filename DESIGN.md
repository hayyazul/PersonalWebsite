# DESIGN.md — Visual language

Locked decisions only. If it is still being argued about, it is not in here.
Source of the whole system: `Cool Pics/file2.webp` (gouache, concert crowd) for
colour and outline logic; `Cool Pics/the-human-being...webp` (Der Mensch, engraved
plate) for the masthead register; the Fomenko for scale and grandness.

## Ground

`--kraft: #E9DCC0`. Not a milky cream. The rejected v0 used `#F7F1E6`, which
reads as tasteful and therefore as every AI-generated portfolio since 2024.

## Type

| Role | Face | Rule |
|---|---|---|
| Display | **Bodoni Moda** | Masthead, section titles, large numerals. Set in caps, letterspaced, engraved register. **Never body text, never UI labels, never small.** |
| Body / UI | TBD | Dense, workmanlike, high x-height. Must not be Inter. |
| Data / caption | TBD mono | Tense chips, coordinates, readouts. |

Bodoni Moda is the exemplar of the intended register: brutal thick/thin
contrast, hairline serifs, loud. Its power comes from scarcity — used
everywhere it becomes wallpaper and stops meaning anything.

## Colour

Two rules, and they are what let the palette be large:

1. **Every colour field is outlined in `--ink` (#17120F).** The outline is what
   keeps many saturated hues from turning to mud. This is how the gouache does it.
2. **Flat fills only.** No gradients, no blur, no opacity-blending between hues.
   A colour is either there or it is not.

Consequence: the palette can be wide without becoming noise, which is the whole
argument against minimalism here. There is **no grey** in the source painting.
Shadow is plum, not grey.

## Type on colour

Every colour field carries white type (`--chalk #F8F4EC`). A pigment that
cannot hold white is not used as a field — it stays a button or a tab. The six
field pigments are oxblood, ultramarine, bottle, plum, violet, olive; all clear
7:1 against chalk. Bright pigments (vermillion, chrome, orange, rose, sap) take
ink type and appear as whole sections or controls, never as card grounds.

## Placeholders

Anything not built yet is a **solid black rectangle** with a small tag, never a
sketch or a simulation of the finished thing. A drawing of a demo is a claim
that the demo exists.

## Depth

Two conventions, and they do different jobs.

**Controls press.** Buttons carry a hard offset shadow in ink, blur radius `0`,
light from the upper-left so the offset falls down-right. Pressing collapses the
offset to zero and the object sinks into the page. Nothing else uses this.

**The work panels are the same control at panel scale.** Same ink rule, same
offset, same press. They are objects you push, not tiles you read — a press that
lands swings the panel open on its hinge and the offset collapses to zero.

Rejected: creased-sheet geometry, mitred extrusions, per-tile bevels, gradient
falloff along a fold. Every one of them made the grid into a separate visual
system from the buttons. There is one depth convention on this site.

No blurred shadows, no glassmorphism, no depth animated on scroll.

## Copy

Body copy is written by Ayyaz, not by Claude. Mockups carry bracket
placeholders stating what the text must do, why, and roughly how:

```
[HEADLINE — what it must accomplish, for whom, constraint on length/tone]
```

## The references are not source images

**Nothing from `Cool Pics/` may appear on the site, redrawn or otherwise.** The
references contribute *behaviour*, not pictures. A radiating fan of wedges, a
gas mask, a coil, a lounging figure — all forbidden. What transfers is what the
plates *do*:

- Fomenko: formal rigour plus semantic mystery. One element enormous, exact,
  and unlabelled. Extreme scale gap. Nothing is explained to you.
- *Der Mensch*: the tool is rendered more carefully than the self-description.
  Detail that resolves on attention rather than announcing itself.
- The wine man: one unhesitating line. Economy, wit, ease. Nothing labelled.

All three reduce to the same instruction: **do not explain yourself.** Which is
the same rule as "never state the philosophy", arrived at from the other side.

## The figure

The site's posture is the wine man: legs crossed, drink up, entirely at ease
with the device in hand. Not striving, not performing, not small. Confidence
expressed as economy rather than as volume.

## Honesty grammar

Every claim on the site carries its tense: `DID` / `BUILDING` / `WANT TO`.
The site states no philosophy. It enacts it. Nothing on the page may print the
words "New Sincerity", "Gestalt", or name a design influence.
