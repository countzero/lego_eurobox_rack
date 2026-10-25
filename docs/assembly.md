# Assembly

How one person builds the rack. Every number is a copy of `design/rack.json`,
which wins where the two differ, and is provisional until the boxes are
measured (roadmap 0004). Parts are named by their ID from `design.md` →
*Contracts*; `x`, `y` and `z` are the rack's coordinates (`x` to the right,
`y` to the back, `z` up, origin on the floor at the front-left frame
corner). Columns count 1-3 from the left seen from the
front, levels 1-5 from the bottom.

![Three-quarter view](../renders/three_quarter.png)

The renders show the top plate on the frame. It is part of the structure and
is fitted before the rack is loaded (step 11).

The rack is two flat frames, front (`y` 0-30) and back (`y` 405-435), each a
bottom bar, a top bar and four uprights, joined by eight depth beams and
covered by a structural top plate. It
stands on four braked castors under castor plates at the corners and holds 15
Eurobox NextGen 2.0 Cycle 400 × 300, short side with the handle at the front:
3 × 220 on level 1 and 12 × 120 on levels 2-5. The back is open: a box comes
out at the front and at the back. Every metal part and the castors come from
motedis in one order (`docs/prices.md`).

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
| `tnut.m6`                 | 84       | 5, 7, 8, 11  |
| `screw.m8x50_socket`      | 8        | 6            |
| `screw.m8x40_socket`      | 8        | 6            |
| `bracket.inside_30`       | 24       | 7            |
| `screw.m6x12_button`      | 68       | 7, 11        |
| `screw.m6x16_countersunk` | 16       | 8            |
| `castor.brake`            | 4        | 8            |
| `screw.m8x35_socket`      | 4        | 8            |
| `washer.m8`               | 8        | 8            |
| `nut.m8_lock`             | 4        | 8            |
| `screw.m5x12_countersunk` | 144      | 9            |
| `cap.end_30`              | 8        | 10           |
| `plate.top`               | 1        | 11           |
| `bracket.plate`           | 20       | 11           |
| `screw.wood_4_5x16`       | 20       | 11           |
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

- Profiles cut to size by motedis, one piece each: 8 × 797
  (`profile.upright`), 4 × 1074 (`profile.bar_top`, `profile.bar_bottom`),
  8 × 375 (`profile.beam_depth`), all 30 × 30 B-type slot 8
  ([motedis 30x30][mo-30]). The cut list is `bom/cutlist.csv`.
- motedis' "M8" machining at **both ends of each of the 8 uprights**. motedis
  states no thread depth; the design takes 25 mm (`UNVERIFIED`, asked by
  email), and the bolts engage 20 mm at the bottom and 18 mm at the top.
- Angles 40 × 40 × 4, anodised ([motedis angle][mo-angle]): 9 bars of
  1980 mm, cut by motedis to 4 × 435 each ("Zuschnitt ganzer Stab"),
  36 pieces: 6 `angle.base`, 24 `angle.support`, 6 `angle.guard`. Their holes
  are drilled at home (step 3).
- Castor plates: motedis Aluminium Plättchen 8 × 90, EN AW-5083, one 740 mm
  bar cut to 4 × 90 ([motedis plate][mo-plate]), 4 pieces of 90 × 90 × 8. Their
  holes are drilled at home (step 4).
- Top plate: 21 mm birch plywood cut to 1114 × 483, grain along the 1114
  length (`docs/prices.md`); its corners are rounded at home (step 11).
- The through holes in the bars are drilled at home (step 1); motedis offers
  machining only at the profile ends.

### Tools

