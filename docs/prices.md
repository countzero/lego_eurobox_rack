# Prices

What every part of `design/rack.json` costs and where it is bought (roadmap
0007, redone for one motedis order in 0022 and read again for the
angle-bracket frame in 0023).

## Rules

- The motedis order was read on **2026-10-26** on motedis' own product pages:
  the gross prices of their product data (`valueAddedTaxIncluded`), the
  delivery times of the shop's own delivery query for Germany. The boxes were
  read on 2026-10-21, the top plate on 2026-10-22.
- Every price includes 19 % VAT for a private buyer in Germany. A net price is
  multiplied by 1.19, rounded to the cent and marked `DERIVED`.
- Status follows `docs/conventions.md` → *Sources*. A price marked
  `UNVERIFIED` is an estimate and is not a fact; it is in a total only where
  the row says so.
- Quantities and lengths come from `parts` in `design/rack.json`. Profiles
  30 × 30: 8 × 797 + 4 × 1074 + 8 × 375 = 13.672 m in 20 pieces. Angles:
  36 × 435 = 15.66 m, cut from 9 bars of 1980 mm. Top plate 1114 × 483 mm =
  0.538 m².
- motedis sells loose pieces with a pick fee per order line ("Pickzuschlag",
  0.25 € net before its own surcharge) and bags without one. A price for loose
  pieces is worked out the way the shop's product data does it: (piece price ×
  quantity + pick fee) × 1.111 × 1.19, `DERIVED`; 1.111 is the factor that
  turns motedis' internal prices into its shown net prices on every page read.
- Angle bars and the plate bar are cut by motedis from whole bars to a list
  ("Zuschnitt ganzer Stab"): the whole bar is paid, the offcut is not
  delivered.

## The motedis order

Every metal part and the castors, in one order. The wood screws come from a
hardware store.

| Part                                 | Product                                                    | Bought                             | Price incl. VAT     | Status   | Delivery, working days |
| ------------------------------------ | ---------------------------------------------------------- | ---------------------------------- | ------------------- | -------- | ---------------------- |
| `profile.*` (20)                     | Aluprofil 30x30 B-Typ Nut 8, Zuschnitt, 9.87 €/m           | 8 × 797, 4 × 1074, 8 × 375         | 134.88 €            | DERIVED  | 2–4                    |
| `angle.*` (36)                       | Winkelstange eloxiert 40x40x4mm, Zuschnitt ganzer Stab     | 9 × 1980 mm, cut to 4 × 435 each   | 149.98 €            | DERIVED  | 2–4                    |
| `plate.castor` (4)                   | Aluminium Plättchen 8x90 mm (EN AW-5083)                   | 1 × 740 mm, cut to 4 × 90          | 31.55 €             | DERIVED  | 2–4                    |
| `castor.brake_75` (4)                | Rolle 75 Rückenloch mit Bremse (06.07.02), total lock      | 1 bag of 4                         | 22.83 €             | VERIFIED | 1–2                    |
| `bracket.inside_30`, `bracket.plate` | Winkel 30 B-Typ Nut 8, 7.27 € per 10                       | 4 bags of 10 + 4 loose (44)        | 32.52 €             | DERIVED  | 1–2                    |
| `tnut.m6` (84)                       | Hammermutter B-Typ Nut 8 [M6]                              | 84 loose                           | 12.55 €             | DERIVED  | 1–2                    |
| `tnut.m5` (192)                      | Hammermutter B-Typ Nut 8 [M5], 14.54 € per 100             | 1 bag of 100 + 92 loose            | 28.25 €             | DERIVED  | 1–3                    |
| `screw.m5x12_countersunk` (192)      | DIN 7991 M5x12, 8.8, zinc-plated, 3.97 € per 100           | 2 bags of 100                      | 7.93 €              | DERIVED  | 1–3                    |
| `screw.m6x16_countersunk` (16)       | DIN 7991 M6x16, 8.8, zinc-plated                           | 16 loose                           | 1.18 €              | DERIVED  | 1–3                    |
| `screw.m6x12_button` (68)            | DIN EN ISO 7380 M6x12, 8.8, zinc-plated                    | 68 loose                           | 3.93 €              | DERIVED  | 1–3                    |
| `screw.m8x35_socket` (4)             | DIN 912 M8x35 Edelstahl A2, at least A2-50, 0.62 € for one | 4 loose                            | 1.49 €              | DERIVED  | 1–3                    |
| `nut.m8_lock` (4)                    | Mutter DIN 985 M8, zinc-plated                             | 1 bag of 10                        | 0.53 €              | VERIFIED | 1–3                    |
| `washer.m8` (8)                      | U-Scheibe DIN 125 M8, zinc-plated                          | 8 loose                            | 0.65 €              | DERIVED  | 1–3                    |
| `cap.end_30` (8)                     | Abdeckkappe für Profil 30 Typ B Nut 8, black PA            | 8 loose                            | 2.34 €              | DERIVED  | 1–2                    |
| **Parts**                            |                                                            |                                    | **430.61 €**        | DERIVED  |                        |
| Shipping                             | long goods up to 1,109.89 €, packing, once or twice        | about 31 kg, longest piece 1074 mm | 27.22–37.02 €       | DERIVED  |                        |
| **Order**                            |                                                            |                                    | **457.83–467.63 €** | DERIVED  | **2–4**                |

