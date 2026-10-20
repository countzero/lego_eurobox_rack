# Assembly

How one person builds the rack. Every number is a copy of `design/rack.json`,
which wins where the two differ, and is provisional until the boxes are
measured (roadmap 0004). Parts are named by their ID from `design.md` →
*Contracts*; `x`, `y` and `z` are the rack's coordinates (`x` to the right,
`y` to the back, `z` up, origin on the floor at the front-left frame corner).
Columns count 1-3 from the left seen from the front, levels 1-4 from the
bottom.

![Three-quarter view](../renders/three_quarter.png)

> **Open issue, read before ordering.** As drawn, the inside brackets of the
> 12 `profile.beam_width` collide with the angles: on top of a bottom width
> beam the bracket fills `z` 130-160 at the upright, where `angle.base` lies
> (flat leg 130-133, vertical leg up to 180); under a top width beam it fills
> `z` 863-893, where the hanging leg of `angle.guard` lies (843-893). The
> brackets of the 8 `profile.beam_depth` are clear. Step 4 says what to do
> until the design is decided; see *Open points* at the end.

## Before you start

### Parts

| Part ID                   | Quantity | Used in step |
| ------------------------- | -------- | ------------ |
| `profile.upright`         | 8        | 1, 3, 4      |
| `profile.beam_width`      | 12       | 3, 4         |
| `profile.beam_depth`      | 8        | 3, 4         |
| `bracket.inside_30`       | 40       | 4            |
| `screw.m6x12_button`      | 80       | 4            |
| `tnut.m6`                 | 80       | 3, 4         |
| `castor.brake`            | 4        | 5            |
| `castor.plain`            | 4        | 5            |
| `screw.m8x25`             | 8        | 5            |
| `washer.m8_large`         | 8        | 5            |
| `angle.base`              | 6        | 2, 6         |
| `angle.support`           | 18       | 2, 6         |
| `angle.guard`             | 6        | 2, 6         |
| `screw.m5x10_countersunk` | 120      | 6            |
| `tnut.m5`                 | 180      | 3, 6, 8      |
| `tape.uhmw_25`            | 14640 mm | 7            |
| `panel.back`              | 1        | 8            |
| `panel.side`              | 2        | 8            |
| `screw.m5x10_button`      | 60       | 8            |
| `cap.end_30`              | 8        | 9            |
| `cover.slot_8`            | 4696 mm  | 9            |
| `box.e220`                | 6        | 10           |
| `box.e120`                | 6        | 10           |
| `insert.ek2`              | 1        | 10           |
| `insert.ek4`              | 10       | 10           |
| `insert.ek8`              | 24       | 10           |

Buy about ten spare `tnut.m5` and `tnut.m6`, plus ten M5 and ten M6 hammer
nuts for B-type slot 8. A hammer nut goes into an already closed slot from the
open slot face and turns 90° as the screw is tightened ([motedis][mo-hm],
[BM Profiles][bm-nuts]); a T-nut does not and must be in the slot before a
beam closes it. A forgotten T-nut is replaced by a hammer nut, not by taking
the frame apart.

### Order pre-machined

- Profiles cut to length, ends square and deburred: 8 × 823 (`profile.upright`),
  12 × 416 (`profile.beam_width`), 8 × 550 (`profile.beam_depth`). The cut list
  is `bom/cutlist.csv`.
- An M8 core thread in the **bottom end of each of the 8 uprights** only. The
  motedis profile offers the core thread as a machining option
  ([motedis 30x30][mo-30]). Ask for a thread depth of at least 20 mm, so the
  `screw.m8x25` has full engagement after the castor plate (`UNVERIFIED`; the
  castor plate thickness is not yet read).
- Angles 50 × 50 × 3 cut to 610: 6 `angle.base`, 18 `angle.support`,
  6 `angle.guard`. The holes are drilled at home (step 2).
