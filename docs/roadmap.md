# Roadmap

## Goal

A rolling rack that holds 12 Euroboxes 600 × 400 as LEGO drawers: 3 columns,
2 levels of 220 mm boxes below and 2 levels of 120 mm boxes with inserts above,
on 8 castors, with a wooden top plate prepared for later. It must take NextGen
boxes (ab-in-die-BOX) and regular Euroboxes (Auer, Utz and others) alike.
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

| ID   | Step                                                         | Status               | PR                                                          |
| ---- | ------------------------------------------------------------ | -------------------- | ----------------------------------------------------------- |
| 0001 | [Repository and roadmap](#0001-repository-and-roadmap)       | Done                 | [#1](https://github.com/countzero/lego_eurobox_rack/pull/1) |
| 0002 | [Rack specification](#0002-rack-specification)               | Done                 | [#2](https://github.com/countzero/lego_eurobox_rack/pull/2) |
| 0003 | [Blender model and renders](#0003-blender-model-and-renders) | Done                 | [#6](https://github.com/countzero/lego_eurobox_rack/pull/6) |
| 0004 | [Measure the boxes](#0004-measure-the-boxes)                 | Waiting for the user |                                                             |
| 0005 | [Insert plan](#0005-insert-plan)                             | Done                 | [#4](https://github.com/countzero/lego_eurobox_rack/pull/4) |
| 0006 | [Parts and cut list](#0006-parts-and-cut-list)               | Done                 | [#3](https://github.com/countzero/lego_eurobox_rack/pull/3) |
| 0007 | [Price comparison](#0007-price-comparison)                   | Done                 | [#8](https://github.com/countzero/lego_eurobox_rack/pull/8) |
| 0008 | [Assembly guide](#0008-assembly-guide)                       | Done                 | [#7](https://github.com/countzero/lego_eurobox_rack/pull/7) |
| 0009 | [Web viewer](#0009-web-viewer)                               | Done                 | [#5](https://github.com/countzero/lego_eurobox_rack/pull/5) |
| 0010 | [Width-beam joints](#0010-width-beam-joints)                 | Planned              |                                                             |

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

**Goal:** the numbers no maker publishes, so the angles and clearances rest on
measurements.

**Delivers:** measured values in `docs/sources.md` and corrections to
`design/rack.json`.

**Acceptance:**

- With a caliper, on one NextGen 2.0 and one Auer EG box of each height: rim
  width and length, foot width and length at the bearing line, foot height,
  rim overhang, real height.
- Or the makers' written answer (Müller & Sohn for NextGen,
  info@kunststoffe-mueller.de; Auer).
- One Auer EK 2/100 tried in a NextGen 120 box.

**Open:** every value above; until then the design uses the envelope of
`docs/design.md`.

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
the angles, found while writing the assembly guide (0008).

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