# Prices

The cheapest sound way to buy every part of `design/rack.json` (roadmap 0007).

## Rules

- Checked on **2026-10-21**, on the supplier's own product page unless the
  status says otherwise; the castors, castor plates, brackets, nuts and
  screws of roadmap 0014 were read again on **2026-10-22**.
- Every price includes 19 % VAT for a private buyer in Germany. A net price is
  multiplied by 1.19, rounded to the cent and marked `DERIVED`.
- Status follows `docs/conventions.md` → *Sources*. A price marked
  `UNVERIFIED` is an estimate and is not a fact; it is in a total only where
  the row says so.
- Quantities and lengths come from `parts` in `design/rack.json`. Profiles
  30 × 30: 8 × 791 + 4 × 1068 + 8 × 375 = 13.600 m in 20 pieces, 0.843 kg/m
  (11.46 kg). Angles: 36 × 435 = 15.660 m in 36 pieces, 0.809 kg/m. Weights
  per metre `VERIFIED` at Dold. Top plate 1108 × 483 mm = 0.535 m². No panels.
- aluprofile-express.de is run by Dold Mechatronik GmbH (same imprint, same
  shipping table, same products and prices), so it is not a second supplier;
  it is listed once as Dold.
- Alternative supplier rows are kept from the 2026-10-20 reading where the part
  still exists; their totals for the new quantities are `DERIVED`.
- Dold's screw and washer pages show a base price plus a surcharge per size in
  the variant list; that sum is not the price in the cart (DIN 912 M8x50 reads
  0.05 + 0.55 € but costs 0.84 €), so a price read that way is `UNVERIFIED`.

## Parts with status build

### Frame