- Panels cut to size: `panel.back` 1368 × 823, 2 × `panel.side` 613 × 823,
  3 mm aluminium composite. Holes are drilled at home (step 8).

### Tools

| Tool                                    | For                                             |
| --------------------------------------- | ----------------------------------------------- |
| Hex keys 3, 4 and 6 mm (or bits)        | M5 countersunk, M5 and M6 button heads, M8 bolt |
| Spanner or socket 13 mm                 | `screw.m8x25` (hex head)                        |
| Drill, 5.5 mm HSS bit                   | Clearance holes in the angles and panels        |
| 90° countersink bit, at least 12 mm     | Countersinking the angles                       |
| Deburring tool or fine file             | Cut ends and drilled holes                      |
| Steel square, tape measure, steel rule  | Marking and squaring                            |
| Fine marker, centre punch               | Marking heights and holes                       |
| Spirit level, at least 600 mm           | Levels horizontal, uprights plumb               |
| Two clamps, a few wooden blocks         | Holding a beam while a bracket is fitted        |
| Cutter knife, cloth, isopropyl alcohol  | UHMW tape                                       |

Work on a flat, clean floor with a blanket or cardboard under the profiles.

### Deburr

Deburr every cut end of profiles and angles, and both sides of every drilled
hole. A burr on a hanging leg catches the rim of a box; a burr on a beam end
keeps the joint from closing.

## Step 1: Prepare and mark the uprights

**Parts:** `profile.upright` × 8.

1. Check that each upright is 823 long and that the M8 core thread is in one
   end. That end is the bottom (`z` 100); the other is the top (`z` 923).
2. Name the uprights by position: front row `F0`, `F1`, `F2`, `F3` at `x` 0,
   446, 892, 1338 (left edge of the profile), back row `B0` to `B3` at the same
   `x`, `y` 580. Write the name on a piece of tape at the top end.
3. Measured from the bottom end (`z` 100 on the rack is 0 on the upright), mark
   on each face that will carry an angle (the inner faces; `F1`, `F2`, `B1`,
   `B2` have two) the top of each angle's fixing leg:

| Angle           | Level | Flat leg  | Fixing leg on the upright | Mark on the upright (from bottom end) |
| --------------- | ----- | --------- | ------------------------- | ------------------------------------- |
| `angle.base`    | 1     | 130-133   | 130-180, leg up           | 30 (underside of flat leg)            |
| `angle.support` | 2     | 374-377   | 327-377, leg down         | 277 (top of flat leg)                 |
| `angle.support` | 3     | 618-621   | 571-621, leg down         | 521 (top of flat leg)                 |
| `angle.support` | 4     | 754-757   | 707-757, leg down         | 657 (top of flat leg)                 |
| `angle.guard`   | guard | 890-893   | 843-893, leg down         | 793 (top of flat leg)                 |

The `z` of a mark is the mark plus 100. Mark the bottom frame (0-30) and the
top frame (793-823) as well: no angle T-nut may end up in these zones.

**Check:** 8 uprights, every mark on the same face of every upright; laid side
by side, the marks line up with the square.

## Step 2: Drill and countersink the angles

**Parts:** `angle.base` × 6, `angle.support` × 18, `angle.guard` × 6.

Each angle has 4 holes, 2 per end, in the leg that lies against the upright
(the vertical leg of `angle.base`, the hanging leg of the others). The holes
sit on the centre line of the upright's slot, 15 mm from each end of the angle
(`y` 15 and `y` 595), and 18 mm and 38 mm from the outside face of the flat
leg. These hole positions are a proposal of this guide (`UNVERIFIED`), chosen
so the heads clear the inner corner of the angle and stay within the 50 mm
leg.

| Angle           | Hole centres, `z`  |
| --------------- | ------------------ |
| `angle.base`    | 148, 168           |
| `angle.support` | level 2: 359, 339  |
| `angle.support` | level 3: 603, 583  |
| `angle.support` | level 4: 739, 719  |
| `angle.guard`   | 875, 855           |

