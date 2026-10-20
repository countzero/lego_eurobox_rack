# Design

Read when changing the rack. Every number here is a copy of
`design/rack.json`, which wins where the two differ. The values are provisional
until the boxes are measured (roadmap 0004).

## Decisions

| Decision                                 | Reason                                                                                                         | Source                                       |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| 3 columns, 4 levels, short side to front | The user's layout: two levels of 220 mm boxes, two of 120 mm boxes, drawer style                               | the user                                     |
| Boxes stand on their floor, not the rim  | Floor support takes Auer, RAKO and NextGen; the one rim-hanging drawer found excludes Auer                     | `sources.md` → *Racks that take every brand* |
| 416 mm between the uprights              | 410 mm between the hanging legs, as Gruber (409) and profilzuschnitt24 (410) use                               | `sources.md` → *Racks that take every brand* |
| Angles 50 × 50 × 3, flat leg on top      | One angle carries the box above, guides the rim of the box below sideways and stops it tipping when pulled out | `DERIVED` below                              |
| Levels set for the tallest box per class | 233 mm for the 220 class (NextGen 228 + 5), 125 mm for the 120 class, 8 mm gap above                           | `sources.md` → *Boxes*                       |
| No slides, no pull-out stop              | The user's choice; a box comes out like from an open shelf                                                     | the user                                     |
| A castor under every upright             | The load goes straight down; no beam bends between castors                                                     | `DERIVED`                                    |
| Back panel as the back stop              | The boxes need a stop, and the panel also keeps the frame from racking                                         | `DERIVED`                                    |
| Top plate planned, not built             | The top frame stays open; brackets swing in later without taking the frame apart                               | `sources.md` → *Top plate*                   |
| 120 class boxes from Auer                | Auer confirms its EK inserts for its own boxes; in NextGen boxes the fit is unconfirmed                        | `sources.md` → *Inserts*                     |

## Box envelope

The rack must take every box inside this envelope. No maker publishes the foot
width, the rim overhang or the taper, so the foot width is derived from the
narrowest published floor (Utz RAKO, 352–358 mm inner at the floor, plus the
wall).

| Value             | Min | Max | Status     |
| ----------------- | --- | --- | ---------- |
| Rim width         | 396 | 405 | DERIVED    |
| Rim length        | 594 | 605 | DERIVED    |
| Foot width        | 356 |     | UNVERIFIED |
| Height, 120 class |     | 125 | DERIVED    |
| Height, 220 class |     | 233 | DERIVED    |

Wibo and keeeper boxes are excluded: they have no continuous bottom edge to
stand on.

### Fit check

| Check                                   | Value                                | Result                          |
| --------------------------------------- | ------------------------------------ | ------------------------------- |
| Widest rim between the hanging legs     | 405 in 410                           | 2.5 mm play per side            |
| Narrowest rim sideways travel           | (410 − 396) / 2                      | 7 mm                            |
| Foot on each leg, box centred           | (356 − 316) / 2                      | 20 mm                           |
| Foot on each leg, box fully to one side | 20 − 7                               | 13 mm                           |
| Gap above the tallest box, every level  | next flat leg bottom − (floor + max) | 8 mm                            |
| Gap above an Auer 220 in a 220 level    | 8 + 233 − 220                        | 21 mm; the tip guard acts later |
| Box length in the depth                 | 605 in 610 − 5 front margin          | fits; the back panel stops it   |

## Dimensions

| Item                         | Value                       |
| ---------------------------- | --------------------------- |
| Frame width × depth × height | 1368 × 610 × 923            |
| Outer with panels            | 1374 × 613 × 923            |
| Clear width per column       | 416 between uprights        |
| Upright length               | 823 (100 to 923)            |
| Castor height                | 100                         |
| Top plate (planned)          | 1414 × 653 × 18, top at 941 |

| Level | Class | Floor (flat leg top) | Tallest box top | Next flat leg bottom | Angle           |
| ----- | ----- | -------------------- | --------------- | -------------------- | --------------- |
| 1     | 220   | 133                  | 366             | 374                  | `angle.base`    |
| 2     | 220   | 377                  | 610             | 618                  | `angle.support` |
| 3     | 120   | 621                  | 746             | 754                  | `angle.support` |
| 4     | 120   | 757                  | 882             | 890                  | `angle.support` |
| guard |       |                      |                 |                      | `angle.guard`   |