| Part                           | Supplier              | Product                                     | Price incl. VAT                   | Unit       | For the quantity | Status     | Source        |
| ------------------------------ | --------------------- | ------------------------------------------- | --------------------------------- | ---------- | ---------------- | ---------- | ------------- |
| `profile.*` 30 × 30 (20)       | Dold                  | Aluminiumprofil 30x30L B-Typ Nut 8, cut     | 9.90 €/m + 0.50 € per piece       | metre      | 144.64 €         | DERIVED    | [dold-30]     |
| `profile.upright` M8           | Dold                  | M8 thread: 8 ends + 8 ends 80 mm deep       | 1.00 € per end, 2.00 € extra deep | end        | 24.00 €          | UNVERIFIED | [dold-30]     |
| `profile.*` 30 × 30 (20)       | motedis               | Aluprofil 30x30 B-Typ Nut 8, Zuschnitt      | 7.89–9.87 €/m; cut fee not read   | metre      | 107.30–134.23 €  | DERIVED    | [mo-30]       |
| `profile.upright` M8           | motedis               | machining "M8", depth not read              | 1.00 € net, 1.19 € per end        | end        | 19.04 €          | DERIVED    | [mo-30]       |
| `profile.upright` M8           | myaluprofil           | Processing "M8", depth not read             | 2.00 € per end                    | end        | 32.00 €          | DERIVED    | [mya-30]      |
| `angle.*` (36)                 | Dold                  | Winkelprofil 50x50x3 EN AW-6060 T66, cut    | 11.65 €/m + 0.50 €/cut + 3.00 €   | metre      | 203.44 €         | DERIVED    | [dold-50]     |
| `angle.*` (36)                 | alu-profile-zuschnitt | Alu Winkel 50x50x3 AlMgSi0,5                | 12.02 €/m; cut fee not shown      | metre      | 188.23 € + cuts  | DERIVED    | [apz-50]      |
| `angle.*` (36)                 | profilzuschnitt24     | L-Profil Aluminium 50x50x3 (roh)            | 12.11 €/m + 1.10 € per cut        | metre      | 229.24 €         | DERIVED    | [pz-50]       |
| `plate.castor` (4)             | Dold                  | Gussplatte EN AW-5083 10 × 90, AGP-10-90-Z  | 51.82 €/m + 1.00 € per cut        | 90 mm cut  | 22.66 €          | DERIVED    | [dold-agp]    |
| `plate.castor` (4)             | motedis               | Aluminium Plättchen 8x90 mm, 740 mm bar     | 30.63 € per bar                   | bar        | 30.63 €          | VERIFIED   | [mo-agp]      |
| `bracket.inside_30` (28)       | motedis               | Winkel 30 B-Typ Nut 8                       | 7.27 € per 10                     | pack of 10 | 21.81 € (3)      | VERIFIED   | [mo-winkel]   |
| `bracket.inside_30` (28)       | Dold                  | Winkel 30 B-Typ Nut 8 (66895)               | 1.27 €, 1.09 € from 10            | piece      | 30.52 €          | DERIVED    | [dold-winkel] |
| `bracket.inside_30` (28)       | profilzuschnitt24     | Winkel 30x30 mm Nut 8                       | 1.59 € from 1                     | piece      | 44.52 €          | DERIVED    | [pz-nut8]     |
| `tnut.m6` (72)                 | Dold                  | Hammermutter M6 B-Typ Nut 8 (66833-1)       | 0.52 €, 0.19 € from 100           | piece      | 19.00 € (100)    | DERIVED    | [dold-hm6]    |
| `tnut.m6` (72)                 | motedis               | Hammermutter B-Typ Nut 8 M6                 | 14.54 € per 100                   | pack 100   | 14.54 € (1)      | DERIVED    | [mo-hm]       |
| `tnut.m5` (144)                | motedis               | Hammermutter B-Typ Nut 8 M5                 | 14.54 € per 100                   | pack 100   | 29.08 € (2)      | VERIFIED   | [mo-hm5]      |
| `tnut.m5` (144)                | Dold                  | Nutenstein schwer M5 B-Typ Nut 8 (DM.2111)  | 0.18 € from 100                   | piece      | 25.92 €          | DERIVED    | [dold-nuts]   |
| `screw.m6x12_button` (56)      | motedis               | ISO 7380 M6x12, zinc-plated                 | 5.29 € per 100                    | pack 100   | 5.29 €           | VERIFIED   | [mo-7380-6]   |
| `screw.m6x12_button` (56)      | Dold                  | DIN 7380 10.9 M6x12, zinc-plated            | 0.53 €                            | piece      | 29.68 €          | DERIVED    | [dold-7380]   |
| `screw.m6x16_countersunk` (16) | motedis               | DIN 7991 M6x16 (= ISO 10642), zinc-plated   | 5.29 € per 100                    | pack 100   | 5.29 €           | VERIFIED   | [mo-7991-6]   |
| `screw.m6x16_countersunk` (16) | Dold                  | DIN 7991 8.8 M6x16, zinc-plated             | about 0.21 € (0.05 + 0.16)        | piece      | about 3.36 €     | UNVERIFIED | [dold-7991]   |
| `screw.m5x10_countersunk`      | motedis               | DIN 7991 M5x10 (= ISO 10642), zinc-plated   | 5.29 € per 100                    | pack 100   | 10.58 € (2)      | VERIFIED   | [mo-7991]     |
| `screw.m5x10_countersunk`      | Dold                  | DIN 7991 8.8 M5x10, zinc-plated             | 0.47 €                            | piece      | 67.68 €          | DERIVED    | [dold-7991]   |
| `screw.m8x70_socket` (8)       | Dold                  | DIN 912 8.8 M8x70, zinc-plated              | about 2.79 € (0.05 + 2.74)        | piece      | about 22.32 €    | UNVERIFIED | [dold-912]    |
| `screw.m8x50_socket` (8)       | Dold                  | DIN 912 8.8 M8x50, zinc-plated              | 0.84 €                            | piece      | 6.72 €           | DERIVED    | [dold-912]    |
| `screw.m8x20_socket` (4)       | Dold                  | DIN 912 8.8 M8x20, zinc-plated              | about 0.31 € (0.05 + 0.26)        | piece      | about 1.24 €     | UNVERIFIED | [dold-912]    |
| `washer.m8` (4)                | Dold                  | DIN 125 A 8.4 × 16, zinc-plated             | about 0.10 € (0.05 + 0.05)        | piece      | about 0.40 €     | UNVERIFIED | [dold-125]    |
| `castor.plain` (4)             | Dold                  | Lenkrolle 100 Rückenloch ohne Bremse 69483  | 6.00 €                            | piece      | 24.00 €          | VERIFIED   | [dold-100]    |
| `castor.plain` (4)             | motedis               | Rolle 100 Rückenloch ohne Bremse (995)      | 22.31 € per 4, out of stock       | pack of 4  | 22.31 €          | VERIFIED   | [mo-100]      |
| `cap.end_30` (8)               | Dold                  | Profilabdeckkappe 30 B-Typ Nut 8            | 0.86 €                            | piece      | 6.88 €           | DERIVED    | [dold-caps]   |
| `cap.end_30` (8)               | profilzuschnitt24     | Profilabdeckkappe Schwarz Nut 8 30x30       | 0.62 €                            | piece      | 4.96 €           | DERIVED    | [pz-cap]      |