| Tool                                     | For                                                   |
| ---------------------------------------- | ----------------------------------------------------- |
| Hex keys 3, 4, 5 and 6 mm (or bits)      | M5 and M6 countersunk, M6 button and M8 socket screws |
| 13 mm spanner                            | The castors' lock nuts                                |
| Drill stand, 8.5 mm HSS bit              | Through holes in the bars, square to the profile      |
| 14 mm counterbore (or flat drill)        | Sinking the M8 heads in the top bars                  |
| 14 mm HSS bit                            | Corner bolt head hole in the castor plates            |
| 9 mm HSS bit                             | Castor bolt hole in the castor plates                 |
| 6.6 mm HSS bit                           | Clearance holes for M6 in the castor plates           |
| Drill, 5.5 mm HSS bit                    | Clearance holes in the angles                         |
| 90° countersink bit, at least 13 mm      | Countersinking the angles and the castor plates       |
| Deburring tool or fine file              | Cut ends and drilled holes                            |
| Steel square, tape measure, steel rule   | Marking and squaring                                  |
| Fine marker, centre punch                | Marking heights and holes                             |
| Spirit level, at least 600 mm            | Levels horizontal, uprights plumb                     |
| Two clamps, a few wooden blocks          | Holding a beam while a bracket or plate is fitted     |
| Medium threadlocker, optional            | The 16 M8 core bolts of the frames (step 6)           |
| Drill, 2.5 mm wood bit with a depth stop | Pilot holes in the top plate, at most 14 mm deep      |
| Jigsaw or rasp, sandpaper                | R10 corners and round edges of the top plate          |

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
| `profile.bar_top`    | 8.5 through | 15, 363, 711, 1059                  | top, 14 mm counterbore |
| `profile.bar_bottom` | 8.5 through | 15, 363, 711, 1059                  | underside              |

1. Lay the bars side by side, ends flush, and mark all four with the square in
   one go, so the holes of front and back match.
2. Punch, then drill 8.5 mm in the drill stand, square to the face, through
   the full 30 mm of each bar.
3. Counterbore the top bars from the top face, 14 mm, 8 mm deep, so the head
   of a `screw.m8x40_socket` sits flush (`UNVERIFIED`; try on the first hole).
4. Deburr.

**Check:** a bolt passes each hole square; laid end to end, front and back
holes line up.

## Step 2: Mark the uprights

**Parts:** `profile.upright` × 8.

1. Check that each upright is 797 long with an M8 core thread at both ends.
   Screw an M8 bolt into each thread by hand and measure how far it goes: it
   must take at least 22 mm, or the bolts of step 6 stop before the joint is
   tight (`UNVERIFIED` thread depth). Either end can be the bottom (`z` 163);
   the other is the top (`z` 960).
2. Name the uprights by position: front row `F0`, `F1`, `F2`, `F3` at `x` 0,
   348, 696, 1044 (left edge of the profile), back row `B0` to `B3` at the same
   `x`, `y` 405. Write the name on a piece of tape at the top end.
3. Measured from the bottom end (`z` 163 on the rack is 0 on the upright), mark
   on each face that carries angles (the inner `x` faces; `F1`, `F2`, `B1`,
   `B2` have two) the flat leg of each angle:

| Angle           | Level | Flat leg | Fixing leg on the upright | Mark on the upright (from bottom end) |
| --------------- | ----- | -------- | ------------------------- | ------------------------------------- |
| `angle.base`    | 1     | 163-167  | 163-203, leg up           | 0 (underside of flat leg, on the bar) |
| `angle.support` | 2     | 408-412  | 372-412, leg down         | 249 (top of flat leg)                 |
| `angle.support` | 3     | 545-549  | 509-549, leg down         | 386 (top of flat leg)                 |
| `angle.support` | 4     | 682-686  | 646-686, leg down         | 523 (top of flat leg)                 |
| `angle.support` | 5     | 819-823  | 783-823, leg down         | 660 (top of flat leg)                 |
| `angle.guard`   | guard | 956-960  | 920-960, leg down         | 797 (top end, under the top bar)      |

The `z` of a mark is the mark plus 163.

**Check:** 8 uprights, every mark on the same face of every upright; laid side
by side, the marks line up with the square.

## Step 3: Drill and countersink the angles

**Parts:** `angle.base` × 6, `angle.support` × 24, `angle.guard` × 6.

Each angle has 4 holes, 2 per end, in the leg that lies against the upright
(the vertical leg of `angle.base`, the hanging leg of the others), on the
centre line of the upright's slot, 15 mm from each end of the angle (`y` 15
and `y` 420), and 11 and 28 mm from the inner face of the flat leg. These hole
positions are a proposal of this guide (`UNVERIFIED`), chosen so the heads
clear the inner corner of the angle and the hole at 28 stays 8 mm from the tip
of the 40 mm leg.

| Angle           | Level | Hole centres, `z` |
| --------------- | ----- | ----------------- |
| `angle.base`    | 1     | 178, 195          |
| `angle.support` | 2     | 397, 380          |
| `angle.support` | 3     | 534, 517          |
| `angle.support` | 4     | 671, 654          |
| `angle.support` | 5     | 808, 791          |
| `angle.guard`   | guard | 945, 928          |

In the leg that means 11 and 28 from the flat leg for every angle, so one
template serves them all.