### Front view

```
        |<------------------------------ 1368 frame ------------------------------->|
  923 - ++=======================++=======================++=======================++   top frame, open
  890 - ||#####             #####||#####             #####||#####             #####||   angle.guard
        ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
        ||  | 120 + inserts   |  ||  | 120 + inserts   |  ||  | 120 + inserts   |  ||   L4
  757 - ||##+-----------------+##||##+-----------------+##||##+-----------------+##||   angle.support
        ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
        ||  | 120 + inserts   |  ||  | 120 + inserts   |  ||  | 120 + inserts   |  ||   L3
  621 - ||##+-----------------+##||##+-----------------+##||##+-----------------+##||   angle.support
        ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
        ||  |     220 / 228   |  ||  |     220 / 228   |  ||  |     220 / 228   |  ||   L2
        ||  |                 |  ||  |                 |  ||  |                 |  ||
  377 - ||##+-----------------+##||##+-----------------+##||##+-----------------+##||   angle.support
        ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
        ||  |     220 / 228   |  ||  |     220 / 228   |  ||  |     220 / 228   |  ||   L1
        ||  |                 |  ||  |                 |  ||  |                 |  ||
  133 - ||L_+-----------------+_J||L_+-----------------+_J||L_+-----------------+_J||   angle.base
  100 - ++=======================++=======================++=======================++   bottom frame
       (O)                     (O)                     (O)                     (O)     castors (front 4 of 8)
    0 - =============================================================================
        30<----- 416 clear ----->30<----- 416 clear ----->30<----- 416 clear ----->30
```

### Side view from the left

```
         front                            back
        |<--------------- 613 --------------->|
  923 - +--+==============================+--+|   top depth beam (open top)
  890 - [====================================]|   angle.guard
        |  |                              |  ||
  757 - [====================================]|   L4  angle.support, 610 long
        |  |                              |  ||
  621 - [====================================]|   L3
        |  |                              |  ||
        |  |                              |  ||
  377 - [====================================]|   L2
        |  |                              |  ||
        |  |                              |  ||
  133 - [====================================]|   L1  angle.base
  100 - +--+==============================+--+|   bottom depth beam
        (O)                               (O)     castor, M8 into the upright
    0 - =======================================
        ^ boxes pull out here                 ^ panel.back = back stop
```

### One support angle

```
 upright   angle.support 50 x 50 x 3, flat leg on top
   ||
   ||#############      <- the box ABOVE stands on the 50 mm flat leg (UHMW tape)
   ||#
   ||#    8 mm gap      <- the box BELOW tips up into the flat leg: tip guard
   ||#  +----------     <- rim of the box BELOW
   ||#  |               <- the hanging leg keeps the rim within 410 mm
   ||#   \
   ||     \
```

The angles are fixed with countersunk M5 screws into T-nuts in the uprights'
inner slots, two per end, so the hanging leg stays smooth for the rim.

## Joints

| Joint                            | Count | Parts each                                                 |
| -------------------------------- | ----- | ---------------------------------------------------------- |
| Beam end to upright              | 40    | 1 `bracket.inside_30`, 2 `screw.m6x12_button`, 2 `tnut.m6` |
| Angle end to upright             | 60    | 2 `screw.m5x10_countersunk`, 2 `tnut.m5`                   |
| Panel to frame, every 150–200 mm | 60    | 1 `screw.m5x10_button`, 1 `tnut.m5`                        |
| Castor to upright                | 8     | 1 `screw.m8x25`, 1 `washer.m8_large`, M8 core thread       |

The 20 beams have 40 ends. The bracket sits under a bottom beam and over a top
beam, where it carries the load into the upright; the boxes load only the
angles, which bolt straight to the uprights.

## Contracts

The wave steps (roadmap 0003, 0005–0009) agree through these names. A step
that needs a change to a contract says so in its pull request instead of
making it.

### Part IDs

The part catalog is `parts` in `design/rack.json`. Every document, list and
price refers to a part by its `id`; `status` is `build` for what is bought now
and `planned` for the top plate and its fixings.

