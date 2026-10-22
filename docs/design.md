# Design

Read when changing the rack. Every number here is a copy of
`design/rack.json`, which wins where the two differ. The values are provisional
until the boxes are measured (roadmap 0004).

## Decisions

| Decision                                        | Reason                                                                                                                      | Source                                                      |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| 3 columns, 5 levels, short side to front        | The user's layout: one level of 220 mm boxes at the bottom, four levels of 120 mm boxes with inserts above, drawer style    | the user                                                    |
| Eurobox NextGen 2.0 Cycle 400 × 300, anthracite | One vendor (ab-in-die-BOX, aidB) for boxes, inserts and ColorClips; the short 300 side with the open handle faces the front | the user; `sources.md` → *Boxes*                            |
| Box envelope narrowed to 400 × 300              | The 600 × 400 design is gone; the user agreed that 600 × 400 boxes no longer fit                                            | the user                                                    |
| Boxes stand on their floor, not the rim         | Floor support takes every 400 × 300 box with a continuous bottom edge                                                       | `sources.md` → *Racks that take every brand*                |
| 316 mm between the uprights                     | 310 mm between the hanging legs: 2.5 mm play per side for a 305 mm rim                                                      | `DERIVED` below                                             |
| Angles 50 × 50 × 3, flat leg on top             | One angle carries the box above, guides the rim of the box below sideways and stops it tipping when pulled out              | `DERIVED` below                                             |
| Levels set for the tallest box per class        | 233 mm for the 220 class, 125 mm for the 120 class, 8 mm gap above                                                          | `sources.md` → *Boxes*                                      |
| No slides, no pull-out stop                     | The user's choice; a box comes out like from an open shelf                                                                  | the user                                                    |
| One 1068 mm bar front and back, top and bottom  | One piece over all three columns; the uprights stand between the bars on an M8 through-bolt into their core thread          | the user                                                    |
| Bottom bars 30 × 60                             | With castors only at the corners the middle uprights hang on the bottom bars; a 30 × 30 bar would sag about 4.7 mm          | `DERIVED` in *Loads*                                        |
| 4 castors at the corner uprights                | 125 mm, 100 kg each, brakes at the front; enough for the realistic load on three castors                                    | `sources.md` → *Frame additions*; *Loads*                   |
| No panels                                       | `bracket.stop` on the back uprights is the back stop; 16 joint plates on the front and back faces brace the frame           | the user                                                    |
| Top plate planned, not built                    | The top frame stays open; brackets swing in later without taking the frame apart                                            | `sources.md` → *Top plate*                                  |
| Inserts only in the 120 boxes                   | aidB NextGen insert sets made for 400 × 300 × 120; the 220 boxes stay open                                                  | `sources.md` → *Inserts*                                    |

## Box envelope

The rack must take every box inside this envelope: any 400 × 300 Eurobox with a
continuous bottom edge to stand on. No maker publishes the foot width, so it
is an estimate. 600 × 400 boxes, Wibo and keeeper / OKT Robusto are excluded.

| Value             | Min | Max | Status     |
| ----------------- | --- | --- | ---------- |
| Rim width         | 296 | 305 | DERIVED    |
| Rim length        | 394 | 405 | DERIVED    |
| Foot width        | 260 |     | UNVERIFIED |
| Height, 120 class |     | 125 | DERIVED    |
| Height, 220 class |     | 233 | DERIVED    |

### Fit check

| Check                                   | Value                                | Result                          |
| --------------------------------------- | ------------------------------------ | ------------------------------- |
| Widest rim between the hanging legs     | 305 in 310                           | 2.5 mm play per side            |
| Narrowest rim sideways travel           | (310 - 296) / 2                      | 7 mm                            |
| Foot on each leg, box centred           | (260 - 216) / 2                      | 22 mm                           |
| Foot on each leg, box fully to one side | 22 - 7                               | 15 mm                           |
| Gap above the tallest box, every level  | next flat leg bottom - (floor + max) | 8 mm                            |
| Gap above a 220 box in a 220 level      | 8 + 233 - 220                        | 21 mm; the tip guard acts later |
| Box length in the depth                 | 400 from y 5 to the stop at y 405    | fits; `bracket.stop` stops it   |

