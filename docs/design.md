# Design

Read when changing the rack. Every number here is a copy of
`design/rack.json`, which wins where the two differ. The values are provisional
until the boxes are measured (roadmap 0004).

## Decisions

| Decision                                                  | Reason                                                                                                                                                                                                         | Source                                                                            |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| 3 columns, 5 levels, short side to front                  | The user's layout: one level of 220 mm boxes at the bottom, four levels of 120 mm boxes with inserts above, drawer style                                                                                       | the user                                                                          |
| Eurobox NextGen 2.0 Cycle 400 × 300, anthracite           | One vendor (ab-in-die-BOX, aidB) for boxes, inserts and ColorClips; the short 300 side with the closed handle faces the front                                                                                  | the user; `sources.md` → *Boxes*                                                  |
| Box envelope narrowed to 400 × 300                        | The 600 × 400 design is gone; the user agreed that 600 × 400 boxes no longer fit                                                                                                                               | the user                                                                          |
| Boxes stand on their floor, not the rim                   | Floor support takes every 400 × 300 box with a continuous bottom edge                                                                                                                                          | `sources.md` → *Racks that take every brand*                                      |
| 316 mm between the uprights                               | 310 mm between the hanging legs: 2.5 mm play per side for a 305 mm rim                                                                                                                                         | `DERIVED` below                                                                   |
| Angles 50 × 50 × 3, flat leg on top                       | One angle carries the box above, guides the rim of the box below sideways and stops it tipping when pulled out                                                                                                 | `DERIVED` below                                                                   |
| Levels set for the tallest box per class                  | 233 mm for the 220 class, 125 mm for the 120 class, 8 mm gap above                                                                                                                                             | `sources.md` → *Boxes*                                                            |
| No slides, no slide tape, no pull-out stop                | The user's choice; a box comes out like from an open shelf and slides on the bare aluminium of the flat legs; the slots stay open for an industrial look, only the eight bar ends get caps                     | the user                                                                          |
| No back stop: boxes pull out to the front and to the back | The user's choice; each box sits centred in the depth and pulls out 270 mm at either end; the rack must stand free in the room; the core-bolt joints keep the frames square                                    | the user                                                                          |
| One 1068 mm bar front and back, top and bottom            | One piece over all three columns; the uprights stand between the bars on an M8 through-bolt into their core thread                                                                                             | the user                                                                          |
| No joint plates; core-bolt joints keep the frames square  | The real CPL3030 / CPT3030 webs would block the level 1 and level 5 boxes; one tightened M8 core bolt per upright end holds the frames square (*Joints*, `UNVERIFIED`); threadlocker optional                  | the user; *Joints*                                                                |
| Bottom bars 30 × 30, top plate structural                 | With castors only at the corners the middle uprights hang between them; top bar with the screwed top plate and bottom bar share their load: about 1.3 mm sag long-term, 4.85 mm for a 30 × 30 bar alone        | `DERIVED` in *Loads*                                                              |
| 4 plain castors 100 mm, 70 kg, no brakes                  | Dold 69483, 125 high, back hole 11, offset 28; four suffice for the design load on three castors by Blickle's rule; the braked Dold 69490 has the same height, hole and offset and drops in at the front later | the user; `sources.md` → *Castor plates and open back* (added with 0014); *Loads* |
| Castor plates 90 × 90 × 10 under the corners              | EN AW-5083 plate under bar and bottom depth beam, castor centre 45 in from both outer faces, so the castor head (Ø46, `SECONDARY`) stays inside the outline; the wheel may swing up to 34 mm out               | the user; `sources.md` → *Castor plates and open back* (added with 0014)          |
| Bottom depth beams flush with the bars' undersides        | Bar and beam give the castor plate one flat face, 135 above the floor                                                                                                                                          | `DERIVED` below                                                                   |
| Top plate built and structural                            | 21 mm birch, screwed from below with 20 brackets into the top bars' inner slots, nothing visible on top; it stiffens the top chord so the bottom bars can be 30 × 30                                           | `sources.md` → *Top plate*; *Loads*                                               |
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

