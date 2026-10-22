# Insert plan

The coarse division of the twelve boxes of height class 120 on levels L2 to
L5. Every dimension below comes from `design/rack.json` → `inserts`; every
price and product property cites `docs/sources.md`. Prices include 19 % VAT
and were read on 2026-10-21.

## System: NextGen Einsatzkästen x-100

aidB sells NextGen "Einsatzkästen" (insert boxes) 100 mm high in three
footprints, made for the Eurobox NextGen 400 × 300 × 120 ([aidB set 1/2][aidb-half],
[aidB set 1/4][aidb-quarter]):

| Insert   | Outer L × W × H    | Used here           | Status     |
| -------- | ------------------ | ------------------- | ---------- |
| 3613-100 | 365 × 133 × 100 mm | 2 per half box      | VERIFIED   |
| 1813-100 | 182 × 133 × 100 mm | 4 per quarter box   | VERIFIED   |
| 0906-100 | 91 × 67 × 100 mm   | not used            | SECONDARY  |

They fit only the NextGen 400 × 300 × 120 box. Two rows of 133 mm give
266 mm across the 300 side; one 3613 or two 1813 give 365 or 364 mm along the
400 side. The block of 266 × 365 mm (quarter: 266 × 364 mm) fills the inner top
of 265 × 365 mm within the box's ±5 mm tolerance (`DERIVED`).

**Height.** The 120 box has 115 mm inside; the 100 mm insert stays 15 mm below
the rim and leaves the 105 mm usable height of a stacked box free, so the box
above or the support angle does not touch it (`DERIVED`).

**Bought as sets.** Set 1/2 (EES43-01-100-04) holds 2 × 3613-100, set 1/4
(EES43-02-100-04) holds 4 × 1813-100. A single 1813-100 costs 3.25 €, so four
singles (13.00 €) cost more than the set (`DERIVED`).

## Layouts

Top view, the user's drawings. "Griff" is the handle; the handles are on the
short 300 sides, and the front handle faces the aisle. The two rows of
`rack.json` lie side by side across the 300 side; the cells of a row run along
the 400 side.

```
Set 1/2                                   Set 1/4
         +-------------------------------+          +---------------+---------------+
         |             3613              |          |     1813      |     1813      |
Griff -> +-------------------------------+ <- Griff +---------------+---------------+
         |             3613              |          |     1813      |     1813      |
         +-------------------------------+          +---------------+---------------+
```

| Layout  | Set             | Inserts      | Compartments | Price per box | Per compartment | Status   |
| ------- | --------------- | ------------ | ------------ | ------------- | --------------- | -------- |
| half    | EES43-01-100-04 | 2 × 3613-100 | 2            | 9.95 €        | 4.98 €          | VERIFIED |
| quarter | EES43-02-100-04 | 4 × 1813-100 | 4            | 12.49 €       | 3.12 €          | VERIFIED |

The prices per box are read on aidB's pages; the prices per compartment are
`DERIVED`.

## Mix for the twelve 120 boxes

Front view of levels L2 to L5 (`rack.json` → `inserts.boxes`). The division
runs from fine to coarse, top to bottom: the small compartments at eye and
hand height, the larger ones below, the undivided 220 boxes on L1.

```
           C1            C2            C3
      +-------------+-------------+-------------+
  L5  |   quarter   |   quarter   |   quarter   |
      +-------------+-------------+-------------+
  L4  |   quarter   |   quarter   |   quarter   |
      +-------------+-------------+-------------+
  L3  |   half      |   half      |   half      |
      +-------------+-------------+-------------+
  L2  |   half      |   half      |   half      |
      +-------------+-------------+-------------+
```

| Layout  | Boxes | Sets | Inserts       | Compartments |
| ------- | ----- | ---- | ------------- | ------------ |
| half    | 6     | 6    | 12 × 3613-100 | 12           |
| quarter | 6     | 6    | 24 × 1813-100 | 24           |
| Total   | 12    | 12   | 36            | 36           |

The count matches the parts `insert.set_half` (6) and `insert.set_quarter`
(6). Total: 6 × 9.95 + 6 × 12.49 = 59.70 + 74.94 = **134.64 € incl. 19 % VAT**
(`DERIVED`), in the aidB order with the boxes, which ships free
(`docs/prices.md`).

The three 220 boxes on L1 have no inserts.

## Handles

The end walls of two inserts stand right behind each handle opening. With the
handle geometry read from the product photos (opening 24 to 54 mm below the
rim, insert top 15 mm below the rim) the opening is blocked from inside, so the
handle is gripped from outside only. `UNVERIFIED` until a box is measured.

## ColorClips

One ColorClip set (2 rings, R200-00-xx-SET) per box, on both handles, one
colour per insert type (`rack.json` → `color_clips`): neighbouring cool hues,
lighter towards the top, so the colour says which insert a box holds. The
sRGB values are the median ring colour in aidB's photos and drive the model
(`UNVERIFIED`).

| Level | Boxes           | Colour      | Article        | sRGB      | Part              | Packs |
| ----- | --------------- | ----------- | -------------- | --------- | ----------------- | ----- |
| L5    | 120, set 1/4    | light green | R200-00-13-SET | `#B7E686` | `clip.lightgreen` | 3     |
| L4    | 120, set 1/4    | light green | R200-00-13-SET | `#B7E686` | `clip.lightgreen` | 3     |
| L3    | 120, set 1/2    | turquoise   | R200-00-12-SET | `#00A8A8` | `clip.turquoise`  | 3     |
| L2    | 120, set 1/2    | turquoise   | R200-00-12-SET | `#00A8A8` | `clip.turquoise`  | 3     |
| L1    | 220, no inserts | blue        | R200-00-02-SET | `#055FE9` | `clip.blue`       | 3     |

## What goes where

**Suggestion only.** Brick Architect's LEGO Storage Guide advises sorting by
category rather than by colour, starting with broad groups such as bricks,
plates and "other" and splitting a category once it grows; shallow containers
make a part easier to find, and every drawer keeps an "everything else"
compartment for parts of which there are only a few
([Brick Architect, chapter 2][ba], [chapter 4][ba-medium]). The guide estimates
about 250 pieces per litre ([chapter 4][ba-medium]); a 1813 holds roughly
2.4 l and a 3613 roughly 4.8 l (`UNVERIFIED`, from the outer size), so a few
hundred and about a thousand parts.

| Compartment       | Where       | Suggested contents                                        |
| ----------------- | ----------- | --------------------------------------------------------- |
| 1813 (182 × 133)  | L5, L4      | small parts: 1 × n plates, tiles, 1 × 1 rounds, cheese    |
|                   |             | slopes, clips and bars, Technic pins, minifig accessories |
| 1813 (182 × 133)  | one per box | a category that is still small; "everything else"         |
| 3613 (365 × 133)  | L3          | bricks 1 × n and 2 × n, the categories with most parts    |
| 3613 (365 × 133)  | L2          | long parts: long plates, Technic beams and axles; wheels  |

Large plates and baseplates go into the 220 boxes without inserts.

[aidb-half]: https://www.ab-in-die-box.de/b2cde/einsatzkaesten-set-1-2-unterteilung-fuer-400x300x120.html
[aidb-quarter]: https://www.ab-in-die-box.de/b2cde/einsatzkaesten-set-1-4-unterteilung-fuer-400x300x120.html
[ba]: https://brickarchitect.com/guide/bricks/organization/
[ba-medium]: https://brickarchitect.com/guide/bricks/medium/