1. Mark one angle, punch, drill 5.5 mm. Use it as a drilling template for the
   others, clamped end to end and flat leg to flat leg.
2. Countersink each hole at 90° from the side that faces the box, that is the
   side away from the upright. Sink until the head of a
   `screw.m5x12_countersunk` sits flush or a hair below the surface; test on
   the first hole. The head is 2.5 mm high in the 4 mm leg, so 1.5 mm of
   aluminium stays under it.
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
| 9 through                          | (45, 45)                      | `screw.m8x35_socket` of the castor                          |
| 14 through                         | (15, 15)                      | Head of the corner upright's `screw.m8x50_socket`           |
| 6.6 through, countersunk 90° below | (60, 15), (80, 15)            | `screw.m6x16_countersunk` into the bar's bottom slot        |
| 6.6 through, countersunk 90° below | (15, 60), (15, 80)            | `screw.m6x16_countersunk` into the depth beam's bottom slot |

The pattern is symmetric about the plate's diagonal through the outer corner,
so all four plates are identical: for the other corners the plate is only
turned, never made as a mirror image.

1. Mark one plate, punch, drill in the drill stand, and use it as a template
   for the other three.
2. The 14 mm hole takes the ISO 4762 M8 head, 13 across and 8 high: in the
   8 mm plate it sits exactly flush with the underside. Try a bolt head in the
   first hole; a head that stands proud keeps the castor from sitting flat.
3. Countersink the four M6 holes from the underside (the side away from the
   profiles) until a `screw.m6x16_countersunk` sits flush or a hair below.
4. Deburr.

**Check:** a bolt head drops into the 14 mm hole and does not stand proud; an
M8 bolt passes the 9 mm hole; no M6 head stands proud underneath.

## Step 5: Hammer nuts

**Parts:** `tnut.m5` × 144, `tnut.m6` × 84.

All nuts are hammer nuts, so each can go in when its part is fitted; putting
the ones of a frame in before it stands up just saves bending later. Where
they go:

| Slot                                                            | Nuts                                 |
| --------------------------------------------------------------- | ------------------------------------ |
| Each inner `x` face of an upright that carries angles (12)      | 12 × `tnut.m5` (6 angles × 2 screws) |
| Inner `y` face of each upright, top end, under the top beam (8) | 1 × `tnut.m6`                        |
| Each top depth beam (4)                                         | 4 × `tnut.m6`                        |
| Each middle bottom depth beam, both sides (2)                   | 4 × `tnut.m6`                        |
| Inner faces of the bars, at each depth beam end (16 brackets)   | 1 × `tnut.m6`                        |
| Inner slot of the top bars, at each plate bracket (20)          | 1 × `tnut.m6`                        |
| Bottom slots of bar and depth beam under each castor plate (4)  | 4 × `tnut.m6`                        |

That is 144 `tnut.m5` for the angles (step 9) and 84 `tnut.m6`: 48 for the
24 brackets (2 each, step 7), 16 for the 4 castor plates (step 8) and 20 for
the plate brackets (step 11).

**Check:** count again before each step; a nut missing in a hidden spot is
added from the slot face.

## Step 6: Front and back frame

**Parts:** `profile.bar_bottom` × 2, `profile.bar_top` × 2,
`profile.upright` × 8, `screw.m8x50_socket` × 8,
`screw.m8x40_socket` × 8.

![Front](../renders/front.png)

Build each frame flat on the floor, outer face up. Nothing but the M8 core
bolts holds a frame square (`design.md` → *Joints*), so the upright ends must
sit flat and tight on the bars. If you use threadlocker, a medium-strength one
such as Loctite 243 (blue, can be undone with hand tools; `UNVERIFIED`), put a
few drops on the thread of each M8 bolt just before it goes in, and square and
tighten the frame before it sets.

1. **Bottom bar.** Lay a `profile.bar_bottom` (30 × 30) with its holes' head
   side down.
2. **Uprights.** Stand all four uprights (`F0` to `F3`, or `B0` to `B3`) on
   the bar's top face over the holes and bolt each with a
   `screw.m8x50_socket` from below into its core thread, 20 mm engaged. At the
   corners the head stays proud of the bar's underside; it sits in the castor
   plate's 14 mm hole in step 8.
3. **Top bar.** Lay a `profile.bar_top` on the top ends, counterbores up, and
   bolt all four uprights with a `screw.m8x40_socket` each, head sunk in the
   counterbore, 18 mm engaged.
