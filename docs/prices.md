# Prices

The cheapest sound way to buy every part of `design/rack.json` (roadmap 0007).

## Rules

- Checked on **2026-10-20**, on the supplier's own product page unless the
  status says otherwise.
- Every price includes 19 % VAT for a private buyer in Germany. A net price is
  multiplied by 1.19, rounded to the cent and marked `DERIVED`.
- Status follows `docs/conventions.md` → *Sources*. A price marked
  `UNVERIFIED` is an estimate and is not a fact; it is in a total only where
  the row says so.
- Quantities and lengths come from `parts` in `design/rack.json`. Profiles:
  8 × 823 + 12 × 416 + 8 × 550 = 15.976 m in 28 pieces. Angles: 30 × 610 =
  18.300 m in 30 pieces. Panels: 1368 × 823 + 2 × 613 × 823 = 2.135 m².
- aluprofile-express.de is run by Dold Mechatronik GmbH (same imprint, same
  shipping table, same products and prices), so it is not a second supplier;
  it is listed once as Dold.

## Parts with status build

### Frame

| Part                      | Supplier              | Product                                    | Price incl. VAT                     | Unit       | For the quantity | Status     | Source        |
| ------------------------- | --------------------- | ------------------------------------------ | ----------------------------------- | ---------- | ---------------- | ---------- | ------------- |
| `profile.*` (28 pcs)      | Dold                  | Aluminiumprofil 30x30L B-Typ Nut 8, cut    | 9.90 €/m + 0.50 € per piece         | metre      | 172.16 €         | VERIFIED   | [dold-30]     |
| `profile.upright` M8      | Dold                  | Bearbeitung "1x M8 Gewinde"                | 1.00 € per end                      | end        | 8.00 €           | VERIFIED   | [dold-30]     |
| `profile.*` (28 pcs)      | motedis               | Aluprofil 30x30 B-Typ Nut 8, Zuschnitt     | 7.89-9.87 €/m; cut fee not read     | metre      | 126.05-157.68 €  | DERIVED    | [mo-30]       |
| `profile.upright` M8      | motedis               | machining "M8"                             | 1.00 € net, 1.19 € per end          | end        | 9.52 €           | DERIVED    | [mo-30]       |
| `profile.*`               | myaluprofil           | Aluminium profile 30x30 groove 8 B-type    | metre price not read; cut 0.68 €    | metre      | not priced       | UNVERIFIED | [mya-30]      |
| `profile.upright` M8      | myaluprofil           | Processing "M8/- (one side M8)"            | 2.00 € per end                      | end        | 16.00 €          | VERIFIED   | [mya-30]      |
| `angle.*` (30 pcs)        | Dold                  | Winkelprofil 50x50x3 EN AW-6060 T66, cut   | 11.65 €/m + 0.50 €/cut + 3.00 €     | metre      | 231.20 €         | VERIFIED   | [dold-50]     |
| `angle.*` (30 pcs)        | alu-profile-zuschnitt | Alu Winkel 50x50x3 AlMgSi0,5               | 12.02 €/m; cut fee not shown        | metre      | 219.97 € + cuts  | VERIFIED   | [apz-50]      |
| `angle.*` (30 pcs)        | profilzuschnitt24     | L-Profil Aluminium 50x50x3 (roh)           | 12.11 €/m + 1.10 € per cut          | metre      | 254.61 €         | VERIFIED   | [pz-50]       |
| `angle.*`                 | motedis               | no 50 × 50 × 3 angle found                 |                                     |            |                  | UNVERIFIED | [mo-30]       |
| `bracket.inside_30`       | motedis               | Winkel 30 B-Typ Nut 8                      | 7.27 € per 10                       | pack of 10 | 29.08 €          | VERIFIED   | [mo-winkel]   |
| `bracket.inside_30`       | Dold                  | Winkel 30 B-Typ Nut 8 (66895)              | 1.09 € from 10                      | piece      | 43.60 €          | VERIFIED   | [dold-winkel] |
| `bracket.inside_30`       | profilzuschnitt24     | Winkel 30x30 mm Nut 8                      | 1.59 € from 1                       | piece      | 63.60 €          | VERIFIED   | [pz-nut8]     |
| `tnut.m6`                 | Dold                  | Hammermutter M6 B-Typ Nut 8 (DM.2005)      | 0.15 € from 50                      | piece      | 12.00 €          | VERIFIED   | [dold-nuts]   |
| `tnut.m6`                 | motedis               | Hammermutter B-Typ Nut 8 M6                | 14.54 € per 100                     | pack 100   | 14.54 €          | VERIFIED   | [mo-hm]       |
| `tnut.m5`                 | motedis               | Hammermutter B-Typ Nut 8 M5                | 14.54 € per 100                     | pack 100   | 29.08 €          | VERIFIED   | [mo-hm5]      |
| `tnut.m5`                 | Dold                  | Nutenstein schwer M5 B-Typ Nut 8 (DM.2111) | 0.18 € from 100                     | piece      | 32.40 €          | VERIFIED   | [dold-nuts]   |
| `screw.m6x12_button`      | motedis               | ISO 7380 M6x12, zinc-plated                | 5.29 € per 100                      | pack 100   | 5.29 €           | VERIFIED   | [mo-7380-6]   |
| `screw.m6x12_button`      | Dold                  | DIN 7380 10.9 M6x12, zinc-plated           | 0.53 €                              | piece      | 42.40 €          | VERIFIED   | [dold-7380]   |
| `screw.m5x10_countersunk` | motedis               | DIN 7991 M5x10 (= ISO 10642), zinc-plated  | 5.29 € per 100                      | pack 100   | 10.58 €          | VERIFIED   | [mo-7991]     |
| `screw.m5x10_countersunk` | Dold                  | DIN 7991 8.8 M5x10, zinc-plated            | from 0.32 €; M5x10 surcharge unread | piece      | from 38.40 €     | UNVERIFIED | [dold-7991]   |
| `screw.m5x10_button`      | motedis               | ISO 7380 M5x10, zinc-plated                | 6.61 € per 100                      | pack 100   | 6.61 €           | VERIFIED   | [mo-7380-5]   |
| `screw.m5x10_button`      | Dold                  | DIN 7380 10.9 M5x10, zinc-plated           | 0.35 €                              | piece      | 21.00 €          | VERIFIED   | [dold-7380]   |
| `screw.m8x25`             | motedis               | DIN 933 M8x25 (= ISO 4017), zinc-plated    | 1.85 € per 10                       | pack 10    | 1.85 €           | VERIFIED   | [mo-933]      |
| `screw.m8x25`             | Dold                  | DIN 912 M8x25 8.8 (socket head)            | 0.61 €                              | piece      | 4.88 €           | VERIFIED   | [dold-912]    |
| `washer.m8_large`         | Dold                  | DIN 9021 (= ISO 7093) washer, zinc-plated  | from 0.13 €; M8 price not read      | piece      | about 1.04 €     | UNVERIFIED | [dold-9021]   |
| `washer.m8_large`         | motedis               | not found in the screw shop                |                                     |            |                  | UNVERIFIED |               |
| `castor.brake`            | motedis               | Rolle 75 Rückenloch mit Bremse (06.07.02)  | 22.83 € per 4                       | pack of 4  | 22.83 €          | VERIFIED   | [mo-75b]      |
| `castor.brake`            | Dold                  | Lenkrolle 75 Rückenloch mit Bremse         | 5.36 €                              | piece      | 21.44 €          | VERIFIED   | [dold-75b]    |
| `castor.brake`            | profilzuschnitt24     | Lenkrolle 75 mm Rückenloch mit Bremse      | 7.90 € from 4                       | piece      | 31.60 €          | VERIFIED   | [pz-75b]      |
| `castor.plain`            | motedis               | Rolle 75 Rückenloch ohne Bremse (06.07.01) | 19.75 € per 4                       | pack of 4  | 19.75 €          | VERIFIED   | [mo-75]       |
| `castor.plain`            | Dold                  | Lenkrolle 75 Rückenloch ohne Bremse        | 5.40 €                              | piece      | 21.60 €          | VERIFIED   | [dold-75]     |
| `cap.end_30`              | Dold                  | Profilabdeckkappe 30 B-Typ Nut 8           | 0.86 €                              | piece      | 6.88 €           | VERIFIED   | [dold-caps]   |
| `cap.end_30`              | profilzuschnitt24     | Profilabdeckkappe Schwarz Nut 8 30x30      | 0.62 €                              | piece      | 4.96 €           | VERIFIED   | [pz-cap]      |
| `cap.end_30`              | motedis               | Abdeckkappe Profil 30 Typ B Nut 8          | 25.12 € per 100                     | pack 100   | 25.12 €          | VERIFIED   | [mo-cap]      |
| `cover.slot_8`            | Dold                  | Abdeckprofil grau B-Typ Nut 8, 1 m, VPE 5  | 8.75 € per 5 m                      | pack of 5  | 8.75 €           | VERIFIED   | [dold-caps]   |
| `cover.slot_8`            | Dold (ape shop)       | Abdeckprofil Natur B-Typ Nut 8, 1 m        | 2.19 €                              | piece      | 10.95 €          | VERIFIED   | [ape-cover]   |
| `cover.slot_8`            | motedis               | Abdeckprofil schwarz B-Typ Nut 8 (1 m + X) | 51.56 € per 100                     | pack 100   | 51.56 €          | VERIFIED   | [mo-cover]    |

