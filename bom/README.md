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

| Column        | Meaning                                                      |
| ------------- | ------------------------------------------------------------ |
| `id`          | Part ID, used by every document, list and price              |
| `category`    | profile, angle, connector, fastener, panel, box and so on    |
| `description` | What the part is and where it goes                           |
| `material`    | Section, material or finish                                  |
| `length`      | Cut or overall length in mm; empty where it does not apply   |
| `width`       | Width in mm for panels, plates and inserts; otherwise empty  |
| `quantity`    | Count for unit `piece`, total length in mm for unit `length` |
| `unit`        | `piece` or `length`                                          |
| `status`      | `build` for what is bought now, `planned` for the top plate  |

## cutlist.csv

One row per cut of the profile and angle parts, grouped by stock bar.

| Column         | Meaning                                                  |
| -------------- | -------------------------------------------------------- |
| `material`     | Section of the bar                                       |
| `bar`          | Bar number, counted from 1 per material                  |
| `stock_length` | Length of the bought bar in mm                           |
| `part_id`      | Part the cut yields                                      |
| `cut_length`   | Length of the cut in mm                                  |
| `start`        | Offset of the cut on the bar in mm, earlier kerfs added  |

## Packing

Stock lengths and the saw kerf per material come from `rack.json` → `stock`.
For each candidate stock length the cuts are sorted longest first and placed
first-fit into the bars (first-fit decreasing); a cut needs its length plus one
kerf for every cut before it on the bar. The candidate with the least bought
length wins, then the least waste, then the fewest bars. First-fit decreasing
is not guaranteed optimal, but for these cuts it reaches the lower bound.

| Material             | Bars          | Cut length | Waste           |
| -------------------- | ------------- | ---------- | --------------- |
| 30x30 B-type slot 8  | 6 x 3000 mm   | 15976 mm   | 2024 mm, 11.2 % |
| 50x50x3 EN AW-6060   | 10 x 2000 mm  | 18300 mm   | 1700 mm, 8.5 %  |

Waste includes the kerfs and the offcut at the end of each bar.

## Shop order list

Most shops cut profiles to length, so you order the pieces below and the cut
list does not matter. It matters when you buy stock bars or cut yourself.

| Material             | Pieces       | Part IDs                                       |
| -------------------- | ------------ | ---------------------------------------------- |
| 30x30 B-type slot 8  | 8 x 823 mm   | `profile.upright`                              |
| 30x30 B-type slot 8  | 8 x 550 mm   | `profile.beam_depth`                           |
| 30x30 B-type slot 8  | 12 x 416 mm  | `profile.beam_width`                           |
| 50x50x3 EN AW-6060   | 30 x 610 mm  | `angle.base`, `angle.support`, `angle.guard`   |
