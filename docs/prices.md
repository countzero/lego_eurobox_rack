# Prices

The cheapest sound way to buy every part of `design/rack.json` (roadmap 0007).

## Rules

- Checked on **2026-10-21**, on the supplier's own product page unless the
  status says otherwise.
- Every price includes 19 % VAT for a private buyer in Germany. A net price is
  multiplied by 1.19, rounded to the cent and marked `DERIVED`.
- Status follows `docs/conventions.md` → *Sources*. A price marked
  `UNVERIFIED` is an estimate and is not a fact; it is in a total only where
  the row says so.
- Quantities and lengths come from `parts` in `design/rack.json`. Profiles
  30 × 30: 8 × 791 + 2 × 1068 + 8 × 375 = 11.464 m in 18 pieces. Profiles
  30 × 60: 2 × 1068 = 2.136 m in 2 pieces. Angles: 36 × 435 = 15.660 m in 36
  pieces. No panels.
- aluprofile-express.de is run by Dold Mechatronik GmbH (same imprint, same
  shipping table, same products and prices), so it is not a second supplier;
  it is listed once as Dold.
- Alternative supplier rows are kept from the 2026-10-20 reading where the part
  still exists; their totals for the new quantities are `DERIVED`.

## Parts with status build

### Frame

| Part                      | Supplier              | Product                                     | Price incl. VAT                     | Unit       | For the quantity | Status     | Source        |
| ------------------------- | --------------------- | ------------------------------------------- | ----------------------------------- | ---------- | ---------------- | ---------- | ------------- |
| `profile.*` 30 × 30 (18)  | Dold                  | Aluminiumprofil 30x30L B-Typ Nut 8, cut     | 9.90 €/m + 0.50 € per piece         | metre      | 122.49 €         | DERIVED    | [dold-30]     |
| `profile.upright` M8      | Dold                  | M8 thread: 8 ends + 8 ends 80 mm deep       | 1.00 € per end, 2.00 € extra deep   | end        | 24.00 €          | UNVERIFIED | [dold-30]     |
| `profile.*` 30 × 30 (18)  | motedis               | Aluprofil 30x30 B-Typ Nut 8, Zuschnitt      | 7.89–9.87 €/m; cut fee not read     | metre      | 90.45–113.15 €   | DERIVED    | [mo-30]       |
| `profile.upright` M8      | motedis               | machining "M8", depth not read              | 1.00 € net, 1.19 € per end          | end        | 19.04 €          | DERIVED    | [mo-30]       |
| `profile.upright` M8      | myaluprofil           | Processing "M8", depth not read             | 2.00 € per end                      | end        | 32.00 €          | DERIVED    | [mya-30]      |
| `profile.bar_bottom` (2)  | Dold                  | Aluminiumprofil 30x60L B-Typ Nut 8, cut     | 19.00 €/m + 1.00 € per cut          | metre      | 42.58 €          | VERIFIED   | [dold-3060]   |
| `angle.*` (36)            | Dold                  | Winkelprofil 50x50x3 EN AW-6060 T66, cut    | 11.65 €/m + 0.50 €/cut + 3.00 €     | metre      | 203.44 €         | DERIVED    | [dold-50]     |
| `angle.*` (36)            | alu-profile-zuschnitt | Alu Winkel 50x50x3 AlMgSi0,5                | 12.02 €/m; cut fee not shown        | metre      | 188.23 € + cuts  | DERIVED    | [apz-50]      |
| `angle.*` (36)            | profilzuschnitt24     | L-Profil Aluminium 50x50x3 (roh)            | 12.11 €/m + 1.10 € per cut          | metre      | 229.24 €         | DERIVED    | [pz-50]       |
| `plate.joint_l` (8)       | motedis               | Verbinderplatte-L Alu eloxiert 3030 CPL3030 | 2.00 € net + 0.28 € net per line    | piece      | 19.37 €          | DERIVED    | [mo-plate-l]  |
| `plate.joint_t` (8)       | motedis               | Verbinderplatte-T Alu eloxiert 3030 CPT3030 | 2.00 € net + 0.28 € net per line    | piece      | 19.37 €          | DERIVED    | [mo-plate-t]  |
| `bracket.*` (62)          | motedis               | Winkel 30 B-Typ Nut 8                       | 7.27 € per 10                       | pack of 10 | 50.89 € (7)      | VERIFIED   | [mo-winkel]   |
| `bracket.*` (62)          | Dold                  | Winkel 30 B-Typ Nut 8 (66895)               | 1.09 € from 10                      | piece      | 67.58 €          | DERIVED    | [dold-winkel] |
| `bracket.*` (62)          | profilzuschnitt24     | Winkel 30x30 mm Nut 8                       | 1.59 € from 1                       | piece      | 98.58 €          | DERIVED    | [pz-nut8]     |
| `tnut.m6` (174)           | Dold                  | Hammermutter M6 B-Typ Nut 8 (DM.2005)       | 0.15 € from 50                      | piece      | 26.10 €          | DERIVED    | [dold-nuts]   |
| `tnut.m6` (174)           | motedis               | Hammermutter B-Typ Nut 8 M6                 | 14.54 € per 100                     | pack 100   | 29.08 € (2)      | DERIVED    | [mo-hm]       |
| `tnut.m5` (144)           | motedis               | Hammermutter B-Typ Nut 8 M5                 | 14.54 € per 100                     | pack 100   | 29.08 € (2)      | VERIFIED   | [mo-hm5]      |
| `tnut.m5` (144)           | Dold                  | Nutenstein schwer M5 B-Typ Nut 8 (DM.2111)  | 0.18 € from 100                     | piece      | 25.92 €          | DERIVED    | [dold-nuts]   |
| `screw.m6x12_button` (94) | motedis               | ISO 7380 M6x12, zinc-plated                 | 5.29 € per 100                      | pack 100   | 5.29 €           | VERIFIED   | [mo-7380-6]   |
| `screw.m6x12_button` (94) | Dold                  | DIN 7380 10.9 M6x12, zinc-plated            | 0.53 €                              | piece      | 49.82 €          | DERIVED    | [dold-7380]   |
| `screw.m6x10_socket` (80) | motedis               | ISO 4762 M6x10, zinc-plated                 | not read                            | piece      | not priced       | UNVERIFIED |               |
| `screw.m5x10_countersunk` | motedis               | DIN 7991 M5x10 (= ISO 10642), zinc-plated   | 5.29 € per 100                      | pack 100   | 10.58 € (2)      | VERIFIED   | [mo-7991]     |
| `screw.m5x10_countersunk` | Dold                  | DIN 7991 8.8 M5x10, zinc-plated             | from 0.32 €; M5x10 surcharge unread | piece      | from 46.08 €     | UNVERIFIED | [dold-7991]   |
| `screw.m8x100_socket` (8) | Dold                  | DIN 912 8.8 M8x100, zinc-plated             | 0.05 € + 1.06 € = 1.11 €            | piece      | 8.88 €           | DERIVED    | [dold-912]    |
| `screw.m8x50_socket` (8)  | Dold                  | DIN 912 8.8 M8x50, zinc-plated              | 0.60 €                              | piece      | 4.80 €           | DERIVED    | [dold-912]    |
| `washer.m8_large` (4)     | Dold                  | DIN 9021 (= ISO 7093) washer, zinc-plated   | about 0.13 €; M8 price not read     | piece      | about 0.52 €     | UNVERIFIED | [dold-9021]   |
| `castor.brake` (2)        | motedis               | Rolle 125 Rückenloch mit Bremse             | 10.51 € (4-pack 40.78 €)            | piece      | 21.02 €          | VERIFIED   | [mo-125b]     |
| `castor.plain` (2)        | motedis               | Rolle 125 Rückenloch ohne Bremse            | 7.73 € (4-pack 30.01 €)             | piece      | 15.46 €          | VERIFIED   | [mo-125]      |
| `cap.end_30` (4)          | Dold                  | Profilabdeckkappe 30 B-Typ Nut 8            | 0.86 €                              | piece      | 3.44 €           | DERIVED    | [dold-caps]   |
| `cap.end_30` (4)          | profilzuschnitt24     | Profilabdeckkappe Schwarz Nut 8 30x30       | 0.62 €                              | piece      | 2.48 €           | DERIVED    | [pz-cap]      |
| `cap.end_30x60` (4)       | Dold                  | end cap 30x60                               | not read                            | piece      | not priced       | UNVERIFIED |               |
| `cover.slot_8` (3636 mm)  | Dold                  | Abdeckprofil grau B-Typ Nut 8, 1 m, VPE 5   | 8.75 € per 5 m                      | pack of 5  | 8.75 €           | VERIFIED   | [dold-caps]   |
| `cover.slot_8` (3636 mm)  | Dold (ape shop)       | Abdeckprofil Natur B-Typ Nut 8, 1 m         | 2.19 €                              | piece      | 8.76 € (4)       | DERIVED    | [ape-cover]   |

