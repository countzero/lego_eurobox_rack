# Insert plan

The coarse division of the six boxes of height class 120 on levels 3 and 4.
Every dimension below comes from `design/rack.json` → `inserts`; every price
and product property cites `docs/sources.md`. Prices were read on 2026-10-20.

## System: Auer EK x/100

Auer's „Einsatzkasten“ (insert box) EK x/100 is 100 mm high and comes in three
footprints that tile the floor of a 600 × 400 box:

| Insert    | Outer L × W × H     | Per box | Net, single | Incl. 19 % VAT | Status   |
| --------- | ------------------- | ------- | ----------- | -------------- | -------- |
| EK 2/100  | 563 × 183 × 100 mm  | 2       | 7.49 €      | 8.91 €         | VERIFIED |
| EK 4/100  | 282 × 183 × 100 mm  | 4       | 4.47 €      | 5.32 €         | VERIFIED |
| EK 8/100  | 141 × 183 × 100 mm  | 8       | 3.31 €      | 3.94 €         | VERIFIED |

Sizes and net prices are from Auer's own shop ([Auer EK AT][auer-ek],
[Auer EK DE][auer-ek-de]); the gross prices are `DERIVED` (net × 1.19). Both
the Austrian and the German page now show the same net single-piece prices and
both say „Alle Preise zzgl. MwSt.“ (all prices plus VAT). An earlier reading
of the two pages differed; this plan uses the German net price with 19 % VAT.
Pallet prices (EK 2/100 5.00 €, EK 4/100 2.98 €, EK 8/100 2.21 € net) need
220 to 880 pieces and do not apply. Freight is free from 250 € net.

**Why EK.** Two rows of 183 mm give 366 mm across; four EK 8 (4 × 141), two
EK 4 (2 × 282) or one EK 2 (563 mm) give 563–564 mm along. The tile of
564 × 366 mm fills the box with no filler pieces (`DERIVED`). Auer states that
"a Eurobox of 60 × 40 cm base holds up to eight inserts" ([Auer EK][auer-ek]).
By contrast, aidB's insert sets for the NextGen 120 box are a 566 × 366 mm
block that needs 8 filler boxes of 34 × 46 mm in the middle
([aidB set][aidb-set]).

**Heights.** The 120 box has 115 mm inside: the EK x/100 (100 mm) and the
EK x/50 (50 mm) fit under the rim; the EK x/150 (150 mm) does not (`DERIVED`
from the inner height). The 100 mm insert leaves the 103–105 mm usable height
of a stacked box free, so a box above or the support angle does not touch it.

**Confirmed for which box:**

| Box                       | Inner L × W (top) | EK fit                                     | Status     |
| ------------------------- | ----------------- | ------------------------------------------ | ---------- |
| Auer EG 64/12 HG          | 570 × 370 mm      | confirmed by Auer: up to 8 per 60 × 40 box | VERIFIED   |
| aidB NextGen 2.0 N2G64-12 | 565 × 365 mm      | very likely, not confirmed                 | UNVERIFIED |

The NextGen box is 1 mm narrower at the top than the 366 mm tile, inside its
± 5 mm tolerance; aidB's own block is 566 × 366 mm and fits, so EK most likely
fits too. Roadmap 0004 tries one EK 2/100 in a NextGen 120 box. Until then the
parts list buys Auer EG 64/12 HG for the 120 class (`box.e120`).

## Layouts

Top view, the handle side at the front (top of the drawing). The two rows of
`rack.json` lie side by side across the 400 mm width; row 1 is drawn on the
left. The cells of a row run from the front to the back along the 600 mm
length. Sizes are the outer sizes of the inserts; the inner sizes are a few
millimetres smaller and are not published.

### eight: 8 compartments

```
                      FRONT (handle side)
          +--------------------+--------------------+
          |  EK 8  141 x 183   |  EK 8  141 x 183   |
          +--------------------+--------------------+
          |  EK 8  141 x 183   |  EK 8  141 x 183   |
          +--------------------+--------------------+
          |  EK 8  141 x 183   |  EK 8  141 x 183   |
          +--------------------+--------------------+
          |  EK 8  141 x 183   |  EK 8  141 x 183   |
          +--------------------+--------------------+
                            BACK
```

8 × EK 8/100: 26.48 € net, **31.51 €** incl. VAT (`DERIVED`).

### six: 6 compartments

```
                      FRONT (handle side)
          +--------------------+--------------------+
          |                    |  EK 8  141 x 183   |
          |  EK 4  282 x 183   +--------------------+
          |                    |  EK 8  141 x 183   |
          +--------------------+--------------------+
          |                    |  EK 8  141 x 183   |
          |  EK 4  282 x 183   +--------------------+
          |                    |  EK 8  141 x 183   |
          +--------------------+--------------------+
                            BACK
```

2 × EK 4/100 + 4 × EK 8/100: 22.18 € net, **26.39 €** incl. VAT (`DERIVED`).

### four: 4 compartments