Notes:

- The through holes for the M8 bolts in the bars and the holes of the castor
  plates (one M8 thread, one Ø14 hole, four countersunk M6 holes each) are
  drilled at home. Dold drills CNC holes only in the configurator, from 2 € per
  hole (`UNVERIFIED`).
- The castor plate is cut from Dold's 10 × 90 mm milled cast plate:
  4 × (90 mm × 51.82 €/m + 1.00 €) = 4 × (4.66 + 1.00) = 22.66 €; the prices
  are `VERIFIED`, the total `DERIVED`. The motedis bar is 8 mm thick and is cut
  at home.
- The Dold M8 thread prices come from the page JSON, not from the visible
  page, hence `UNVERIFIED`; the 24.00 € is in the Dold total.
- 100 Dold M6 hammer nuts at 0.19 € cost 19.00 €, less than the 72 needed at
  0.52 € (37.44 €); the rest are spares.
- The castor is the same at Dold and motedis: 100 mm PP wheel with PU tread,
  125 mm high, 11 mm back hole, 28 mm offset, 70 kg. Dold has it in stock;
  motedis shows "Derzeit nicht genügend Bestand verfügbar" (both `VERIFIED`
  2026-10-22). Non-marking is not stated.
- The braked twin, Dold 69490 at 8.10 €, has the same height, hole and offset
  but is "Nicht vorrätig" (`VERIFIED`); it is a drop-in upgrade for the front
  corners later and is not in the totals.
- The Dold angle carries a 3.00 € logistics fee per order line.
- Dold's DM.2111 M5 nut is 3.16 € cheaper than the motedis M5 hammer nut; the
  split keeps the motedis nut, the one the angles were planned with.
- The M8x70 price is Dold's base plus variant surcharge (0.05 + 2.74 €), not
  the cart price, hence `UNVERIFIED`. The surcharge is above the M8x100's
  (1.06 €, 1.35 € in the cart), so the Dold total takes the higher 22.32 €; at
  the M8x100's 1.35 € it would be 10.80 €.

### Top plate

| Part                     | Supplier           | Product                                    | Price incl. VAT     | For the quantity   | Status     | Source        |
| ------------------------ | ------------------ | ------------------------------------------ | ------------------- | ------------------ | ---------- | ------------- |
| `plate.top`              | Holz-Speckmann     | Multiplex Birke BB/CP 21 mm, Zuschnitt     | 66.95 €/m²          | 35.82 € (0.535 m²) | DERIVED    | [hs-mpx]      |
| `plate.top`              | plattenzuschnitt24 | Birke Multiplex 21 mm, BB/BB               | 91.40 €/m²          | 48.90 € (0.535 m²) | DERIVED    | [pz-mpx]      |
| `bracket.plate` (20)     | Dold               | Winkel 30 B-Typ Nut 8 mit Befestigungssatz | 1.51 € from 10      | 30.20 €            | DERIVED    | [dold-winkel] |
| `bracket.plate` (20)     | motedis            | Winkel 30 B-Typ Nut 8 + hammer nut + screw | 7.27 € per 10 + set | about 20 €         | UNVERIFIED | [mo-winkel]   |
| `screw.wood_4_5x16` (20) | any hardware store | wood screw 4.5 × 16 pan head               | not read            | about 2 €          | UNVERIFIED |               |