Notes:

- The through holes for the M8 bolts in the bars are drilled at home. Dold
  drills CNC holes only in the configurator, from 2 € per hole (`UNVERIFIED`).
- The Dold M8 thread prices come from the page JSON, not from the visible
  page, hence `UNVERIFIED`; the 24.00 € is in the Dold total.
- The motedis plate price is per order line: (8 × 2.00 + 0.28) × 1.19 = 19.37 €
  per plate type.
- The motedis castors are PU on PP, total lock, 11 mm back hole, 41 mm offset,
  160 mm high, 100 kg each; non-marking is not stated. Prices are the
  single-piece prices from the page data.
- The Dold angle carries a 3.00 € logistics fee per order line.
- Dold's DM.2111 M5 nut is 3.16 € cheaper than the motedis M5 hammer nut; the
  split keeps the motedis nut, the one the angles were planned with.

### Slide tape

| Part           | Supplier        | Product                                   | Price incl. VAT         | Unit         | For the quantity | Status    | Source       |
| -------------- | --------------- | ----------------------------------------- | ----------------------- | ------------ | ---------------- | --------- | ------------ |
| `tape.uhmw_25` | Amazon (Dimeho) | Schubladen-Gleitband 25 mm, 33 ft (~10 m) | 7.69 € per roll         | roll         | 15.38 € (2)      | SECONDARY | [tape-amz]   |
| `tape.uhmw_25` | movet           | PE-UHMW sliding strip 25 × 0.8 mm, 15 m   | 101.56 € net = 120.86 € | roll of 15 m | 120.86 €         | DERIVED   | [tape-movet] |

