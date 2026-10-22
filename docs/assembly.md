# Assembly

How one person builds the rack. Every number is a copy of `design/rack.json`,
which wins where the two differ, and is provisional until the boxes are
measured (roadmap 0004). Parts are named by their ID from `design.md` →
*Contracts*; `x`, `y` and `z` are the rack's coordinates (`x` to the right,
`y` to the back, `z` up, origin on the floor at the front-left frame corner,
without the joint plates). Columns count 1-3 from the left seen from the
front, levels 1-5 from the bottom.

![Three-quarter view](../renders/three_quarter.png)

The renders show the planned top plate on the frame; it is fitted last, if at
all (*Fitting the top plate later*).

The rack is two flat frames, front (`y` 0-30) and back (`y` 405-435), each a
bottom bar, a top bar and four uprights, joined by eight depth beams. It
stands on four castors under castor plates at the corners and holds 15
Eurobox NextGen 2.0 Cycle 400 × 300, short side with the handle at the front:
3 × 220 on level 1 and 12 × 120 on levels 2-5. The back is open: a box comes
out at the front and at the back.

## Before you start

### Parts

| Part ID                   | Quantity | Used in step |
| ------------------------- | -------- | ------------ |
| `profile.bar_top`         | 2        | 1, 6         |
| `profile.bar_bottom`      | 2        | 1, 6         |
| `profile.upright`         | 8        | 2, 6         |
| `profile.beam_depth`      | 8        | 7            |
| `angle.base`              | 6        | 3, 9         |
| `angle.support`           | 24       | 3, 9         |
| `angle.guard`             | 6        | 3, 9         |
| `plate.castor`            | 4        | 4, 8         |
| `tnut.m5`                 | 144      | 5, 9         |
| `tnut.m6`                 | 152      | 5, 6, 7, 8   |
| `screw.m8x100_socket`     | 8        | 6            |
| `screw.m8x50_socket`      | 8        | 6            |
| `plate.joint_l`           | 8        | 6            |
| `plate.joint_t`           | 8        | 6            |
| `screw.m6x10_socket`      | 80       | 6            |
| `bracket.inside_30`       | 28       | 7            |
| `screw.m6x12_button`      | 56       | 7            |
| `screw.m6x16_countersunk` | 16       | 8            |
| `castor.plain`            | 4        | 8            |
| `screw.m8x20_socket`      | 4        | 8            |
| `washer.m8`               | 4        | 8            |
| `screw.m5x10_countersunk` | 144      | 9            |
| `tape.uhmw_25`            | 13050 mm | 10           |
| `cap.end_30`              | 4        | 11           |
| `cap.end_30x60`           | 4        | 11           |
| `cover.slot_8`            | 3636 mm  | 11           |
| `box.e220`                | 3        | 12           |
| `box.e120`                | 12       | 12           |
| `clip.blue`               | 3        | 12           |
| `clip.turquoise`          | 6        | 12           |
| `clip.lightgreen`         | 6        | 12           |
| `insert.set_quarter`      | 6        | 12           |
| `insert.set_half`         | 6        | 12           |

Buy about ten spare `tnut.m5` and `tnut.m6`. Both are hammer nuts for B-type
slot 8: they go into a slot from its open face, also where the slot is closed
at both ends, and turn 90° as the screw is tightened ([motedis][mo-hm],
[BM Profiles][bm-nuts]). So no nut has to be threaded in before a joint is
made, and a forgotten one is added later without taking the frame apart.

### Order pre-machined

- Profiles cut to length, ends square and deburred: 8 × 791
  (`profile.upright`), 2 × 1068 30 × 30 (`profile.bar_top`), 2 × 1068 30 × 60
  (`profile.bar_bottom`), 8 × 375 (`profile.beam_depth`). The cut list is
  `bom/cutlist.csv`.
- An M8 core thread in **both ends of each of the 8 uprights**, the bottom one
  extra deep, 80 mm, so the `screw.m8x100_socket` has full engagement after the
  60 mm bar ([Dold 30x60L][dold-3060]; the thread options are read from the
  page data, `UNVERIFIED`).
- Angles 50 × 50 × 3 cut to 435: 6 `angle.base`, 24 `angle.support`,
  6 `angle.guard`. Their holes are drilled at home (step 3).