| Value                 | Model value                                                                        | Status     |
| --------------------- | ---------------------------------------------------------------------------------- | ---------- |
| Rim band              | 6, at the 400 × 300 envelope                                                       | UNVERIFIED |
| Collar below the rim  | 31, set back 5                                                                     | UNVERIFIED |
| Ledge lip             | 3 thick, at the envelope, below the collar                                         | UNVERIFIED |
| Foot band             | 18, set back 1, a 45° chamfer of 4 up to the panel                                 | UNVERIFIED |
| Side panel recess     | 6                                                                                  | UNVERIFIED |
| Rib webs              | 2.5 thick, outer face at the envelope, from the foot chamfer to the rim            | UNVERIFIED |
| Rib pairs, long sides | centres 103 and 297 from the front, 16 wide outside, open pocket between the webs  | UNVERIFIED |
| Corner webs           | one in each face, centre 24 from the corner, open pocket towards the corner        | UNVERIFIED |
| Pin blocks            | long sides, collar height, 30 wide, centre 49 from each corner, hole Ø4            | UNVERIFIED |
| Outer corner radius   | 8                                                                                  | UNVERIFIED |
| Inner corner radius   | 6                                                                                  | UNVERIFIED |
| Inner floor, 120 box  | 359 × 259; the wall tapers from the 365 × 265 inner top                            | SECONDARY  |
| Inner floor, 220 box  | 354 × 254, the same wall slope over 215                                            | DERIVED    |
| Handle frame          | 145 × 50, corner radius 12, from 15 below the rim; two webs 2.5 wide up to the rim | UNVERIFIED |
| Handle tray           | inside the frame, 8 deep; a raised lip 2 wide stands round the grip pocket         | UNVERIFIED |
| Handle grip pocket    | closed, 116 × 24, corner radius 6, 12 deep, from 28 below the rim                  | UNVERIFIED |
| ColorClip ring        | 145 × 50 × 2, radii 12 outside and 6 inside, round the grip pocket                 | UNVERIFIED |
| Colour                | about sRGB #3F3F3F lit in the photo; drawn at linear 0.04, IOR 1.49                | UNVERIFIED |

The relief (webs, pockets, ledge lip, chamfer, pin blocks, handle tray and grip
pocket) is read from aidB's photo of C2G43-12; every piece stays inside the
400 × 300 × height envelope, which the build checks.

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
| Outer width × depth × height | 1068 × 435 × 986, the frame itself; 1007 to the top of the plate                            |
| Clear width per column       | 316 between uprights, 310 between legs                                                      |
| Upright length               | 791 (165 to 956), x 0, 346, 692, 1038                                                       |
| Bottom bar                   | 30 × 30, 1068 long, 135 to 165                                                              |
| Top bar                      | 30 × 30, 1068 long, 956 to 986                                                              |
| Depth beam                   | 375 long, 135 to 165 and 956 to 986                                                         |
| Castor height                | 125                                                                                         |
| Castor plate                 | 90 × 90 × 10, 125 to 135, castor centre 45 in from both outer faces (x 45, 1023; y 45, 390) |
| Angle length                 | 435                                                                                         |
| Box position                 | front at y 17.5, centred in the depth                                                       |
| Pull-out travel, removal     | 270, 400, to the front and to the back                                                      |
| Top plate                    | 1108 × 483 × 21, top at 1007, corners R10, edges broken 1.5, grain along 1108               |

| Level | Class | Floor (flat leg top) | Tallest box top | Next flat leg bottom | Angle           |
| ----- | ----- | -------------------- | --------------- | -------------------- | --------------- |
| 1     | 220   | 168                  | 401             | 409                  | `angle.base`    |
| 2     | 120   | 412                  | 537             | 545                  | `angle.support` |
| 3     | 120   | 548                  | 673             | 681                  | `angle.support` |
| 4     | 120   | 684                  | 809             | 817                  | `angle.support` |
| 5     | 120   | 820                  | 945             | 953                  | `angle.support` |
| guard |       |                      |                 |                      | `angle.guard`   |

The frame from bar bottom to top is 851 (986 - 135). The uprights keep their
791; the bottom bars are 30 × 30 and sit flush with the bottom depth beams.

### Front view