Notes:

- motedis lists two 75 mm back-hole castors. Only the older 06.07.0x pair is
  rated 60 kg; the cheaper "NEU" pair (10146, 10147) is rated 48 kg and fails
  the spec.
- The Dold angle carries a 3.00 € logistics fee per order line, shown on the
  page next to the metre price.
- Dold's 0.50 € is per cut piece; motedis shows its cut fee only in the cart,
  so the motedis profile total is a range without cuts.

### Panels and slide tape

| Part           | Supplier           | Product                                   | Price incl. VAT                 | Unit         | For the quantity | Status    | Source       |
| -------------- | ------------------ | ----------------------------------------- | ------------------------------- | ------------ | ---------------- | --------- | ------------ |
| `panel.*`      | plattenzuschnitt24 | Alu Verbundplatte weiß 3 mm (Dilite), cut | 48.10 €/m²                      | m², cut      | 102.69 €         | VERIFIED  | [p24-acp]    |
| `panel.*`      | ws-onlineshop      | ALUCOM weiß beidseitig matt 3 mm, cut     | from 73.27 € per board          | board        | not priced       | VERIFIED  | [ws-acp]     |
| `panel.*`      | Dold               | Dibond Platte weiss 3 mm, Zuschnitt       | 160.32 €/m² + 10.00 € per piece | m², cut      | 372.26 €         | VERIFIED  | [dold-acp]   |
| `tape.uhmw_25` | Amazon (Dimeho)    | Schubladen-Gleitband 25 mm, 33 ft (~10 m) | 7.69 € per roll                 | roll         | 15.38 € (2)      | SECONDARY | [tape-amz]   |
| `tape.uhmw_25` | movet              | PE-UHMW sliding strip 25 × 0.8 mm, 15 m   | 101.56 € net = 120.86 €         | roll of 15 m | 120.86 €         | DERIVED   | [tape-movet] |