- Castor plates: Dold AGP-10-90-Z, milled cast plate EN AW-5083, 10 thick,
  90 wide, cut 90 long, 4 pieces of 90 × 90 × 10 ([Dold plate][dold-plate]).
  Their holes are drilled at home (step 4); Dold's CNC machining is an option,
  its price `UNVERIFIED`.
- The through holes in the bars are drilled at home (step 1); the shop's CNC
  holes are dearer and only in its configurator (`UNVERIFIED`).

### Tools

| Tool                                      | For                                                      |
| ----------------------------------------- | -------------------------------------------------------- |
| Hex keys 3, 4, 5 and 6 mm (or bits)       | M5 and M6 countersunk, M6 button and socket, M8 bolts    |
| Drill stand, 8.5 mm HSS bit               | Through holes in the bars, square to the profile         |
| 14 mm counterbore (or flat drill)         | Sinking the M8 heads in the top bars                     |
| 14 mm HSS bit                             | Corner bolt head hole in the castor plates               |
| 6.8 mm HSS bit, M8 tap with tap wrench    | M8 thread in the castor plates                           |
| 6.6 mm HSS bit                            | Clearance holes for M6 in the castor plates              |
| Drill, 5.5 mm HSS bit                     | Clearance holes in the angles                            |
| 90° countersink bit, at least 13 mm       | Countersinking the angles and the castor plates          |
| Deburring tool or fine file               | Cut ends and drilled holes                               |
| Steel square, tape measure, steel rule    | Marking and squaring                                     |
| Fine marker, centre punch                 | Marking heights and holes                                |
| Spirit level, at least 600 mm             | Levels horizontal, uprights plumb                        |
| Two clamps, a few wooden blocks           | Holding a beam while a bracket is fitted                 |
| Cutter knife, cloth, isopropyl alcohol    | UHMW tape                                                |

Work on a flat, clean floor with a blanket or cardboard under the profiles.

### Deburr

Deburr every cut end of profiles, angles and plates, and both sides of every
drilled hole. A burr on a hanging leg catches the rim of a box; a burr on a
profile end keeps the joint from closing.

## Step 1: Mark and drill the bars

**Parts:** `profile.bar_top` × 2, `profile.bar_bottom` × 2.

Each bar carries four uprights, one under or over each through hole. The holes
are vertical (along `z`), on the centre line of the bar's depth, at the
upright centres.

| Bar                  | Hole        | Hole centres, `x` from the left end | Head side              |
| -------------------- | ----------- | ----------------------------------- | ---------------------- |
| `profile.bar_top`    | 8.5 through | 15, 361, 707, 1053                  | top, 14 mm counterbore |
| `profile.bar_bottom` | 8.5 through | 15, 361, 707, 1053                  | underside              |

1. Lay the bars side by side, ends flush, and mark all four with the square in
   one go, so the holes of front and back match.
2. Punch, then drill 8.5 mm in the drill stand, square to the face; through
   the 60 mm height of the bottom bars, drill from both sides if the bit is
   short, meeting in the middle.
3. Counterbore the top bars from the top face, 14 mm, deep enough that the head
   of a `screw.m8x50_socket` sits flush or below (`UNVERIFIED`; try on the
   first hole).
4. Deburr.

**Check:** a bolt passes each hole square; laid end to end, front and back
holes line up.

## Step 2: Mark the uprights

**Parts:** `profile.upright` × 8.

1. Check that each upright is 791 long with an M8 core thread at both ends; the
   80 mm deep one is the bottom (`z` 195), the other the top (`z` 986).
2. Name the uprights by position: front row `F0`, `F1`, `F2`, `F3` at `x` 0,
   346, 692, 1038 (left edge of the profile), back row `B0` to `B3` at the same
   `x`, `y` 405. Write the name on a piece of tape at the top end.
3. Measured from the bottom end (`z` 195 on the rack is 0 on the upright), mark
   on each face that carries angles (the inner `x` faces; `F1`, `F2`, `B1`,
   `B2` have two) the flat leg of each angle:

| Angle           | Level | Flat leg  | Fixing leg on the upright | Mark on the upright (from bottom end) |
| --------------- | ----- | --------- | ------------------------- | ------------------------------------- |
| `angle.base`    | 1     | 195-198   | 195-245, leg up           | 0 (underside of flat leg, on the bar) |
| `angle.support` | 2     | 439-442   | 392-442, leg down         | 247 (top of flat leg)                 |
| `angle.support` | 3     | 575-578   | 528-578, leg down         | 383 (top of flat leg)                 |
| `angle.support` | 4     | 711-714   | 664-714, leg down         | 519 (top of flat leg)                 |
| `angle.support` | 5     | 847-850   | 800-850, leg down         | 655 (top of flat leg)                 |
| `angle.guard`   | guard | 983-986   | 936-986, leg down         | 791 (top end, under the top bar)      |

The `z` of a mark is the mark plus 195.

**Check:** 8 uprights, every mark on the same face of every upright; laid side
by side, the marks line up with the square.

## Step 3: Drill and countersink the angles

**Parts:** `angle.base` × 6, `angle.support` × 24, `angle.guard` × 6.

Each angle has 4 holes, 2 per end, in the leg that lies against the upright
(the vertical leg of `angle.base`, the hanging leg of the others), on the
centre line of the upright's slot, 15 mm from each end of the angle (`y` 15
and `y` 420), and 15 and 35 mm from the inner face of the flat leg. These hole
positions are a proposal of this guide (`UNVERIFIED`), chosen so the heads
clear the inner corner of the angle and stay within the 50 mm leg.

| Angle           | Level | Hole centres, `z` |
| --------------- | ----- | ----------------- |
| `angle.base`    | 1     | 213, 233          |
| `angle.support` | 2     | 424, 404          |
| `angle.support` | 3     | 560, 540          |
| `angle.support` | 4     | 696, 676          |
| `angle.support` | 5     | 832, 812          |
| `angle.guard`   | guard | 968, 948          |

In the leg that means 15 and 35 from the flat leg for every angle, so one
template serves them all.

1. Mark one angle, punch, drill 5.5 mm. Use it as a drilling template for the
   others, clamped end to end and flat leg to flat leg.
2. Countersink each hole at 90° from the side that faces the box, that is the
   side away from the upright. Sink until the head of a
   `screw.m5x10_countersunk` sits flush or a hair below the surface; test on
   the first hole. The leg is only 3 mm thick, so stop as soon as the head is
   flush: a sink that is too deep leaves no seat and the head pulls through
   (`UNVERIFIED`; try on an offcut first).
3. Deburr both sides.

**Check:** a screw in every hole of a test angle; run a fingernail along the
leg: no head, no burr stands proud. The hanging leg must stay smooth for the
box rim.

## Step 4: Drill the castor plates

**Parts:** `plate.castor` × 4.

Each plate sits under one frame corner, below the bottom bar and the bottom
depth beam, whose undersides are flush. Hole positions are measured from the
plate's outer corner, the one that sits at the frame corner; the first number
runs along the bar, the second along the depth beam.

| Hole                               | Centres from the outer corner | For                                                         |
| ---------------------------------- | ----------------------------- | ----------------------------------------------------------- |
| 6.8 drilled, M8 thread             | (45, 45)                      | `screw.m8x20_socket` of the castor                          |
| 14 through                         | (15, 15)                      | Head of the corner upright's `screw.m8x100_socket`          |
| 6.6 through, countersunk 90° below | (60, 15), (80, 15)            | `screw.m6x16_countersunk` into the bar's bottom slot        |
| 6.6 through, countersunk 90° below | (15, 60), (15, 80)            | `screw.m6x16_countersunk` into the depth beam's bottom slot |

The pattern is symmetric about the plate's diagonal through the outer corner,
so all four plates are identical: for the other corners the plate is only
turned, never made as a mirror image.

1. Mark one plate, punch, drill in the drill stand, and use it as a template
   for the other three.
2. Tap the M8 thread square to the face; 10 mm of aluminium gives 1.25 d of
   engagement, the low end of the usual 1.25-2 d (`UNVERIFIED`), so cut a
   clean full thread.
3. The 14 mm hole takes the ISO 4762 M8 head, 13 across and 8 high
   (`UNVERIFIED` standard value); the 10 mm plate hides it. Try a bolt head in
   the first hole.