```
                      FRONT (handle side)
          +--------------------+--------------------+
          |                    |                    |
          |  EK 4  282 x 183   |  EK 4  282 x 183   |
          |                    |                    |
          +--------------------+--------------------+
          |                    |                    |
          |  EK 4  282 x 183   |  EK 4  282 x 183   |
          |                    |                    |
          +--------------------+--------------------+
                            BACK
```

4 × EK 4/100: 17.88 € net, **21.28 €** incl. VAT (`DERIVED`).

### three: 3 compartments

```
                      FRONT (handle side)
          +--------------------+--------------------+
          |                    |                    |
          |                    |  EK 4  282 x 183   |
          |                    |                    |
          |  EK 2  563 x 183   +--------------------+
          |                    |                    |
          |                    |  EK 4  282 x 183   |
          |                    |                    |
          +--------------------+--------------------+
                            BACK
```

1 × EK 2/100 + 2 × EK 4/100: 16.43 € net, **19.55 €** incl. VAT (`DERIVED`).

## Mix for the six 120 boxes

Front view of the two top levels (`rack.json` → `inserts.boxes`):

```
           C1            C2            C3
      +-------------+-------------+-------------+
  L4  |   eight     |   eight     |   six       |
      +-------------+-------------+-------------+
  L3  |   six       |   four      |   three     |
      +-------------+-------------+-------------+
```

| Layout | Boxes | EK 2 | EK 4 | EK 8 | Compartments |
| ------ | ----- | ---- | ---- | ---- | ------------ |
| eight  | 2     | 0    | 0    | 16   | 16           |
| six    | 2     | 0    | 4    | 8    | 12           |
| four   | 1     | 0    | 4    | 0    | 4            |
| three  | 1     | 1    | 2    | 0    | 3            |
| Total  | 6     | 1    | 10   | 24   | 35           |

The count matches the parts `insert.ek2` (1), `insert.ek4` (10) and
`insert.ek8` (24). Total: 1 × 7.49 + 10 × 4.47 + 24 × 3.31 = **131.63 € net,
156.64 € incl. 19 % VAT** (`DERIVED`), below the 250 € net of free freight, so
Auer's freight comes on top (not read).

## What goes where

**Suggestion only.** Brick Architect's LEGO Storage Guide advises sorting by
category rather than by colour, starting with broad groups such as bricks,
plates and "other" and splitting a category once it grows; shallow containers
make a part easier to find, and every drawer keeps an "everything else"
compartment for parts of which there are only a few
([Brick Architect, chapter 2][ba], [chapter 4][ba-medium]). The guide estimates
about 250 pieces per litre ([chapter 4][ba-medium]); an EK 8 holds roughly
2.5 l (`UNVERIFIED`, from the outer size), so a few hundred parts.

| Compartment       | Where             | Suggested contents                                        |
| ----------------- | ----------------- | --------------------------------------------------------- |
| EK 8 (141 × 183)  | L4.C1, L4.C2      | small parts: 1 × n plates, tiles, 1 × 1 rounds, cheese    |
|                   |                   | slopes, clips and bars, Technic pins, minifig accessories |
| EK 8 (141 × 183)  | L4.C3, L3.C1 back | a category that is still small; "everything else"         |
| EK 4 (282 × 183)  | L4.C3, L3.C1      | 2 × n plates, slopes, Technic beams up to 7 long          |
| EK 4 (282 × 183)  | L3.C2             | bricks 1 × n and 2 × n, the categories with most parts    |
| EK 2 (563 × 183)  | L3.C3             | long parts: long plates, Technic beams and axles          |
| EK 4 (282 × 183)  | L3.C3             | wheels and tyres, windows and doors                       |

Large plates and baseplates go into the 220 boxes without inserts.

## Fallback for NextGen boxes

If roadmap 0004 shows that EK does not fit a NextGen 120 box, slot-together
„Trennwände“ (divider walls) of HPS (high-impact polystyrene) divide the box
instead. TBA Plastové obaly sells them for the 60 × 40 × 12 box: 562 × 3 ×
100 mm long and 370 × 3 × 100 mm short, with pre-cut slots; a division needs
at least one long and one short wall ([TBA wall][tba-wall]). The long wall
costs 3.45 € net, 4.17 € incl. VAT. The short wall of 370 mm is wider than the
365 mm inner top width of NextGen; whether it fits the tapering wall at
100 mm height is open (`UNVERIFIED`), and a wall can be cut shorter. The walls
leave open slots at their crossings, so small parts can creep between
compartments.

[auer-ek]: https://www.auer-packaging.com/at/de/Einsatzk%C3%A4sten-f%C3%BCr-Eurobeh%C3%A4lter.html
[auer-ek-de]: https://www.auer-packaging.com/de/de/Einsatzk%C3%A4sten-f%C3%BCr-Eurobeh%C3%A4lter.html
[aidb-set]: https://www.ab-in-die-box.de/b2bde/einsatzkaesten-set-1-4-unterteilung-fuer-600x400x120.html
[ba]: https://brickarchitect.com/guide/bricks/organization/
[ba-medium]: https://brickarchitect.com/guide/bricks/medium/
[tba-wall]: https://www.tbaplast.de/trennwand-fur-eurobehalter-60x40x12-cm--lang
