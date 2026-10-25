"""Write bom/parts.csv and bom/cutlist.csv from design/rack.json.

Run from anywhere: python bom/build_bom.py

The cut list packs every profile and angle piece into stock bars. A material
whose stock is cut to size (rack.json -> stock -> cut_to_size) gets one row per
piece instead. For every other material and each candidate stock length the
cuts are packed first-fit decreasing, after the bar's end trim, with one kerf
before each further cut, leaving no rest or at least the stock's min_rest; the
candidate with the least bought length wins, then the least waste, then the
fewest bars, then the shorter stock length.
"""

import csv
import io
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RACK = ROOT / "design" / "rack.json"
PARTS_CSV = ROOT / "bom" / "parts.csv"
CUTLIST_CSV = ROOT / "bom" / "cutlist.csv"

PARTS_HEADER = ["id", "category", "description", "material", "length", "width", "quantity", "unit", "status"]
CUTLIST_HEADER = ["material", "bar", "stock_length", "part_id", "cut_length", "start"]
CUT_CATEGORIES = ("profile", "angle")

# Material string -> stock key, read from the section that defines the material.
STOCK_SOURCES = (
    (("frame", "profile", "type"), "profile_30x30"),
    (("angles", "section", "type"), "angle_40x40x4"),
)


def fail(message):
    sys.exit(f"build_bom: {message}")


def lookup(data, path):
    for key in path:
        data = data[key]
    return data


def stock_map(rack):
    mapping = {}
    for path, key in STOCK_SOURCES:
        if key not in rack["stock"]:
            fail(f"stock key {key!r} missing in rack.json")
        mapping[lookup(rack, path)] = key
    return mapping


def write_csv(path, header, rows):
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(header)
    writer.writerows(rows)
    path.write_bytes(buffer.getvalue().encode("utf-8"))


def cell(part, key):
    value = part.get(key)
    return "" if value is None else value


def validate(parts):
    seen = set()
    for part in parts:
        if part["id"] in seen:
            fail(f"duplicate part id {part['id']}")
        seen.add(part["id"])
        quantity = part["quantity"]
        if part["unit"] == "piece" and (not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0):
            fail(f"{part['id']}: quantity {quantity!r} is not a positive integer")


def fits(used, length, min_rest):
    rest = length - used
    return rest == 0 or rest >= min_rest


def pack(cuts, length, stock):
    """First-fit decreasing; cuts are (cut_length, part_id), sorted by caller."""
    kerf, trim, min_rest = stock["kerf"], stock.get("trim", 0), stock.get("min_rest", 0)
    bars = []
    for cut in cuts:
        for bar in bars:
            if fits(bar["used"] + kerf + cut[0], length, min_rest):
                bar["cuts"].append(cut)
                bar["used"] += kerf + cut[0]
                break
        else:
            bars.append({"cuts": [cut], "used": trim + cut[0]})
    return bars


def best_packing(material, cuts, stock):
    longest = cuts[0][0]
    candidates = []
    for length in sorted(stock["lengths"]):
        if not fits(stock.get("trim", 0) + longest, length, stock.get("min_rest", 0)):
            continue
        bars = pack(cuts, length, stock)
        bought = length * len(bars)
        cut_total = sum(c[0] for c in cuts)
        candidates.append((bought, bought - cut_total, len(bars), length, bars))
    if not candidates:
        fail(f"{material}: cut {longest} mm exceeds every stock length {stock['lengths']}")
    return min(candidates, key=lambda c: c[:4])


def main():
    rack = json.loads(RACK.read_text(encoding="utf-8"))
    parts = rack["parts"]
    validate(parts)
    write_csv(PARTS_CSV, PARTS_HEADER, [[cell(p, k) for k in PARTS_HEADER] for p in parts])

    mapping = stock_map(rack)
    by_material = {}
    for part in parts:
        if part["category"] in CUT_CATEGORIES and part["unit"] == "piece" and part.get("length"):
            if part["material"] not in mapping:
                fail(f"{part['id']}: no stock for material {part['material']!r}")
            by_material.setdefault(part["material"], []).extend([(part["length"], part["id"])] * part["quantity"])

    rows = []
    summary = []
    for material in sorted(by_material):
        stock = rack["stock"][mapping[material]]
        cuts = sorted(by_material[material], key=lambda c: (-c[0], c[1]))
        cut_total = sum(c[0] for c in cuts)
        if stock.get("cut_to_size"):
            for number, (cut_length, part_id) in enumerate(cuts, start=1):
                rows.append([material, number, cut_length, part_id, cut_length, 0])
            summary.append(f"{material}: {len(cuts)} pieces cut to size, {cut_total} mm")
            continue
        bought, waste, count, length, bars = best_packing(material, cuts, stock)
        for number, bar in enumerate(bars, start=1):
            start = stock.get("trim", 0)
            for cut_length, part_id in bar["cuts"]:
                rows.append([material, number, length, part_id, cut_length, start])
                start += cut_length + stock["kerf"]
        summary.append(f"{material}: {count} x {length} mm, cut {cut_total} mm, "
                       f"waste {waste} mm ({100 * waste / bought:.1f} %)")
    write_csv(CUTLIST_CSV, CUTLIST_HEADER, rows)

    for line in summary:
        print(line)


if __name__ == "__main__":
    main()