### Box shape in the model

The model draws the box from `box_shape` and `box_models` in
`design/rack.json`. aidB and Müller & Sohn publish no drawing or CAD, so the
values below were read from aidB's product photos by perspective measurement
and are `UNVERIFIED` until a box is measured (roadmap 0004); the inner floor is
`SECONDARY` or `DERIVED` as marked.

| Value                | Model value                                                         | Status     |
| -------------------- | ------------------------------------------------------------------- | ---------- |
| Rim band             | 6                                                                   | UNVERIFIED |
| Collar below the rim | 31                                                                  | UNVERIFIED |
| Ledge                | 5                                                                   | UNVERIFIED |
| Foot band            | 18                                                                  | UNVERIFIED |
| Side panel recess    | 3                                                                   | UNVERIFIED |
| Corner post          | 14                                                                  | UNVERIFIED |
| Outer corner radius  | 8                                                                   | UNVERIFIED |
| Inner corner radius  | 6                                                                   | UNVERIFIED |
| Inner floor, 120 box | 359 × 259; the wall tapers from the 365 × 265 inner top             | SECONDARY  |
| Inner floor, 220 box | 354 × 254, the same wall slope over 215                             | DERIVED    |
| Ribs per long side   | 88-110 and 290-312 from the front                                   | UNVERIFIED |
| Handle frame         | 145 × 50, corner radius 12, from 15 below the rim                   | UNVERIFIED |
| Handle opening       | 125 × 30, corner radius 8, from 24 below the rim                    | UNVERIFIED |
| ColorClip ring       | 145 × 50 × 2, radii 12 outside and 6 inside, round the opening      | UNVERIFIED |
| Colour               | about sRGB #3F3F3F lit in the photo; drawn at linear 0.04, IOR 1.49 | UNVERIFIED |

The inner floor of the 120 box is that of Bito XL43121 and Utz RAKO
400 × 300 × 120 (both 359 × 259); aidB's insert sets, 366 × 266 at the top and
4 smaller per side at the floor, need at least 358 × 258. aidB says the insert
sets fit only boxes of their own height "aufgrund der Konizität" (because of
the taper).

The published facts are `VERIFIED` (`sources.md` → *Boxes: aidB Eurobox
NextGen 2.0*): outer 400 × 300 × 120 / 220, inner 365 × 265 × 115 / 215,
11 l / 20 l, 800 g / 1180 g, r-PP, load 25 kg, ±5 mm.

## Dimensions

| Item                         | Value                                  |
| ---------------------------- | -------------------------------------- |
| Frame width × depth × height | 1068 × 435 × 1041                      |
| Outer with joint plates      | 1068 × 443 × 1041                      |
| Clear width per column       | 316 between uprights, 310 between legs |
| Upright length               | 791 (220 to 1011), x 0, 346, 692, 1038 |
| Bottom bar                   | 30 × 60, 1068 long, 160 to 220         |
| Top bar                      | 30 × 30, 1068 long, 1011 to 1041       |
| Depth beam                   | 375 long, 190 to 220 and 1011 to 1041  |
| Castor height                | 160                                    |
| Angle length                 | 435                                    |
| Pull-out travel, removal     | 270, 400                               |
| Top plate (planned)          | 1108 × 483 × 18, top at 1059           |

| Level | Class | Floor (flat leg top) | Tallest box top | Next flat leg bottom | Angle           |
| ----- | ----- | -------------------- | --------------- | -------------------- | --------------- |
| 1     | 220   | 223                  | 456             | 464                  | `angle.base`    |
| 2     | 120   | 467                  | 592             | 600                  | `angle.support` |
| 3     | 120   | 603                  | 728             | 736                  | `angle.support` |
| 4     | 120   | 739                  | 864             | 872                  | `angle.support` |
| 5     | 120   | 875                  | 1000            | 1008                 | `angle.support` |
| guard |       |                      |                 |                      | `angle.guard`   |

### Front view