4. Square the frame (diagonals equal within 1 mm), then tighten all eight M8
   bolts firmly with the hex key, checking the diagonals again after each.
   The bolts are stainless A2 (at least A2-50): firm, not brute force.

**Check:** each frame 1074 wide and 857 high (`z` 133-990 once on castors);
clear width 318 between neighbouring uprights at top and bottom; diagonals
equal within 1 mm; no gap between an upright end and its bar.

## Step 7: Join the frames

**Parts:** `profile.beam_depth` × 8, `bracket.inside_30` × 24,
`screw.m6x12_button` × 48.

One joint: one `bracket.inside_30` in the inside corner, each leg with one
`screw.m6x12_button` into a `tnut.m6` ([motedis Winkel][mo-winkel]). Tighten
firmly by hand with the hex key; do not use an impact driver, which can damage
the slot lips ([cnc-zubehoer][cnc-hm]).

1. Stand the front frame up, held by a helper object (a table, a wall), and the
   back frame 435 behind it.
2. **Bottom depth beams**, one under each upright pair, `z` 133-163, between
   the inner faces of the bottom bars, flush with the bars top and bottom;
   their tops are level with the upright feet (`z` 163).
3. **Top depth beams**, one over each upright pair, `z` 960-990, flush with
   the top bars.
4. **Brackets, 24 in all:**
   - Upright to top depth beam, 8: on the upright's inner `y` face, under the
     top depth beam.
   - Top depth beam to bar, 8: on the side of the top depth beam towards its
     bay in the corner with the bar's inner face, above the guard (within
     `z` 960-990).
   - Middle bottom depth beams to bar, 8: one on each side of each middle
     bottom beam, at both ends, in the corner with the bar's inner face
     (within `z` 133-163).
   No bracket sits on an upright face that carries an angle, so the angles
   stay clear.
5. **Corner bottom beams.** They have no bracket: the castor plate of step 8
   joins each to its bars. Until then hold each with a clamp across the bar
   and the beam, flush top and bottom, and go straight on to step 8.
6. Tighten in diagonal order, checking square as you go.

**Check:**

- Frame 1074 × 435 × 857; with the top plate 1114 × 483 at the top.
- Diagonals of the top and the bottom equal within 2 mm.
- Every upright plumb with the spirit level, both directions.

## Step 8: Castor plates and castors

**Parts:** `plate.castor` × 4, `screw.m6x16_countersunk` × 16, `tnut.m6` × 16,
`castor.brake` × 4, `screw.m8x35_socket` × 4, `washer.m8` × 8,
`nut.m8_lock` × 4.

1. Lay the frame on its back on a blanket, so the undersides of the bottom bars
   and the bottom depth beams are reachable.
2. **Plates.** Lay a `plate.castor` under each corner, outer corner flush with
   the frame corner, countersinks out, the corner bolt head in the 14 mm hole.
   Screw it with 4 `screw.m6x16_countersunk` into hammer nuts in the bottom
   slot of the bar (2) and of the depth beam (2). Now the plate holds the
   corner bottom beam; take the clamp off.
3. **Castors.** Put a `washer.m8` on a `screw.m8x35_socket` and push it from
   inside the castor's housing up through its back hole (11 mm). Hold the
   castor on the plate, the bolt through the plate's 9 mm hole, and put a
   `washer.m8` and a `nut.m8_lock` on the bolt from above, in the space beside
   the corner (`x` and `y` 30-60 from the corner). Hold the nut with the
   13 mm spanner and tighten the bolt with the 6 mm hex key until the castor
   sits firm. The bolt's tip ends a few millimetres above the nut, below the
   bars' top (`design.md` → *Joints*).
4. Stand the frame up on its castors and set the brakes.

**Check:** each plate flush with the frame's outer faces and flat under bar
and beam; every castor head (⌀46, `SECONDARY`) inside the frame outline seen
from above; every castor swivels freely with the brake off, the wheel may
swing out up to about 34 mm (`DERIVED`); every brake locks wheel and swivel;
the frame stands level; the bottom bars run `z` 133-163, the top at 990.

A plate taken off later, for instance to change a castor, frees its corner
bottom beam: clamp the beam first.

## Step 9: Angles, from the bottom up

**Parts:** `angle.base` × 6, `angle.support` × 24, `angle.guard` × 6,
`screw.m5x12_countersunk` × 144, `tnut.m5` × 144.

![Angle detail](../renders/angle_detail.png)