4. Countersink the four M6 holes from the underside (the side away from the
   profiles) until a `screw.m6x16_countersunk` sits flush or a hair below.
5. Deburr.

**Check:** a bolt head drops into the 14 mm hole; an M8 screw runs into the
thread by hand; no M6 head stands proud underneath.

## Step 5: Hammer nuts

**Parts:** `tnut.m5` × 144, `tnut.m6` × 152.

All nuts are hammer nuts, so each can go in when its part is fitted; putting
the ones of a frame in before it stands up just saves bending later. Where
they go:

| Slot                                                                | Nuts                                 |
| ------------------------------------------------------------------- | ------------------------------------ |
| Each inner `x` face of an upright that carries angles (12)          | 12 × `tnut.m5` (6 angles × 2 screws) |
| Inner `y` face of each upright, top end, under the top beam (8)     | 1 × `tnut.m6`                        |
| Each top depth beam (4)                                             | 4 × `tnut.m6`                        |
| Each corner bottom depth beam, top face (2)                         | 2 × `tnut.m6`                        |
| Each middle bottom depth beam, top face and side (2)                | 4 × `tnut.m6`                        |
| Inner faces of the bars, at each depth beam end (20 brackets)       | 1 × `tnut.m6`                        |
| Outer face of each joint plate's bar and upright (16 plates)        | 5 × `tnut.m6`                        |
| Bottom slots of bar and depth beam under each castor plate (4)      | 4 × `tnut.m6`                        |

That is 144 `tnut.m5` for the angles (step 9) and 152 `tnut.m6`: 56 for the
28 brackets (2 each, step 7), 80 for the 16 joint plates (step 6) and 16 for
the 4 castor plates (step 8).

**Check:** count again before each step; a nut missing in a hidden spot is
added from the slot face.

## Step 6: Front and back frame

**Parts:** `profile.bar_bottom` × 2, `profile.bar_top` × 2,
`profile.upright` × 8, `screw.m8x100_socket` × 8,
`screw.m8x50_socket` × 8, `plate.joint_l` × 8, `plate.joint_t` × 8,
`screw.m6x10_socket` × 80.

![Front](../renders/front.png)

Build each frame flat on the floor, outer face up.

1. **Bottom bar.** Lay a `profile.bar_bottom` (30 × 60, 60 high) with its
   holes' head side down.
2. **Uprights.** Stand all four uprights (`F0` to `F3`, or `B0` to `B3`) on
   the bar's top face over the holes and bolt each with a
   `screw.m8x100_socket` from below into its 80 mm core thread. At the corners
   the head stays proud of the bar's underside; it sits in the castor plate's
   14 mm hole in step 8.
3. **Top bar.** Lay a `profile.bar_top` on the top ends, counterbores up, and
   bolt all four uprights with a `screw.m8x50_socket` each, head sunk in the
   counterbore.
4. **Plates.** On the outer face (the front face of the front frame, the back
   face of the back frame) fit a `plate.joint_l` at each corner joint and a
   `plate.joint_t` at each middle upright, top and bottom: 8 plates per frame,
   each with 5 `screw.m6x10_socket` into hammer nuts in the bar and the
   upright.
5. Square the frame (diagonals equal within 1 mm), then tighten bolts and
   plate screws.

**Check:** each frame 1068 wide and 881 high (`z` 135-1016 once on castors);
clear width 316 between neighbouring uprights at top and bottom; diagonals
equal within 1 mm.

## Step 7: Join the frames

**Parts:** `profile.beam_depth` × 8, `bracket.inside_30` × 28,
`screw.m6x12_button` × 56.

One joint: one `bracket.inside_30` in the inside corner, each leg with one
`screw.m6x12_button` into a `tnut.m6` ([motedis Winkel][mo-winkel]). Tighten
firmly by hand with the hex key; do not use an impact driver, which can damage
the slot lips ([cnc-zubehoer][cnc-hm]).

1. Stand the front frame up, held by a helper object (a table, a wall), and the
   back frame 435 behind it.
2. **Bottom depth beams**, one under each upright pair, `z` 135-165, between
   the inner faces of the bottom bars, so their undersides are flush with the
   bars'. Their tops stay 30 below the upright feet (`z` 195).
