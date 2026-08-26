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

**The work grid is flat.** Borders collapse inside the slab — the grid owns top
and left, each panel owns right and bottom — so no panel owns its own edges. It
sits *on* the page, with no offset beneath it. The letterpress offset belongs to
controls: buttons, and nothing the size of a section.

Rejected: per-panel shadows with gaps between the panels; creased-sheet
geometry; mitred extrusions; per-tile bevels; gradient falloff along a fold.

No blurred shadows, no glassmorphism, no depth animated on scroll.

## No corner tabs

**Never put a mark in the corner of a panel.** No dog-ear, no folded-page
triangle, no wedge, no ribbon, no notch, no badge — nothing whose job is to sit
in a corner and hint that a thing is interactive.

This was tried once, as a small ink triangle in each work panel's bottom corner
meaning "this opens". It was wrong on its own and it kept poisoning everything
built afterwards. A corner is where a panel meets two neighbours and, on a
folded surface, where its geometry is doing the most work; anything parked there
competes with that geometry and loses. Worse, it *reads* as geometry — every
later depth experiment had its corners misread as voids, holes, or artifacts,
and the diagnosis went to the fold each time when the tab was the problem.

If a panel needs to advertise that it opens, the panel does it: the hinge spine
on its bound edge, the way it behaves under the cursor, its interior. Not a
sticker in the corner.

## How a panel opens

**Outward, toward the viewer.** A lid swings out of the page, never back into
it. Into the page is the motion every SaaS card accordion makes and it reads as
one.

**The bound edge is measured, never assigned.** Each panel counts the panels
between it and each of the four grid edges and hinges on the nearest one, so it
opens into the space outside the grid rather than over a neighbour. Ties go
horizontal, because the grid is always wider than it is tall. No arrangement is
enumerated anywhere: three-across, two-across, and anything a column auto-fit
invents are all the same rule. A hinge spine sits on whichever edge that turned
out to be, and the revealed panel pads that edge so the standing lid never
crosses its text.

**The cursor changes the shade, not the position.** Hovering a shut panel
switches its field to a lighter pigment — a flat colour mixed before paint, not
the pigment blended with what sits behind it — with **no transition**. It lands
the instant the cursor arrives. Nothing moves, tilts, or goes ajar under the
cursor; movement is what a click is for.

**The swing is 60ms, linear, and has no tail.** A lid that spends its last few
degrees drifting into the stop reads as soft, and softness here reads as
corporate. At 60ms the swing is continuous but has almost no in-between: the
panel is shut, and then it is open. The peak stays under 90° so a lid never
shows the viewer its own back, and the focal length is long enough (2000px)
that a lid never splays far enough to lay a sliver over a neighbouring row —
that sliver gets read as a rendering artifact, the same failure as a corner tab.

**What is underneath arrives.** The revealed panel's contents come in just
behind the lid rather than sitting there pre-composed, on a delay derived from
the swing rather than a timing of their own.

Rejected: the eased tail; overswing that carries past and settles; a lift off
the slab before pivoting; a pause between unlatching and swinging; stepped
detents. All of them are legible as *technique*, which is the failure mode.

Under `prefers-reduced-motion`, panels do not flap at all.

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