```
         |<------------------------------ 1068 frame ------------------------------->|
  1041 - ++=======================================================================++
  1008 - ||#####             #####||#####             #####||#####             #####||
         ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
         ||  |    120, 1/4     |  ||  |    120, 1/4     |  ||  |    120, 1/4     |  ||   L5
   875 - ||##+-----------------+##||##+-----------------+##||##+-----------------+##||
         ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
         ||  |    120, 1/4     |  ||  |    120, 1/4     |  ||  |    120, 1/4     |  ||   L4
   739 - ||##+-----------------+##||##+-----------------+##||##+-----------------+##||
         ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
         ||  |    120, 1/2     |  ||  |    120, 1/2     |  ||  |    120, 1/2     |  ||   L3
   603 - ||##+-----------------+##||##+-----------------+##||##+-----------------+##||
         ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
         ||  |    120, 1/2     |  ||  |    120, 1/2     |  ||  |    120, 1/2     |  ||   L2
   467 - ||##+-----------------+##||##+-----------------+##||##+-----------------+##||
         ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
         ||  |       220       |  ||  |       220       |  ||  |       220       |  ||   L1
         ||  |                 |  ||  |                 |  ||  |                 |  ||
   223 - ||L_+-----------------+_J||L_+-----------------+_J||L_+-----------------+_J||
   220 - ++=======================================================================++
         ||                     30 × 60 bottom bar                                ||
   160 - ++=======================================================================++
        (O)                                                                       (O)   castors
     0 - ===============================================================================
         30<----- 316 clear ----->30<----- 316 clear ----->30<----- 316 clear ----->30
```

`#####` at 1008 is `angle.guard`, `##` at 467-875 `angle.support`, and `L_` and
`_J` at 223 `angle.base`. The top bar at 1041 and the bottom bar at 160-220 run
in one piece over all three columns. Castors stand only under the two outer
uprights; the middle uprights hang on the 30 × 60 bottom bar. The top stays
open until the top plate is fitted.

### Side view from the left

```
          front                             back
         |<-------------------- 435 ------------------->|
  1041 - |+--+====================================+--+|   top bar, top depth beam (open top)
  1008 - |[==========================================]|   angle.guard
         ||  |                                    |  ||
   875 - |[==========================================]|   L5  angle.support, 435 long
         ||  |                                    |##||   bracket.stop
   739 - |[==========================================]|   L4
         ||  |                                    |##||
   603 - |[==========================================]|   L3
         ||  |                                    |##||
   467 - |[==========================================]|   L2
         ||  |                                    |##||
   223 - |[==========================================]|   L1  angle.base
   220 - |+--+====================================+--+|   bottom depth beam, 190-220
   160 - |+--+                                    +--+|   bottom bar 30 × 60
         |(O)                                     (O) |   castor, M8 through the bar into the upright
     0 - ===============================================
         ^ joint plate, 4                              ^ joint plate, 4
         ^ boxes pull out here (front at y 5)    stop face at y 405 ^
```

### One support angle

```
 upright   angle.support 50 x 50 x 3, flat leg on top
   ||
   ||#############      <- the box ABOVE stands on the 50 mm flat leg (UHMW tape)
   ||#
   ||#    8 mm gap      <- the box BELOW tips up into the flat leg: tip guard
   ||#  +----------     <- rim of the box BELOW
   ||#  |               <- the hanging legs keep the rim within 310 mm
   ||#   \
   ||     \
```

The angles are fixed with countersunk M5 screws into T-nuts in the uprights'
inner slots, two per end, so the hanging leg stays smooth for the rim. Hole
centres sit 15 and 35 mm from the flat leg (`UNVERIFIED` proposal): base 238,
258; L2 449, 429; L3 585, 565; L4 721, 701; L5 857, 837; guard 993, 973.

## Joints

| Joint                                 | Count | Parts each                                                                                                 |
| ------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------- |
| Upright to bottom bar (and castor)    | 8     | 1 `screw.m8x100_socket` into the M8 core thread; at a corner 1 `washer.m8_large` in the castor's back hole |
| Upright to top bar                    | 8     | 1 `screw.m8x50_socket`, head sunk in the counterbore                                                       |
| Upright to depth beam                 | 16    | 1 `bracket.inside_30`, 2 `screw.m6x12_button`, 2 `tnut.m6`                                                 |
| Depth beam to bar                     | 16    | 1 `bracket.inside_30`, 2 `screw.m6x12_button`, 2 `tnut.m6`                                                 |
| Joint plate on the front or back face | 16    | 1 `plate.joint_l` or `plate.joint_t`, 5 `screw.m6x10_socket`, 5 `tnut.m6`                                  |
| Back stop on a back upright           | 30    | 1 `bracket.stop`, 1 `screw.m6x12_button`, 1 `tnut.m6`                                                      |
| Angle end to upright                  | 72    | 2 `screw.m5x10_countersunk`, 2 `tnut.m5`                                                                   |

