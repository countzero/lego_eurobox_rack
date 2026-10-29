# Roadmap

## Goal

A rolling rack that holds 15 Euroboxes NextGen 2.0 Cycle 400 × 300
(ab-in-die-BOX) as LEGO drawers, the short side with the handle at the front:
3 columns, one level of 220 mm boxes at the bottom and four levels of 120 mm
boxes with inserts above, one long bar front and back, on 4 castors, without
panels, under a structural birch plywood top plate. It takes NextGen 2.0
boxes 400 × 300 only (0022, the user's choice).
Everything needed to buy the parts and build it is in this repository, and a
web viewer on GitHub Pages shows the rack in 3D with boxes that pull out.

## Steps

> [!IMPORTANT]
> This document is the one place that says what is planned, in which order,
> and how far each step has got.

### Working on a step

Every step has an ID that never changes. It names the branch `feature/<ID>`,
the worktree `.worktrees/<ID>/` and the `[<ID>]` prefix of its commits and pull
request (`docs/conventions.md` → *Steps and version control*). The rows are
sorted by ID; the order of work follows from the status.

- **Status** is one of *Done*, *In progress*, *Blocked by* (the IDs not yet
  *Done*), *Waiting for* (a step of the user), *Planned* and *Deferred*.
- The pull request that moves a step updates its row; the one that makes it
  *Done* removes its ID from every *Blocked by*, which becomes *Planned* once
  no ID is left.
- A step's section below is its specification: **Goal**, **Delivers** (the
  files it alone writes), **Acceptance** (what must be true for *Done*) and
  **Open** (facts still missing). A step writes only the files it delivers;
  `docs/roadmap.md` and `docs/sources.md` are updated when its pull request is
  merged.