The rack needs 13.05 m. The Amazon tape is a thin film of unstated thickness;
the movet strip is a rated 0.8 mm UHMW-PE. The totals take Amazon and name
movet as the durable option (+105.48 €).

### Boxes, rings and inserts

All from ab-in-die-BOX (aidB), private shop: the user wants one vendor for
boxes, rings and inserts.

| Part                  | Product                                            | Price incl. VAT     | Qty | For the quantity | Status   | Source         |
| --------------------- | -------------------------------------------------- | ------------------- | --- | ---------------- | -------- | -------------- |
| `box.e120`            | NextGen 2.0 Cycle C2O43-12, open handles, no rings | 8.08 €              | 12  | 96.96 €          | VERIFIED | [aidb-12]      |
| `box.e220`            | NextGen 2.0 Cycle C2O43-22, open handles, no rings | 11.26 €             | 3   | 33.78 €          | VERIFIED | [aidb-22]      |
| `clip.*`              | ColorClip set R200-00-xx-SET, 2 rings              | 0.82 € per pack     | 15  | 12.30 €          | VERIFIED | [aidb-12]      |
| `insert.set_half`     | Set 1/2 EES43-01-100-04, 2 × 3613-100              | 9.95 € (8.36 net)   | 6   | 59.70 €          | VERIFIED | [aidb-half]    |
| `insert.set_quarter`  | Set 1/4 EES43-02-100-04, 4 × 1813-100              | 12.49 € (10.50 net) | 6   | 74.94 €          | VERIFIED | [aidb-quarter] |