The Amazon tape is a thin film of unstated thickness; the movet strip is a
rated 0.8 mm UHMW-PE. Both are sold for this use; the totals take Amazon and
name movet as the durable option (+105.48 €).

### Boxes and inserts

| Part         | Supplier | Product                          | Price incl. VAT       | Unit  | For the quantity | Status  | Source      |
| ------------ | -------- | -------------------------------- | --------------------- | ----- | ---------------- | ------- | ----------- |
| `box.e120`   | Auer     | EG 64/12 HG, smooth closed floor | 10.66 € net = 12.69 € | piece | 76.11 €          | DERIVED | [auer-shop] |
| `box.e120`   | aidB     | NextGen 2.0 N2G64-12, grey       | 10.55 € net = 12.55 € | piece | 75.33 €          | DERIVED | [aidb-12]   |
| `box.e220`   | Auer     | EG 64/22 HG, closed floor        | 14.93 € net = 17.77 € | piece | 106.60 €         | DERIVED | [auer-shop] |
| `box.e220`   | aidB     | NextGen 2.0 N2G64-22, grey       | 15.39 € net = 18.31 € | piece | 109.88 €         | DERIVED | [aidb-22]   |
| `insert.ek2` | Auer     | EK 2/100 (563 × 183 × 100)       | 7.49 € net = 8.91 €   | piece | 8.91 €           | DERIVED | [auer-ek]   |
| `insert.ek4` | Auer     | EK 4/100 (282 × 183 × 100)       | 4.47 € net = 5.32 €   | piece | 53.19 €          | DERIVED | [auer-ek]   |
| `insert.ek8` | Auer     | EK 8/100 (183 × 141 × 100)       | 3.31 € net = 3.94 €   | piece | 94.53 €          | DERIVED | [auer-ek]   |