The plate is structural and is fitted before the rack is loaded
(`docs/assembly.md`, step 11), so it is in the totals: Holz-Speckmann's plate
for 35.82 €, the Dold brackets for 20 × 1.51 = 30.20 € in the Dold order, and
about 2 € of wood screws, an `UNVERIFIED` estimate counted in the totals. The
plate is 1108 × 483 mm = 0.535 m²; the square-metre prices are from the
2026-10-22 reading. The R10 corners, the edge finish and the plate's shipping
are not priced.

### Boxes, rings and inserts

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

## Shipping

| Supplier | This order                                                  | Cost    | Free from   | Status    | Source      |
| -------- | ----------------------------------------------------------- | ------- | ----------- | --------- | ----------- |
| Dold     | DPD, pieces over 1 m up to 1.5 m, about 29 kg (up to 30 kg) | 14.90 € | none        | VERIFIED  | [dold-ship] |
| motedis  | accessories only, above 16.66 €                             | 0.00 €  | 16.66 €     | DERIVED   | [mo-ship]   |
| aidB     | free in Germany from 150 €                                  | 0.00 €  | 150 €       | VERIFIED  | [aidb-12]   |

Dold's DPD class up to 1.5 m costs 14.90 € up to 30 kg and 23.90 € up to
60 kg; the table does not say whether its prices include VAT. The 1068 mm
bars put the order in that class. The weight is DERIVED: profiles and angles
11.46 + 12.67 = 24.13 kg, castors 1.16 kg, castor plates 0.87 kg, plus
brackets, caps and screws. Holz-Speckmann's shipping for the plate is
not read and not in the totals.

The motedis order no longer holds a profile, so it ships at the accessory
rate, free above 16.66 € (`VERIFIED` 2026-10-22). That every part in it counts
as an accessory is `UNVERIFIED`; if one does not, the order pays the basic
rate for up to 221.09 € plus the packing charge, 16.33 + 3.89 = 20.22 €
(whether net or gross is not stated).

## Recommended order split

Four shops and a hardware store: Dold for everything long, the castors, the
castor plates, the M6 hammer nuts, the M8 socket screws and the plate
brackets, motedis for connectors and the small screws,
Holz-Speckmann for the top plate, a hardware store for the wood screws, aidB
for boxes, rings and inserts. The
castors and plates go to Dold because motedis has the castor out of stock and
its plate is thinner and uncut.

| Shop           | Parts                                                                                                                                                                                            | Subtotal     | Shipping | Total        |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ | -------- | ------------ |
| Dold           | `profile.*` incl. M8 threads, `angle.*`, `plate.castor`, `castor.plain`, `tnut.m6`, `screw.m8x70_socket`, `screw.m8x50_socket`, `screw.m8x20_socket`, `washer.m8`, `cap.end_30`, `bracket.plate` | 505.50 €     | 14.90 €  | 520.40 €     |
| motedis        | `bracket.inside_30`, `screw.m6x12_button`, `screw.m6x16_countersunk`, `screw.m5x10_countersunk`, `tnut.m5`                                                                                       | 72.05 €      | 0.00 €   | 72.05 €      |
| Holz-Speckmann | `plate.top`, cut to 1108 × 483                                                                                                                                                                   | 35.82 €      | not read | 35.82 €      |
| Hardware store | `screw.wood_4_5x16` × 20                                                                                                                                                                         | about 2.00 € | 0.00 €   | about 2.00 € |
| aidB           | `box.e120` × 12, `box.e220` × 3, `clip.*` × 15, `insert.set_half` × 6, `insert.set_quarter` × 6                                                                                                  | 277.68 €     | 0.00 €   | 277.68 €     |