- A carton of 16 C2O43-12 costs 7.53 € each, 120.47 € for 16; it buys four
  boxes more than needed for 23.51 € more.
- Boxes with rings fitted cost 9.36 € (120) and 12.41 € (220): 149.55 € for
  the 15 boxes against 143.04 € for boxes plus separate ColorClips, which also
  allow one colour per level (3 packs each of red, turquoise, purple, yellow
  and blue; `docs/inserts.md`).
- The sets fit only NextGen 400 × 300 × 120 boxes (`docs/inserts.md`).

## Shipping

| Supplier | This order                                         | Cost    | Free from     | Status    | Source      |
| -------- | -------------------------------------------------- | ------- | ------------- | --------- | ----------- |
| Dold     | DPD, pieces over 1 m up to 1.5 m, ~25.5 kg (30 kg) | 14.90 € | none          | VERIFIED  | [dold-ship] |
| motedis  | 16.33 € net + packing 3.89 € net, above 111.09 net | 24.06 € | none          | DERIVED   | [mo-ship]   |
| Amazon   | with Prime or above the threshold                  | 0.00 €  | seller rule   | SECONDARY | [tape-amz]  |
| aidB     | free in Germany from 150 €                         | 0.00 €  | 150 €         | VERIFIED  | [aidb-12]   |

Dold's shipping table does not say whether its prices include VAT. The
1068 mm bars are what puts the Dold order in the DPD class up to 1.5 m.

## Recommended order split

Four shops: Dold for everything long and the M8 screws, motedis for
connectors, small screws and castors, Amazon for the tape, aidB for boxes,
rings and inserts.

| Shop    | Parts                                                                                                                                                      | Subtotal | Shipping | Total    |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | -------- | -------- |
| Dold    | `profile.*` incl. M8 threads, `angle.*`, `tnut.m6`, `cap.end_30`, `cover.slot_8`, `washer.m8_large`, `screw.m8x100_socket`, `screw.m8x50_socket`           | 445.00 € | 14.90 €  | 459.90 € |
| motedis | `plate.joint_l`, `plate.joint_t`, `bracket.inside_30`, `bracket.stop`, `screw.m6x12_button`, `screw.m5x10_countersunk`, `tnut.m5`, `castor.*`              | 171.06 € | 24.06 €  | 195.12 € |
| Amazon  | `tape.uhmw_25` (2 rolls)                                                                                                                                   | 15.38 €  | 0.00 €   | 15.38 €  |
| aidB    | `box.e120` × 12, `box.e220` × 3, `clip.*` × 15, `insert.set_half` × 6, `insert.set_quarter` × 6                                                            | 277.68 € | 0.00 €   | 277.68 € |

Dold: 122.49 + 24.00 + 42.58 + 203.44 + 26.10 + 3.44 + 8.75 + 0.52 + 8.88 +
4.80 = 445.00 €, with the 0.52 € washer estimate. motedis: 38.74 + 50.89 +
5.29 + 10.58 + 29.08 + 21.02 + 15.46 = 171.06 €; `screw.m6x10_socket` is not
priced.

| Total                           | Amount       |
| ------------------------------- | ------------ |
| Rack without boxes              | 670.40 €     |
| Boxes, rings and inserts (aidB) | 277.68 €     |
| **Overall**                     | **948.08 €** |

The rack total is 459.90 + 195.12 + 15.38 €; `screw.m6x10_socket` and
`cap.end_30x60` are not priced and come on top.