Auer and aidB both show net prices; the per-piece price is the single-unit
price. aidB's own insert sets are the only alternative to the EK inserts and
fit only aidB boxes (`docs/sources.md` → *Inserts*), so the EK inserts have
one supplier.

## NextGen against Auer

| Box class | Auer each | Auer × 6 | NextGen each | NextGen × 6 | Difference × 6  |
| --------- | --------- | -------- | ------------ | ----------- | --------------- |
| 120       | 12.69 €   | 76.11 €  | 12.55 €      | 75.33 €     | NextGen -0.78 € |
| 220       | 17.77 €   | 106.60 € | 18.31 €      | 109.88 €    | Auer -3.28 €    |

- Dimensions (`design/rack.json` → `box_models`, `docs/design.md`): both are
  600 × 400 outside. Auer is 570 × 370 inside, NextGen 565 × 365. The NextGen
  "220" is 228 mm tall, the Auer 220 mm; both stay inside the 220 class
  (max 233 mm).
- The EK inserts are confirmed only for Auer boxes; in a NextGen box they are
  likely but `UNVERIFIED` (roadmap 0004). This is why `box.e120` is Auer.
- The price gap is small either way. Buying both classes at Auer puts boxes and
  inserts in one order above Auer's free-shipping threshold; a NextGen order of
  6 × 220 alone (109.88 €) stays below aidB's 126.05 € threshold.

## Shipping

| Supplier            | This order                                                  | Cost     | Free from                 | Status    | Source      |
| ------------------- | ----------------------------------------------------------- | -------- | ------------------------- | --------- | ----------- |
| Dold                | DHL up to 1 m, ~29 kg (profiles 13.5, angles 14.8)          | 12.90 €  | none                      | DERIVED   | [dold-ship] |
| motedis             | base 5.83 € net + packaging 3.89 € net                      | 11.57 €  | accessories only: 16.66 € | DERIVED   | [mo-ship]   |
| plattenzuschnitt24  | XL parcel to 10 kg 9.45 € + bulky surcharge 8.00 €          | 17.45 €  | none                      | DERIVED   | [p24-ship]  |
| Auer                | carton 6.95 €                                               | 0.00 €   | 250 € net                 | VERIFIED  | [auer-ship] |
| aidB                | not read                                                    | not read | 126.05 €                  | VERIFIED  | [aidb-22]   |
| alu-profile-zuschn. | to 1.20 m: 8.00 € to 10 kg, 9.40 € to 20 kg; packing 1.40 € | 10.80 €  | none                      | VERIFIED  | [apz-ship]  |
| ws-onlineshop       | freight 79.95 €, under 250 € plus 35 €                      | 114.95 € | none                      | VERIFIED  | [ws-acp]    |
| Amazon              | with Prime or above the threshold                           | 0.00 €   | seller dependent          | SECONDARY | [tape-amz]  |

Dold's weight is 15.976 m × 0.843 kg/m + 18.3 m × 0.809 kg/m = 28.3 kg plus
small parts and packing, just under the 30 kg line (12.90 €); above it DHL
costs 26.90 € (+14.00 €). Whether motedis counts castors as accessories
is not stated; the total takes the higher fee with packaging.

## Recommended order split

Five shops: Dold for everything long, motedis for small parts and castors,
plattenzuschnitt24 for the panels, Amazon for the tape, Auer for boxes and
inserts. Moving the motedis items to Dold costs about 90 € more than the
motedis shipping saves; moving the caps to profilzuschnitt24 saves 1.92 € but
adds a shop.

| Shop               | Parts                                                                                                 | Subtotal | Shipping | Total    |
| ------------------ | ----------------------------------------------------------------------------------------------------- | -------- | -------- | -------- |
| Dold               | `profile.*` incl. 8 M8 threads, `angle.*`, `tnut.m6`, `cap.end_30`, `cover.slot_8`, `washer.m8_large` | 440.03 € | 12.90 €  | 452.93 € |
| motedis            | `bracket.inside_30`, `tnut.m5`, all screws, `castor.brake`, `castor.plain`                            | 125.07 € | 11.57 €  | 136.64 € |
| plattenzuschnitt24 | `panel.back`, `panel.side` × 2                                                                        | 102.69 € | 17.45 €  | 120.14 € |
| Amazon             | `tape.uhmw_25` (2 rolls)                                                                              | 15.38 €  | 0.00 €   | 15.38 €  |
| Auer               | `box.e120` × 6, `box.e220` × 6, `insert.ek2/ek4/ek8`                                                  | 339.34 € | 0.00 €   | 339.34 € |