1. Mark one angle, punch, drill 5.5 mm. Use it as a drilling template for the
   others of the same type, clamped end to end and flat leg to flat leg.
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

## Step 3: Load the slots with T-nuts

**Parts:** `tnut.m6` × 80, `tnut.m5` × 150 (the last 30 in step 8).

Every slot of a beam is closed at both ends by the uprights, and every face of
an upright that a beam meets is closed at 100-130 and 893-923. A T-nut that
belongs in such a slot goes in now, through the open end, before the joint is
made. Slide them in and park them in the middle; they are moved into place
later.

| Slot                                                        | T-nuts                                    |
| ----------------------------------------------------------- | ----------------------------------------- |
| Each inner face of an upright that carries angles (12)      | 10 × `tnut.m5` (5 angles × 2 screws)      |
| Same faces, for the width-beam brackets                     | 2 × `tnut.m6`, bottom and top bracket     |
| The face of each upright that meets depth beams (8)         | 2 × `tnut.m6`, bottom and top bracket     |
| Each beam, in the face that takes the brackets (20)         | 2 × `tnut.m6`, one near each end          |
| Outer face of the 4 outer `profile.beam_depth` (side panel) | 3 × `tnut.m5`                             |
| Back face of the 6 back `profile.beam_width` (back panel)   | 3 × `tnut.m5`                             |

That is 120 `tnut.m5` for the angles, 12 + 18 = 30 `tnut.m5` for the panels
on the beams, and 80 `tnut.m6`: 40 in the uprights (24 + 16) and 40 in the
beams. In an upright's inner face the order from the
bottom is: 1 `tnut.m6` (bottom bracket), 10 `tnut.m5` (angles), 1 `tnut.m6`
(top bracket).

The outer faces of the uprights (the outer `x` face of `F0`, `B0`, `F3`, `B3`
and the back face of `B0` to `B3`) stay open at the top end until the end caps
go on; their 30 panel T-nuts go in during step 8.

**Check:** count again, slot by slot. Each upright's inner face holds 12 nuts
(10 M5 between 2 M6).

## Step 4: Build the frame

**Parts:** `profile.upright` × 8, `profile.beam_width` × 12,
`profile.beam_depth` × 8, `bracket.inside_30` × 40, `screw.m6x12_button` × 80,
the `tnut.m6` loaded in step 3.

![Front](../renders/front.png)

One joint: the beam end butts square against the upright's face; one
`bracket.inside_30` sits in the inside corner, one leg on the beam, one on the
upright, each with one `screw.m6x12_button` into a `tnut.m6`
([motedis Winkel][mo-winkel]). Tighten firmly by hand with the hex key; do not
use an impact driver, which can damage the slot lips ([cnc-zubehoer][cnc-hm]).

Build two side ladders first, then join them, so you never hold more than one
loose profile:

1. **Left side ladder.** Lay `F0` and `B0` on the floor, inner faces up.
   Between them, a bottom `profile.beam_depth` with its underside flush with
   the bottom ends (`z` 100-130) and a top one flush with the top ends
   (`z` 893-923). Fit the brackets on top of the bottom beam and under the top
   beam. Repeat for the right ladder (`F3`, `B3`) and the two middle ladders
   (`F1`/`B1`, `F2`/`B2`).
2. **Check each ladder:** outside width 610 (`y` 0-610); diagonals equal
   within 1 mm; flat on the floor.
3. **Join with the width beams.** Stand the left ladder up, held by a helper
   object (a table, a wall). Fit the bottom front and bottom back
   `profile.beam_width` (`z` 100-130) to `F0`/`B0`, then the next ladder, then
   the top width beams (`z` 893-923). Continue to the right. Spacing: 446 mm
   centre to centre, 416 mm clear between uprights at every height.
