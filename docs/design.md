# Design

Read when changing the rack. Every number here is a copy of
`design/rack.json`, which wins where the two differ. The values are provisional
until the boxes are measured (roadmap 0004).

## Decisions

| Decision                                                  | Reason                                                                                                                                                                                                         | Source                                                                            |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| 3 columns, 5 levels, short side to front                  | The user's layout: one level of 220 mm boxes at the bottom, four levels of 120 mm boxes with inserts above, drawer style                                                                                       | the user                                                                          |
| Eurobox NextGen 2.0 Cycle 400 × 300, anthracite           | One vendor (ab-in-die-BOX, aidB) for boxes, inserts and ColorClips; the short 300 side with the open handle faces the front                                                                                    | the user; `sources.md` → *Boxes*                                                  |
| Box envelope narrowed to 400 × 300                        | The 600 × 400 design is gone; the user agreed that 600 × 400 boxes no longer fit                                                                                                                               | the user                                                                          |
| Boxes stand on their floor, not the rim                   | Floor support takes every 400 × 300 box with a continuous bottom edge                                                                                                                                          | `sources.md` → *Racks that take every brand*                                      |
| 316 mm between the uprights                               | 310 mm between the hanging legs: 2.5 mm play per side for a 305 mm rim                                                                                                                                         | `DERIVED` below                                                                   |
| Angles 50 × 50 × 3, flat leg on top                       | One angle carries the box above, guides the rim of the box below sideways and stops it tipping when pulled out                                                                                                 | `DERIVED` below                                                                   |
| Levels set for the tallest box per class                  | 233 mm for the 220 class, 125 mm for the 120 class, 8 mm gap above                                                                                                                                             | `sources.md` → *Boxes*                                                            |
| No slides, no pull-out stop                               | The user's choice; a box comes out like from an open shelf                                                                                                                                                     | the user                                                                          |
| No back stop: boxes pull out to the front and to the back | The user's choice; each box sits centred in the depth and pulls out 270 mm at either end; the rack must stand free in the room; the core-bolt joints keep the frames square                                    | the user                                                                          |
| One 1068 mm bar front and back, top and bottom            | One piece over all three columns; the uprights stand between the bars on an M8 through-bolt into their core thread                                                                                             | the user                                                                          |
| No joint plates; core-bolt joints keep the frames square  | The real CPL3030 / CPT3030 webs would block the level 1 and level 5 boxes; one tightened M8 core bolt per upright end holds the frames square (*Joints*, `UNVERIFIED`); threadlocker optional                  | the user; *Joints*                                                                |
| Bottom bars 30 × 60                                       | With castors only at the corners the middle uprights hang on the bottom bars: 0.66 mm sag; a 30 × 30 bar would sag about 4.8 mm                                                                                | `DERIVED` in *Loads*                                                              |
| 4 plain castors 100 mm, 70 kg, no brakes                  | Dold 69483, 125 high, back hole 11, offset 28; four suffice for the design load on three castors by Blickle's rule; the braked Dold 69490 has the same height, hole and offset and drops in at the front later | the user; `sources.md` → *Castor plates and open back* (added with 0014); *Loads* |
| Castor plates 90 × 90 × 10 under the corners              | EN AW-5083 plate under bar and bottom depth beam, castor centre 45 in from both outer faces, so the castor head (Ø46, `SECONDARY`) stays inside the outline; the wheel may swing up to 34 mm out               | the user; `sources.md` → *Castor plates and open back* (added with 0014)          |
| Bottom depth beams flush with the bars' undersides        | Bar and beam give the castor plate one flat face, 135 above the floor                                                                                                                                          | `DERIVED` below                                                                   |
| Top plate planned, not built                              | The top frame stays open; brackets swing in later without taking the frame apart                                                                                                                               | `sources.md` → *Top plate*                                                        |
| Inserts only in the 120 boxes                             | aidB NextGen insert sets made for 400 × 300 × 120; the 220 boxes stay open                                                                                                                                     | `sources.md` → *Inserts*                                                          |

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

| Check                                   | Value                                                        | Result                                                             |
| --------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------ |
| Widest rim between the hanging legs     | 305 in 310                                                   | 2.5 mm play per side                                               |
| Narrowest rim sideways travel           | (310 - 296) / 2                                              | 7 mm                                                               |
| Foot on each leg, box centred           | (260 - 216) / 2                                              | 22 mm                                                              |
| Foot on each leg, box fully to one side | 22 - 7                                                       | 15 mm                                                              |
| Gap above the tallest box, every level  | next flat leg bottom - (floor + max)                         | 8 mm                                                               |
| Gap above a 220 box in a 220 level      | 8 + 233 - 220                                                | 21 mm; the tip guard acts later                                    |
| Box length in the depth                 | 400 centred at y 17.5–417.5 in 435; a 405 rim spans y 15–420 | fits; no stop, the box pulls out at either end; envelope unchanged |

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