```
         |<------------------------------ 1068 frame ------------------------------->|
  1007 -#############################################################################   top plate 21
   986 - ++=======================================================================++
   953 - ||#####             #####||#####             #####||#####             #####||
         ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
         ||  |    120, 1/4     |  ||  |    120, 1/4     |  ||  |    120, 1/4     |  ||   L5
   820 - ||##+-----------------+##||##+-----------------+##||##+-----------------+##||
         ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
         ||  |    120, 1/4     |  ||  |    120, 1/4     |  ||  |    120, 1/4     |  ||   L4
   684 - ||##+-----------------+##||##+-----------------+##||##+-----------------+##||
         ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
         ||  |    120, 1/2     |  ||  |    120, 1/2     |  ||  |    120, 1/2     |  ||   L3
   548 - ||##+-----------------+##||##+-----------------+##||##+-----------------+##||
         ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
         ||  |    120, 1/2     |  ||  |    120, 1/2     |  ||  |    120, 1/2     |  ||   L2
   412 - ||##+-----------------+##||##+-----------------+##||##+-----------------+##||
         ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
         ||  |       220       |  ||  |       220       |  ||  |       220       |  ||   L1
         ||  |                 |  ||  |                 |  ||  |                 |  ||
   168 - ||L_+-----------------+_J||L_+-----------------+_J||L_+-----------------+_J||
   165 - ++=======================================================================++
         ||                     30 × 30 bottom bar                                ||
   135 - ++=======================================================================++
   125 - [=====]                                                             [=====]   castor plates
           (O)                                                                 (O)     castors, 45 in
     0 - ===============================================================================
         30<----- 316 clear ----->30<----- 316 clear ----->30<----- 316 clear ----->30
```

`#####` at 953 is `angle.guard`, `##` at 412-820 `angle.support`, and `L_` and
`_J` at 168 `angle.base`. The top bar at 956-986 and the bottom bar at 135-165
run in one piece over all three columns. The castors stand under castor plates
at the corners, 45 in from the outer faces; the middle uprights hang from the
top bar, stiffened by the screwed top plate, and stand on the 30 × 30 bottom
bar. The top plate overhangs the frame by 20 at each side.

### Side view from the left

```
          front                             back
         |<-------------------- 435 ------------------->|
  1007 -##################################################################   top plate 21, screwed to the top bars from below
   986 - |+--+====================================+--+|   top bar, top depth beam
   953 - |[==========================================]|   angle.guard
         ||  |                                    |  ||
   820 - |[==========================================]|   L5  angle.support, 435 long
         ||  |                                    |  ||
   684 - |[==========================================]|   L4
         ||  |                                    |  ||
   548 - |[==========================================]|   L3
         ||  |                                    |  ||
   412 - |[==========================================]|   L2
         ||  |                                    |  ||
   168 - |[==========================================]|   L1  angle.base
   165 - |+--+====================================+--+|   bottom bar 30 × 30 and bottom depth beam, both 135-165
   135 - |+--+====================================+--+|   flush top and underside
   125 - [=====]                                [=====]   castor plate 90 × 90 × 10
           (O)                                    (O)     castor, centre 45 in
     0 - ===============================================
         ^ boxes pull out here (front at y 17.5)  and here (back at y 417.5) ^
```

### One support angle

```
 upright   angle.support 50 x 50 x 3, flat leg on top
   ||
   ||#############      <- the box ABOVE stands on the 50 mm flat leg
   ||#
   ||#    8 mm gap      <- the box BELOW tips up into the flat leg: tip guard
   ||#  +----------     <- rim of the box BELOW
   ||#  |               <- the hanging legs keep the rim within 310 mm
   ||#   \
   ||     \
```

The angles are fixed with countersunk M5 screws into T-nuts in the uprights'
inner slots, two per end, so the hanging leg stays smooth for the rim. Hole
centres sit 15 and 35 mm from the flat leg (`UNVERIFIED` proposal): base 183,
203; L2 394, 374; L3 530, 510; L4 666, 646; L5 802, 782; guard 938, 918.

## Joints