| Total                | Amount        |
| -------------------- | ------------- |
| Rack without boxes   | 725.09 €      |
| Boxes (12, all Auer) | 182.71 €      |
| Inserts (35)         | 156.63 €      |
| **Overall**          | **1064.43 €** |

The Dold subtotal includes the 1.04 € washer estimate; motedis is 29.08 +
29.08 + 5.29 + 10.58 + 6.61 + 1.85 + 22.83 + 19.75 €.

## Planned top plate (not in the totals)

| Part                | Supplier           | Product                                    | Price incl. VAT     | For the quantity   | Status     | Source        |
| ------------------- | ------------------ | ------------------------------------------ | ------------------- | ------------------ | ---------- | ------------- |
| `plate.top`         | Holz-Speckmann     | Multiplex Birke BB/CP 18 mm, Zuschnitt     | 56.95 €/m²          | 52.58 € (0.923 m²) | VERIFIED   | [hs-mpx]      |
| `plate.top`         | plattenzuschnitt24 | Birke Multiplex 18 mm, BB/BB               | 67.30 €/m²          | 62.14 €            | VERIFIED   | [pz-mpx]      |
| `bracket.plate`     | Dold               | Winkel 30 B-Typ Nut 8 mit Befestigungssatz | 1.51 € from 10      | 15.10 €            | VERIFIED   | [dold-winkel] |
| `bracket.plate`     | motedis            | Winkel 30 B-Typ Nut 8 + hammer nut + screw | 7.27 € per 10 + set | about 10 €         | UNVERIFIED | [mo-winkel]   |
| `screw.wood_4_5x12` | any hardware store | wood screw 4.5 × 12 pan head               | not read            | about 2 €          | UNVERIFIED |               |

The R25 corners, the edge finish and the plate's shipping are not priced; the
known part is about 70 € (52.58 + 15.10 + ~2).

## Not verified

- motedis cut fee for the profile and its exact metre price per length.
- myaluprofil metre price (only the machining and cut surcharges were read).
- alu-profile-zuschnitt cut fee for 50 × 50 × 3 (configurator, not in the page).
- Dold DIN 7991 M5x10 and DIN 9021 M8 variant prices.
- Shipping weight class at Dold (just around 30 kg), motedis accessory rule
  for castors, plattenzuschnitt24 parcel class for the 1368 × 823 panel.
- Amazon tape thickness and seller shipping.