| Item                         | Value                                                                                       |
| ---------------------------- | ------------------------------------------------------------------------------------------- |
| Outer width × depth × height | 1068 × 435 × 1016, the frame itself                                                         |
| Clear width per column       | 316 between uprights, 310 between legs                                                      |
| Upright length               | 791 (195 to 986), x 0, 346, 692, 1038                                                       |
| Bottom bar                   | 30 × 60, 1068 long, 135 to 195                                                              |
| Top bar                      | 30 × 30, 1068 long, 986 to 1016                                                             |
| Depth beam                   | 375 long, 135 to 165 and 986 to 1016                                                        |
| Castor height                | 125                                                                                         |
| Castor plate                 | 90 × 90 × 10, 125 to 135, castor centre 45 in from both outer faces (x 45, 1023; y 45, 390) |
| Angle length                 | 435                                                                                         |
| Box position                 | front at y 17.5, centred in the depth                                                       |
| Pull-out travel, removal     | 270, 400, to the front and to the back                                                      |
| Top plate (planned)          | 1108 × 483 × 18, top at 1034                                                                |

| Level | Class | Floor (flat leg top) | Tallest box top | Next flat leg bottom | Angle           |
| ----- | ----- | -------------------- | --------------- | -------------------- | --------------- |
| 1     | 220   | 198                  | 431             | 439                  | `angle.base`    |
| 2     | 120   | 442                  | 567             | 575                  | `angle.support` |
| 3     | 120   | 578                  | 703             | 711                  | `angle.support` |
| 4     | 120   | 714                  | 839             | 847                  | `angle.support` |
| 5     | 120   | 850                  | 975             | 983                  | `angle.support` |
| guard |       |                      |                 |                      | `angle.guard`   |

The frame from bar bottom to top stays 881 (1016 - 135); every cut length is
unchanged.

### Front view

```
         |<------------------------------ 1068 frame ------------------------------->|
  1016 - ++=======================================================================++
   983 - ||#####             #####||#####             #####||#####             #####||
         ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
         ||  |    120, 1/4     |  ||  |    120, 1/4     |  ||  |    120, 1/4     |  ||   L5
   850 - ||##+-----------------+##||##+-----------------+##||##+-----------------+##||
         ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
         ||  |    120, 1/4     |  ||  |    120, 1/4     |  ||  |    120, 1/4     |  ||   L4
   714 - ||##+-----------------+##||##+-----------------+##||##+-----------------+##||
         ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
         ||  |    120, 1/2     |  ||  |    120, 1/2     |  ||  |    120, 1/2     |  ||   L3
   578 - ||##+-----------------+##||##+-----------------+##||##+-----------------+##||
         ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
         ||  |    120, 1/2     |  ||  |    120, 1/2     |  ||  |    120, 1/2     |  ||   L2
   442 - ||##+-----------------+##||##+-----------------+##||##+-----------------+##||
         ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
         ||  |       220       |  ||  |       220       |  ||  |       220       |  ||   L1
         ||  |                 |  ||  |                 |  ||  |                 |  ||
   198 - ||L_+-----------------+_J||L_+-----------------+_J||L_+-----------------+_J||
   195 - ++=======================================================================++
         ||                     30 × 60 bottom bar                                ||
   135 - ++=======================================================================++
   125 - [=====]                                                             [=====]   castor plates
           (O)                                                                 (O)     castors, 45 in
     0 - ===============================================================================
         30<----- 316 clear ----->30<----- 316 clear ----->30<----- 316 clear ----->30
```

`#####` at 983 is `angle.guard`, `##` at 442-850 `angle.support`, and `L_` and
`_J` at 198 `angle.base`. The top bar at 1016 and the bottom bar at 135-195 run
in one piece over all three columns. The castors stand under castor plates at
the corners, 45 in from the outer faces; the middle uprights hang on the
30 × 60 bottom bar. The top stays open until the top plate is fitted.

### Side view from the left