## Planned top plate (not in the totals)

| Part                | Supplier           | Product                                    | Price incl. VAT     | For the quantity   | Status     | Source        |
| ------------------- | ------------------ | ------------------------------------------ | ------------------- | ------------------ | ---------- | ------------- |
| `plate.top`         | Holz-Speckmann     | Multiplex Birke BB/CP 18 mm, Zuschnitt     | 56.95 €/m²          | 30.48 € (0.535 m²) | DERIVED    | [hs-mpx]      |
| `plate.top`         | plattenzuschnitt24 | Birke Multiplex 18 mm, BB/BB               | 67.30 €/m²          | 36.02 € (0.535 m²) | DERIVED    | [pz-mpx]      |
| `bracket.plate`     | Dold               | Winkel 30 B-Typ Nut 8 mit Befestigungssatz | 1.51 € from 10      | 15.10 €            | VERIFIED   | [dold-winkel] |
| `bracket.plate`     | motedis            | Winkel 30 B-Typ Nut 8 + hammer nut + screw | 7.27 € per 10 + set | about 10 €         | UNVERIFIED | [mo-winkel]   |
| `screw.wood_4_5x12` | any hardware store | wood screw 4.5 × 12 pan head               | not read            | about 2 €          | UNVERIFIED |               |

The plate is 1108 × 483 mm = 0.535 m². The square-metre prices are from the
2026-10-20 reading. The R25 corners, the edge finish and the plate's shipping
are not priced; the known part is about 48 € (30.48 + 15.10 + ~2).

## Not verified

- Dold M8 core thread prices (page JSON) and its CNC hole price.
- Dold DIN 7991 M5x10, DIN 9021 M8 and 30 × 60 end cap prices.
- motedis M6x10 socket screw price, its profile cut fee and metre price per
  length, and the thread depth of its M8 machining.
- Whether Dold's shipping table includes VAT.
- Whether the motedis castor tread is non-marking.
- Amazon tape thickness and seller shipping.
- Whether the inserts block the handle openings (`docs/inserts.md`).

## Rejected castors

- Dold 100 mm Vollgummi castors (112 kg, non-marking, 133 mm high) exist only
  as a braked swivel (27.83 €) and a fixed castor (23.03 €, 136 mm), 101.72 €
  for four, and the two heights differ.
- motedis "NEU" 75 mm (48 kg) and Dold 75 mm (60 kg) are too weak for 4 castors.

## Panels (dropped)

The side and back panels of 3 mm white aluminium composite are gone with the
redesign; the back stop is now `bracket.stop` and the joint plates brace the
frame (`docs/design.md`). This saves about 102.69 € for the panels plus
17.45 € shipping from plattenzuschnitt24.