3. **Top depth beams**, one over each upright pair, `z` 986-1016, flush with
   the top bars.
4. **Brackets, 28 in all:**
   - Upright to top depth beam, 8: on the upright's inner `y` face, under the
     top depth beam.
   - Top depth beam to bar, 8: on the side of the top depth beam in the corner
     with the bar's inner face, above the guard (within `z` 986-1016).
   - Bottom depth beam to bar, 8: on the beam's top face (`z` 165) in the
     corner with the bar's inner face, into the bar's upper inner slot
     (within `z` 165-195).
   - Middle bottom depth beams to bar, 4: on the side of each middle bottom
     beam in the corner with the bar's inner face (within `z` 135-165). The
     corners get none; the castor plate joins bar and beam there.
   No bracket sits on an upright face that carries an angle, so the angles
   stay clear.
5. Tighten in diagonal order, checking square as you go.

**Check:**

- Frame 1068 × 435 × 881; outer 1068 × 443 with the plates.
- Diagonals of the top and the bottom equal within 2 mm.
- Every upright plumb with the spirit level, both directions.

## Step 8: Castor plates and castors

**Parts:** `plate.castor` × 4, `screw.m6x16_countersunk` × 16, `tnut.m6` × 16,
`castor.plain` × 4, `screw.m8x20_socket` × 4, `washer.m8` × 4.

1. Lay the frame on its back on a blanket, so the undersides of the bottom bars
   and the bottom depth beams are reachable.
2. **Plates.** Lay a `plate.castor` under each corner, outer corner flush with
   the frame corner, countersinks out, the corner bolt head in the 14 mm hole.
   Screw it with 4 `screw.m6x16_countersunk` into hammer nuts in the bottom
   slot of the bar (2) and of the depth beam (2).
3. **Castors.** Hold a `castor.plain` on the plate, put a `washer.m8` on a
   `screw.m8x20_socket`, and screw it from inside the housing up through the
   castor's back hole (11 mm) into the plate's M8 thread. Dold lists M8x20,
   washer and slot nut as the fixing for this castor
   ([Dold castor][dold-castor]); here the plate's thread takes the place of
   the slot nut. Tighten firmly; the screw's tip ends at most about 5 mm above
   the plate in free space.
4. Stand the frame up on its castors.

**Check:** each plate flush with the frame's outer faces and flat under bar
and beam; every castor head (⌀46, `SECONDARY`) inside the frame outline seen
from above; every castor swivels freely, the wheel may swing out up to about
34 mm (`DERIVED`); the frame stands level; the bottom bars run `z` 135-195,
the top at 1016.

## Step 9: Angles, from the bottom up

**Parts:** `angle.base` × 6, `angle.support` × 24, `angle.guard` × 6,
`screw.m5x10_countersunk` × 144, `tnut.m5` × 144.

![Angle detail](../renders/angle_detail.png)

Each angle runs the full depth, `y` 0-435, and is held by 2 screws at each end
into the inner slot of a front and a back upright. Fit one level at a time,
from the bottom up:

1. **Level 1, `angle.base`, 6 pieces.** Flat leg at the bottom on the bottom
   bars (`z` 195-198), vertical leg up against the upright.
2. **Levels 2-5, `angle.support`, 6 per level.** Flat leg on top, hanging leg
   down along the upright; flat leg top at 442, 578, 714, 850.
3. **Guard, `angle.guard`, 6 pieces.** Same orientation, flat leg 983-986,
   just under the top bar.
4. Before tightening each angle, set the spirit level across the pair of
   angles of one column and on each angle along its length.

**Check, every level:**

- Flat leg height at front and back within 1 mm of the table in step 2.
- Clear width 310 between the two hanging legs (between the vertical legs at
  level 1) of each column, front and back; 216 between the leg tips.
- Both angles of a column at the same height.
- No screw head stands proud of the leg.

## Step 10: UHMW tape on the carrying legs

**Parts:** `tape.uhmw_25`, 30 pieces of 435 mm (13050 mm).

The tape goes on the top of the flat leg of each `angle.base` and
`angle.support`, the 30 legs that carry a box. The guard carries nothing and
gets none.

