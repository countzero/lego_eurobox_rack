# Changelog

This changelog follows [Common Changelog](https://common-changelog.org) and this
project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.7.0] - 2026-10-26

_Not ready to build: the box dimensions are provisional until the boxes are measured, the angle joints hold on an estimated tightening torque, and an empty rack can tip when a child hangs on a pulled-out box ([roadmap](https://github.com/countzero/lego_eurobox_rack/blob/main/docs/roadmap.md))._

_Upgrade note: no profile is drilled or machined any more and the castors changed, so do not order from the old parts list, cut list or price list; the rack also stands 60 mm lower. Order the new ones._

### Changed

- **Breaking:** the uprights now stand on the bottom bars and hang from the top bars held by the base and guard angles alone, 192 M5 countersunk screws into hammer nuts, with no holes, counterbores or core bolts in any profile and no machining paid to motedis; the castors are the smaller swivel with total lock, wheel 75 mm, 100 high, 60 kg (motedis 06.07.02), which lets everything drop 60 mm: frame 1074 × 435 × 965 mm, top plate top at 986 mm, level floors 142, 387, 524, 661 and 798 mm, motedis order 457.83–467.63 € ([#30](https://github.com/countzero/lego_eurobox_rack/pull/30))

## [0.6.0] - 2026-10-25

_Not ready to build: the box dimensions are provisional until the boxes are measured, the depth of motedis' M8 core thread is not yet confirmed, and an empty rack can tip when a child hangs on an extended box ([roadmap](https://github.com/countzero/lego_eurobox_rack/blob/main/docs/roadmap.md))._

_Upgrade note: every frame dimension changes. Do not order from the old parts list, cut list or price list; order the new ones, all metal parts and castors from motedis. The rack now takes NextGen 2.0 boxes only._

### Changed

- **Breaking:** buy every metal part and the castors from motedis in one order, cut by the shop, about 480 € and 2–4 working days: 40 × 40 × 4 angles instead of 50 × 50 × 3, 318 mm bays and 1074 mm bars, 797 mm uprights, 8 mm castor plates with a lock nut on the castor bolt, four braked castors, stainless M8 core bolts and 24 instead of 28 joint brackets; the frame is 1074 × 435 × 990 mm and the top plate 1114 × 483 mm, and the box envelope narrows to NextGen 2.0 boxes ([#28](https://github.com/countzero/lego_eurobox_rack/pull/28))
- Halve the web model with meshopt compression and cleaner box meshes, 94 kB deflated ([#27](https://github.com/countzero/lego_eurobox_rack/pull/27))

### Fixed

- Keep the castor bolt clear of the corner bracket, which it ran into, and in its castor in the exploded view instead of through the wheel ([#28](https://github.com/countzero/lego_eurobox_rack/pull/28))

## [0.5.2] - 2026-10-25

_Not ready to build: the box dimensions are provisional until the boxes are measured, and an empty rack can tip when a child hangs on an extended box ([roadmap](https://github.com/countzero/lego_eurobox_rack/blob/main/docs/roadmap.md))._

### Fixed

- Lift the uprights off the bottom bars in the exploded view, as the top bars lift off the uprights, so both bar joints show apart; `renders/exploded.png` follows ([`f46effb`](https://github.com/countzero/lego_eurobox_rack/commit/f46effb))

## [0.5.1] - 2026-10-25

_Not ready to build: the box dimensions are provisional until the boxes are measured, and an empty rack can tip when a child hangs on an extended box ([roadmap](https://github.com/countzero/lego_eurobox_rack/blob/main/docs/roadmap.md))._

### Changed

- Let the exploded view open in front of the rack instead of beside it: the boxes slide out to the front, their levels spread up so each level's inserts lift clear, and nothing moves past the side of the rack; `renders/exploded.png` and the viewer's camera follow ([`167613a`](https://github.com/countzero/lego_eurobox_rack/commit/167613a))

## [0.5.0] - 2026-10-25

_Not ready to build: the box dimensions are provisional until the boxes are measured, and an empty rack can tip when a child hangs on an extended box ([roadmap](https://github.com/countzero/lego_eurobox_rack/blob/main/docs/roadmap.md))._

_Upgrade note: do not order the slide tape or the slot covers any more; the parts list, the prices and the assembly guide no longer have them, and the guide's steps 11 to 13 are now 10 to 12._

### Added

- Draw every bought part in the model: 476 screws, hammer nuts and washers in their holes, the end caps, the holes of the bars, angles and castor plates, and the brackets in the shape of motedis S8BBR30; the build stops unless every part of the parts list is drawn as often as listed ([#22](https://github.com/countzero/lego_eurobox_rack/pull/22))
- Add an exploded view: an `explode` slider in Blender, `renders/exploded.png` and an Explode button (key E) in the web viewer; the boxes slide out to the front and aside before the rack comes apart, the inserts lift out and the ColorClip rings come off ([#23](https://github.com/countzero/lego_eurobox_rack/pull/23))

### Changed

- Shrink the web model from 945 kB to 636 kB with every part in it: shared meshes and quantized vertices ([#22](https://github.com/countzero/lego_eurobox_rack/pull/22))

### Removed

- **Breaking:** drop the UHMW slide tape and the slot covers; the boxes slide on the bare aluminium and the slots stay open, the rack costs 24.13 € less ([`f7f3725`](https://github.com/countzero/lego_eurobox_rack/commit/f7f3725))

## [0.4.2] - 2026-10-23

_Not ready to build: the box dimensions are provisional until the boxes are measured, and an empty rack can tip when a child hangs on an extended box ([roadmap](https://github.com/countzero/lego_eurobox_rack/blob/main/docs/roadmap.md))._

### Changed

- Link the web viewer's title to the repository, drop the storage volume line, soften the title and the buttons, keep Web Awesome's typography and turn the view about the middle of the rack ([`4755856`](https://github.com/countzero/lego_eurobox_rack/commit/4755856))

## [0.4.1] - 2026-10-23

_Not ready to build: the box dimensions are provisional until the boxes are measured, and an empty rack can tip when a child hangs on an extended box ([roadmap](https://github.com/countzero/lego_eurobox_rack/blob/main/docs/roadmap.md))._

### Changed

- Draw the web viewer with Blender's AgX Punchy like the renders, smooth its edges with MSAA while moving and TAA at rest, and draw nothing while idle ([#18](https://github.com/countzero/lego_eurobox_rack/pull/18))
- Turn the web viewer's buttons into icons with keys (Esc resets, C shows the colours), add full screen on touch screens, and make the viewer meet WCAG 2.2 AA: every box opens by keyboard, the view turns and zooms without dragging, and the title sits on a panel ([#19](https://github.com/countzero/lego_eurobox_rack/pull/19))

## [0.4.0] - 2026-10-23

_Not ready to build: the box dimensions are provisional until the boxes are measured, and an empty rack can tip when a child hangs on an extended box ([roadmap](https://github.com/countzero/lego_eurobox_rack/blob/main/docs/roadmap.md))._

_Upgrade note: the bottom bars become 30 × 30 and everything above them moves 30 mm down; the uprights keep their length. The top plate is now part of the structure and must be screwed on before the rack is loaded. Order the boxes with closed handles (C2G43-12, C2G43-22) and the hardware from the new parts list._

### Changed

- **Breaking:** screw the 21 mm birch top plate to the top bars from below with 20 hidden brackets and make it carry the middle uprights with the top bars, so the bottom bars drop from 30 × 60 to 30 × 30 and the rack is 30 mm lower ([`74b7d12`](https://github.com/countzero/lego_eurobox_rack/commit/74b7d12))
- Use the closed-handle boxes C2G43-12 and C2G43-22 and draw their grip pocket, lip and struts from aidB's photos ([`74b7d12`](https://github.com/countzero/lego_eurobox_rack/commit/74b7d12))
- Draw the ribbed boxes and the birch top plate in the renders ([#16](https://github.com/countzero/lego_eurobox_rack/pull/16))
- Simplify the web viewer to Reset and Colours, show the storage volume, draw the plywood and the shading as in Blender, and shorten the colour link ([`bc5f8ce`](https://github.com/countzero/lego_eurobox_rack/commit/bc5f8ce))

### Removed

- Drop the joint plates ([#15](https://github.com/countzero/lego_eurobox_rack/pull/15))

## [0.3.0] - 2026-10-22

_Not ready to build: the box dimensions are provisional until the boxes are measured, and an empty rack can tip when a child hangs on an extended box ([roadmap](https://github.com/countzero/lego_eurobox_rack/blob/main/docs/roadmap.md))._

_Upgrade note: the castors, the castor plates and the brackets change, and the back stops are gone. The cut lengths of 0.2.0 still hold. Order the hardware from the new parts list._

### Changed

- **Breaking:** put four plain 100 mm castors under 90 × 90 corner plates inside the frame outline, lower the frame by 25 mm and open the back, so every box pulls out to the front and to the back ([#12](https://github.com/countzero/lego_eurobox_rack/pull/12))
- Model the boxes and inserts with rounded edges, the inner taper and plastic materials, and render them in studio light ([#13](https://github.com/countzero/lego_eurobox_rack/pull/13))

## [0.2.0] - 2026-10-22

_Not ready to build: the box dimensions are provisional until the boxes are measured ([roadmap](https://github.com/countzero/lego_eurobox_rack/blob/main/docs/roadmap.md))._

_Upgrade note: no profile, angle, box or insert of 0.1.0 carries over. Order and cut from the new parts and cut list._

### Changed

- **Breaking:** change the rack to 15 Euroboxes NextGen 2.0 Cycle 400 × 300, 3 wide and 5 high, with one long bar front and back, 4 castors, no panels and aidB's insert sets ([`37dd16d`](https://github.com/countzero/lego_eurobox_rack/commit/37dd16d))

### Added

- Add the ColorClip picker to the web viewer, with presets and a link that shares the colours of each level ([#10](https://github.com/countzero/lego_eurobox_rack/pull/10))

## [0.1.0] - 2026-10-20

_Not ready to build: the box dimensions are provisional until the boxes are measured, and the joints of the width beams clash with the base and guard angles ([roadmap](https://github.com/countzero/lego_eurobox_rack/blob/main/docs/roadmap.md))._

### Added

- Add the dimensions and part catalog of a rolling rack for 12 Euroboxes 600 × 400, 3 wide and 4 high, that takes NextGen and regular boxes ([#2](https://github.com/countzero/lego_eurobox_rack/pull/2))
- Add the Blender model, built headless from the dimensions, with its renders and web export ([#6](https://github.com/countzero/lego_eurobox_rack/pull/6))
- Add the 3D web viewer with boxes that pull out, published on GitHub Pages ([#5](https://github.com/countzero/lego_eurobox_rack/pull/5))
- Add the insert plan for the 120 mm boxes with Auer EK inserts and no filler pieces ([#4](https://github.com/countzero/lego_eurobox_rack/pull/4))
- Add the parts list and the cut list, generated from the dimensions ([#3](https://github.com/countzero/lego_eurobox_rack/pull/3))
- Add the price comparison with the cheapest order split ([#8](https://github.com/countzero/lego_eurobox_rack/pull/8))
- Add the assembly guide ([#7](https://github.com/countzero/lego_eurobox_rack/pull/7))

[0.4.0]: https://github.com/countzero/lego_eurobox_rack/releases/tag/v0.4.0
[0.3.0]: https://github.com/countzero/lego_eurobox_rack/releases/tag/v0.3.0
[0.2.0]: https://github.com/countzero/lego_eurobox_rack/releases/tag/v0.2.0
[0.1.0]: https://github.com/countzero/lego_eurobox_rack/releases/tag/v0.1.0