| ID                        | Category   | Quantity | Status  |
| ------------------------- | ---------- | -------- | ------- |
| `profile.upright`         | profile    | 8        | build   |
| `profile.beam_width`      | profile    | 12       | build   |
| `profile.beam_depth`      | profile    | 8        | build   |
| `angle.base`              | angle      | 6        | build   |
| `angle.support`           | angle      | 18       | build   |
| `angle.guard`             | angle      | 6        | build   |
| `bracket.inside_30`       | connector  | 40       | build   |
| `screw.m6x12_button`      | fastener   | 80       | build   |
| `tnut.m6`                 | fastener   | 80       | build   |
| `screw.m5x10_countersunk` | fastener   | 120      | build   |
| `screw.m5x10_button`      | fastener   | 60       | build   |
| `tnut.m5`                 | fastener   | 180      | build   |
| `castor.brake`            | castor     | 4        | build   |
| `castor.plain`            | castor     | 4        | build   |
| `screw.m8x25`             | fastener   | 8        | build   |
| `washer.m8_large`         | fastener   | 8        | build   |
| `panel.back`              | panel      | 1        | build   |
| `panel.side`              | panel      | 2        | build   |
| `tape.uhmw_25`            | consumable | 14640 mm | build   |
| `cap.end_30`              | finish     | 8        | build   |
| `cover.slot_8`            | finish     | 4696 mm  | build   |
| `box.e120`                | box        | 6        | build   |
| `box.e220`                | box        | 6        | build   |
| `insert.ek2`              | insert     | 1        | build   |
| `insert.ek4`              | insert     | 10       | build   |
| `insert.ek8`              | insert     | 24       | build   |
| `plate.top`               | plate      | 1        | planned |
| `bracket.plate`           | connector  | 10       | planned |
| `screw.wood_4_5x12`       | fastener   | 20       | planned |

### Parts and cut list files

`bom/parts.csv`, one row per part ID, in the order of the catalog:

```
id,category,description,material,length,width,quantity,unit,status
```

`bom/cutlist.csv`, one row per cut, grouped by stock bar:

```
material,bar,stock_length,part_id,cut_length,start
```

`bar` counts from 1 per material; `start` is the cut's offset on the bar,
kerf included. Lengths are millimetres, empty where they do not apply.

### Renders

PNG, 1600 × 1200, under `renders/`, top plate hidden:

| File                        | View                                                          |
| --------------------------- | ------------------------------------------------------------- |
| `renders/front.png`         | Orthographic, from the front                                  |
| `renders/side.png`          | Orthographic, from the left                                   |
| `renders/three_quarter.png` | Perspective, front left, slightly from above                  |
| `renders/drawer_out.png`    | Three-quarter, box `L3.C2` pulled out by `pull_out.travel`    |
| `renders/inserts_top.png`   | Orthographic from above, the six 120 boxes with their inserts |
| `renders/angle_detail.png`  | Close-up of one support angle with the boxes above and below  |

### Model objects and the web export

Blender works in metres (rack millimetres / 1000). `web/rack.glb` is a binary
glTF in metres, Y up, as Blender's exporter writes it: rack `x` stays glTF `x`,
rack `z` becomes glTF `y`, rack `y` becomes glTF `−z`. The boxes pull out
towards the front, rack `−y`, which is glTF `+z`.

| Node name                             | Holds                                           | glTF extras                                                                                                                                   |
| ------------------------------------- | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `frame`                               | uprights, beams, angles, castors                | `{ "kind": "frame" }`                                                                                                                         |
| `panel.back`                          | the back panel                                  | `{ "kind": "panel" }`                                                                                                                         |
| `panel.side.left`, `panel.side.right` | the side panels                                 | `{ "kind": "panel" }`                                                                                                                         |
| `box.L<level>.C<column>`              | one box and, as children, its inserts; 12 nodes | `{ "kind": "box", "level": 1–4, "column": 1–3, "class": "120" or "220", "model": "<box_models key>", "travel": 0.4, "pull_axis": [0, 0, 1] }` |
| `plate.top`                           | the planned top plate                           | `{ "kind": "plate", "status": "planned" }`                                                                                                    |

The scene's extras carry `{ "rack_schema": 1, "outer_mm": [1374, 613, 923] }`.
Columns count 1–3 from the left seen from the front, levels 1–4 from the
bottom. Moving a box node by `travel` along `pull_axis` pulls the box and its
inserts out together.

Material names: `aluminium`, `panel_white`, `box_grey`, `insert_grey`,
`castor`, `plywood`.