4. **Width-beam brackets (open issue).** Where a width beam meets an upright,
   the bracket in the corner collides with the angles (see the note at the
   top). Until the design decides, fit the 24 width-beam brackets as follows
   and do not tighten yet: on the bottom beams, on the top face, and on the
   top beams, on the underside. Before step 6, hold an `angle.base` and an
   `angle.guard` in place: if they do not seat flat on the upright, the design
   fix of *Open points* is needed before going on.
5. Tighten all 80 screws, in diagonal order, checking square as you go.

**Check:**

- Frame 1368 × 610 × 823 (`z` 100-923 once on castors).
- Clear width 416 between neighbouring uprights, top and bottom, front and
  back.
- Diagonals of the front face, the back face, the top and the bottom equal
  within 2 mm.
- Every upright plumb with the spirit level, both directions.

## Step 5: Castors

**Parts:** `castor.brake` × 4, `castor.plain` × 4, `screw.m8x25` × 8,
`washer.m8_large` × 8.

1. Lay the frame on its back on a blanket (back face down), so the bottom ends
   are reachable.
2. Brake castors go under the 4 front uprights `F0` to `F3`, where the brakes
   can be reached; plain castors under `B0` to `B3`.
3. Put a `washer.m8_large` on a `screw.m8x25`, through the castor's back hole
   (11 mm, [Dold 75 brake][dold-75b]) into the upright's core thread. Tighten
   firmly.
4. Stand the frame up on its castors.

**Check:** the castor plate sits flat on the upright's end; every castor
swivels freely; the frame stands level, top beams checked with the spirit
level; the bottom beams are 100 above the floor and the top at 923.

## Step 6: Angles, from the bottom up

**Parts:** `angle.base` × 6, `angle.support` × 18, `angle.guard` × 6,
`screw.m5x10_countersunk` × 120, the `tnut.m5` in the uprights' inner faces.

![Angle detail](../renders/angle_detail.png)

Each angle runs the full depth, `y` 0-610, and is held by 2 screws at each
end into the inner slot of a front and a back upright. Fit them one level at a
time, from the bottom up, so the T-nuts not yet used sit above the work:

1. **Level 1, `angle.base`, 6 pieces.** Flat leg at the bottom, its underside
   at `z` 130 (top at 133), vertical leg up against the upright. Slide 2 nuts
   behind each end, screw in, snug.
2. **Levels 2-4, `angle.support`, 6 per level.** Flat leg on top, hanging leg
   down along the upright; flat leg top at 377, 621, 757.
3. **Guard, `angle.guard`, 6 pieces.** Same orientation, flat leg underside at
   890 (top 893), just under the top frame.
4. Before tightening each angle, set the spirit level across the pair of
   angles of one column and on each angle along its length.

**Check, every level:**

- Flat leg height at front and back within 1 mm of the table in step 1.
- Clear width 410 mm between the two hanging legs (between the vertical legs
  at level 1) of each column, at the front and at the back.
- Both angles of a column at the same height: spirit level across them.
- No screw head stands proud of the hanging leg.

## Step 7: UHMW tape on the carrying legs

**Parts:** `tape.uhmw_25`, 24 pieces of 610 mm (14640 mm).

The tape goes on the top of the flat leg of each `angle.base` and
`angle.support`, the 24 legs that carry a box. The guard carries nothing and
gets none.

1. Clean the flat leg with isopropyl alcohol and let it dry.
2. Cut 610 mm, peel a few centimetres of liner, and lay the tape from the
   front end along the outer edge of the flat leg, pulling the liner as you
   go. Press it down firmly with a cloth along the whole length.
3. Round the front corner of each piece with the knife, so a box pushed in
   does not lift the tape.

**Check:** no bubbles, no lifted corner; a box slides on it without catching.
Self-adhesive tapes reach full strength only after some time; leave the rack
unloaded overnight if the maker says so (`UNVERIFIED`).

## Step 8: Back and side panels

**Parts:** `panel.back` × 1, `panel.side` × 2, `screw.m5x10_button` × 60,
`tnut.m5` × 60 (30 already in the beams, 30 now).