1. Clean the flat leg with isopropyl alcohol and let it dry.
2. Cut 435 mm, peel a few centimetres of liner, and lay the tape from the front
   end along the outer edge of the flat leg, pulling the liner as you go. Press
   it down firmly with a cloth along the whole length.
3. Round both end corners of each piece with the knife, so a box pushed in from
   the front or the back does not lift the tape.

**Check:** no bubbles, no lifted corner; a box slides on it without catching.
Self-adhesive tapes reach full strength only after some time; leave the rack
unloaded overnight if the maker says so (`UNVERIFIED`).

## Step 11: End caps and slot covers

**Parts:** `cap.end_30` × 4, `cap.end_30x60` × 4, `cover.slot_8` × 3636 mm.

1. Press a `cap.end_30` into each end of the two top bars and a
   `cap.end_30x60` into each end of the two bottom bars.
2. Cut `cover.slot_8` for the top faces: 2 × 1068 (top bars) and 4 × 375 (top
   depth beams), 3636 mm in all, and press it in. Leave out the inner slots of
   the top bars if the top plate is to follow (see below).

**Check:** no open slot on the top; no sharp edge at hand height.

## Step 12: Boxes, ColorClips and inserts

**Parts:** `box.e220` × 3, `box.e120` × 12, `clip.blue` × 3,
`clip.turquoise` × 6, `clip.lightgreen` × 6, `insert.set_quarter` × 6,
`insert.set_half` × 6.

![Box pulled out](../renders/drawer_out.png)

1. Clip one ColorClip pack (2 rings) per box, one ring on each handle frame,
   one colour per insert type (table below).
2. Inserts: two rows across the 300 side, each 133 wide; the cells of a row run
   along the 400 side from the front. A set fills 266 × 365 (quarter
   266 × 364) of the 265 × 365 inner top (box tolerance ±5). The end walls of
   two inserts stand right behind each handle opening, so the handle is gripped
   from outside only (`UNVERIFIED` until a box is measured).
3. Level 1 takes `box.e220`, levels 2-5 `box.e120`. Fill level 1 first. Each
   box goes in with its short side to the front; push it in until it is
   centred, 17.5 behind the front and the back face of the frame. Nothing stops
   it there: pushed on, it comes out at the other side.

![Inserts from above](../renders/inserts_top.png)

| Box                | Class | Layout  | Inserts                                     | ColorClip         |
| ------------------ | ----- | ------- | ------------------------------------------- | ----------------- |
| `L1.C1` to `L1.C3` | 220   | none    | none                                        | `clip.blue`       |
| `L2.C1` to `L2.C3` | 120   | half    | `insert.set_half`: 2 × 3613 (133 × 365)     | `clip.turquoise`  |
| `L3.C1` to `L3.C3` | 120   | half    | `insert.set_half`: 2 × 3613 (133 × 365)     | `clip.turquoise`  |
| `L4.C1` to `L4.C3` | 120   | quarter | `insert.set_quarter`: 4 × 1813 (133 × 182)  | `clip.lightgreen` |
| `L5.C1` to `L5.C3` | 120   | quarter | `insert.set_quarter`: 4 × 1813 (133 × 182)  | `clip.lightgreen` |

**Check, every box:** it slides in and out without catching, the rim runs
between the hanging legs; pulled out by 270 mm (`pull_out.travel`) to the
front or to the back it stays on its legs, and it comes out entirely at
400 mm (`pull_out.removal`).

## Final checks and moving the rack

- Levels horizontal across and along, every column.
- All 15 boxes in and centred, none rubbing.
- Every screw tight; check again after the first week of use.
- The rack stands free in the room, so a box can be pulled from both sides.
- The castors have no brakes: the rack can roll a little when a box is pulled.
- **Rolling:** take the boxes out or at least the heavy ones, push at the frame
  (not at a box), slowly over thresholds.

## Fitting the top plate later

**Parts (planned):** `plate.top` × 1, `bracket.plate` × 10,
`screw.wood_4_5x12` × 20.

![Side](../renders/side.png)

The top stays open; the plate can be added without taking anything apart,
because the brackets come with swing-in nuts ([BM Profiles][bm-nuts]).

1. The plate: 1108 × 483 × 18 birch plywood, corners rounded R25. It overhangs
   the frame by 20 on all four sides (over the plates at front and back); its
   top is at 1034. Break and sand all edges round; children will lean on it.