| Joint                                                 | Count | Parts each                                                                                                                                  |
| ----------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Upright to bottom bar                                 | 8     | 1 `screw.m8x70_socket` from below, 40 mm into the 80 mm core thread; at a corner its head sits in the castor plate's Ø14 hole               |
| Upright to top bar                                    | 8     | 1 `screw.m8x50_socket`, head sunk in the counterbore                                                                                        |
| Upright to top depth beam                             | 8     | 1 `bracket.inside_30` on the upright's inner y face under the top depth beam, 2 `screw.m6x12_button`, 2 `tnut.m6`                           |
| Top depth beam to bar                                 | 8     | 1 `bracket.inside_30` above the guard, 2 `screw.m6x12_button`, 2 `tnut.m6`                                                                  |
| Bottom depth beam to bar, bay side                    | 8     | 1 `bracket.inside_30` in the corner of beam side and bar inner face on the beam's bay side (z 135–165), 2 `screw.m6x12_button`, 2 `tnut.m6` |
| Bottom depth beam to bar, other side, middle uprights | 4     | 1 `bracket.inside_30` in the same corner on the beam's other side, 2 `screw.m6x12_button`, 2 `tnut.m6`                                      |
| Castor plate under a corner                           | 4     | 1 `plate.castor`, 4 `screw.m6x16_countersunk`, 4 `tnut.m6`; it joins bar and beam, so the corner needs no side bracket                      |
| Castor to plate                                       | 4     | 1 `castor.plain`, 1 `screw.m8x20_socket`, 1 `washer.m8`                                                                                     |
| Top plate to top bar                                  | 20    | 1 `bracket.plate` in the bar's inner slot, 1 `screw.wood_4_5x16` from below into a pre-drilled hole                                         |
| Angle end to upright                                  | 72    | 2 `screw.m5x10_countersunk`, 2 `tnut.m5`                                                                                                    |

That makes 28 `bracket.inside_30`. The bottom bars and the bottom depth beams
both run 135-165, so the castor plate lies flat under both and the uprights
stand on the bar at 165. Each bottom depth beam is held by a bracket in the
corner of its side face and the bar's inner face on the beam's bay side, and at
the middle uprights by a second one on the other side; at a corner the castor
plate joins bar and beam as well. The top plate hangs on 20 `bracket.plate`,
10 per top bar at x 90, 165, 240, 315, 470, 628, 772, 846, 920 and 993, each
with one `screw.wood_4_5x16` from below into a pre-drilled hole, at least 5 mm
of wood above the tip; nothing shows on top. The castor bolt,
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
joints of both frames then hold about 16 × 50 N·m / 0.821 m = 970 N pushed
sideways at the top bar before the first joint opens (lever from bar centre to
bar centre, z 150 to 971); pushing the loaded rack on its castors takes about
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
`UNVERIFIED` (small parts, inserts, top plate, the plywood's density, the wood
screws' capacity, n = 3, the plate's alloy strength, the M8 thread engagement)
are assumptions; a result that rests on
them is no more certain than they are.

**Masses.**

| Item                         | Calculation                             | Mass, kg   | Status                       |
| ---------------------------- | --------------------------------------- | ---------- | ---------------------------- |
| 30 × 30 profile              | 13.600 m × 0.843 kg/m                   | 11.46      | DERIVED from Dold `VERIFIED` |
| Angles                       | 15.66 m × 0.809 kg/m                    | 12.67      | DERIVED from Dold `VERIFIED` |
| Brackets                     | 28 × 0.02 kg (Dold 66895 `VERIFIED`)    | 0.56       | DERIVED                      |
| Plate brackets, wood screws  | 20 × bracket.plate + 20 × screw         | about 0.4  | UNVERIFIED                   |
| Screws, nuts, washers        | estimate                                | about 2    | UNVERIFIED                   |
| Castors                      | 4 × 0.29 kg (Dold `VERIFIED`)           | 1.16       | DERIVED                      |
| Castor plates                | 4 × 90 mm × 2.43 kg/m (Dold `VERIFIED`) | 0.87       | DERIVED                      |
| Frame                        | sum                                     | about 29.1 | DERIVED                      |
| Boxes                        | 12 × 0.80 + 3 × 1.18 (aidB `VERIFIED`)  | 13.14      | DERIVED                      |
| Inserts                      | estimate                                | about 5    | UNVERIFIED                   |
| Top plate                    | 0.535 m² × 14.3 kg/m², 21 mm            | about 7.7  | DERIVED                      |
| Empty rack with top plate    | 29.1 + 13.14 + 5 + 7.7                  | about 55.0 | DERIVED                      |

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
115.2 kg. The top plate is part of the structure, so the design total is
55.0 + 115.2 = 170.2 kg, the typical one 55.0 + 76.8 = 131.8 kg.