Notes:

- **Profile:** 13.672 m × 9.87 €/m; motedis cuts each piece to size and
  charges no cut fee. No profile is machined or drilled.
- **Angle:** "Zuschnitt ganzer Stab" shows 8.42 €/m, 149.98 € for the 9 bars
  (read 2026-10-26). The page data still holds a hidden overstock price of
  142.49 €, which may apply in the cart. 12 bars of
  1500 mm (143.93 €, read 2026-10-25) ship from outside Germany in 6–10
  working days. The alloy is not stated.
- **Plate:** a closeout item ("Schlussverkauf"); only 2 stock bars of 1490 mm
  were left. The 740 mm bar is stocked; a 490 mm bar would cost 20.89 € but is
  not a stocked length.
- **Castors:** motedis 06.07.02 (wheel 75, 100 high, back hole 11, offset 24,
  60 kg, total lock): four castors on a level floor keep the design load at
  about 51 kg each at safety factor 1.2. 22.83 € per 4, a sale price on local
  overstock ("On Sale, Limited Stock"), from the next order day
  (`VERIFIED` 2026-10-26).
- **Brackets:** motedis' Winkel 30 comes without screws; the 20 plate brackets
  take one `screw.m6x12_button` and one `tnut.m6` each, counted in those rows.
- **Shipping:** motedis' table for orders with profiles: up to 1,109.89 €
  23.33 €, plus packing 3.89 €, again for every 20 kg. Nothing over 1150 mm
  ships (the bars are cut), so no length surcharge. 23.33 + 3.89 = 27.22 €
  once, 31.11 € if the 31 kg count twice; the page does not say whether these
  are net or gross, so the range ends at 31.11 × 1.19 = 37.02 €.
- **Delivery:** motedis' delivery query gives 2–4 working days for the cut
  profiles, the angles and the plate, 1–3 for the rest, from the next order
  cutoff (06:00 or 08:00). motedis calls its delivery times non-binding. On
  2026-10-26 the shop's stock arrays showed no German stock for the M5 and M6
  hammer nuts and the brackets (about 7 and 11 weeks), while the product data
  showed large standard stock; to be confirmed in the cart (`UNVERIFIED`).

## Top plate

| Part                     | Supplier           | Product                                | Price incl. VAT | For the quantity   | Status     | Source   |
| ------------------------ | ------------------ | -------------------------------------- | --------------- | ------------------ | ---------- | -------- |
| `plate.top`              | Holz-Speckmann     | Multiplex Birke BB/CP 21 mm, Zuschnitt | 66.95 €/m²      | 36.02 € (0.538 m²) | DERIVED    | [hs-mpx] |
| `plate.top`              | plattenzuschnitt24 | Birke Multiplex 21 mm, BB/BB           | 91.40 €/m²      | 49.17 € (0.538 m²) | DERIVED    | [pz-mpx] |
| `screw.wood_4_5x16` (20) | any hardware store | wood screw 4.5 × 16 pan head           | not read        | about 2 €          | UNVERIFIED |          |

The plate is structural and is fitted before the rack is loaded
(`docs/assembly.md`, step 9), so it is in the totals: Holz-Speckmann's plate
for 36.02 € and about 2 € of wood screws, an `UNVERIFIED` estimate counted in
the totals. The square-metre prices are from the 2026-10-22 reading. The R10
corners, the edge finish and the plate's shipping are not priced.

## Boxes, rings and inserts

All from ab-in-die-BOX (aidB), private shop: the user wants one vendor for
boxes, rings and inserts.

| Part                 | Product                                              | Price incl. VAT     | Qty | For the quantity | Status   | Source         |
| -------------------- | ---------------------------------------------------- | ------------------- | --- | ---------------- | -------- | -------------- |
| `box.e120`           | NextGen 2.0 Cycle C2G43-12, closed handles, no rings | 8.08 €              | 12  | 96.96 €          | VERIFIED | [aidb-12]      |
| `box.e220`           | NextGen 2.0 Cycle C2G43-22, closed handles, no rings | 11.26 €             | 3   | 33.78 €          | VERIFIED | [aidb-22]      |
| `clip.*`             | ColorClip set R200-00-xx-SET, 2 rings                | 0.82 € per pack     | 15  | 12.30 €          | VERIFIED | [aidb-12]      |
| `insert.set_half`    | Set 1/2 EES43-01-100-04, 2 × 3613-100                | 9.95 € (8.36 net)   | 6   | 59.70 €          | VERIFIED | [aidb-half]    |
| `insert.set_quarter` | Set 1/4 EES43-02-100-04, 4 × 1813-100                | 12.49 € (10.50 net) | 6   | 74.94 €          | VERIFIED | [aidb-quarter] |

