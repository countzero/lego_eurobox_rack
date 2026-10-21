# lego_eurobox_rack

A rolling rack of 30 × 30 aluminium profiles that holds 15 Euroboxes NextGen
2.0 Cycle 400 × 300 from ab-in-die-BOX as LEGO drawers: 3 columns, one level of
220 mm boxes at the bottom and four levels of 120 mm boxes with inserts above.
One long bar runs over all three columns front and back, top and bottom; the
rack stands on 4 castors and has no panels. Its top is prepared for a wooden
plate to be fitted later.

**[Open the 3D viewer](https://countzero.github.io/lego_eurobox_rack/)**: turn
the rack, pull the boxes out, show the planned top plate.

![The rack, three-quarter view, one box pulled out](renders/drawer_out.png)

> [!WARNING]
> Not ready to build. The box geometry is provisional until the boxes are
> measured (roadmap 0004). The [roadmap](docs/roadmap.md) says what is planned
> and how far each step has got.

## Front view

Heights in mm, not to scale. One bar runs across all three columns at the top
and at the bottom (30 × 60). Each box stands on a 50 × 50 × 3 angle, whose
hanging leg guides the rim of the box below and keeps it from tipping when it
is pulled out.

```
        |<------------------------------ 1068 frame ------------------------------->|
 1041 - =============================================================================  top bar
 1008 - ||#####             #####||#####             #####||#####             #####||
        ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
        ||  | 120, 1/4        |  ||  | 120, 1/4        |  ||  | 120, 1/4        |  ||   L5
  875 - ||##+-----------------+##||##+-----------------+##||##+-----------------+##||
        ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
        ||  | 120, 1/4        |  ||  | 120, 1/4        |  ||  | 120, 1/4        |  ||   L4
  739 - ||##+-----------------+##||##+-----------------+##||##+-----------------+##||
        ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
        ||  | 120, 1/2        |  ||  | 120, 1/2        |  ||  | 120, 1/2        |  ||   L3
  603 - ||##+-----------------+##||##+-----------------+##||##+-----------------+##||
        ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
        ||  | 120, 1/2        |  ||  | 120, 1/2        |  ||  | 120, 1/2        |  ||   L2
  467 - ||##+-----------------+##||##+-----------------+##||##+-----------------+##||
        ||  +-----------------+  ||  +-----------------+  ||  +-----------------+  ||
        ||  | 220             |  ||  | 220             |  ||  | 220             |  ||   L1
        ||  |                 |  ||  |                 |  ||  |                 |  ||
        ||  |                 |  ||  |                 |  ||  |                 |  ||
  223 - ||L_+-----------------+_J||L_+-----------------+_J||L_+-----------------+_J||
  220 - =============================================================================  bottom bar
  160 - =============================================================================
       (O)                                                                        (O)  castors
    0 - =============================================================================
        30<----- 316 clear ----->30<----- 316 clear ----->30<----- 316 clear ----->30
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