```
          front                             back
         |<-------------------- 435 ------------------->|
  1016 - |+--+====================================+--+|   top bar, top depth beam (open top)
   983 - |[==========================================]|   angle.guard
         ||  |                                    |  ||
   850 - |[==========================================]|   L5  angle.support, 435 long
         ||  |                                    |  ||
   714 - |[==========================================]|   L4
         ||  |                                    |  ||
   578 - |[==========================================]|   L3
         ||  |                                    |  ||
   442 - |[==========================================]|   L2
         ||  |                                    |  ||
   198 - |[==========================================]|   L1  angle.base
   195 - |+--+                                    +--+|   bottom bar 30 × 60, 135-195
   165 - ||  |====================================|  ||   bottom depth beam, 135-165
   135 - |+--+====================================+--+|   flush underside
   125 - [=====]                                [=====]   castor plate 90 × 90 × 10
           (O)                                    (O)     castor, centre 45 in
     0 - ===============================================
         ^ boxes pull out here (front at y 17.5)  and here (back at y 417.5) ^
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
centres sit 15 and 35 mm from the flat leg (`UNVERIFIED` proposal): base 213,
233; L2 424, 404; L3 560, 540; L4 696, 676; L5 832, 812; guard 968, 948.

## Joints

| Joint                                          | Count | Parts each                                                                                                                    |
| ---------------------------------------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------- |
| Upright to bottom bar                          | 8     | 1 `screw.m8x100_socket` from below into the 80 mm core thread; at a corner its head sits in the castor plate's Ø14 hole       |
| Upright to top bar                             | 8     | 1 `screw.m8x50_socket`, head sunk in the counterbore                                                                          |
| Upright to top depth beam                      | 8     | 1 `bracket.inside_30` on the upright's inner y face under the top depth beam, 2 `screw.m6x12_button`, 2 `tnut.m6`             |
| Top depth beam to bar                          | 8     | 1 `bracket.inside_30` above the guard, 2 `screw.m6x12_button`, 2 `tnut.m6`                                                    |
| Bottom depth beam top face to bar              | 8     | 1 `bracket.inside_30` on the beam's top face (z 165–195) into the bar's upper inner slot, 2 `screw.m6x12_button`, 2 `tnut.m6` |
| Bottom depth beam side to bar, middle uprights | 4     | 1 `bracket.inside_30` in the corner of beam side and bar inner face (z 135–165), 2 `screw.m6x12_button`, 2 `tnut.m6`          |
| Castor plate under a corner                    | 4     | 1 `plate.castor`, 4 `screw.m6x16_countersunk`, 4 `tnut.m6`; it joins bar and beam, so the corner needs no side bracket        |
| Castor to plate                                | 4     | 1 `castor.plain`, 1 `screw.m8x20_socket`, 1 `washer.m8`                                                                       |
| Angle end to upright                           | 72    | 2 `screw.m5x10_countersunk`, 2 `tnut.m5`                                                                                      |

That makes 28 `bracket.inside_30`. The bottom depth beams sit flush with the
bars' undersides so the castor plate lies flat under both; that leaves a 30 mm
gap between the beam top (165) and the upright foot (195), so the old bracket
between upright and bottom depth beam is gone and the beam's top face takes a
bracket into the bar instead. At a corner a side bracket would stand over the
castor bolt, and the plate joins bar and beam there anyway. The castor bolt,
ISO 4762 M8x20 with an ISO 7089 washer, goes from inside the housing up into
the plate's M8 thread (10 mm engagement, 1.25 d, the low end of the usual rule
for aluminium, `UNVERIFIED`). No connector sits on an upright's x face, so the
angles stay clear: the bracket/angle collision of roadmap 0010 no longer
exists, and 0014 closes it.

No plate braces the front and the back frame. Each upright end is pressed
against its bar by one M8 core bolt, and that butt joint resists bending as
long as the bolt holds it closed. With about 10 kN of clamping force from an M8
tightened in the core thread and the contact face taken as a solid 30 × 30
square, a joint stays closed up to about 10 kN × 30 mm / 6 = 50 N·m. The 16
joints of both frames then hold about 16 × 50 N·m / 0.836 m = 950 N pushed
sideways at the top bar before the first joint opens (lever from bar centre to
bar centre, z 165 to 1001); pushing the loaded rack on its castors takes about
100 N. The estimate is `UNVERIFIED`. The risk is a bolt working loose from
rolling, which an optional threadlocker and a check after the first moves
cover (`assembly.md`). Real joint plates (motedis CPL3030 / CPT3030) fill the
corner between their arms; on the outer faces they would reach 49 mm into the
path of the level 1 boxes and 36 mm into that of the level 5 boxes, at the
front and the back, so the rack has none.

There is no back stop: a box pushed on through comes out at the other side,
and the tip guard holds a pulled box at the back exactly as at the front.

## Loads

Values are `DERIVED` from the stated inputs unless marked. Sources in
`sources.md` → *Castor plates and open back* (added with 0014). Inputs marked
`UNVERIFIED` (small parts, inserts, top plate, n = 3, the plate's alloy
strength, the M8 thread engagement) are assumptions; a result that rests on
them is no more certain than they are.

**Masses.**

| Item                         | Calculation                             | Mass, kg   | Status                       |
| ---------------------------- | --------------------------------------- | ---------- | ---------------------------- |
| 30 × 30 profile              | 11.464 m × 0.843 kg/m                   | 9.66       | DERIVED from Dold `VERIFIED` |
| 30 × 60 profile              | 2.136 m × 1.489 kg/m                    | 3.18       | DERIVED from Dold `VERIFIED` |
| Angles                       | 15.66 m × 0.809 kg/m                    | 12.67      | DERIVED from Dold `VERIFIED` |
| Brackets                     | 28 × 0.02 kg (Dold 66895 `VERIFIED`)    | 0.56       | DERIVED                      |
| Screws, nuts, washers        | estimate                                | about 2    | UNVERIFIED                   |
| Castors                      | 4 × 0.29 kg (Dold `VERIFIED`)           | 1.16       | DERIVED                      |
| Castor plates                | 4 × 90 mm × 2.43 kg/m (Dold `VERIFIED`) | 0.87       | DERIVED                      |
| Frame                        | sum                                     | about 30.1 | DERIVED                      |
| Boxes                        | 12 × 0.80 + 3 × 1.18 (aidB `VERIFIED`)  | 13.14      | DERIVED                      |
| Inserts                      | estimate                                | about 5    | UNVERIFIED                   |
| Empty rack without top plate | 30.1 + 13.14 + 5                        | about 48.2 | DERIVED                      |
| Top plate (planned)          | estimate                                | about 6.5  | UNVERIFIED                   |

**LEGO bulk density.**

| Source                                                                           | Value                                   | Status                         |
| -------------------------------------------------------------------------------- | --------------------------------------- | ------------------------------ |
| Brick Architect: "around 250 pieces per liter", "around 700 pieces per kilogram" | 250 / 700 = 0.36 kg/l                   | DERIVED from `VERIFIED` quotes |
| Eurobricks forum: Pick-a-Brick cup 985 ml, 395 g on average                      | 0.40 kg/l                               | MEASURED                       |
| Eurobricks forum: 5.68 l tub of random LEGO, 1.72–1.91 kg                        | 0.30–0.34 kg/l                          | MEASURED                       |
| Eurobricks forum: densely packed cups                                            | about 0.57–0.64 kg/l, volumes estimated | MEASURED                       |
| Solid ABS (INEOS Terluran GP-35; that LEGO uses it is `UNVERIFIED`)              | 1.04 kg/l, the impossible ceiling       | VERIFIED                       |

The rack uses low 0.25, typical 0.40 and design 0.60 kg/l (sorted drawers of
small parts). The boxes hold 12 × 11 l + 3 × 20 l = 192 l (aidB's nominal
volumes, `VERIFIED`; 196 l from the inner dimensions), so 48, 76.8 and
115.2 kg. With the top
plate the design total is 48.2 + 6.5 + 115.2 = 169.9 kg, the typical one
48.2 + 6.5 + 76.8 = 131.5 kg.

**Castor rating.** Blickle's rule T = (E + Z) / n × S, with S = 1.0–1.5 for
manual transport indoors over obstacles below 5 % of the wheel diameter
(`VERIFIED`, https://www.blickle.de/ratgeber/tragfaehigkeit), and n = 3 of 4
castors for an uneven floor (`UNVERIFIED` convention). Design case at S = 1.2:
169.9 / 3 × 1.2 = 68.0 kg against 70 kg per castor; the castor holds up to
S = 1.24. Typical case: 52.6 kg at S 1.2, 65.8 kg at S 1.5. Thresholds above
5 mm lie outside the rule's indoor case: push slowly.

**Bottom bar sag.** Castor centres L = 978 apart, each middle upright
a = 316 from a castor (x 361 and 707), P = W / 6 = 1666.7 N / 6 = 278 N per
middle upright, E = 70 GPa. Under two equal loads placed symmetrically the bar
sags most at mid-span, d = P a (3L² - 4a²) / (24 E I): a 30 × 60 bar
(I = 19.51 cm⁴, Dold `VERIFIED`) sags 0.66 mm (0.57 mm under the middle
uprights); a 30 × 30 bar (I = 2.68 cm⁴, `VERIFIED`) would sag 4.8 mm. The
corner uprights stand 30 mm outside the castors, which lifts the middle
slightly; that is ignored, so the values are conservative.

**Tipping, forwards and backwards.** Backwards is the mirror image of forwards.

- The worst wheel contact lies at y 45 + 28 = 73 at the front (362 at the
  back); the centre of mass at y 217.5; lever 0.1445 m.
- The empty rack, 48.2 kg, restores 48.2 × 0.1445 = 6.96 kg·m. One 120 box with
  its inserts (about 1.2 kg) pulled 270 mm out shifts 0.33 kg·m, leaving
  6.63 kg·m.
- EN 14749 / EN 16122 (`SECONDARY`, via the CPSC rule text): 75 N (7.65 kg) on
  the front of one extended drawer, drawers empty. The box front at
  y 17.5 - 270 = -252.5 gives a lever of 0.3255 m: 2.49 kg·m against 6.63,
  passes with factor 2.7.
- ASTM F2057-23 / 16 CFR 1261 (`VERIFIED`,
  https://www.cpsc.gov/Business--Manufacturing/Business-Education/Business-Guidance/Clothing-Storage-Units):
  27.2 kg (60 lb) on the top edge of the extended element. Not binding (the
  rack is no clothing storage unit), but the only test built for a child. One
  box out on the empty rack: 27.2 × 0.3255 = 8.85 kg·m against 6.63: the rack
  tips. All 15 boxes out to the front (about 18.2 kg, 4.90 kg·m) leave
  2.06 kg·m: it tips.
- With LEGO spread evenly the one-box case passes from about 16 kg of LEGO:
  (8.85 + 0.33) / 0.1445 - 48.2 = 15.3 kg. Ballast for the empty rack at
  factor 1.2, low and central: one box out (1.2 × 8.85 + 0.33) / 0.1445 - 48.2
  = 27.6 kg; every box out to one side (1.2 × 8.85 + 4.90) / 0.1445 - 48.2
  = 59.2 kg.
- Without brakes the rack rolls when a box is pulled; rolling resistance of a
  few per cent of the weight caps the pulling force.

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
| `bracket.inside_30`       | connector  | 28       | build   |
| `plate.castor`            | connector  | 4        | build   |
| `screw.m6x12_button`      | fastener   | 56       | build   |
| `screw.m6x16_countersunk` | fastener   | 16       | build   |
| `tnut.m6`                 | fastener   | 72       | build   |
| `screw.m5x10_countersunk` | fastener   | 144      | build   |
| `tnut.m5`                 | fastener   | 144      | build   |
| `screw.m8x100_socket`     | fastener   | 8        | build   |
| `screw.m8x50_socket`      | fastener   | 8        | build   |
| `screw.m8x20_socket`      | fastener   | 4        | build   |
| `washer.m8`               | fastener   | 4        | build   |
| `castor.plain`            | castor     | 4        | build   |
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
rack `z` becomes glTF `y`, rack `y` becomes glTF `-z`. The front is rack `-y`,
which is glTF `+z`.

| Node name                                        | Holds                                                                               | glTF extras                                                                                                                                                                |
| ------------------------------------------------ | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `frame`                                          | uprights, bars, depth beams, castor plates, brackets, angles, castors               | `{ "kind": "frame" }`                                                                                                                                                      |
| `box.L<level>.C<column>`                         | one box and, as children, its inserts and its ColorClip rings; 15 nodes             | `{ "kind": "box", "level": 1-5, "column": 1-3, "class": "120" or "220", "model": "<box_models key>", "travel": 0.27, "pull_axis": [0, 0, 1], "sides": ["front", "back"] }` |
| `insert.L<level>.C<column>.R<row>.<cell>.<type>` | one insert, child of its box node                                                   | `{ "kind": "insert" }`                                                                                                                                                     |
| `clip.L<level>.C<column>.<colour>`               | the ColorClip rings of both handles, child of its box node                          | `{ "kind": "clip", "colour": "<color_clips.levels value>" }`                                                                                                               |
| `plate.top`                                      | the planned top plate                                                               | `{ "kind": "plate", "status": "planned" }`                                                                                                                                 |

There are no panel and no back stop nodes. The scene's extras carry
`{ "rack_schema": 3, "outer_mm": [1068, 435, 1016] }`. Columns count 1-3 from
the left seen from the front, levels 1-5 from the bottom. `pull_axis` points to
the front; moving a box node by `travel` along it pulls the box, its inserts
and its rings out together. When `sides` contains `"back"`, the viewer pulls
the box the other way, along `-pull_axis`, for a click on its back half.

Material names: `aluminium`, `box_anthracite`, `insert_grey`, `clip_red`,
`clip_turquoise`, `clip_purple`, `clip_yellow`, `clip_blue`, `castor`,
`plywood`.