Dold: 144.64 + 24.00 + 203.44 + 22.66 + 24.00 + 19.00 + 22.32 + 6.72 + 1.24 +
0.40 + 6.88 + 30.20 = 505.50 €, with the 23.96 € estimate for the
M8x70 and M8x20 screws and the washers (22.32 + 1.24 + 0.40). motedis:
21.81 + 5.29 + 5.29 + 10.58 + 29.08 = 72.05 €.

| Total                           | Amount       |
| ------------------------------- | ------------ |
| Rack without boxes              | 630.27 €     |
| Boxes, rings and inserts (aidB) | 277.68 €     |
| **Overall**                     | **907.95 €** |

The rack total is 520.40 + 72.05 + 35.82 + 2.00 €, without the plate's
shipping. If motedis charges the basic rate, add 20.22 €. If Dold's M8x70
costs what its M8x100 costs (1.35 €), the Dold subtotal falls by 11.52 € to
493.98 €.

## Not verified

- Dold M8 core thread prices (page JSON) and its CNC hole price.
- Dold DIN 7991 M6x16, DIN 912 M8x70 and M8x20 and DIN 125 A 8.4 prices (base
  plus surcharge, not the cart price).
- Holz-Speckmann's shipping for the plate and the price of the wood screws.
- motedis profile cut fee and metre price per
  length, and the thread depth of its M8 machining.
- Whether Dold's shipping table includes VAT.
- Whether motedis counts every part of this order as an accessory.
- Whether the castor tread is non-marking.

## Rejected castors

- motedis 125 mm castors (160 mm high, 100 kg) with and without brake, the
  choice before roadmap 0014: too high under a castor plate; the 100 mm castor
  (125 mm high) carries the rack 25 mm lower.
- Dold 100 mm Vollgummi castors (112 kg, non-marking, 133 mm high) exist only
  as a braked swivel (27.83 €) and a fixed castor (23.03 €, 136 mm), 101.72 €
  for four, and the two heights differ.
- motedis "NEU" 75 mm (48 kg) and Dold 75 mm (60 kg) are too weak for 4 castors.

## Panels (dropped)

The side and back panels of 3 mm white aluminium composite are gone with the
redesign; the core-bolt joints keep the frames square and the back stays open
(`docs/design.md`). This saves about 102.69 € for the panels plus 17.45 €
shipping from plattenzuschnitt24.

## Slide tape and slot covers (dropped)

The user dropped both: the boxes slide on the bare aluminium of the flat legs,
and the slots stay open for an industrial look; only the eight bar ends keep
their caps (`docs/design.md`). The slot covers would have sat under the top
plate anyway. This saves 15.38 € for two rolls of Amazon (Dimeho) slide tape
`SECONDARY` [tape-amz] (the 0.8 mm movet strip [tape-movet] would have cost
120.86 €) and 8.75 € for a pack of five 1 m Dold slot covers `VERIFIED`
[dold-caps] ([ape-cover] sold them singly at 2.19 €), 24.13 € in all, and the
Amazon order with its shipping.