2. Take out the slot cover from the inner slot of each top bar, if fitted.
3. Swing a `bracket.plate` into those slots, 5 at the front and 5 at the back:
   one near each end and one per column, the bracket's free leg flush with the
   top of the bar (`z` 1016). Snug the nuts.
4. Lay the plate on top, 20 overhang on each side; mark through the bracket
   holes from below.
5. Lift off, pre-drill 2.5 mm, at most 10 mm deep so the tip stays inside the
   18 mm plate; lay it back and screw from below, 2 `screw.wood_4_5x12` per
   bracket.
6. Tighten the bracket nuts.

**Check:** the plate lies flat, does not rock; the overhang is equal all
around; no screw tip on top.

## Safety

- A box takes at most 25 kg, the maker's rating ([aidB 120][aidb-12],
  [aidB 220][aidb-22]). Keep the heavy boxes low.
- Each castor is rated 70 kg ([Dold castor][dold-castor]). The full rack in
  the design case, about 171 kg with the top plate (`DERIVED`), on three
  castors of an uneven floor puts about 57 kg on each, 68 kg with a safety
  factor of 1.2 (`DERIVED`, see `design.md`).
- **Tipping:** an empty rack can tip forward (or backward) when a child hangs
  on a pulled-out box: the ASTM F2057-23 test load of 27.2 kg on the edge of
  one extended box tips it ([CPSC][cpsc-csu]; `DERIVED`, see `design.md`).
  Fill the bottom level first and keep the rack loaded, pull one box at a
  time, never more than its 270 mm travel.
- The braked castor Dold 69490 has the same height, hole and offset
  (`VERIFIED`) and fits the front corners later without any other change.
- The rack is not made to be climbed or stood on, top plate or not.

## Open points

1. The box geometry used here (handle opening, rim, ribs) is read from the
   product photos (`UNVERIFIED`); roadmap 0004 measures a box.
2. The angle hole positions (15 and 35 from the flat leg, 15 from each end) are
   a proposal (`UNVERIFIED`).
3. Through-hole alignment: drilled at home, a hole off the core axis puts the
   upright off its line; drill front and back bars together (step 1).
4. Counterbore depth in the 30 mm top bar is not yet tried (`UNVERIFIED`).
5. Prices of `screw.m6x10_socket` and `cap.end_30x60` are not read.
6. The fit of the M8 head in the castor plate's 14 mm hole and the 10 mm
   thread engagement are not yet tried (`UNVERIFIED`).

[mo-hm]: https://www.motedis.com/de/Hammermutter-B-Typ-Nut-8-M6
[mo-winkel]: https://www.motedis.com/de/Winkel-30-B-Typ-Nut-8
[dold-castor]: https://www.dold-mechatronik.de/Lenkrolle-100-Rueckenloch-ohne-Bremse
[dold-plate]: https://www.dold-mechatronik.de/Plangefraeste-Gussplatte-Aluminium-EN-AW-5083-foliert-Dicke-10mm-Breite-90mm-243kg-m-Zuschnitt-20-3000mm
[bm-nuts]: https://www.bm-profile.com/de/ratgeber/nutensteine/
[cnc-hm]: https://www.cnc-zubehoer.eu/Edelstahl-Nutenstein-Hammermutter-Nut-8-M6-schmal/AP.HM.N8M6S.ES
[dold-3060]: https://www.dold-mechatronik.de/Aluminiumprofil-30x60L-B-Typ-Nut-8-149kg-m-Zuschnitt-50-6000mm
[cpsc-csu]: https://www.cpsc.gov/Business--Manufacturing/Business-Education/Business-Guidance/Clothing-Storage-Units
[aidb-12]: https://www.ab-in-die-box.de/b2cde/euroboxen/nextgen/nextgen-2-0-cycle/eurobox-nextgen-2-0-cycle-griffe-offen-400-x-300-x-120-mm-anthrazit.html
[aidb-22]: https://www.ab-in-die-box.de/b2cde/euroboxen/nextgen/nextgen-2-0-cycle/eurobox-nextgen-2-0-cycle-griffe-offen-400-x-300-x-220-mm-anthrazit.html
