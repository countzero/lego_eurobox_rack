# lego_eurobox_rack

A rolling rack of 30 × 30 aluminium profiles that holds 12 Euroboxes
600 × 400 as LEGO drawers: 3 columns, two levels of 220 mm boxes below and two
levels of 120 mm boxes with inserts above, on 8 castors. It takes NextGen boxes
(ab-in-die-BOX) and regular Euroboxes (Auer and others) alike, and its top is
prepared for a wooden plate to be fitted later.

**[Open the 3D viewer](https://countzero.github.io/lego_eurobox_rack/)**: turn
the rack, pull the boxes out, show the planned top plate.

![The rack, three-quarter view, one box pulled out](renders/drawer_out.png)

> [!WARNING]
> Not ready to build. The box dimensions are provisional until the boxes are
> measured (roadmap 0004), and the joints of the width beams clash with the
> angles (roadmap 0010). The [roadmap](docs/roadmap.md) says what is planned
> and how far each step has got.

## Front view

Heights in mm, not to scale. Each box stands on a 50 × 50 × 3 angle, whose
hanging leg guides the rim of the box below and keeps it from tipping when it
is pulled out.

```
        |<------------------------------ 1368 frame ------------------------------->|
  923 - ++=======================++=======================++=======================++
  890 - ||#####             #####||#####             #####||#####             #####||
        ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
        ||  | 120 + inserts   |  ||  | 120 + inserts   |  ||  | 120 + inserts   |  ||   L4
  757 - ||##+-----------------+##||##+-----------------+##||##+-----------------+##||
        ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
        ||  | 120 + inserts   |  ||  | 120 + inserts   |  ||  | 120 + inserts   |  ||   L3
  621 - ||##+-----------------+##||##+-----------------+##||##+-----------------+##||
        ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
        ||  |     220 / 228   |  ||  |     220 / 228   |  ||  |     220 / 228   |  ||   L2
        ||  |                 |  ||  |                 |  ||  |                 |  ||
  377 - ||##+-----------------+##||##+-----------------+##||##+-----------------+##||
        ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
        ||  |     220 / 228   |  ||  |     220 / 228   |  ||  |     220 / 228   |  ||   L1
        ||  |                 |  ||  |                 |  ||  |                 |  ||
  133 - ||L_+-----------------+_J||L_+-----------------+_J||L_+-----------------+_J||
  100 - ++=======================++=======================++=======================++
       (O)                     (O)                     (O)                     (O)      castors
    0 - =============================================================================
        30<----- 416 clear ----->30<----- 416 clear ----->30<----- 416 clear ----->30
```

## Repository

| Path                  | What                                                       |
| --------------------- | ---------------------------------------------------------- |
| `design/rack.json`    | Every dimension and the part catalog: the single source    |
| `docs/design.md`      | Decisions, fit check, drawings, joints and contracts       |
| `docs/inserts.md`     | The inserts of the 120 mm boxes                            |
| `docs/prices.md`      | Prices of every part, the order split and the totals       |
| `docs/assembly.md`    | The build, step by step                                    |
| `bom/`                | Parts list and cut list, generated from `rack.json`        |
| `blender/`            | The model, built headless from `rack.json`, and its export |
| `renders/`            | Renders of the model                                       |
| `web/`                | The 3D viewer, published on GitHub Pages                   |
| `docs/roadmap.md`     | The steps, their specifications and their status           |
| `docs/sources.md`     | Every fact with its status and source                      |
| `docs/conventions.md` | Branches, commits, pull requests, how facts are cited      |
| `docs/releases.md`    | How a release is cut and published                         |
| `docs/worktrees.md`   | How parallel steps use git worktrees                       |
| `docs/web_viewer.md`  | How the viewer is built                                    |

## License

[MIT](LICENSE)