[dold-30]: https://www.dold-mechatronik.de/Aluminiumprofil-30x30L-B-Typ-Nut-8-084kg-m-Zuschnitt-50-6000mm
[dold-50]: https://www.dold-mechatronik.de/Winkelprofile-gleichschenklig-50x50x3mm-Aluminium-EN-AW-6060-T66-AlMgSi05-0809kg-m-Zuschnitt-20-6000mm
[dold-winkel]: https://www.dold-mechatronik.de/Winkel-und-Verbinder-30-B-Typ-Nut-8
[dold-nuts]: https://www.dold-mechatronik.de/Nutensteine-Hammermuttern-und-Schrauben-fuer-Aluminiumprofile-B-Typ-Nut-8
[dold-7380]: https://www.aluprofile-express.de/DIN-7380-Flachrundschraube-mit-Innensechskant-10.9-verzinkt
[dold-7991]: https://www.aluprofile-express.de/DIN-7991-Senkschraube-mit-Innensechskant-88-verzinkt
[dold-912]: https://www.aluprofile-express.de/DIN-912-Zylinderschraube-mit-Innensechskant-8.8-verzinkt
[dold-9021]: https://www.aluprofile-express.de/DIN-9021-Unterlegscheibe-gross-Stahl-verzinkt
[dold-75b]: https://www.dold-mechatronik.de/Lenkrolle-75-Rueckenloch-mit-Bremse
[dold-75]: https://www.dold-mechatronik.de/Lenkrolle-75-Rueckenloch-ohne-Bremse
[dold-caps]: https://www.dold-mechatronik.de/Abdeckkappen-und-profile-30-B-Typ-Nut-8
[dold-acp]: https://www.dold-mechatronik.de/Dibond-Platte-weiss-Dicke-3mm-Zuschnitt-Laenge-und-Breite-waehlbar
[dold-ship]: https://www.dold-mechatronik.de/Versandinformationen
[ape-cover]: https://www.aluprofile-express.de/Abdeckprofile_5
[mo-30]: https://www.motedis.com/de/Aluprofil-30x30-B-Typ-Nut-8
[mo-winkel]: https://www.motedis.com/de/Winkel-30-B-Typ-Nut-8
[mo-hm]: https://www.motedis.com/de/Hammermutter-B-Typ-Nut-8-M6
[mo-hm5]: https://www.motedis.com/de/Hammermutter-B-Typ-Nut-8-M5
[mo-7380-6]: https://www.motedis.com/de/Schraube-DIN-EN-ISO-7380-Linsenkopfschraube/M6x12
[mo-7380-5]: https://www.motedis.com/de/Schraube-DIN-EN-ISO-7380-Linsenkopfschraube/M5x10
[mo-7991]: https://www.motedis.com/de/Senkschraube-mit-Innensechskant-nach-DIN-7991/M5x10
[mo-933]: https://www.motedis.com/de/Sechskantschraube-DIN-EN-ISO-933/M8x25
[mo-75b]: https://www.motedis.com/de/Rolle-75-Rueckenloch-mit-Bremse
[mo-75]: https://www.motedis.com/de/Rolle-75-Rueckenloch-ohne-Bremse
[mo-cap]: https://www.motedis.com/de/Profilabdeckkappe-30-B-Typ-Nut-8
[mo-cover]: https://www.motedis.com/de/Abdeckprofil-schwarz-B-Typ-Nut-8-1-Meter-X
[mo-ship]: https://www.motedis.com/de/Liefer-und-Versandkosten:_:1.html
[mya-30]: https://www.myaluprofil.de/Aluminium-profile-30x30-groove-8-B-type.html?language=en
[apz-50]: https://www.alu-profile-zuschnitt.de/aluprofile/alu-winkel/alu-winkel-50x50x3
[apz-ship]: https://www.alu-profile-zuschnitt.de/versand
[pz-50]: https://www.profilzuschnitt24.de/l-profil-alu-50x50x3mm.html
[pz-nut8]: https://www.profilzuschnitt24.de/nut-profile/nutprofil-zubehoer/Nut-8/
[pz-75b]: https://www.profilzuschnitt24.de/lenkrolle-75mm-rueckenloch-mit-bremse.html
[pz-cap]: https://www.profilzuschnitt24.de/Profilabdeckkappe-Schwarz-Nut-8-30x30-mm.html
[p24-acp]: https://www.plattenzuschnitt24.de/Alu-Verbundplatte-weiss-3mm.html
[p24-ship]: https://www.plattenzuschnitt24.de/info/Versandinformationen.html
[ws-acp]: https://www.ws-onlineshop.de/alucom-alu-verbundplatten-weiss-3mm-stark-beidseitig-matt.html
[tape-amz]: https://www.amazon.de/dp/B0CPT2NR3N
[tape-movet]: https://www.movet.eu/en/conveyor-wear-strips/movet-fix-adhesive-wear-strips/7333/movet-sliding-strip-pe-uhmw-color-natural-fda-25-x-0.8-mm-15-m.-1roll
[auer-shop]: https://www.auer-packaging.com/de/de/Eurobeh%C3%A4lter-geschlossen.html
[auer-ek]: https://www.auer-packaging.com/de/de/Einsatzk%C3%A4sten-f%C3%BCr-Eurobeh%C3%A4lter.html
[auer-ship]: https://www.auer-packaging.com/de/de/Frachtkosten.html
[aidb-12]: https://www.ab-in-die-box.de/eurobox-nextgen-2-0-griffe-geschlossen-600-x-400-x-120-mm.html
[aidb-22]: https://www.ab-in-die-box.de/eurobox-nextgen-2-0-griffe-geschlossen-600-x-400-x-220-mm.html
[hs-mpx]: https://www.holz-speckmann.de/Multiplexplatte-Birke-E1-BB-CP-im-Zuschnitt-18-mm/MULBIZ-18MM
[pz-mpx]: https://www.plattenzuschnitt24.de/Multiplexplatten-Zuschnitt/Multiplexplatte-Birke/