The bracket between upright and depth beam sits on the upright's y face, above
the bottom depth beam and below the top one. The bracket between depth beam
and bar sits under the base angle's flat leg at the bottom and above the guard
at the top. The angles take the uprights' x faces, so no bracket shares a face
with an angle: the old bracket/angle collision (roadmap 0010) no longer exists.

The joint plates, L at the four corners and T at the middle uprights, top and
bottom of the front and the back frame, brace the frame against racking now
that there is no back panel. Two `bracket.stop` per box on the back uprights,
stop face at y 405, 20-50 mm above the floor of a 120 level and 60-90 mm above
the floor of the 220 level, keep the boxes from going through at the back.

## Loads

All values are `DERIVED` from the stated inputs.

- **Castor load.** 192 l of boxes at about 0.6 kg/l of LEGO (`UNVERIFIED`;
  LEGO never reaches the 25 kg box rating) is about 115 kg, plus boxes 13 kg,
  inserts about 5 kg and frame about 29 kg: about 162 kg. On three castors
  (uneven floor) that is 54 kg each against 100 kg.
- **Bottom bar sag.** P = W / 6 = 265 N per middle upright, castor centres
  1038 apart, each middle upright 346 from its castor:
  d = P a² (3L - 4a) / (6 E I). With 30 × 60 (I = 19.5 cm⁴, Dold page data,
  E = 70 GPa) d is about 0.7 mm; a 30 × 30 bar (2.75 cm⁴) would sag about
  4.7 mm.
- **Tipping forward.** The empty rack (about 47 kg, worst castor contact at
  y 56) restores about 7.6 kg·m. A full L5 box pulled out 270 mm tips with
  about 0.8 kg·m; a 20 kg child hanging on its front edge with about 6.4 kg·m.
  Keep the brakes on and the rack loaded.

## Inserts and ColorClips

The twelve 120 boxes take aidB NextGen insert sets, 100 mm high, in two rows
of 133 mm across the 300 side, from fine to coarse top to bottom: set 1/4
(4 × 1813-100) on L5 and L4, set 1/2 (2 × 3613-100) on L3 and L2. The 220
boxes on L1 have none. The handle
opening is blocked from inside by the insert walls, so a box is gripped from
outside (`UNVERIFIED`). Details, drawings and fit in `docs/inserts.md`.