| ID   | Step                                                         | Status               | PR                                                            |
| ---- | ------------------------------------------------------------ | -------------------- | ------------------------------------------------------------- |
| 0001 | [Repository and roadmap](#0001-repository-and-roadmap)       | Done                 | [#1](https://github.com/countzero/lego_eurobox_rack/pull/1)   |
| 0002 | [Rack specification](#0002-rack-specification)               | Done                 | [#2](https://github.com/countzero/lego_eurobox_rack/pull/2)   |
| 0003 | [Blender model and renders](#0003-blender-model-and-renders) | Done                 | [#6](https://github.com/countzero/lego_eurobox_rack/pull/6)   |
| 0004 | [Measure the boxes](#0004-measure-the-boxes)                 | Done                 | [#32](https://github.com/countzero/lego_eurobox_rack/pull/32) |
| 0005 | [Insert plan](#0005-insert-plan)                             | Done                 | [#4](https://github.com/countzero/lego_eurobox_rack/pull/4)   |
| 0006 | [Parts and cut list](#0006-parts-and-cut-list)               | Done                 | [#3](https://github.com/countzero/lego_eurobox_rack/pull/3)   |
| 0007 | [Price comparison](#0007-price-comparison)                   | Done                 | [#8](https://github.com/countzero/lego_eurobox_rack/pull/8)   |
| 0008 | [Assembly guide](#0008-assembly-guide)                       | Done                 | [#7](https://github.com/countzero/lego_eurobox_rack/pull/7)   |
| 0009 | [Web viewer](#0009-web-viewer)                               | Done                 | [#5](https://github.com/countzero/lego_eurobox_rack/pull/5)   |
| 0010 | [Width-beam joints](#0010-width-beam-joints)                 | Done                 | [#12](https://github.com/countzero/lego_eurobox_rack/pull/12) |
| 0011 | [ColorClip picker](#0011-colorclip-picker)                   | Done                 | [#10](https://github.com/countzero/lego_eurobox_rack/pull/10) |
| 0012 | [Photorealistic boxes](#0012-photorealistic-boxes)           | Done                 | [#13](https://github.com/countzero/lego_eurobox_rack/pull/13) |
| 0013 | [Viewer lighting](#0013-viewer-lighting)                     | Done                 | [#18](https://github.com/countzero/lego_eurobox_rack/pull/18) |
| 0014 | [Castor plates, open back](#0014-castor-plates-open-back)    | Done                 | [#12](https://github.com/countzero/lego_eurobox_rack/pull/12) |
| 0016 | [Ribbed boxes, top plate](#0016-ribbed-boxes-top-plate)      | Done                 | [#16](https://github.com/countzero/lego_eurobox_rack/pull/16) |
| 0017 | [No joint plates](#0017-no-joint-plates)                     | Done                 | [#15](https://github.com/countzero/lego_eurobox_rack/pull/15) |
| 0018 | [Every part in the model](#0018-every-part-in-the-model)     | Done                 | [#22](https://github.com/countzero/lego_eurobox_rack/pull/22) |
| 0019 | [Viewer controls](#0019-viewer-controls)                     | Done                 | [#19](https://github.com/countzero/lego_eurobox_rack/pull/19) |
| 0020 | [Exploded view](#0020-exploded-view)                         | Done                 | [#23](https://github.com/countzero/lego_eurobox_rack/pull/23) |
| 0021 | [Model size](#0021-model-size)                               | Done                 | [#27](https://github.com/countzero/lego_eurobox_rack/pull/27) |
| 0022 | [Switch to motedis](#0022-switch-to-motedis)                 | Done                 | [#28](https://github.com/countzero/lego_eurobox_rack/pull/28) |
| 0023 | [Angle-bracket frame](#0023-angle-bracket-frame)             | Done                 | [#30](https://github.com/countzero/lego_eurobox_rack/pull/30) |

0003, 0005, 0006, 0007, 0008 and 0009 write disjoint files and run in one wave
once 0002 is *Done*, each in its own worktree. They agree through the contracts
0002 fixes: part IDs, CSV columns, render names and the names of the model's
objects. 0004 needs a caliper or the makers' answer and corrects
`design/rack.json` afterwards; the first release after it is 1.0.0.

## 0001 Repository and roadmap

**Goal:** the repository, its rules and this roadmap, so every later step has a
specification and a place.

**Delivers:** `AGENTS.md`, `README.md`, `docs/roadmap.md`,
`docs/conventions.md`, `docs/releases.md`, `docs/worktrees.md`,
`docs/sources.md`; on `main` before it: `LICENSE` (MIT), `.gitattributes`,
`.gitignore`.

**Acceptance:**

- The public repository `countzero/lego_eurobox_rack` has `main` and
  `develop`, `develop` as the default branch, merge commits only and automatic
  branch deletion off.
- GitHub detects the license as MIT.
- `docs/sources.md` holds every fact of the research so far with its status and
  URL.

## 0002 Rack specification

**Goal:** every dimension of the rack in one machine-readable file, and the
contracts the wave needs.

**Delivers:** `design/rack.json`, `docs/design.md`.

- `rack.json`: the box envelope, frame, profiles, angles, castors, panels, the
  level heights, the top plate (planned, not built) and the part catalog with
  IDs and quantities. Millimetres, integers where the part is cut.
- `design.md`: the decisions with their reasons, the dimensions as tables and
  ASCII drawings, and the contracts:
  - part IDs (`profile.upright`, `angle.support`, …) used by 0006, 0007, 0008;
  - the columns of `bom/parts.csv` and `bom/cutlist.csv`;
  - the render file names under `renders/` used by 0003, 0008 and `README.md`;
  - the object names and glTF extras of the exported model used by 0003 and
    0009, including each box's level, column, nominal height and pull-out
    travel.

**Acceptance:**

- A NextGen 2.0 box (600 × 400 × 120 and × 228) and an Auer EG box
  (600 × 400 × 120 and × 220) fit every level on paper: rim within the clear
  width, foot on both supports at any sideways position, height under the tip
  guard.
- Each value in `design.md` that comes from outside names its source entry.

## 0003 Blender model and renders

**Goal:** a model built only from `design/rack.json`, renders for the documents
and the export for the web viewer.

**Delivers:** `blender/build_rack.py`, `blender/export_web.py`,
`blender/rack.blend`, `renders/*.png`, `web/rack.glb`.

**Acceptance:**

- `build_rack.py` runs headless (`AGENTS.md` → *Tools*) and writes
  `rack.blend` and the renders; a second run gives the same files.
- Collections: frame, angles, castors, panels, boxes, inserts, top plate (hidden
  in the renders).
- Renders: front, side, three-quarter, one box of level 3 pulled out, top view
  of the inserts; names as fixed by 0002.
- `export_web.py` writes `web/rack.glb` with the object names and extras of
  0002.

## 0004 Measure the boxes

**Goal:** the numbers no maker publishes, measured on the NextGen 2.0 boxes
the rack holds, so the angles and clearances rest on measurements.

**Delivers:** `design/rack.json`, `blender/build_rack.py`,
`blender/rack.blend`, `renders/*.png`, `web/rack.glb`, `docs/design.md`,
`docs/assembly.md`, `docs/roadmap.md`, `README.md`.

**Acceptance:**

- Measured by the user on a C2G43-12 and a C2G43-22 (2026-10-28): the outer
  size at the rim (398 × 298), the height with the foot (120, 220), the
  section of the wall from rim to foot (flanges, panel, shoulder, bottom band,
  cross ribs) and the foot (the flat floor 264 × 364, 5 high, 17 in from the
  outline); every value is `MEASURED`, `DERIVED` or `UNVERIFIED` in
  `rack.json` and `docs/design.md`.
- The frame stays (the user's option A): 310 between the hanging legs, 238
  between the leg tips. `foot_width_min` is 264 in place of 282: 13 on each
  leg centred, at least 7 pushed to one side, the user's agreement in place of
  the 15 of 0022. The box envelope (rim 296–305 × 394–405) is unchanged.
- The boxes stand centred at `y` 18.5 ((435 - 398) / 2), spanning
  18.5–416.5; *Fit check* and *Loads* follow, the tipping lever corrected to
  the 75 mm castor of 0023 on the way.
- The model draws the measured section; the build stops unless every box is
  398 × 298 × its height at the rim, the inner top is 365 × 265 and no insert
  reaches through a box wall.
- `build_rack.py` runs headless and a second run gives the same files;
  `npm --prefix web run build` runs clean and `web/rack.glb` deflated stays at
  or below 110 kB. The pull request reports its size.
- The pull request lists the `sources.md` rows to add on merge and the rows
  they supersede.

**Open:** the relief on the walls (rib pairs, corner webs, pin blocks), the
handle (frame, tray, grip pocket), the corner radii and whether the foot's
face is flush with the panel's bottom stay read from the photos
(`UNVERIFIED`). Auer boxes and inserts are no longer tried: the rack takes
NextGen 2.0 boxes only since 0022.

## 0005 Insert plan

**Goal:** the coarse division of the six 120 mm boxes, with inserts that fill
the box without filler pieces.

**Delivers:** `docs/inserts.md`.

**Acceptance:**

- Auer EK x/100 inserts (EK 2, EK 4, EK 8) as the system; each layout drawn in
  ASCII with its sizes, compartments and price.
- A mix for the six boxes and its total, and which box brand each layout is
  confirmed for.
- What goes where, from a LEGO sorting guide.

## 0006 Parts and cut list

**Goal:** what to order and how to cut it, generated from `design/rack.json`.

**Delivers:** `bom/build_bom.py`, `bom/parts.csv`, `bom/cutlist.csv`,
`bom/README.md`.

**Acceptance:**

- `build_bom.py` writes both CSV files from `rack.json` alone, with the columns
  of 0002, and a second run gives the same files.
- The cut list packs the cuts into stock lengths and states the waste.

## 0007 Price comparison

**Goal:** the cheapest sound way to buy every part of the catalog in 0002.

**Delivers:** `docs/prices.md`.

**Acceptance:**

- For every part ID: at least two suppliers where they exist, price incl. VAT,
  unit, status and URL, checked on the date stated.
- Shipping per supplier and the cheapest order split, with a total.
- NextGen and Auer boxes compared by price.

## 0008 Assembly guide

**Goal:** a build that one person can follow.

**Delivers:** `docs/assembly.md`.

**Acceptance:**

- Steps in order, each with the part IDs and quantities of 0002, the tools and
  a check; renders referenced by the names of 0002.
- The top plate's later fitting as a section of its own.

## 0009 Web viewer

**Goal:** the rack in 3D in the browser, one self-contained `index.html`, with
boxes that pull out, published on GitHub Pages as the repository's website.

**Delivers:** `web/package.json`, `web/package-lock.json`, `web/build.mjs`,
`web/src/*`, `.github/workflows/pages.yml`, `docs/web_viewer.md`.

**Acceptance:**

- `npm --prefix web run build` bundles three.js, the viewer and
  `web/rack.glb` (deflated) into `web/dist/index.html`, which opens by
  double-click with no network access.
- Orbit, pan and zoom; front, side and top views; reset.
- A click on a box pulls it out along its travel and a second click pushes it
  back; one button pulls out all or none.
- The top plate can be shown and hidden.
- The workflow builds the page on every push to `main` and deploys it to
  GitHub Pages; the repository's website points to
  `https://countzero.github.io/lego_eurobox_rack/`.
- Until 0003 is merged the viewer is tested with a stand-in model that follows
  the names of 0002.

## 0010 Width-beam joints

**Goal:** joints for the 12 width beams that leave the upright faces free for
the angles, found while writing the assembly guide (0008). The 400 × 300
redesign of 2026-10-21 removes the collision: its brackets sit off the angle
faces.

**Delivers:** changes to `design/rack.json` (parts and joints) and
`docs/design.md` → *Joints*; the model, the parts list, the prices and the
assembly guide generated or updated to match.

**Acceptance:**

- No connector of a width beam overlaps `angle.base` (130–180) or the hanging
  leg of `angle.guard` (843–893) on any upright face.
- The candidates are compared with price and source: a central connector
  („Automatik-Verbinder“) in the beam end with an access bore in the upright,
  connector plates on the outer faces, or notched angle ends.
- `docs/assembly.md` and `bom/` agree with the chosen joint.

**Open:** which joint the user prefers; the machining the shops offer for it.

## 0011 ColorClip picker

**Goal:** the ColorClip colour of each level chosen in the web viewer from the
nine colours aidB sells, with presets and a link that shares the choice, so the
colours are settled before the model and the order follow them.

**Delivers:** `design/rack.json` (`color_clips`: the nine colours and the
presets), `web/src/*`, `docs/web_viewer.md`, `docs/design.md` → *Inserts and
ColorClips*.

**Acceptance:**

- A ColorClips panel shows one row per level with the nine colours as
  swatches; a pick recolours the rings of that level's three boxes.
- "Current" (`color_clips.levels`) and five presets set all levels in one
  click.
- The choice lives in the URL fragment, `#clips=<L1>,…,<L5>`, read on load and
  on every change of the fragment and written on every pick; a link restores
  it, offline too.
- The panel names the packs to order per colour and the weakest step between
  neighbouring levels (CIEDE2000).
- The palette and the presets are read from `rack.json` at build time;
  `web/rack.glb`, the Blender model and the parts list stay unchanged.

**Open:** the rings' real colours. aidB publishes no RAL code, so the sRGB
values are read from its product photos (`UNVERIFIED`).

## 0012 Photorealistic boxes

**Goal:** boxes and renders that look like the NextGen 2.0 Cycle in aidB's
photos: rounded corners and bevelled edges, the inner wall tapered towards the
floor, the rounded handle opening with its frame and the ColorClip ring, the
insert trays tapered like the box, a plastic material, and renders with studio
light.

**Delivers:** `blender/build_rack.py`, `blender/rack.blend`, `renders/*.png`,
`web/rack.glb`, `design/rack.json` (`box_shape` and the insert taper),
`docs/design.md` → *Box shape in the model*.

**Acceptance:**

- `build_rack.py` runs headless and a second run gives the same files, checked
  by hash.
- The build stops unless every box is 400 × 300 × its height outside, the inner
  top is 365 × 265 and no insert reaches through a box wall.
- Every new `box_shape` value names its status; the pull request lists the
  `sources.md` rows to add on merge.
- The renders keep their names and views; EEVEE without ray tracing, AgX.
  Cycles on the CPU was tried first and dropped: about 4.5 minutes against
  about 6 seconds for nearly the same look.
- `web/rack.glb` keeps the node names, extras and material names of 0002 and
  0011, and stays under twice its size before the step (355 KB).

**Open:** the real shape values (0004, or a drawing from Müller & Sohn).

## 0013 Viewer lighting

**Goal:** the web viewer shows the plastic and the aluminium as the Blender
renders do.

**Started:** AgX tone mapping and a `RoomEnvironment` are in `web/src/main.js`
(work no step owned, on `develop`), so the aluminium no longer renders black;
the colour match by eye is still open.

**Delivers:** `web/src/*` (but `icons.js`, `ui.js`, `a11y.js`, `index.html`,
`style.css`), `docs/web_viewer.md` → *Performance* and the shading line of
*What it does*.

**Acceptance:**

- AgX tone mapping and a `RoomEnvironment` light the model; the page still
  opens offline.
- The tone mapping is a port of Blender's AgX with the look of the renders
  (`build_rack.py`: "AgX - Punchy"), not three.js's own AgX.
- The render path of the house viewer: no canvas MSAA; 4× MSAA on half-float
  targets at a pixel ratio of at most 1 while anything moves; 32 TAA samples
  gathered once the view is still; nothing drawn while nothing changes; the
  shadow map redrawn only on a change; no orbit damping; the middle button
  pans.
- The box, ring and insert colours match the renders by eye.

## 0014 Castor plates, open back

**Goal:** a lower rack on four plain 100 mm castors whose heads stay inside the
frame outline, with no back stop, so every box pulls out to the front and to
the back, and loads checked against cited rules.

**Delivers:** `design/rack.json` (frame heights, castors, castor plates,
joints, parts, `box_position`, `pull_out`, schema 3), `docs/design.md` (all but
*Box shape in the model*), `docs/assembly.md`, `docs/prices.md`, `README.md`,
`blender/build_rack.py` (frame, castors, stops, box extras), `blender/rack.blend`,
`renders/*.png`, `web/rack.glb`, `bom/parts.csv`, `web/src/main.js`,
`web/src/index.html`, `docs/web_viewer.md`.

**Acceptance:**

- Four `castor.plain` (Dold 69483: 100 mm, 125 mm high, 70 kg, back hole
  11 mm, offset 28 mm), no `castor.brake`. Each is bolted into a
  `plate.castor` (90 × 90 × 10 EN AW-5083) screwed under the bottom bar and the
  bottom depth beam, castor centre 45 mm from both outer faces; seen from above
  the castor head stays inside the frame.
- The bottom depth beams sit flush with the underside of the bottom bars; every
  height follows `castor_height` plus the plate: frame 1068 × 435 × 1016,
  level floors 198, 442, 578, 714, 850; cut lengths unchanged.
- No connector overlaps another part, and none sits on an upright face that
  carries an angle (the check of 0010, which this step closes): the bottom
  depth-beam brackets, the corner M8 bolts in the plates' clearance holes, the
  castor bolts and the joint plates are drawn in the model and the assembly
  guide.
- No `bracket.stop`; the boxes stand centred at `y` 17.5 and pull out 270 mm
  to the front and to the back; the box envelope of `docs/design.md` is
  unchanged.
- `docs/design.md` → *Loads* gives the frame mass, the LEGO density with
  sources (low 0.25, typical 0.40, design 0.60 kg/l), the castor load by
  Blickle's rule, the bottom bar sag and the tipping forwards and backwards
  without brakes against EN 14749 and ASTM F2057-23.
- The web viewer pulls a box out to the side that was clicked; "All out" pulls
  to the front; the box extra `sides` and `rack_schema` 3 are documented in
  `docs/design.md` → *Contracts*.
- `build_rack.py` runs headless and a second run gives the same files;
  `build_bom.py` and `npm --prefix web run build` run clean.

**Open:** the castor head diameter (Ø46 from motedis' drawing, `SECONDARY`);
the thread engagement of M8 in a 10 mm aluminium plate; the castor's
non-marking tread; the empty rack tips under a 27.2 kg child on an extended
box. 0012 changes the same model files: the step merged second rebuilds
`rack.blend`, the renders and `rack.glb`.

## 0016 Ribbed boxes, top plate

**Goal:** boxes whose outer walls carry the moulded relief of aidB's photos,
the planned birch plywood top plate drawn as oiled plywood and shown in the
renders, studio light that makes the relief readable, and the ColorClips set
to one colour per insert type (blue, turquoise, turquoise, light green, light
green from L1 up).

**Delivers:** `blender/build_rack.py`, `blender/export_web.py`,
`blender/rack.blend`, `renders/*.png`, `web/rack.glb`, `design/rack.json`
(`box_shape`, `top_plate`, `color_clips.levels`, `color_clips.rule`, the
preset "Complementary steps" in place of "Harmonious cool", the `clip.*`
parts), `bom/parts.csv`, `docs/design.md` → *Box shape in the model*,
*Dimensions* (top plate), *Renders*, *Inserts and ColorClips*, *Part IDs* and
material names, `docs/inserts.md` → *ColorClips*, `docs/assembly.md` (clip
parts), `docs/prices.md` (clip note), `docs/web_viewer.md` (example),
`README.md` (render caption).

**Acceptance:**

- The outer wall shows thin rib webs with open pockets between them, a ledge
  lip, a recessed collar, pin blocks next to the corners, a
  chamfer from the foot band to the panel and a handle with a raised frame, a
  recessed tray and a lip round the opening, as in aidB's photos of C2O43-12
  and C2O43-22.
- The build stops unless every box is 400 × 300 × its height outside, the
  inner top is 365 × 265 and no insert reaches through a box wall; the box
  envelope of `docs/design.md` is unchanged.
- The top plate has R25 corners (`top_plate.corner_radius`), broken edges, an
  oiled birch face and 13 plies on its edges, drawn with built-in shader nodes
  and no image file; it shows in every render but `inserts_top`.
- The renders keep their names and views; EEVEE with ray tracing at fixed
  settings, AgX.
- `build_rack.py` runs headless; a second run gives the same meshes, objects
  and materials in `rack.blend` and the same `rack.glb` by hash. The renders
  differ by at most 1 of 255 in under 2 % of their pixels (screen-space ray
  tracing); the bytes of `rack.blend` differ between runs on `develop`
  already.
- `web/rack.glb` keeps the node names, extras and material names of 0002 and
  0011, shows the plate in its plain `plywood` colour and stays under 1 MB
  (708 KB before the step).
- Model, renders, parts list and documents use the ColorClips of
  `color_clips.levels`; the web viewer opens with them, the same choice as
  `#clips=blue,turquoise,turquoise,lightgreen,lightgreen`.
- Every new `box_shape` and `top_plate` value names its status; the pull
  request lists the `sources.md` rows to add on merge.

**Open:** the real relief values (0004); the ply count and finish of the plate
until it is bought. This step supersedes 0003's "top plate hidden in the
renders" and 0012's "EEVEE without ray tracing".

## 0017 No joint plates

**Goal:** front and back frames held square by the M8 core bolts of the
upright joints alone, without the 16 joint plates, whose real chamfered webs
would stand in the way of the level 1 and level 5 boxes at the front and the
back.

**Delivers:** `design/rack.json` (`frame.joint_plate`, `outer`, the parts
`plate.joint_l`, `plate.joint_t`, `screw.m6x10_socket`, `tnut.m6`),
`blender/build_rack.py` (joint plates), `blender/rack.blend`, `renders/*.png`,
`web/rack.glb`, `bom/parts.csv`, `docs/design.md` (*Decisions*, *Dimensions*,
side view, *Joints*, *Loads*, *Part IDs*, node table), `docs/assembly.md`,
`docs/prices.md`, `README.md`.

**Acceptance:**

- No `plate.joint_l`, `plate.joint_t` or `screw.m6x10_socket` in `rack.json`,
  the parts list, the model or `web/rack.glb`; `tnut.m6` is 72 (56 for the
  brackets, 16 for the castor plates).
- The outer size is 1068 × 435 × 1016 in `rack.json`, the scene's `outer_mm`,
  the documents and the README.
- The top plate keeps its size and place.
- `docs/design.md` says why the core-bolt joints suffice, with the joint
  estimate marked `UNVERIFIED`; *Loads* follows the lower mass.
- The assembly guide squares and tightens the frames without plates, names a
  medium-strength threadlocker (Loctite 243) on the 16 M8 core bolts as
  optional and `UNVERIFIED`, and checks the bolts again after the first moves.
- `build_rack.py` runs headless and a second run gives the same `rack.blend`
  and `rack.glb`; `build_bom.py` and `npm --prefix web run build` run clean.

**Open:** the clamping force and tightening torque of an M8 in the core
thread; whether the frames stay square after rolling. 0016 changes the same
model files and `rack.json`: the step merged second rebuilds `rack.blend`, the
renders and `rack.glb`.

## 0018 Every part in the model

**Goal:** the model holds every part ordered for the build at its real shape
and place, so the renders and the viewer show what is bought.

**Delivers:** `blender/build_rack.py`, `blender/export_web.py`,
`blender/rack.blend`, `renders/*.png`, `web/rack.glb`, `design/rack.json`
(shapes of screws, nuts, washers, brackets and caps), `web/src/main.js`,
`docs/design.md` → *Contracts*, `docs/web_viewer.md`.

**Acceptance:**

- Every `build` part of `rack.json` is drawn; each object names its part ID,
  and the build stops unless the count per ID equals the parts list.
- Screws, hammer nuts and washers sit in their holes with the heads where the
  assembly guide puts them, each a child of the part it holds; the castor
  plates and the angles show their holes, the brackets the shape of motedis
  S8BBR30; the end caps sit on the ends of the four bars.
- Fasteners and caps carry `{ "kind": "fastener" | "cap", "part": "<id>" }`
  in `web/rack.glb`.
- Every shape value names its status; the pull request lists the `sources.md`
  rows to add on merge.
- Parts of one kind share one mesh; a click in the viewer passes through
  fasteners and caps to the boxes. The pull request reports the size of
  `web/rack.glb`; the 1 MB limit moves to 0021.
- `build_rack.py` runs headless and a second run gives the same files.

**Open:** the brackets' hole offset (motedis CAD); the counterbore depth of the
top bars.

## 0019 Viewer controls

**Goal:** the web viewer's controls as icon buttons with keys, a full-screen
toggle on touch screens, and the whole page meeting WCAG 2.2 Level AA.

**Delivers:** `web/package.json`, `web/package-lock.json`, `web/build.mjs`,
`web/src/*` (but `agx.js` and `view.js`), `docs/web_viewer.md`,
`docs/accessibility.md`.

**Acceptance:**

- The toolbar reads reset | colours | full screen, as the Font Awesome Free
  icons `rotate-left`, `palette` and `expand` (`compress` while full screen),
  inlined at build time; each button is named for a screen reader and shows
  its name and key on hover and focus.
- Esc first hides a shown hint, then closes the ColorClips panel when the
  focus is in it, and otherwise resets; C shows or hides the panel while the
  view or a toolbar button has the focus.
- The full-screen button shows only on a touch screen whose browser grants
  full screen to the page.
- The title and the storage volume sit on a panel, so their contrast does not
  depend on the scene behind them.
- Every box opens and closes by keyboard, and orbit and zoom work by keyboard
  and without dragging or pinching; the page meets WCAG 2.2 Level AA, checked
  as `docs/accessibility.md` describes.
- `npm --prefix web run build` runs clean and the page still opens offline.

## 0020 Exploded view

**Goal:** the rack drawn apart, every part moved out of its place along a
clear direction, in Blender and in the web viewer, so it shows how the rack
goes together.

**Delivers:** `design/rack.json` (`explode`), `blender/build_rack.py`,
`blender/export_web.py`, `blender/rack.blend`, `renders/*.png`,
`web/rack.glb`, `web/src/*` (but `agx.js`), `docs/design.md` → *Renders* and
*Model objects and the web export*, `docs/web_viewer.md`,
`docs/accessibility.md`, `README.md` (render list).

**Acceptance:**

- `rack.json` → `explode` holds the move of each group in mm: top plate up,
  plate brackets up, top bars and top depth beams up, front frame forward and
  back frame back, angles towards the middle of their bay, castor plates and
  castors down, end caps out along their bar, screws out of their hole along
  their own axis, hammer nuts and washers the opposite way, and the boxes with
  their inserts and rings forward along `pull_axis`, clear of the frame.
- In Blender a scene property `explode` from 0 to 1 moves every part between
  its place and its exploded place through simple-expression drivers, which
  run without Python auto-run; `rack.blend` is saved at 0.
- `renders/exploded.png` shows the rack at 1, three-quarter from the front.
- Every exported node that moves carries `explode` as an offset from its home
  in glTF axes, relative to its parent; `web/rack.glb` holds the rack at 0.
- The toolbar reads reset | colours | explode | full screen; explode is the
  Font Awesome Free solid icon `bomb`, inlined at build time like the others,
  a toggle with `aria-pressed` under the constant name "Explode", key E,
  "Explode E" on hover and focus, announced as "Exploded" or "Assembled".
- Exploding closes open boxes first; a click on a box while exploded
  assembles the rack; Reset (Esc) assembles it too. The move takes 0.6 s with
  the box easing and jumps under `prefers-reduced-motion`.
- The shadows, the ground and the camera fit take in the exploded rack; clicks
  still pass through fasteners and caps.
- The page meets WCAG 2.2 Level AA in both states, checked as
  `docs/accessibility.md` describes, at 320 × 256 and 390 × 844 with four
  buttons.
- `build_rack.py` runs headless and a second run gives the same files;
  `npm --prefix web run build` runs clean and the page opens offline. The pull
  request reports the size of `web/rack.glb`.

**Open:** the move distances are set by eye.

## 0021 Model size

**Goal:** `web/rack.glb` small enough to load fast on a phone, with every part
of 0018 and the exploded view of 0020.

**Delivers:** `blender/build_rack.py`, `blender/export_web.py`,
`blender/rack.blend`, `renders/*.png`, `web/rack.glb`, `web/build.mjs`,
`web/src/main.js`, `docs/design.md` → *Model objects and the web export*,
`docs/web_viewer.md`.

**Acceptance:**

- `web/rack.glb` deflated is at most 110 kB, as `npm --prefix web run build`
  reports it, and the build stops above that; at the start of the step it was
  211 kB, two thirds of it the two box meshes.
- The box meshes lose their slivers: after the rounding, near-coincident
  vertices are welded, degenerate faces dissolved and coplanar faces merged;
  the build still checks every box's outer size and inner top.
- `export_web.py` keeps its quantization and stores every mesh's indices and
  vertices with `KHR_meshopt_compression`, encoded by the meshoptimizer that
  ships with Blender's glTF exporter, the triangles first ordered for the
  vertex cache; identical buffers are stored once. No new dependency.
- The viewer decodes the model with three.js's `MeshoptDecoder`, whose
  licence goes into the page's licence notice.
- The node names, extras and material names of 0002, 0018 and 0020 stay; the
  viewer opens boxes, explodes and recolours clips as before.
- Not taken: GPU instancing, which would drop the per-node names and extras
  the viewer reads, while the whole JSON is 11 kB deflated; Draco, whose
  decoder outweighs its saving; one clip mesh for all colours, a few kB after
  meshopt.
- `build_rack.py` runs headless and a second run gives the same files;
  `npm --prefix web run build` runs clean and the page opens offline. The pull
  request reports the size of `web/rack.glb` and of the page.

## 0022 Switch to motedis

**Goal:** every metal part and the castors from motedis in one order, with
40 × 40 × 4 angles, 8 mm castor plates and braked castors, the rack redrawn
around them, so the build rests on what one shop sells, cuts and ships
together in a few days.

**Delivers:** `design/rack.json` (frame heights and widths, castor, castor
plate, angles, fasteners, `top_plate`, `box_envelope`, levels, `outer`,
`parts`, `stock`), `blender/build_rack.py`, `blender/rack.blend`,
`renders/*.png`, `web/rack.glb`, `bom/build_bom.py`, `bom/parts.csv`,
`bom/cutlist.csv`, `bom/README.md`, `docs/design.md`, `docs/assembly.md`,
`docs/prices.md`, `README.md`, `AGENTS.md` (*Single Source of Truth*, the box
envelope bullet).

**Acceptance:**

- Angles 40 × 40 × 4, anodised (motedis), cut to 435 from whole 1980 mm bars:
  `rack.json` → `stock` holds the bar, its kerf, end trim and smallest rest, and
  the cut list packs 36 pieces into 9 bars. The holes sit 15 from each end and
  11 and 28 from the inner face of the flat leg, for `screw.m5x12_countersunk`.
- 310 between the hanging legs stays: bays 318, leg tips 238 apart, bars 1074,
  frame 1074 × 435 × 990; castor plate 125–133 (motedis 8 × 90 EN AW-5083,
  a 740 mm bar cut to 4 × 90), bottom bars 133–163, uprights 797 (163–960),
  top bars 960–990; level floors 167, 412, 549, 686, 823, guard 956–960; top
  plate 1114 × 483 × 21, its top at 1011. The same numbers in `rack.json`,
  the scene's `outer_mm`, the documents and the README.
- The upright joints use stainless A2 bolts (at least A2-50):
  `screw.m8x50_socket` from below and `screw.m8x40_socket` from above into
  motedis' M8 core thread, taken as 25 mm deep (`UNVERIFIED`); the build stops
  unless each engages at most the thread depth less 2 mm.
- Four `castor.brake` (motedis 1748: 100 mm, 125 high, back hole 11, offset 28,
  70 kg, total lock), each held by `screw.m8x35_socket`, two `washer.m8` and
  `nut.m8_lock` (DIN 985) through a 9 mm hole in the castor plate. The four
  corner bottom brackets are gone: 24 `bracket.inside_30` and 20
  `bracket.plate`, the plate brackets' screws and nuts counted as
  `screw.m6x12_button` and `tnut.m6`.
- No `castor.plain`, `screw.m8x70_socket`, `screw.m8x20_socket` or
  `screw.m5x10_countersunk` in `rack.json`, the parts list, the model,
  `web/rack.glb` or the documents, apart from earlier roadmap sections and
  superseded rows of `docs/sources.md`.
- The box envelope takes NextGen 2.0 boxes only, the user's choice:
  `AGENTS.md`, this roadmap's goal and `docs/design.md` say so; the foot width
  of at least 282 is `UNVERIFIED` until 0004. The fit check passes on paper: a
  305 rim in 310, the foot 22 mm on each leg centred and 15 mm pushed to one
  side, 8 mm above the tallest box on every level.
- The build stops unless the uprights fill the space between the bars, the gap
  above the tallest box is the same on every level and the castor bolt's tip
  stays below the bottom bars' top.
- `docs/design.md` → *Loads* follows the new masses, bar length and castor
  positions and the A2-50 bolts; tipping and rolling are stated for braked
  castors.
- `docs/prices.md` gives one motedis order with its shipping as read, the top
  plate from Holz-Speckmann, the wood screws from a hardware store and the
  boxes from aidB; Dold stays as a comparison outside the totals.
- `docs/assembly.md` lists the new parts, the holes drilled at home and the
  tools: no 6.8 mm drill and no M8 tap; a 9 mm drill and two 13 mm spanners.
- Every new dimension, price and product property names its status and the
  date it was read (2026-10-25); the pull request lists the `sources.md` rows
  to add on merge and the Dold rows to mark superseded.
- `build_rack.py` runs headless and a second run gives the same files;
  `build_bom.py` runs twice with the same CSV files; `npm --prefix web run
  build` runs clean, `web/rack.glb` deflated stays at or below 110 kB and the
  page opens offline. The pull request reports both sizes.

**Open:** the depth of motedis' M8 core thread (asked by email); the boxes'
foot width (0004); the castor's metal thickness at its back hole, which the
1748 drawing does not give; the motedis profile's moment of inertia, which
motedis does not publish (the loads use Dold's 2.68 cm⁴, `UNVERIFIED` for
motedis); whether motedis still has four 1748 when ordering (fallback: the
plain 995). This step supersedes the Dold parts and plain castors of 0014 and
the joint estimate of 0017.

## 0023 Angle-bracket frame

**Goal:** no hole drilled or machined in any profile and no drill stand: the
base and guard angles become the joints of the uprights, held to the upright
and to the bar beside it, and the rack stands on motedis 06.07.02 castors
(75 mm, 60 kg, total lock), the smaller castor the user asked for in place of
the 125 mm one first read for this step.

**Delivers:** `design/rack.json`, `blender/build_rack.py`,
`blender/rack.blend`, `renders/*.png`, `web/rack.glb`, `bom/parts.csv`,
`bom/cutlist.csv`, `bom/README.md` if it changes, `docs/design.md`,
`docs/assembly.md`, `docs/prices.md`, `README.md`, `docs/roadmap.md`.

**Acceptance:**

- No bar holes, counterbores, core bolts (`screw.m8x50_socket`,
  `screw.m8x40_socket`) or motedis M8 machining in `rack.json`, the parts
  list, the model, `web/rack.glb` or the documents, apart from earlier roadmap
  sections and superseded rows of `docs/sources.md`.
- Each upright end is held by the angle beside it: `angle.base` at the
  bottom, `angle.guard` at the top, each with 2 `screw.m5x12_countersunk` per
  end into the upright's slot and 2 through its flat leg into the bar's slot,
  14 and 32 from the upright face and 15 from the angle end, on the slot line.
  The build stops if two hammer nuts in one slot overlap.
  `screw.m5x12_countersunk` and `tnut.m5` 192 each.
- Heights 60 below the first reading of this step: frame 1074 × 435 × 965,
  top plate top at 986, level floors 142, 387, 524, 661, 798. The same numbers
  in `rack.json`, the scene's `outer_mm`, the documents and the README.
- Four `castor.brake_75` (motedis 06.07.02: wheel 75, 100 high, back hole 11,
  offset 24, 60 kg, total lock); the castor plates keep 5 holes; the fork's
  metal at the back hole and its boss are `MEASURED` from motedis' CAD file.
- `docs/design.md` *Loads* follows: four castors on a level floor, 51.1 of
  60 kg each at safety factor 1.2, tipping lever 148.5, EN 75 N test factor
  3.03.
- `docs/prices.md` gives the motedis order read 2026-10-26, castor 06.07.02 at
  22.83 € per 4 (`VERIFIED`), and the totals recomputed.
- `build_rack.py` runs headless and a second run gives the same files;
  `build_bom.py` runs twice with the same CSV files; `npm --prefix web run
  build` runs clean.
- The pull request lists the `sources.md` rows to add on merge.

**Open:** the rated load of motedis' hammer nuts; the alloy of the angles; the delivery time of
the hammer nuts and brackets, which motedis' shop data shows two ways; whether
the box underside is flat or stepped (0004).