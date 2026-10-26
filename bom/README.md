# Parts and cut list

Both CSV files are generated from `design/rack.json` and are never edited by
hand. After a change to `rack.json`, run from the repository root:

```powershell
python bom/build_bom.py
```

The script uses the Python standard library only, writes UTF-8 with LF line
endings and gives byte-identical files on every run. It stops with an error if
a piece quantity is not a positive integer, a part ID repeats, a cut material
has no stock entry, or a cut is longer than every stock length.

## parts.csv

One row per part of the catalog `parts` in `rack.json`, in catalog order.

| Column        | Meaning                                                                      |
| ------------- | ---------------------------------------------------------------------------- |
| `id`          | Part ID, used by every document, list and price                              |
| `category`    | profile, angle, connector, fastener, castor, box and so on                   |
| `description` | What the part is and where it goes                                           |
| `material`    | Section, material or finish                                                  |
| `length`      | Cut or overall length in mm; empty where it does not apply                   |
| `width`       | Width in mm for plates and inserts; otherwise empty                          |
| `quantity`    | Count for unit `piece`, total length in mm for unit `length`                 |
| `unit`        | `piece` or `length`                                                          |
| `status`      | `build` for what is bought now, `planned` for a part designed but not bought |

## cutlist.csv

One row per cut of the profile and angle parts, grouped by stock bar.

| Column         | Meaning                                                         |
| -------------- | --------------------------------------------------------------- |
| `material`     | Section of the bar                                              |
| `bar`          | Bar number, counted from 1 per material                         |
| `stock_length` | Length of the bought bar in mm; the piece itself if cut to size |
| `part_id`      | Part the cut yields                                             |
| `cut_length`   | Length of the cut in mm                                         |
| `start`        | Offset of the cut on the bar in mm, end trim and kerfs added    |

## Packing

The stock per material comes from `rack.json` → `stock`. A material whose
stock is `cut_to_size` is bought as single pieces, so each piece is its own
row and nothing is packed. For the others, for each candidate stock length,
the cuts are sorted longest first and placed first-fit into the bars
(first-fit decreasing): the first cut starts after the bar's end `trim`, every
further cut needs one `kerf` more, and what is left of a bar is either nothing
or at least `min_rest`. The candidate with the least bought length wins, then
the least waste, then the fewest bars. First-fit decreasing is not guaranteed
optimal, but for these cuts it reaches the lower bound.

| Material            | Bars                     | Cut length | Waste           |
| ------------------- | ------------------------ | ---------- | --------------- |
| 30x30 B-type slot 8 | 20 pieces cut to size    | 13672 mm   | none bought     |
| 40x40x4 anodised    | 9 x 1980 mm, 4 cuts each | 15660 mm   | 2160 mm, 12.1 % |

Waste includes the end trim, the kerfs and the offcut at the end of each bar.

## Shop order list

motedis cuts the profiles to size and the angle bars to the list, so you order
the pieces below (`docs/prices.md`).

| Material            | Pieces                                 | Part IDs                                     |
| ------------------- | -------------------------------------- | -------------------------------------------- |
| 30x30 B-type slot 8 | 4 x 1074 mm                            | `profile.bar_top`, `profile.bar_bottom`      |
| 30x30 B-type slot 8 | 8 x 797 mm                             | `profile.upright`                            |
| 30x30 B-type slot 8 | 8 x 375 mm                             | `profile.beam_depth`                         |
| 40x40x4 anodised    | 9 bars of 1980 mm, each cut 4 x 435 mm | `angle.base`, `angle.support`, `angle.guard` |

No profile is machined or drilled; see `parts.csv`.