- A carton of 16 C2G43-12 costs 7.53 € each, 120.47 € for 16; it buys four
  boxes more than needed for 23.51 € more.
- Boxes with rings fitted cost 9.36 € (120) and 12.41 € (220): 149.55 € for
  the 15 boxes against 143.04 € for boxes plus separate ColorClips, which also
  allow one colour per insert type (3 packs of blue, 6 each of turquoise and
  light green; `docs/inserts.md`).
- The sets fit only NextGen 400 × 300 × 120 boxes (`docs/inserts.md`).
- aidB ships free in Germany from 150 € (`VERIFIED`).

## Order

| Shop           | Parts                                                                                           | Total           |
| -------------- | ----------------------------------------------------------------------------------------------- | --------------- |
| motedis        | every profile, angle, castor plate, bracket, hammer nut, screw, nut, washer, end cap, castor    | 457.83–467.63 € |
| Holz-Speckmann | `plate.top`, cut to 1114 × 483                                                                  | 36.02 €         |
| Hardware store | `screw.wood_4_5x16` × 20                                                                        | about 2.00 €    |
| aidB           | `box.e120` × 12, `box.e220` × 3, `clip.*` × 15, `insert.set_half` × 6, `insert.set_quarter` × 6 | 277.68 €        |

| Total                           | Amount              |
| ------------------------------- | ------------------- |
| Rack without boxes              | 495.85–505.65 €     |
| Boxes, rings and inserts (aidB) | 277.68 €            |
| **Overall**                     | **773.53–783.33 €** |

The rack total is the motedis order, the plate and the wood screws, without
the plate's shipping. The range is motedis' shipping (once or twice the
packing charge, net or gross).

## Comparison: Dold

Before 0022 the rack was planned with 50 × 50 × 3 angles and 10 mm castor
plates, most parts from Dold Mechatronik and the small parts from motedis
(592.45 € for the metal parts on 2026-10-22). Bought from Dold alone the same
design came to about 675–690 € on 2026-10-25, its single screws priced only
as base plus surcharge (`UNVERIFIED`). Dold's cut 30 × 30 profile had a
delivery time of 2–3 weeks, and its braked castor 69490 was "Nicht vorrätig"
(both `VERIFIED` 2026-10-25). motedis sells no 50 × 50 × 3 angle, hence the
40 × 40 × 4 angles. None of these figures is in the totals.

## Not verified

- Whether motedis' shipping table is net or gross, and whether the packing
  charge counts once or twice for about 31 kg.
- The alloy of the 40 × 40 × 4 angle.
- The cart prices: the loose-piece prices are worked out from the product data
  as the shop does, not read from a cart.
- The price of the wood screws and the plate's shipping.
- The rated load of motedis' hammer nuts.
- The delivery time of the hammer nuts and brackets.

## Panels, slide tape and slot covers (dropped)

The side and back panels of 3 mm white aluminium composite are gone with the
400 × 300 redesign; the angle joints and brackets keep the frames square and
the back stays open (`docs/design.md`). The user dropped slide tape and slot
covers too: the boxes slide on the bare aluminium of the flat legs, and the
slots stay open for an industrial look; only the eight bar ends keep their
caps.

[hs-mpx]: https://www.holz-speckmann.de/Multiplexplatte-Birke-E1-BB-CP-im-Zuschnitt-21-mm/MULBIZ-21MM
[pz-mpx]: https://www.plattenzuschnitt24.de/Multiplexplatte-Zuschnitt-21mm.html
[aidb-12]: https://www.ab-in-die-box.de/b2cde/euroboxen/nextgen/nextgen-2-0-cycle/eurobox-nextgen-2-0-cycle-griffe-geschlossen-400-x-300-x-120-mm-anthrazit.html
[aidb-22]: https://www.ab-in-die-box.de/b2cde/euroboxen/nextgen/nextgen-2-0-cycle/eurobox-nextgen-2-0-cycle-griffe-geschlossen-400-x-300-x-220-mm-anthrazit.html
[aidb-half]: https://www.ab-in-die-box.de/b2cde/einsatzkaesten-set-1-2-unterteilung-fuer-400x300x120.html
[aidb-quarter]: https://www.ab-in-die-box.de/b2cde/einsatzkaesten-set-1-4-unterteilung-fuer-400x300x120.html