[dold-30]: https://www.dold-mechatronik.de/Aluminiumprofil-30x30L-B-Typ-Nut-8-084kg-m-Zuschnitt-50-6000mm
[dold-50]: https://www.dold-mechatronik.de/Winkelprofile-gleichschenklig-50x50x3mm-Aluminium-EN-AW-6060-T66-AlMgSi05-0809kg-m-Zuschnitt-20-6000mm
[dold-agp]: https://www.dold-mechatronik.de/Plangefraeste-Gussplatte-Aluminium-EN-AW-5083-foliert-Dicke-10mm-Breite-90mm-243kg-m-Zuschnitt-20-3000mm
[dold-winkel]: https://www.dold-mechatronik.de/Winkel-und-Verbinder-30-B-Typ-Nut-8
[dold-nuts]: https://www.dold-mechatronik.de/Nutensteine-Hammermuttern-und-Schrauben-fuer-Aluminiumprofile-B-Typ-Nut-8
[dold-hm6]: https://www.dold-mechatronik.de/Hammermutter-B-Typ-Nut-8-Gewindedurchmesser-M6
[dold-7380]: https://www.aluprofile-express.de/DIN-7380-Flachrundschraube-mit-Innensechskant-10.9-verzinkt
[dold-7991]: https://www.aluprofile-express.de/DIN-7991-Senkschraube-mit-Innensechskant-88-verzinkt
[dold-912]: https://www.aluprofile-express.de/DIN-912-Zylinderschraube-mit-Innensechskant-8.8-verzinkt
[dold-125]: https://www.aluprofile-express.de/DIN-125-Form-A-Unterlegscheibe-Stahl-verzinkt
[dold-100]: https://www.dold-mechatronik.de/Lenkrolle-100-Rueckenloch-ohne-Bremse
[dold-caps]: https://www.dold-mechatronik.de/Abdeckkappen-und-profile-30-B-Typ-Nut-8
[dold-ship]: https://www.dold-mechatronik.de/Versandinformationen
[ape-cover]: https://www.aluprofile-express.de/Abdeckprofile_5
[mo-30]: https://www.motedis.com/de/Aluprofil-30x30-B-Typ-Nut-8
[mo-agp]: https://www.motedis.com/de/Aluminium-Plaettchen-8x90-mm
[mo-winkel]: https://www.motedis.com/de/Winkel-30-B-Typ-Nut-8
[mo-hm]: https://www.motedis.com/de/Hammermutter-B-Typ-Nut-8-M6
[mo-hm5]: https://www.motedis.com/de/Hammermutter-B-Typ-Nut-8-M5
[mo-7380-6]: https://www.motedis.com/de/Schraube-DIN-EN-ISO-7380-Linsenkopfschraube/M6x12
[mo-7991]: https://www.motedis.com/de/Senkschraube-mit-Innensechskant-nach-DIN-7991/M5x10
[mo-7991-6]: https://www.motedis.com/de/Senkschraube-mit-Innensechskant-nach-DIN-7991/M6x16
[mo-100]: https://www.motedis.com/de/Rolle-100-Rueckenloch-ohne-Bremse
[mo-ship]: https://www.motedis.com/de/Liefer-und-Versandkosten:_:1.html
[mya-30]: https://www.myaluprofil.de/Aluminium-profile-30x30-groove-8-B-type.html?language=en
[apz-50]: https://www.alu-profile-zuschnitt.de/aluprofile/alu-winkel/alu-winkel-50x50x3
[pz-50]: https://www.profilzuschnitt24.de/l-profil-alu-50x50x3mm.html
[pz-nut8]: https://www.profilzuschnitt24.de/nut-profile/nutprofil-zubehoer/Nut-8/
[pz-cap]: https://www.profilzuschnitt24.de/Profilabdeckkappe-Schwarz-Nut-8-30x30-mm.html
[tape-amz]: https://www.amazon.de/dp/B0CPT2NR3N
[tape-movet]: https://www.movet.eu/en/conveyor-wear-strips/movet-fix-adhesive-wear-strips/7333/movet-sliding-strip-pe-uhmw-color-natural-fda-25-x-0.8-mm-15-m.-1roll
[aidb-12]: https://www.ab-in-die-box.de/b2cde/euroboxen/nextgen/nextgen-2-0-cycle/eurobox-nextgen-2-0-cycle-griffe-geschlossen-400-x-300-x-120-mm-anthrazit.html
[aidb-22]: https://www.ab-in-die-box.de/b2cde/euroboxen/nextgen/nextgen-2-0-cycle/eurobox-nextgen-2-0-cycle-griffe-geschlossen-400-x-300-x-220-mm-anthrazit.html
[aidb-half]: https://www.ab-in-die-box.de/b2cde/einsatzkaesten-set-1-2-unterteilung-fuer-400x300x120.html
[aidb-quarter]: https://www.ab-in-die-box.de/b2cde/einsatzkaesten-set-1-4-unterteilung-fuer-400x300x120.html
[hs-mpx]: https://www.holz-speckmann.de/Multiplexplatte-Birke-E1-BB-CP-im-Zuschnitt-21-mm/MULBIZ-21MM
[pz-mpx]: https://www.plattenzuschnitt24.de/Multiplexplatte-Zuschnitt-21mm.html