The back panel is the back stop of the boxes and keeps the frame from racking;
the side panels close the sides.

1. **T-nuts in the uprights.** Through the open top ends, before the end caps,
   slide `tnut.m5` into the outer faces: the back face of `B0` and `B3`, 4 each;
   of `B1` and `B2`, 3 each; the outer side face of `F0`, `B0`, `F3`, `B3`,
   4 each.
2. **Holes.** Drill 5.5 mm holes in the panels to match:

| Panel        | Fixed to                         | Screws | Position                                      |
| ------------ | -------------------------------- | ------ | --------------------------------------------- |
| `panel.back` | each of 6 back width beams       | 18     | 60, 208 and 356 along each beam, slot centre  |
| `panel.back` | `B0`, `B3`                       | 8      | `z` 283, 436, 589, 742                        |
| `panel.back` | `B1`, `B2`                       | 6      | `z` 320, 512, 704                             |
| `panel.side` | each of 2 outer depth beams/side | 6      | `y` 100, 305, 510 (from the frame front)      |
| `panel.side` | front and back upright           | 8      | `z` 283, 436, 589, 742                        |

   That is 32 on the back and 14 on each side, spaced 150-200 mm.
3. **Back panel.** Lay it on the back, flush with the frame at the left, right,
   top and bottom (`z` 100-923), and fix the corners first, then the rest.
4. **Side panels.** Flush with the front face of the frame; at the back they
   cover the edge of the back panel (613 = 610 + 3).

**Check:** frame diagonals again (the panel now holds them); outer size
1374 × 613 × 923; no screw end reaches into a box path.

## Step 9: End caps and slot covers

**Parts:** `cap.end_30` × 8, `cover.slot_8` × 4696 mm.

1. Check that every T-nut is in; the end caps close the last open slot ends.
   Press a `cap.end_30` into the top end of each upright.
2. Cut `cover.slot_8` for the top faces of the top frame: 6 × 416 (top width
   beams) and 4 × 550 (top depth beams), 4696 mm in all, and press it in.
   Leave out the inner slots of the top width beams if the top plate is to
   follow (see below).

**Check:** no open slot on the top; no sharp edge at hand height.

## Step 10: Boxes and inserts

**Parts:** `box.e220` × 6, `box.e120` × 6, `insert.ek2` × 1, `insert.ek4` × 10,
`insert.ek8` × 24.

![Box pulled out](../renders/drawer_out.png)

1. Put the brakes on.
2. Levels 1 and 2 take the 220 class, `box.e220`; levels 3 and 4 the 120 class,
   `box.e120` (Auer, so the EK inserts fit). Each box goes in with its short
   side to the front and slides back until it meets the back panel; its front
   is then 5 mm behind the frame front.
3. Inserts: two rows across the 400 side, each 183 wide; the cells of a row
   run along the 600 side from the front. Row 1 is the left row, seen from the
   front.

![Inserts from above](../renders/inserts_top.png)

| Box     | Layout | Row 1 (left)  | Row 2 (right) |
| ------- | ------ | ------------- | ------------- |
| `L4.C1` | eight  | 4 × `ek8`     | 4 × `ek8`     |
| `L4.C2` | eight  | 4 × `ek8`     | 4 × `ek8`     |
| `L4.C3` | six    | 2 × `ek4`     | 4 × `ek8`     |
| `L3.C1` | six    | 2 × `ek4`     | 4 × `ek8`     |
| `L3.C2` | four   | 2 × `ek4`     | 2 × `ek4`     |
| `L3.C3` | three  | 1 × `ek2`     | 2 × `ek4`     |

**Check, every box:** it slides in and out without catching, the rim runs
between the hanging legs, and pulled out by 400 mm (`pull_out.travel`) it
tips up only slightly against the flat leg above; it comes out entirely at
600 mm (`pull_out.removal`).

## Final checks and moving the rack