**Castor rating.** Blickle's rule T = (E + Z) / n × S, with S = 1.0–1.5 for
manual transport indoors over obstacles below 5 % of the wheel diameter
(`VERIFIED`, https://www.blickle.de/ratgeber/tragfaehigkeit), and n = 3 of 4
castors for an uneven floor (`UNVERIFIED` convention). Design case at S = 1.2:
170.2 / 3 × 1.2 = 68.1 kg against 70 kg per castor; the castor holds up to
S = 1.23. Typical case: 52.7 kg at S 1.2, 65.9 kg at S 1.5. Thresholds above
5 mm lie outside the rule's indoor case: push slowly.

**Bottom bar sag.** Castor centres L = 978 apart, each middle upright
a = 316 from a castor (x 361 and 707), P = W / 6 = 1669 N / 6 ≈ 280 N per
middle upright (W from the 170.2 kg design total), E = 70 GPa. Under two equal
loads placed symmetrically the frame sags most at mid-span,
d = P a (3L² - 4a²) / (24 ΣEI). The middle uprights hang from the top chord
and stand on the bottom bar, so both carry P in proportion to their stiffness.
The composite top chord of top bar and screwed top plate follows EN 1995-1-1
Annex B (γ method) with Kser = ρm^1.5 d / 23 from Table 7.1, doubled for a
metal side, and kdef = 0.8 for plywood in service class 1 (`SECONDARY`); the
plywood has E∥ = 9 858 N/mm² from the Metsä Wood DoP for 21 mm birch and
ρm = 680 kg/m³ (`UNVERIFIED`).

| Case                                                       | Sag, mm             |
| ---------------------------------------------------------- | ------------------- |
| 30 × 30 bottom bar alone (I = 2.68 cm⁴, Dold `VERIFIED`)   | 4.85                |
| With the 30 × 30 top bar                                   | 2.4                 |
| Plus the top plate laid on, not connected                  | 1.6                 |
| Plate screwed at about 75 mm in the outer bays, short-term | about 1.0           |
| Plate screwed at about 75 mm in the outer bays, long-term  | about 1.3           |
| Rigid connection, the lower bound                          | 0.6 short, 0.7 long |

With the screws the top chord's effective I lies between the γ method's rows
for 50 and 100 mm spacing: about 9.6–11.9 cm⁴ short-term, 6.8–8.5 cm⁴
long-term. The shear between plate and bar acts only in the outer 316 mm
segments and is zero between the middle uprights, hence four brackets in each
outer bay and two in the middle one; each screw takes about 250–390 N, below
the 0.8–1 kN a 4.5 mm wood screw holds (`UNVERIFIED`). The 30 × 30 bottom bar
carries about 26 % of the bending moment: about 13 MPa. Without the screwed
plate, during assembly, the rack must not be loaded beyond empty. The corner
uprights stand 30 mm outside the castors, which lifts the middle slightly;
that is ignored, so the values are conservative. All values are `DERIVED`.

**Tipping, forwards and backwards.** Backwards is the mirror image of forwards.

- The worst wheel contact lies at y 45 + 28 = 73 at the front (362 at the
  back); the centre of mass at y 217.5; lever 0.1445 m.
- The empty rack with its top plate, 55.0 kg, restores 55.0 × 0.1445
  = 7.95 kg·m. One 120 box with its inserts (about 1.2 kg) pulled 270 mm out
  shifts 0.33 kg·m, leaving 7.62 kg·m.
- EN 14749 / EN 16122 (`SECONDARY`, via the CPSC rule text): 75 N (7.65 kg) on
  the front of one extended drawer, drawers empty. The box front at
  y 17.5 - 270 = -252.5 gives a lever of 0.3255 m: 2.49 kg·m against 7.62,
  passes with factor 3.1.
- ASTM F2057-23 / 16 CFR 1261 (`VERIFIED`,
  https://www.cpsc.gov/Business--Manufacturing/Business-Education/Business-Guidance/Clothing-Storage-Units):
  27.2 kg (60 lb) on the top edge of the extended element. Not binding (the
  rack is no clothing storage unit), but the only test built for a child. One
  box out on the empty rack: 27.2 × 0.3255 = 8.85 kg·m against 7.62: the rack
  tips. All 15 boxes out to the front (about 18.2 kg, 4.90 kg·m) leave
  3.05 kg·m: it tips.
- With LEGO spread evenly the one-box case passes from about 9 kg of LEGO:
  (8.85 + 0.33) / 0.1445 - 55.0 = 8.5 kg. Ballast for the empty rack at
  factor 1.2, low and central: one box out (1.2 × 8.85 + 0.33) / 0.1445 - 55.0
  = 20.8 kg; every box out to one side (1.2 × 8.85 + 4.90) / 0.1445 - 55.0
  = 52.4 kg.
- Without brakes the rack rolls when a box is pulled; rolling resistance of a
  few per cent of the weight caps the pulling force.

## Inserts and ColorClips

The twelve 120 boxes take aidB NextGen insert sets, 100 mm high, in two rows
of 133 mm across the 300 side, from fine to coarse top to bottom: set 1/4
(4 × 1813-100) on L5 and L4, set 1/2 (2 × 3613-100) on L3 and L2. The 220
boxes on L1 have none. The handles
are closed grip pockets, gripped from outside; the insert end walls stand
behind them (`UNVERIFIED`). Details, drawings and fit in `docs/inserts.md`.

Each box carries a ColorClip ring on both handles, one pack of two per box,
one colour per insert type in neighbouring cool hues, lighter towards the top:
blue on L1 (220, no inserts), turquoise on L2 and L3 (set 1/2), light green on
L4 and L5 (set 1/4) (`rack.json` → `color_clips.levels`, sRGB from aidB's
photo, `UNVERIFIED`).
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
and `planned` for a part that is designed but not yet bought (none at present).

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
| `screw.m8x70_socket`      | fastener   | 8        | build   |
| `screw.m8x50_socket`      | fastener   | 8        | build   |
| `screw.m8x20_socket`      | fastener   | 4        | build   |
| `washer.m8`               | fastener   | 4        | build   |
| `castor.plain`            | castor     | 4        | build   |
| `cap.end_30`              | finish     | 8        | build   |
| `box.e120`                | box        | 12       | build   |
| `box.e220`                | box        | 3        | build   |
| `clip.blue`               | box        | 3        | build   |
| `clip.turquoise`          | box        | 6        | build   |
| `clip.lightgreen`         | box        | 6        | build   |
| `insert.set_half`         | insert     | 6        | build   |
| `insert.set_quarter`      | insert     | 6        | build   |
| `plate.top`               | plate      | 1        | build   |
| `bracket.plate`           | connector  | 20       | build   |
| `screw.wood_4_5x16`       | fastener   | 20       | build   |

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

PNG, 1600 × 1200, under `renders/`, EEVEE with screen-space ray tracing, AgX.
The top plate is drawn as oiled birch plywood with 15 plies
(`top_plate`; plies, finish and colour `UNVERIFIED`) and shows in every
render but `inserts_top`:

| File                        | View                                                                                  |
| --------------------------- | ------------------------------------------------------------------------------------- |
| `renders/front.png`         | Orthographic, from the front                                                          |
| `renders/side.png`          | Orthographic, from the left                                                           |
| `renders/three_quarter.png` | Perspective, front left, slightly from above                                          |
| `renders/drawer_out.png`    | Three-quarter, box `L3.C2` pulled out by `pull_out.travel` (270 mm)                   |
| `renders/inserts_top.png`   | Orthographic from above, the twelve 120 boxes with their inserts, staged in four rows |
| `renders/angle_detail.png`  | Close-up of one support angle with the boxes above and below                          |
| `renders/exploded.png`      | Perspective, front right from above, the rack exploded (`explode` at 1)               |

### Model objects and the web export

Blender works in metres (rack millimetres / 1000). `web/rack.glb` is a binary
glTF in metres, Y up, as Blender's exporter writes it: rack `x` stays glTF `x`,
rack `z` becomes glTF `y`, rack `y` becomes glTF `-z`. The front is rack `-y`,
which is glTF `+z`.

| Node name                                                                                   | Holds                                                                           | glTF extras                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `frame`                                                                                     | every part of the rack but the boxes and the plate, as children                 | `{ "kind": "frame" }`                                                                                                                                                                                        |
| `upright.<n>.<side>`, `bar.<top/bottom>.<side>`, `beam.depth.<top/bottom>.<n>`              | one profile, child of `frame`; side is `front` or `back`                        | `{ "part": "profile.upright" }` and so on                                                                                                                                                                    |
| `angle.base.L1.C<column>.<left/right>`, `angle.support.L<level>…`, `angle.guard.C<column>…` | one angle, child of `frame`                                                     | `{ "part": "angle.base" }` and so on                                                                                                                                                                         |
| `bracket.<n>`, `bracket.plate.<side>.<n>`, `plate.castor.<n>`, `castor.plain.<n>`           | one bracket, castor plate or castor, child of `frame`                           | `{ "part": "<part ID>" }`                                                                                                                                                                                    |
| `<part ID>.<n>`                                                                             | one screw, hammer nut, washer or end cap, child of the part it sits in or holds | none; its mesh carries `{ "part": "<part ID>", "kind": "fastener" or "cap" }`                                                                                                                                |
| `bracket.plate.fixing.<part ID>.<n>`                                                        | the screw or hammer nut of a plate bracket's fixing set, child of the bracket   | `{ "part_of": "bracket.plate" }`; its mesh as above                                                                                                                                                          |
| `box.L<level>.C<column>`                                                                    | one box and, as children, its inserts and its ColorClip rings; 15 nodes         | `{ "kind": "box", "part": "box.e120" or "box.e220", "level": 1-5, "column": 1-3, "class": "120" or "220", "model": "<box_models key>", "travel": 0.27, "pull_axis": [0, 0, 1], "sides": ["front", "back"] }` |
| `insert.L<level>.C<column>.R<row>.<cell>.<type>`                                            | one insert, child of its box node                                               | `{ "kind": "insert", "type": "<type>", "part": "insert.set_half" or "insert.set_quarter" }`                                                                                                                  |
| `clip.L<level>.C<column>.<colour>.<front/back>`                                             | the ColorClip ring of one handle, child of its box node                         | `{ "kind": "clip", "colour": "<color_clips.levels value>" }`                                                                                                                                                 |
| `plate.top`                                                                                 | the top plate                                                                   | `{ "kind": "plate", "part": "plate.top", "status": "build", "plywood": { … } }`                                                                                                                              |

Every part of the parts list is drawn: `build_rack.py` stops unless the count
per part ID equals `rack.json` → `parts` (an insert set counts once per box,
a ColorClip set once per box, a fixing-set piece not at all). Parts of one
kind share one mesh; a right-hand angle or a back castor is its left or front
twin turned half round, not mirrored. A screw, nut, washer or cap carries its
part ID on its mesh, not on its node, which keeps its 484 nodes small; three.js
merges the mesh extras into the node's `userData`, so the viewer reads
`kind` and `part` there alike.

The exploded view: `rack.blend` has a scene property `explode` from 0 to 1,
run in three steps, each a third of the range, so no part passes through
another: (1) the boxes straight out to the front, far enough that they stay in
front of the rack to the end (the build checks this); (2) the boxes' levels
spread upwards, each higher than the one below so that level's inserts clear
the box above; (3) everything else: the frame apart, the fasteners out of their
holes, the inserts out of their boxes, the rings off the handles. Every part
that moves has one simple-expression driver per
moving axis on its delta location, in its parent's axes, a sum of
`<metres>*clamp(e*3-<step>,0,1)`; Blender runs them without Python auto-run,
and the file is saved at 0. `export_web.py` reads the drivers back and writes
each moving node's move as the glTF extra `{ "explode": [[x, y, z], …] }`,
one offset per step, in metres, glTF axes, its parent's space; the glb holds
the rack assembled. A child that only moves with its parent carries none.
The distances are `rack.json` → `explode`.

`export_web.py` compacts the file after Blender's exporter: normals as
normalized 8-bit integers and positions of the meshes within 1 m of their
origin as normalized 16-bit integers (`KHR_mesh_quantization`, required), the
long bars as floats on a 0.01 mm grid, node transforms rounded to 1e-6 m and
1e-7, the JSON without spaces. There are no panel and no back stop nodes. The scene's extras carry
`{ "rack_schema": 3, "outer_mm": [1068, 435, 986] }`. Columns count 1-3 from
the left seen from the front, levels 1-5 from the bottom. `pull_axis` points to
the front; moving a box node by `travel` along it pulls the box, its inserts
and its rings out together. When `sides` contains `"back"`, the viewer pulls
the box the other way, along `-pull_axis`, for a click on its back half.

Material names: `aluminium`, `box_anthracite`, `insert_grey`, `clip_blue`,
`clip_turquoise`, `clip_lightgreen`, `castor`, `plywood`, `steel` (the
zinc-plated screws, nuts and washers), `cap_black` (the end caps).