Each box carries a ColorClip ring on both handles, one pack of two per box,
one colour per level from the bottom: red, turquoise, purple, yellow, blue
(`rack.json` → `color_clips.levels`, sRGB from aidB's photo, `UNVERIFIED`).
`color_clips.colours` lists all nine colours aidB sells, and
`color_clips.presets` five alternatives to try in the web viewer
(`docs/web_viewer.md` → *ColorClips*); the model and the parts list follow
`levels` alone.

## Contracts

The wave steps (roadmap 0003, 0005-0009) agree through these names. A step
that needs a change to a contract says so in its pull request instead of
making it.

### Part IDs

The part catalog is `parts` in `design/rack.json`. Every document, list and
price refers to a part by its `id`; `status` is `build` for what is bought now
and `planned` for the top plate and its fixings.

| ID                        | Category   | Quantity | Status  |
| ------------------------- | ---------- | -------- | ------- |
| `profile.upright`         | profile    | 8        | build   |
| `profile.bar_top`         | profile    | 2        | build   |
| `profile.bar_bottom`      | profile    | 2        | build   |
| `profile.beam_depth`      | profile    | 8        | build   |
| `angle.base`              | angle      | 6        | build   |
| `angle.support`           | angle      | 24       | build   |
| `angle.guard`             | angle      | 6        | build   |
| `bracket.inside_30`       | connector  | 32       | build   |
| `bracket.stop`            | connector  | 30       | build   |
| `plate.joint_l`           | connector  | 8        | build   |
| `plate.joint_t`           | connector  | 8        | build   |
| `screw.m6x12_button`      | fastener   | 94       | build   |
| `screw.m6x10_socket`      | fastener   | 80       | build   |
| `tnut.m6`                 | fastener   | 174      | build   |
| `screw.m5x10_countersunk` | fastener   | 144      | build   |
| `tnut.m5`                 | fastener   | 144      | build   |
| `screw.m8x100_socket`     | fastener   | 8        | build   |
| `screw.m8x50_socket`      | fastener   | 8        | build   |
| `washer.m8_large`         | fastener   | 4        | build   |
| `castor.brake`            | castor     | 2        | build   |
| `castor.plain`            | castor     | 2        | build   |
| `tape.uhmw_25`            | consumable | 13050 mm | build   |
| `cap.end_30`              | finish     | 4        | build   |
| `cap.end_30x60`           | finish     | 4        | build   |
| `cover.slot_8`            | finish     | 3636 mm  | build   |
| `box.e120`                | box        | 12       | build   |
| `box.e220`                | box        | 3        | build   |
| `clip.red`                | box        | 3        | build   |
| `clip.turquoise`          | box        | 3        | build   |
| `clip.purple`             | box        | 3        | build   |
| `clip.yellow`             | box        | 3        | build   |
| `clip.blue`               | box        | 3        | build   |
| `insert.set_half`         | insert     | 6        | build   |
| `insert.set_quarter`      | insert     | 6        | build   |
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

| File                        | View                                                                                  |
| --------------------------- | ------------------------------------------------------------------------------------- |
| `renders/front.png`         | Orthographic, from the front                                                          |
| `renders/side.png`          | Orthographic, from the left                                                           |
| `renders/three_quarter.png` | Perspective, front left, slightly from above                                          |
| `renders/drawer_out.png`    | Three-quarter, box `L3.C2` pulled out by `pull_out.travel` (270 mm)                   |
| `renders/inserts_top.png`   | Orthographic from above, the twelve 120 boxes with their inserts, staged in four rows |
| `renders/angle_detail.png`  | Close-up of one support angle with the boxes above and below                          |

### Model objects and the web export

Blender works in metres (rack millimetres / 1000). `web/rack.glb` is a binary
glTF in metres, Y up, as Blender's exporter writes it: rack `x` stays glTF `x`,
rack `z` becomes glTF `y`, rack `y` becomes glTF `-z`. The boxes pull out
towards the front, rack `-y`, which is glTF `+z`.

| Node name                                        | Holds                                                                   | glTF extras                                                                                                                                    |
| ------------------------------------------------ | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `frame`                                          | uprights, bars, depth beams, joint plates, angles, back stops, castors  | `{ "kind": "frame" }`                                                                                                                          |
| `box.L<level>.C<column>`                         | one box and, as children, its inserts and its ColorClip rings; 15 nodes | `{ "kind": "box", "level": 1-5, "column": 1-3, "class": "120" or "220", "model": "<box_models key>", "travel": 0.27, "pull_axis": [0, 0, 1] }` |
| `insert.L<level>.C<column>.R<row>.<cell>.<type>` | one insert, child of its box node                                       | `{ "kind": "insert" }`                                                                                                                         |
| `clip.L<level>.C<column>.<colour>`               | the ColorClip rings of both handles, child of its box node              | `{ "kind": "clip", "colour": "<color_clips.levels value>" }`                                                                                   |
| `plate.top`                                      | the planned top plate                                                   | `{ "kind": "plate", "status": "planned" }`                                                                                                     |

There are no panel nodes. The scene's extras carry
`{ "rack_schema": 2, "outer_mm": [1068, 443, 1041] }`. Columns count 1-3 from
the left seen from the front, levels 1-5 from the bottom. Moving a box node by
`travel` along `pull_axis` pulls the box, its inserts and its rings out
together.

Material names: `aluminium`, `box_anthracite`, `insert_grey`, `clip_red`,
`clip_turquoise`, `clip_purple`, `clip_yellow`, `clip_blue`, `castor`,
`plywood`.