- Levels horizontal across and along, every column.
- All 12 boxes in, slid fully back, none rubbing.
- Every screw tight; check again after the first week of use.
- **Rolling:** take the boxes out or at least the heavy ones, release all 4
  brakes, push at the frame (not at a box or a panel edge), and put the brakes
  on again where it stands.

## Fitting the top plate later

**Parts (planned):** `plate.top` × 1, `bracket.plate` × 10,
`screw.wood_4_5x12` × 20.

![Side](../renders/side.png)

The top frame stays open; the plate can be added without taking anything
apart, because the brackets come with swing-in nuts ([BM Profiles][bm-nuts]).

1. The plate: 1414 × 653 × 18 birch plywood, corners rounded R25. It
   overhangs the frame by 20 on all four sides; its top is at 941. Break and
   sand all edges round (a router with a small round-over bit, or sandpaper);
   children will lean on it.
2. Take out the slot cover from the inner slot (facing into the rack) of each
   of the 6 top width beams.
3. Swing a `bracket.plate` into those slots, 5 at the front and 5 at the back:
   one near each end of the rack and one per column, the bracket's free leg
   flush with the top of the beam (`z` 923). Snug the nuts.
4. Lay the plate on top, 20 overhang on each side; mark through the bracket
   holes from below.
5. Lift off, pre-drill 2.5 mm, at most 10 mm deep so the tip stays inside the
   18 mm plate; lay it back and screw from below, 2 `screw.wood_4_5x12` per
   bracket.
6. Tighten the bracket nuts.

**Check:** the plate lies flat, does not rock; the overhang is equal all
around; no screw tip on top.

## Safety

- A box takes at most 40 kg, the maker's limit for the NextGen boxes
  ([aidB 120][aidb-12], [aidB 228][aidb-22]). Keep the heavy boxes low; LEGO
  is dense.
- Put the brakes on before pulling a box. A box pulled out moves the centre of
  gravity forwards.
- Pull one box at a time; never let a child pull two levels at once.
- The rack is not made to be climbed or stood on, top plate or not.
- Each castor is rated 60 kg ([Dold 75 brake][dold-75b]); the rack with all
  boxes full must stay below that per castor.

## Open points

These are proposals for the design (roadmap 0002/0004), not decided:

1. Width-beam brackets against the angles (step 4). Options: fit the 12 width
   beams with hidden central connectors into the beam's core instead of inside
   brackets; or use flat connector plates on the outer front and back faces;
   or notch the angle ends. `design.md` → *Joints* also says the bracket sits
   "under a bottom beam and over a top beam", which is outside the uprights
   (`z` below 100 and above 923); it can only sit above a bottom beam and
   below a top beam.
2. Angle hole positions (18 and 38 from the flat leg, 15 from each end) and
   the countersink depth in 3 mm aluminium are not in `rack.json`.
3. Panel screw positions are not in `rack.json`; the split above adds up to
   the 60 of the catalog.

[mo-30]: https://www.motedis.com/de/Aluprofil-30x30-B-Typ-Nut-8
[mo-winkel]: https://www.motedis.com/de/Winkel-30-B-Typ-Nut-8
[mo-hm]: https://www.motedis.com/de/Hammermutter-B-Typ-Nut-8-M6
[bm-nuts]: https://www.bm-profile.com/de/ratgeber/nutensteine/
[cnc-hm]: https://www.cnc-zubehoer.eu/Edelstahl-Nutenstein-Hammermutter-Nut-8-M6-schmal/AP.HM.N8M6S.ES
[dold-75b]: https://www.dold-mechatronik.de/Lenkrolle-75-Rueckenloch-mit-Bremse
[aidb-12]: https://www.ab-in-die-box.de/b2bde/eurobox-nextgen-2-0-griffe-geschlossen-600-x-400-x-120-mm.html
[aidb-22]: https://www.ab-in-die-box.de/b2bde/eurobox-nextgen-2-0-griffe-geschlossen-600-x-400-x-220-mm.html