Each angle runs the full depth, `y` 0-435, and is held by 2 screws at each end
into the inner slot of a front and a back upright. Fit one level at a time,
from the bottom up:

1. **Level 1, `angle.base`, 6 pieces.** Flat leg at the bottom on the bottom
   bars (`z` 163-167), vertical leg up against the upright.
2. **Levels 2-5, `angle.support`, 6 per level.** Flat leg on top, hanging leg
   down along the upright; flat leg top at 412, 549, 686, 823.
3. **Guard, `angle.guard`, 6 pieces.** Same orientation, flat leg 956-960,
   just under the top bar.
4. Before tightening each angle, set the spirit level across the pair of
   angles of one column and on each angle along its length.

**Check, every level:**

- Flat leg height at front and back within 1 mm of the table in step 2.
- Clear width 310 between the two hanging legs (between the vertical legs at
  level 1) of each column, front and back; 238 between the leg tips.
- Both angles of a column at the same height.
- No screw head stands proud of the leg.
- The boxes slide on the bare aluminium: both ends of every flat leg that
  carries a box are deburred and their top edge slightly rounded, so a box
  pushed in from the front or the back does not catch.

## Step 10: End caps

**Parts:** `cap.end_30` × 8.

Press a `cap.end_30` into each end of the two top and the two bottom bars. The
other slots stay open.

**Check:** no sharp edge at hand height.

## Step 11: Top plate

**Parts:** `plate.top` × 1, `bracket.plate` × 20, `screw.m6x12_button` × 20,
`tnut.m6` × 20, `screw.wood_4_5x16` × 20.

![Side](../renders/side.png)

The plate is part of the structure: screwed to both top bars, plate and bar
act as one chord that carries most of the load of the middle uprights, so the
30 × 30 bottom bars need not (`design.md` → *Loads*). Fit it before any box
goes in. Each `bracket.plate` is a motedis Winkel 30 like the joint brackets,
held in the bar by one `screw.m6x12_button` into a swing-in `tnut.m6`, so
nothing is taken apart ([BM Profiles][bm-nuts]).

1. The plate: 1114 × 483 × 21 birch plywood, grain along the 1114 length,
   corners rounded R10. Break and sand all edges round; children will lean on
   it.
2. Fix a `bracket.plate` in the inner slot of each top bar with its centre
   at `x` 90, 165, 242, 317, 472, 632, 776, 850, 926 and 999: 10 at the front
   and 10 at the back, four in each outer column and two in the middle one,
   clear of the depth-beam brackets on the right of each upright. The free leg
   lies flush with the top of the bar (`z` 990). Snug the screws.
3. Lay the plate on top, 20 overhang at the sides and 24 at the front and the
   back, its top at 1011; mark through the bracket holes from below.
4. Lift off, pre-drill 2.5 mm at each mark, at most 14 mm deep (depth stop),
   so at least 5 mm of wood stays above the screw tip; lay the plate back and
   screw from below, 1 `screw.wood_4_5x16` per bracket.
5. Tighten the bracket screws.

**Check:** 20 screws in; the plate lies flat and does not rock; the overhang
is equal on opposite sides; nothing shows on top.

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
   two inserts stand right behind each handle, a closed grip pocket gripped
   from outside (`UNVERIFIED` until a box is measured).
3. Level 1 takes `box.e220`, levels 2-5 `box.e120`. Fill level 1 first. Each
   box goes in with its short side to the front; push it in until it is
   centred, 17.5 behind the front and the back face of the frame. Nothing stops
   it there: pushed on, it comes out at the other side.

![Inserts from above](../renders/inserts_top.png)

| Box                | Class | Layout  | Inserts                                    | ColorClip         |
| ------------------ | ----- | ------- | ------------------------------------------ | ----------------- |
| `L1.C1` to `L1.C3` | 220   | none    | none                                       | `clip.blue`       |
| `L2.C1` to `L2.C3` | 120   | half    | `insert.set_half`: 2 × 3613 (133 × 365)    | `clip.turquoise`  |
| `L3.C1` to `L3.C3` | 120   | half    | `insert.set_half`: 2 × 3613 (133 × 365)    | `clip.turquoise`  |
| `L4.C1` to `L4.C3` | 120   | quarter | `insert.set_quarter`: 4 × 1813 (133 × 182) | `clip.lightgreen` |
| `L5.C1` to `L5.C3` | 120   | quarter | `insert.set_quarter`: 4 × 1813 (133 × 182) | `clip.lightgreen` |