[dold-30]: https://www.dold-mechatronik.de/Aluminiumprofil-30x30L-B-Typ-Nut-8-084kg-m-Zuschnitt-50-6000mm
[dold-3060]: https://www.dold-mechatronik.de/Aluminiumprofil-30x60L-B-Typ-Nut-8-149kg-m-Zuschnitt-50-6000mm
[dold-50]: https://www.dold-mechatronik.de/Winkelprofile-gleichschenklig-50x50x3mm-Aluminium-EN-AW-6060-T66-AlMgSi05-0809kg-m-Zuschnitt-20-6000mm
[dold-winkel]: https://www.dold-mechatronik.de/Winkel-und-Verbinder-30-B-Typ-Nut-8
[dold-nuts]: https://www.dold-mechatronik.de/Nutensteine-Hammermuttern-und-Schrauben-fuer-Aluminiumprofile-B-Typ-Nut-8
[dold-7380]: https://www.aluprofile-express.de/DIN-7380-Flachrundschraube-mit-Innensechskant-10.9-verzinkt
[dold-7991]: https://www.aluprofile-express.de/DIN-7991-Senkschraube-mit-Innensechskant-88-verzinkt
[dold-912]: https://www.aluprofile-express.de/DIN-912-Zylinderschraube-mit-Innensechskant-8.8-verzinkt
[dold-9021]: https://www.aluprofile-express.de/DIN-9021-Unterlegscheibe-gross-Stahl-verzinkt
[dold-caps]: https://www.dold-mechatronik.de/Abdeckkappen-und-profile-30-B-Typ-Nut-8
[dold-ship]: https://www.dold-mechatronik.de/Versandinformationen
[ape-cover]: https://www.aluprofile-express.de/Abdeckprofile_5
[mo-30]: https://www.motedis.com/de/Aluprofil-30x30-B-Typ-Nut-8
[mo-plate-l]: https://www.motedis.com/de/Anschlussplatte-L-Alu-eloxiert-3030
[mo-plate-t]: https://www.motedis.com/de/Anschlussplatte-T-Alu-elox-3030
[mo-winkel]: https://www.motedis.com/de/Winkel-30-B-Typ-Nut-8
[mo-hm]: https://www.motedis.com/de/Hammermutter-B-Typ-Nut-8-M6
[mo-hm5]: https://www.motedis.com/de/Hammermutter-B-Typ-Nut-8-M5
[mo-7380-6]: https://www.motedis.com/de/Schraube-DIN-EN-ISO-7380-Linsenkopfschraube/M6x12
[mo-7991]: https://www.motedis.com/de/Senkschraube-mit-Innensechskant-nach-DIN-7991/M5x10
[mo-125b]: https://www.motedis.com/de/Rolle-125-Rueckenloch-mit-Bremse
[mo-125]: https://www.motedis.com/de/Rolle-125-Rueckenloch-ohne-Bremse
[mo-ship]: https://www.motedis.com/de/Liefer-und-Versandkosten:_:1.html
[mya-30]: https://www.myaluprofil.de/Aluminium-profile-30x30-groove-8-B-type.html?language=en
[apz-50]: https://www.alu-profile-zuschnitt.de/aluprofile/alu-winkel/alu-winkel-50x50x3
[pz-50]: https://www.profilzuschnitt24.de/l-profil-alu-50x50x3mm.html
[pz-nut8]: https://www.profilzuschnitt24.de/nut-profile/nutprofil-zubehoer/Nut-8/
[pz-cap]: https://www.profilzuschnitt24.de/Profilabdeckkappe-Schwarz-Nut-8-30x30-mm.html
[tape-amz]: https://www.amazon.de/dp/B0CPT2NR3N
[tape-movet]: https://www.movet.eu/en/conveyor-wear-strips/movet-fix-adhesive-wear-strips/7333/movet-sliding-strip-pe-uhmw-color-natural-fda-25-x-0.8-mm-15-m.-1roll
[aidb-12]: https://www.ab-in-die-box.de/b2cde/euroboxen/nextgen/nextgen-2-0-cycle/eurobox-nextgen-2-0-cycle-griffe-offen-400-x-300-x-120-mm-anthrazit.html
[aidb-22]: https://www.ab-in-die-box.de/b2cde/euroboxen/nextgen/nextgen-2-0-cycle/eurobox-nextgen-2-0-cycle-griffe-offen-400-x-300-x-220-mm-anthrazit.html
[aidb-half]: https://www.ab-in-die-box.de/b2cde/einsatzkaesten-set-1-2-unterteilung-fuer-400x300x120.html
[aidb-quarter]: https://www.ab-in-die-box.de/b2cde/einsatzkaesten-set-1-4-unterteilung-fuer-400x300x120.html
[hs-mpx]: https://www.holz-speckmann.de/Multiplexplatte-Birke-E1-BB-CP-im-Zuschnitt-18-mm/MULBIZ-18MM
[pz-mpx]: https://www.plattenzuschnitt24.de/Multiplexplatten-Zuschnitt/Multiplexplatte-Birke/