**Check, every box:** it slides in and out without catching, the rim runs
between the hanging legs; pulled out by 270 mm (`pull_out.travel`) to the
front or to the back it stays on its legs, and it comes out entirely at
400 mm (`pull_out.removal`).

## Final checks and moving the rack

- Levels horizontal across and along, every column.
- All 15 boxes in and centred, none rubbing.
- Every screw tight; check again after the first week of use.
- **M8 core bolts:** they alone keep the frames square. Check all 16 again
  after the first few moves and whenever the rack has been rolled far; a frame
  whose diagonals differ by more than 2 mm has a loose bolt.
- The rack stands free in the room, so a box can be pulled from both sides.
- **Brakes:** set all four where the rack stands, so it does not roll when a
  box is pulled.
- **Rolling:** release the brakes, take the boxes out or at least the heavy
  ones, push at the frame (not at a box), slowly over thresholds.

## Safety

- A box takes at most 25 kg, the maker's rating ([aidB 120][aidb-12],
  [aidB 220][aidb-22]). Keep the heavy boxes low.
- Each castor is rated 70 kg ([motedis castor][mo-castor]). The full rack in
  the design case, about 170 kg (`DERIVED`), on three
  castors of an uneven floor puts about 57 kg on each, 68 kg with a safety
  factor of 1.2 (`DERIVED`, see `design.md`).
- **Tipping:** an empty rack can tip forward (or backward) when a child hangs
  on a pulled-out box: the ASTM F2057-23 test load of 27.2 kg on the edge of
  one extended box tips it ([CPSC][cpsc-csu]; `DERIVED`, see `design.md`).
  The brakes stop rolling, not tipping. Fill the bottom level first and keep
  the rack loaded, pull one box at a time, never more than its 270 mm travel.
- Never load the rack without the top plate (step 11): without it the middle
  uprights hang on the 30 × 30 bottom bars alone.
- The rack is not made to be climbed or stood on.

## Open points

1. The box geometry used here (handle grip pocket, rim, ribs, foot width) is
   read from the product photos (`UNVERIFIED`); roadmap 0004 measures a box.
2. The angle hole positions (11 and 28 from the flat leg, 15 from each end) are
   a proposal (`UNVERIFIED`).
3. Through-hole alignment: drilled at home, a hole off the core axis puts the
   upright off its line; drill front and back bars together (step 1).
4. Counterbore depth in the 30 mm top bar is not yet tried (`UNVERIFIED`).
5. The depth of motedis' M8 core thread is not stated; 25 mm is assumed and
   checked by hand in step 2 (`UNVERIFIED`, asked by email).
6. The metal thickness at the castor's back hole is not in motedis' drawing;
   the M8x35 fits from 0 to 13 mm (`UNVERIFIED`).
7. The core-bolt joints' clamping force, tightening torque and the sideways
   load they hold are estimates (`UNVERIFIED`, `design.md` → *Joints*).

[mo-hm]: https://www.motedis.com/de/Hammermutter-B-Typ-Nut-8-M6
[mo-winkel]: https://www.motedis.com/de/Winkel-30-B-Typ-Nut-8
[mo-30]: https://www.motedis.com/de/Aluprofil-30x30-B-Typ-Nut-8
[mo-angle]: https://www.motedis.com/de/Winkelstange-eloxiert-40x40x4mm
[mo-plate]: https://www.motedis.com/de/Aluminium-Plaettchen-8x90-mm
[mo-castor]: https://www.motedis.com/de/Rolle-100-Rueckenloch-mit-Bremse
[bm-nuts]: https://www.bm-profile.com/de/ratgeber/nutensteine/
[cnc-hm]: https://www.cnc-zubehoer.eu/Edelstahl-Nutenstein-Hammermutter-Nut-8-M6-schmal/AP.HM.N8M6S.ES
[cpsc-csu]: https://www.cpsc.gov/Business--Manufacturing/Business-Education/Business-Guidance/Clothing-Storage-Units
[aidb-12]: https://www.ab-in-die-box.de/b2cde/euroboxen/nextgen/nextgen-2-0-cycle/eurobox-nextgen-2-0-cycle-griffe-geschlossen-400-x-300-x-120-mm-anthrazit.html
[aidb-22]: https://www.ab-in-die-box.de/b2cde/euroboxen/nextgen/nextgen-2-0-cycle/eurobox-nextgen-2-0-cycle-griffe-geschlossen-400-x-300-x-220-mm-anthrazit.html
