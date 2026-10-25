# Sources

Every fact the design, the parts list and the prices rest on, with its status
(`docs/conventions.md` → *Sources*). Prices were read on 2026-10-20; the
prices of the 400 × 300 redesign were read on 2026-10-21, those of 0012 and
0014 on 2026-10-22. All include 19 % VAT
unless marked; a net price converted with 19 % is `DERIVED`. A source is a
reference link, defined at the end of its section.

## Boxes: aidB Eurobox NextGen 2.0 Cycle 400 × 300

Sold by ab-in-die-BOX (aidB) in its private shop, made by Müller & Sohn. The
rack holds 12 × C2G43-12 and 3 × C2G43-22, closed handles, anthracite, with the
short 300 mm side and its handle at the front. The closed-handle articles
replace the open-handle [C2O43-12][aidb-o12] and [C2O43-22][aidb-o22] of the
same mould; the body geometry below was read from their photos.

| Fact                             | Value                                                                                                                | Status     | Source                                                                        |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------- | ----------------------------------------------------------------------------- |
| C2G43-12 outer L × W × H         | 400 × 300 × 120 mm                                                                                                   | VERIFIED   | [aidB C120][aidb-c12]                                                         |
| C2G43-12 inner L × W × H (top)   | 365 × 265 × 115 mm; 105 mm usable when stacked                                                                       | VERIFIED   | [aidB C120][aidb-c12]                                                         |
| C2G43-12 volume, weight          | 11 l, 800 g                                                                                                          | VERIFIED   | [aidB C120][aidb-c12]                                                         |
| C2G43-22 outer L × W × H         | 400 × 300 × 220 mm                                                                                                   | VERIFIED   | [aidB C220][aidb-c22]                                                         |
| C2G43-22 inner L × W × H (top)   | 365 × 265 × 215 mm; 205 mm usable when stacked                                                                       | VERIFIED   | [aidB C220][aidb-c22]                                                         |
| C2G43-22 volume, weight          | 20 l, 1180 g                                                                                                         | VERIFIED   | [aidB C220][aidb-c22]                                                         |
| Material                         | r-PP, 100 % PCR                                                                                                      | VERIFIED   | [aidB C120][aidb-c12]                                                         |
| Load, stack load                 | 25 kg, 300 kg                                                                                                        | VERIFIED   | [aidB C120][aidb-c12]                                                         |
| Floor, tolerance, temperature    | smooth; ± 5 mm; -10 to +60 °C                                                                                        | VERIFIED   | [aidB C120][aidb-c12]                                                         |
| C2G43-12 price                   | 8.08 € each without rings; 7.53 € each in a carton of 16; 9.36 € with rings                                          | VERIFIED   | [aidB C120][aidb-c12]                                                         |
| C2G43-22 price                   | 11.26 € each without rings; 10.49 € each in a carton of 8; 12.41 € with rings                                        | VERIFIED   | [aidB C220][aidb-c22]                                                         |
| Shipping                         | free in DE from 150 €                                                                                                | VERIFIED   | [aidB C120][aidb-c12]                                                         |
| Cycle uses the NextGen 2.0 mould | stated by a retailer                                                                                                 | SECONDARY  | kersten-sicherheitstechnik.de                                                 |
| Drawing, RAL code, CAD           | none published by aidB or Müller & Sohn; searched, not found                                                         | UNVERIFIED | roadmap 0004                                                                  |
| Inner floor, model of the 120    | 359 × 259 mm: Bito XL43121 floor 359 × 259 (top 368 × 268, 117 high); Utz RAKO 358 × 258                             | SECONDARY  | [Bito XL43121][bito-43121], [Utz 400x300x120][utz-43-12]                      |
| Inner floor, model of the 220    | 354 × 254 mm: the 120 slope over 215, 365 - 6 × 215 / 115 = 354 (265 - 6 × 215 / 115 = 254)                          | DERIVED    | [Bito XL43121][bito-43121]                                                    |
| Box geometry in the model        | rim 6, collar 31 set back 5, ledge lip 3, foot 18 with a 4 mm chamfer, panel set back 6; read from the photos by eye | UNVERIFIED | [aidB C120 photo 14][aidb-c12-img14], `rack.json` → `box_shape`, roadmap 0004 |
| Ribs in the model                | web pairs 2.5 thick, 16 wide outside, at 103 and 297 mm; a corner web 24 mm in                                       | UNVERIFIED | [aidB C2G43-12 photo 14][aidb-g12-img14]                                      |
| Pin blocks in the model          | 30 wide, centre 49 mm in, hole Ø4                                                                                    | UNVERIFIED | [aidB C2G43-12 photo 14][aidb-g12-img14]                                      |
| Handle tray in the model         | 8 mm deep inside the frame 145 × 50 mm, radius 12, top 15 mm below the rim; two webs from the frame up to the rim    | UNVERIFIED | [aidB C2G43-22 photo 14][aidb-g22-img14]                                      |
| Photo URLs                       | the cached `[aidb-c12-img]` URL returns a 1 KB placeholder on 2026-10-22; the uncached media path serves the photo   | VERIFIED   | [aidB C120 photo 14][aidb-c12-img14]                                          |
| Corner radii in the model        | outer 8 mm, inner 6 mm, edge rounds 0.8 mm; read from the product photo                                              | UNVERIFIED | [aidB C120 photo][aidb-c12-img]                                               |
| Handle in the model              | closed grip pocket 116 × 24 mm, radius 6, 12 mm deep, its top 28 mm below the rim; no lip, no opening                | UNVERIFIED | [aidB C2G43-12 photo 14][aidb-g12-img14], [ColorClip photo][aidb-r200-img]    |
| Colour                           | neutral dark grey, about sRGB #3F3F3F on the lit faces of the photo; no RAL                                          | UNVERIFIED | [aidB C120][aidb-c12]                                                         |
| Colour in the model              | linear 0.04 grey (about sRGB #383838), an estimate                                                                   | UNVERIFIED | `rack.json` → `box_shape`                                                     |

[aidb-c12]: https://www.ab-in-die-box.de/b2cde/euroboxen/nextgen/nextgen-2-0-cycle/eurobox-nextgen-2-0-cycle-griffe-geschlossen-400-x-300-x-120-mm-anthrazit.html
[aidb-c22]: https://www.ab-in-die-box.de/b2cde/euroboxen/nextgen/nextgen-2-0-cycle/eurobox-nextgen-2-0-cycle-griffe-geschlossen-400-x-300-x-220-mm-anthrazit.html
[aidb-o12]: https://www.ab-in-die-box.de/b2cde/euroboxen/nextgen/nextgen-2-0-cycle/eurobox-nextgen-2-0-cycle-griffe-offen-400-x-300-x-120-mm-anthrazit.html
[aidb-o22]: https://www.ab-in-die-box.de/b2cde/euroboxen/nextgen/nextgen-2-0-cycle/eurobox-nextgen-2-0-cycle-griffe-offen-400-x-300-x-220-mm-anthrazit.html
[bito-43121]: https://shop.bito.com/de-de/p/eurostapelbehaelter-xl-grundmodell-pv_6160/44900/188010
[utz-43-12]: https://www.utzgroup.de/geschlossener-eurobehaelter-400-300-120-mm/
[aidb-c12-img]: https://www.ab-in-die-box.de/media/catalog/product/cache/79731d4e47734d79fc5e92bea48c2a75/c/2/c2o43-12-12-1600x1600-shop_3575_1600x1600.jpg
[aidb-r200-img]: https://www.ab-in-die-box.de/media/catalog/product/cache/79731d4e47734d79fc5e92bea48c2a75/r/2/r200-00-01-set-1600x1600-shop_3179_1600x1600.jpg
[aidb-c12-img14]: https://www.ab-in-die-box.de/media/catalog/product/c/2/c2o43-12-14-1600x1600-shop_3149_1600x1600.jpg
[aidb-g12-img14]: https://www.ab-in-die-box.de/media/catalog/product/c/2/c2g43-12-14-1600x1600-shop_3154_1600x1600.jpg
[aidb-g22-img14]: https://www.ab-in-die-box.de/media/catalog/product/c/2/c2g43-22-14-1600x1600-shop_3152_1600x1600.jpg

## ColorClips

| Fact              | Value                                                                                                                                               | Status     | Source                                                            |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ----------------------------------------------------------------- |
| Article, contents | R200-00-xx-SET, 2 rings per pack, one pack per box (both handles)                                                                                   | VERIFIED   | [aidB C120][aidb-c12]                                             |
| Colours           | 9: Rot -01, Blau -02, Gelb -03, Schwarz -06, Grün -08, Magenta -11, Türkis -12, Hellgrün -13, Purpur -15                                            | VERIFIED   | [aidB C120][aidb-c12]                                             |
| Price             | 0.82 € per pack of 2                                                                                                                                | VERIFIED   | [aidB C120][aidb-c12]                                             |
| Colour codes      | no RAL, Pantone or sRGB code published for the rings; searched, not found                                                                           | UNVERIFIED | [aidB][aidb-home]                                                 |
| sRGB              | `rack.json` → `color_clips.colours`; a median read of aidB's nine ColorClip photos agrees within CIE76 8 and gives black #242424                    | UNVERIFIED | [aidB C120][aidb-c12], ColorClip photos                           |
| Size              | not published; the model uses a ring 145 × 50 × 2 mm round the grip pocket on the handle frame, radii 12 outside and 6 inside, read from the photos | UNVERIFIED | [ColorClip photo][aidb-r200-img], [aidB C120 photo][aidb-c12-img] |

[aidb-home]: https://www.ab-in-die-box.de/

## Inserts: NextGen sets for 400 × 300 × 120

| Fact                         | Value                                                                                                         | Status     | Source                                                 |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------ |
| Set 1/2 EES43-01-100-04      | 2 × 3613-100, each 133 × 365 × 100 mm                                                                         | VERIFIED   | [aidB set 1/2][aidb-s43-2]                             |
| Set 1/2 price                | 9.95 € (8.36 € net)                                                                                           | VERIFIED   | [aidB set 1/2][aidb-s43-2]                             |
| Set 1/4 EES43-02-100-04      | 4 × 1813-100, each 133 × 182 × 100 mm                                                                         | VERIFIED   | [aidB set 1/4][aidb-s43-4]                             |
| Set 1/4 price                | 12.49 € (10.50 € net)                                                                                         | VERIFIED   | [aidB set 1/4][aidb-s43-4]                             |
| Single sizes                 | 3613-100, 1813-100 (3.25 €), 0906-100 (67 × 91 mm)                                                            | VERIFIED   | [aidB set 1/4][aidb-s43-4]                             |
| Set outer, inner (both sets) | outer 366 × 266 × 100 mm, inner 355 × 255 × 97 mm, each ± 5 mm                                                | VERIFIED   | [aidB set 1/2][aidb-s43-2], [aidB set 1/4][aidb-s43-4] |
| Set material                 | Kunststoff (PS), polystyrene                                                                                  | VERIFIED   | [aidB set 1/2][aidb-s43-2], [aidB set 1/4][aidb-s43-4] |
| Fits only its own box height | "Aufgrund der Konizität aller Kunststoffboxen passen diese Einteilungen nicht in Euroboxen mit anderen Höhen" | VERIFIED   | [aidB set 1/2][aidb-s43-2], [aidB set 1/4][aidb-s43-4] |
| Insert taper in the model    | 4 mm per side from top to bottom: (366 - 355) / 2 - 1.5 mm wall = 4                                           | DERIVED    | [aidB set 1/2][aidb-s43-2]                             |
| Insert floor in the model    | 3 mm: 100 - 97 = 3; reading the inner size as the floor is UNVERIFIED                                         | DERIVED    | [aidB set 1/2][aidb-s43-2]                             |
| Fill of the inner top        | 266 × 365 mm (1/4: 266 × 364) in 265 × 365 mm ± 5 mm                                                          | DERIVED    | [aidB set 1/2][aidb-s43-2]                             |
| Handle from inside           | closed wall; the insert end walls stand behind it, the grip pocket is reached from outside                    | UNVERIFIED | roadmap 0004                                           |

[aidb-s43-2]: https://www.ab-in-die-box.de/b2cde/einsatzkaesten-set-1-2-unterteilung-fuer-400x300x120.html
[aidb-s43-4]: https://www.ab-in-die-box.de/b2cde/einsatzkaesten-set-1-4-unterteilung-fuer-400x300x120.html

## Materials in the model

| Fact                                  | Value                                                      | Status    | Source                           |
| ------------------------------------- | ---------------------------------------------------------- | --------- | -------------------------------- |
| IOR of PP, box and rings in the model | 1.492 for Plastic (PP); the model uses 1.49                | SECONDARY | [physicallybased PP][pb-pp]      |
| IOR of PS, inserts in the model       | about 1.59 at 589 nm (Sultanova 2009); the model uses 1.59 | SECONDARY | [refractiveindex.info PS][ri-ps] |

[pb-pp]: https://api.physicallybased.info/v2/materials
[ri-ps]: https://refractiveindex.info/?shelf=organic&book=polystyrene&page=Sultanova

## Fasteners and brackets in the model

Added with 0018; the values live in `design/rack.json` → `brackets` and
`fasteners`.

| Fact                                        | Value                                                                                                                 | Status   | Source                                                     |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------- | ---------------------------------------------------------- |
| Bracket 30 B-type slot 8, motedis S8BBR30   | legs 27 long, 6 thick, 28 wide; side walls 3 thick cut off at 32.5; hole 7.0 to 20.7 from the corner, 6.4 to 7.0 wide | VERIFIED | [motedis S8BBR30 CAD][mo-s8bbr30]                          |
| Hammer nut B-type slot 8 M6 and M5, motedis | 16.4 × 8 × 6                                                                                                          | VERIFIED | [motedis M6 CAD][mo-hm6-cad], [motedis M5 CAD][mo-hm5-cad] |
| ISO 4762 M8 head                            | dk 13, k 8                                                                                                            | VERIFIED | [ISO 4762 table][iso-4762]                                 |
| ISO 7380-1 M6 head                          | dk 10.5, k 3.3                                                                                                        | VERIFIED | [ISO 7380-1 table][iso-7380]                               |
| ISO 10642 (DIN 7991) heads M5, M6           | dk max 10 and 12; k = (dk − d) / 2 for the 90° head                                                                   | VERIFIED | [ISO 10642 table][iso-10642]                               |
| ISO 7089 washer M8                          | 8.4 × 16 × 1.6                                                                                                        | VERIFIED | [Böllhoff ISO 7089][boellhoff-7089]                        |

[mo-s8bbr30]: https://www.motedis.com/shop/products_files/Motedis_S8BBR30.zip
[mo-hm6-cad]: https://www.motedis.com/shop/products_files/Motedis_S8BHASNM6_1.zip
[mo-hm5-cad]: https://www.motedis.com/shop/products_files/Motedis_S8BHASNM5_1.zip
[iso-4762]: https://cdn.standards.iteh.ai/samples/34460/06335046afaf46fb8e84d91a3eda001d/ISO-4762-2004.pdf
[iso-7380]: https://cdn.standards.iteh.ai/samples/53671/84df01c5fcce4a91896ac3b0c55ca128/ISO-7380-1-2011.pdf
[iso-10642]: https://www.aramfix.com/content/files/i642buaps/datasheet%20iso%2010642.pdf
[boellhoff-7089]: https://eshop.boellhoff.de/out/media/pdf/ISO_7089_Stahl_HV3_gv___en.pdf

## Frame additions of the 400 × 300 design

| Fact                                  | Value                                                                            | Status     | Source                                 |
| ------------------------------------- | -------------------------------------------------------------------------------- | ---------- | -------------------------------------- |
| Profile 30 × 60L B-type slot 8, Dold  | 19.00 €/m + 1.00 € per cut; 1.489 kg/m; dropped with the 30 × 30 bottom bar      | VERIFIED   | [Dold 30x60][dold-3060]                |
| Profile 30 × 60L moment of inertia Iy | 19.5 cm⁴, from the page data; dropped with the 30 × 30 bottom bar                | SECONDARY  | [Dold 30x60][dold-3060]                |
| M8 core thread surcharges, Dold       | 1.00 € per end; 2.00 € extra for 80 mm deep; from the page JSON                  | UNVERIFIED | [Dold 30x30][dold-30]                  |
| CNC holes, Dold                       | at least 2.00 € per hole, only in the configurator                               | UNVERIFIED | [Dold 30x60][dold-3060]                |
| DIN 912 M8 × 100 8.8 zinc, Dold       | 1.11 € each (0.05 € base + 1.06 €)                                               | DERIVED    | [aluprofile-express][ape-912]          |
| DIN 912 M8 × 70 8.8 zinc, Dold        | about 2.79 € each (0.05 € base + 2.74 €), not the cart price                     | UNVERIFIED | [aluprofile-express][ape-912]          |
| DIN 912 M8 × 50 8.8 zinc, Dold        | 0.60 € each                                                                      | DERIVED    | [aluprofile-express][ape-912]          |
| Shipping Dold, pieces over 1 m        | DPD up to 1.5 m and 30 kg: 14.90 €; VAT basis not stated                         | VERIFIED   | [Dold shipping][dold-ship]             |
| Joint plates L and T 3030, motedis    | CPL3030, CPT3030; 90 × 90 × 4 mm, 5 holes; 2.00 € net each; dropped with 0017    | DERIVED    | [motedis L][mo-pl], [motedis T][mo-pt] |
| Joint plate shape, motedis drawing    | holes Ø6.5, 15 from the edges, 30 apart; corner filled to a chamfer 30–90 mm     | VERIFIED   | [motedis L][mo-pl], [motedis T][mo-pt] |
| Castor 100 mm solid rubber, Dold      | only a braked swivel (27.83 €) and a fixed castor (23.03 €, 136 mm high)         | VERIFIED   | [Dold 100 rubber][dold-100]            |

[dold-3060]: https://www.dold-mechatronik.de/Aluminiumprofil-30x60L-B-Typ-Nut-8-149kg-m-Zuschnitt-50-6000mm
[ape-912]: https://www.aluprofile-express.de/DIN-912-Zylinderschraube-mit-Innensechskant-8.8-verzinkt
[mo-pl]: https://www.motedis.com/de/Anschlussplatte-L-Alu-eloxiert-3030
[mo-pt]: https://www.motedis.com/de/Anschlussplatte-T-Alu-elox-3030

## Frame, angles and castors

| Fact                                     | Value                                                                 | Status    | Source                                       |
| ---------------------------------------- | --------------------------------------------------------------------- | --------- | -------------------------------------------- |
| Profile 30 × 30 B-type slot 8, motedis   | 7.89–9.87 €/m cut to length; M8 core thread offered                   | VERIFIED  | [motedis 30x30][mo-30]                       |
| Profile 30 × 30 B-type slot 8, Dold      | 9.90 €/m + 0.50 € per cut; 0.843 kg/m                                 | VERIFIED  | [Dold 30x30][dold-30]                        |
| Profile 30 × 30, motedis standard length | 7.81 € net/m; cut to length 6.63–8.29 € net/m                         | VERIFIED  | [motedis 30x30][mo-30]                       |
| M8 core thread per end                   | Dold 1.00 €; motedis 1.00 € net; myaluprofil 2.00 €                   | VERIFIED  | [Dold 30x30][dold-30], [myaluprofil][mya-30] |
| aluprofile-express                       | the same company as Dold Mechatronik                                  | VERIFIED  | [aluprofile-express imprint][ape-imp]        |
| Profile 30 × 30 moment of inertia        | 2.75 cm⁴; superseded by Dold's 2.68 cm⁴ (*Castor plates, open back*)  | SECONDARY | [myaluprofil][mya-30]                        |
| Inside angle bracket 30, motedis         | 7.27 € per 10                                                         | VERIFIED  | [motedis Winkel][mo-winkel]                  |
| Hammer nut M6 B-type slot 8, motedis     | 14.54 € per 100; can be fitted into an assembled frame                | VERIFIED  | [motedis Hammermutter][mo-hm]                |
| Heavy T-nut M6 B-type slot 8, motedis    | 31.73 € per 100                                                       | VERIFIED  | [motedis Nutenstein][mo-ns]                  |
| Heavy T-nut M6 slot 8, fitting           | must be in the slot before the profile is joined                      | VERIFIED  | [motedis Nutenstein][mo-ns]                  |
| Hammer nut slot 8, fitting               | inserted lengthwise, turns 90° when tightened                         | SECONDARY | [cnc-zubehoer][cnc-hm]                       |
| Angle 40 × 40 × 3 EN AW-6060             | 9.24 €/m + 0.50 € per cut + 3.00 € logistics                          | VERIFIED  | [aluprofile-express][ape-40]                 |
| Angle 40 × 40 × 3 EN AW-6060             | 9.14 €/m + 0.77 € per cut                                             | VERIFIED  | [alu-profile-zuschnitt][apz-40]              |
| Angle 50 × 50 × 3 EN AW-6060, Dold       | 11.65 €/m + 0.50 € per cut + 3.00 € logistics                         | VERIFIED  | [Dold 50x50x3][dold-50]                      |
| Angle 50 × 50 × 3, alu-profile-zuschnitt | 12.02 €/m, 0.81 kg/m, up to 5000 mm                                   | VERIFIED  | [alu-profile-zuschnitt 50][apz-50]           |
| Angle 50 × 50 × 3, profilzuschnitt24     | 12.11 €/m + 1.10 € per cut                                            | VERIFIED  | [profilzuschnitt24 50][pz-50]                |
| Castor 100 mm grey solid rubber, Dold    | 112 kg, 133 mm high, non-marking, brake, 27.83 €                      | VERIFIED  | [Dold 100 rubber][dold-100]                  |
| UHMW slide tape 25 mm                    | about 8 € per 10 m roll (thin film); movet 0.8 mm: 120.86 €; dropped  | SECONDARY | [Amazon][tape-amz], [movet][tape-movet]      |
| Shipping Dold                            | DHL up to 1 m: 6.90–8.90 €                                            | VERIFIED  | [Dold shipping][dold-ship]                   |
| Shipping motedis                         | 5.83 € net up to 111.09 €, 16.33 € net up to 222.19 €; packing 3.89 € | VERIFIED  | [motedis shipping][mo-ship]                  |

[mo-30]: https://www.motedis.com/de/Aluprofil-30x30-B-Typ-Nut-8
[dold-30]: https://www.dold-mechatronik.de/Aluminum-profile-30x30-B-type-groove-8
[mya-30]: https://www.myaluprofil.de/Aluminium-profile-30x30-groove-8-B-type.html?language=en
[mo-winkel]: https://www.motedis.com/de/Winkel-30-B-Typ-Nut-8
[mo-hm]: https://www.motedis.com/de/Hammermutter-B-Typ-Nut-8-M6
[mo-ns]: https://www.motedis.com/de/Nutenstein-schwer-B-Typ-Nut-8-M6
[ape-40]: https://www.aluprofile-express.de/Winkelprofile-gleichschenklig-40x40x3mm-Aluminium-EN-AW-6060-T66-AlMgSi05-0642kg-m-Zuschnitt-20-6000mm
[apz-40]: https://www.alu-profile-zuschnitt.de/aluprofile/alu-winkel/alu-winkel-40x40x3
[dold-100]: https://www.dold-mechatronik.de/Lenkrolle-100mm-Vollgummi-mit-Rueckenloch-und-Bremse
[tape-amz]: https://www.amazon.de/dp/B0CPT2NR3N
[tape-movet]: https://www.movet.eu/en/conveyor-wear-strips/movet-fix-adhesive-wear-strips/7333/movet-sliding-strip-pe-uhmw-color-natural-fda-25-x-0.8-mm-15-m.-1roll
[dold-ship]: https://www.dold-mechatronik.de/Versandinformationen
[mo-ship]: https://www.motedis.com/de/Liefer-und-Versandkosten:_:1.html
[ape-imp]: https://www.aluprofile-express.de/Impressum
[cnc-hm]: https://www.cnc-zubehoer.eu/Edelstahl-Nutenstein-Hammermutter-Nut-8-M6-schmal/AP.HM.N8M6S.ES
[dold-50]: https://www.dold-mechatronik.de/Winkelprofile-gleichschenklig-50x50x3mm-Aluminium-EN-AW-6060-T66-AlMgSi05-0809kg-m-Zuschnitt-20-6000mm
[apz-50]: https://www.alu-profile-zuschnitt.de/aluprofile/alu-winkel/alu-winkel-50x50x3
[pz-50]: https://www.profilzuschnitt24.de/l-profil-alu-50x50x3mm.html

## Castor plates, open back

Facts of roadmap 0014, read on 2026-10-22. The loads built on them are in
`design.md` → *Loads*.

| Fact                                        | Value                                                                                           | Status     | Source                                          |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------- | ---------- | ----------------------------------------------- |
| Castor 100 mm, back hole, no brake, Dold    | 69483: PU tread on PP, 125 mm high, 70 kg, 11 mm hole, offset 28, 0.29 kg; in stock             | VERIFIED   | [Dold 69483][dold-69483]                        |
| Castor 100 mm, Dold, price                  | 6.00 € each, 24.00 € for 4                                                                      | VERIFIED   | [Dold 69483][dold-69483]                        |
| Castor 100 mm, Dold, fixing                 | DIN 912 M8x20 with a DIN 125 washer, from inside the housing                                    | VERIFIED   | [Dold 69483][dold-69483]                        |
| Castor 100 mm, back hole, brake, Dold       | 69490: 8.10 €, "Nicht vorrätig"; same height, hole and offset as 69483                          | VERIFIED   | [Dold 69490][dold-69490]                        |
| Castor 100 mm, back hole, no brake, motedis | 995: the same castor, 22.31 € per 4; not enough stock                                           | VERIFIED   | [motedis 995][mo-995]                           |
| Castor 100 mm, head diameter                | Ø46 mm, read as text from the drawing; the feature not seen                                     | SECONDARY  | [motedis 995 drawing][mo-995-dwg]               |
| Castor 100 mm, non-marking                  | not stated by Dold or motedis                                                                   | UNVERIFIED | [Dold 69483][dold-69483], [motedis 995][mo-995] |
| Plate EN AW-5083 10 × 90, Dold              | AGP-10-90-Z, milled cast plate; 51.82 €/m + 1.00 € per cut; 2.43 kg/m                           | VERIFIED   | [Dold AGP-10-90-Z][dold-agp]                    |
| Plate 8 × 90, motedis                       | Aluminium Plättchen 8x90 mm, 30.63 € per 740 mm bar                                             | VERIFIED   | [motedis plate][mo-agp]                         |
| M8 thread in the 10 mm plate                | 10 mm engagement, 1.25 d, the low end of the usual rule for aluminium                           | UNVERIFIED | roadmap 0014                                    |
| Inside bracket 30 B-type slot 8, Dold       | 66895: 0.02 kg; 1.27 €, 1.09 € from 10                                                          | VERIFIED   | [Dold brackets][dold-winkel]                    |
| Profile 30 × 30 B-type slot 8, Dold         | 0.843 kg/m; I = 2.68 cm⁴                                                                        | VERIFIED   | [Dold 30x30L][dold-30l]                         |
| Profile 30 × 60L B-type slot 8, Dold        | 1.489 kg/m; Iy = 19.51 cm⁴; dropped with the 30 × 30 bottom bar                                 | VERIFIED   | [Dold 30x60][dold-3060]                         |
| Castor load rule, Blickle                   | T = (E + Z) / n × S; S = 1.0-1.5 for manual transport indoors, obstacles below 5 % of the wheel | VERIFIED   | [Blickle][blickle]                              |
| Castors that carry on an uneven floor       | n = 3 of 4                                                                                      | UNVERIFIED | convention, roadmap 0014                        |
| LEGO bulk density, Brick Architect          | "around 250 pieces per liter", "around 700 pieces per kilogram"                                 | VERIFIED   | [Brick Architect collection][ba-coll]           |
| LEGO bulk density, Eurobricks forum         | Pick-a-Brick cup 985 ml, 395 g; 5.68 l tub, 1.72-1.91 kg; packed cups 0.57-0.64 kg/l            | MEASURED   | [Eurobricks][eb-weight]                         |
| ABS INEOS Terluran GP-35, density           | 1.04 g/cm³                                                                                      | VERIFIED   | [INEOS GP-35][ineos-gp35]                       |
| LEGO is moulded from Terluran GP-35         | not confirmed                                                                                   | UNVERIFIED | [INEOS GP-35][ineos-gp35]                       |
| Clothing storage unit rule, CPSC            | ASTM F2057-23, 16 CFR 1261: 27.2 kg (60 lb) on an extended element                              | VERIFIED   | [CPSC][cpsc-csu]                                |
| EN 14749 / EN 16122 drawer load             | 75 N on the front of one extended drawer, drawers empty; quoted in the CPSC rule text           | SECONDARY  | [CPSC][cpsc-csu]                                |

[dold-69483]: https://www.dold-mechatronik.de/Lenkrolle-100-Rueckenloch-ohne-Bremse
[dold-69490]: https://www.dold-mechatronik.de/Lenkrolle-100-Rueckenloch-mit-Bremse
[mo-995]: https://www.motedis.com/de/Rolle-100-Rueckenloch-ohne-Bremse
[mo-995-dwg]: https://www.motedis.com/shop/products_files/Motedis_995-Drawing.pdf
[dold-agp]: https://www.dold-mechatronik.de/Plangefraeste-Gussplatte-Aluminium-EN-AW-5083-foliert-Dicke-10mm-Breite-90mm-243kg-m-Zuschnitt-20-3000mm
[mo-agp]: https://www.motedis.com/de/Aluminium-Plaettchen-8x90-mm
[dold-winkel]: https://www.dold-mechatronik.de/Winkel-und-Verbinder-30-B-Typ-Nut-8
[dold-30l]: https://www.dold-mechatronik.de/Aluminiumprofil-30x30L-B-Typ-Nut-8-084kg-m-Zuschnitt-50-6000mm
[blickle]: https://www.blickle.de/ratgeber/tragfaehigkeit
[ba-coll]: https://brickarchitect.com/guide/bricks/your_collection/
[eb-weight]: https://www.eurobricks.com/forum/forums/topic/72114-lego-weight/
[ineos-gp35]: https://eshop.ineos-styrolution.com/Product/Terluran_TERLURAN-GP-35_SKU300600120829.html
[cpsc-csu]: https://www.cpsc.gov/Business--Manufacturing/Business-Education/Business-Guidance/Clothing-Storage-Units

## Top plate

| Fact                                   | Value                                                                                                                    | Status     | Source                                                 |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ---------- | ------------------------------------------------------ |
| Swing-in T-nuts fit an assembled frame | hammer nuts and spring T-nuts go in from the open slot face                                                              | VERIFIED   | [BM Profiles][bm-nuts]                                 |
| Bracket with fixing set, B-type slot 8 | Winkel 30 with screw and nut, 1.93 €                                                                                     | SECONDARY  | [aluprofile-express][ape-acc]                          |
| Threaded insert Rampa SK M6            | about 2.46 € each, stainless                                                                                             | SECONDARY  | [schraubenking][rampa]                                 |
| Slot cover B-type slot 8               | about 0.42 € per unit; unit length to be checked; dropped, the user's choice                                             | SECONDARY  | [motedis cover][mo-cover]                              |
| Birch plywood 21 mm, cut to size       | 66.95 €/m² BB/CP, 15 plies (Holz-Speckmann); 91.40 €/m² BB/BB, 20.0–22.4 mm, 14.3 kg/m² (plattenzuschnitt24); 2026-10-22 | VERIFIED   | [Holz-Speckmann][hs-mpx], [plattenzuschnitt24][pz-mpx] |
| Birch plywood 20 mm                    | not sold by either shop; they step from 18 mm (13 plies) to 21 mm                                                        | VERIFIED   | [Holz-Speckmann][hs-mpx], [plattenzuschnitt24][pz-mpx] |
| Multiplex build                        | crosswise glued veneers, at least 5, often 7 or more layers                                                              | VERIFIED   | [plattenzuschnitt24][pz-mpx]                           |
| Plate in the model                     | 21 mm, 15 plies of 1.4 mm, oiled, face sRGB #C38E52 to #D6A86C; R10 corners and 1.5 mm edge break are the user's choice  | UNVERIFIED | `rack.json` → `top_plate`                              |
| Bracket with fixing set, Dold          | Winkel 30 B-Typ Nut 8 mit Befestigungssatz: 1.51 € from 10                                                               | VERIFIED   | [Dold brackets][dold-winkel]                           |
| Birch plywood 21 mm, E∥, Metsä DoP     | E∥ in bending 9 858 N/mm² for 21 mm birch plywood; taken for our generic 21 mm birch plywood, whose maker is not known   | SECONDARY  | [Metsä Wood DoP][metsa-dop]                            |
| EN 1995-1-1 Annex B, γ method          | mechanically jointed beams: (EI)ef = Σ (Ei Ii + γi Ei Ai ai²), γi = 1 / (1 + π² Ei Ai si / (Ki l²))                      | SECONDARY  | EN 1995-1-1:2004 + A1:2008                             |
| EN 1995-1-1 Table 7.1, slip modulus    | Kser = ρm^1.5 d / 23 N/mm per shear plane for screws in pre-drilled holes, doubled for a steel or aluminium side         | SECONDARY  | EN 1995-1-1:2004 + A1:2008                             |
| EN 1995-1-1 kdef for plywood           | kdef 0.8 for EN 636-1 plywood in service class 1; creep raises the plate's deflection by 1 + kdef                        | SECONDARY  | EN 1995-1-1:2004 + A1:2008                             |

[bm-nuts]: https://www.bm-profile.com/de/ratgeber/nutensteine/
[ape-acc]: https://www.aluprofile-express.de/Zubehoer-B-Typ-Nut-8
[rampa]: https://www.schraubenking-shop.de/M6-x-15-x-AD12mm-Rampa-Muffe-Typ-SK-Edelstahl-14305-P009199
[mo-cover]: https://www.motedis.com/de/Abdeckprofil-schwarz-B-Typ-Nut-8-1-Meter-X
[hs-mpx]: https://www.holz-speckmann.de/Multiplexplatte-Birke-E1-BB-CP-im-Zuschnitt-21-mm/MULBIZ-21MM
[pz-mpx]: https://www.plattenzuschnitt24.de/Multiplexplatte-Zuschnitt-21mm.html
[metsa-dop]: https://www.metsagroup.com/contentassets/2e9ddda886f04453825068d3b37afcdc/uk_doc_metsawood_birch_plywood_pf_2022-11-07.pdf

## LEGO sorting

| Fact                 | Value                                                     | Status   | Source                             |
| -------------------- | --------------------------------------------------------- | -------- | ---------------------------------- |
| LEGO sorting order   | by category, not by colour; split categories as they grow | VERIFIED | [Brick Architect][ba]              |
| LEGO sorting density | about 250 pieces per litre; prefer shallow containers     | VERIFIED | [Brick Architect ch. 4][ba-medium] |

[ba]: https://brickarchitect.com/guide/bricks/organization/
[ba-medium]: https://brickarchitect.com/guide/bricks/medium/

## Superseded: the 600 × 400 design

These facts served only the 600 × 400 design, which the 400 × 300 design
replaced on 2026-10-21 with the user's agreement; they are kept unchanged for
reference.

### Boxes: aidB Eurobox NextGen 2.0

Sold by ab-in-die-BOX (aidB), made by Müller & Sohn. The current line is
NextGen 2.0; the older Economy, Grip and Color lines were merged into it
([aidB blog][aidb-blog]).

| Fact                                  | Value                                                                       | Status     | Source                       |
| ------------------------------------- | --------------------------------------------------------------------------- | ---------- | ---------------------------- |
| N2G64-12 outer L × W × H              | 600 × 400 × 120 mm                                                          | VERIFIED   | [aidB 120][aidb-12]          |
| N2G64-12 inner L × W × H (top)        | 565 × 365 × 115 mm                                                          | VERIFIED   | [aidB 120][aidb-12]          |
| N2G64-12 usable height when stacked   | 105 mm                                                                      | VERIFIED   | [aidB 120][aidb-12]          |
| N2G64-12 floor                        | smooth, closed                                                              | VERIFIED   | [aidB 120][aidb-12]          |
| N2G64-12 weight, load, stack load     | 1210 g, 40 kg, 400 kg                                                       | VERIFIED   | [aidB 120][aidb-12]          |
| N2G64-22 outer L × W × H              | 600 × 400 × **228** mm; sold as "220", no true 220 exists                   | VERIFIED   | [aidB 228][aidb-22]          |
| N2G64-22 inner L × W × H (top)        | 565 × 365 × 215 mm                                                          | VERIFIED   | [aidB 228][aidb-22]          |
| N2G64-22 usable height when stacked   | 205 mm                                                                      | VERIFIED   | [aidB 228][aidb-22]          |
| N2G64-22 floor                        | reinforced: honeycomb outside, split by a centre bar, flat inside           | VERIFIED   | [aidB NextGen][aidb-nextgen] |
| N2G64-22 weight, load, stack load     | 2006 g, 40 kg, 400 kg                                                       | VERIFIED   | [aidB 228][aidb-22]          |
| Tolerance                             | ± 5 mm on every dimension                                                   | VERIFIED   | [aidB 120][aidb-12]          |
| Handles                               | grip recesses on the short 400 mm sides                                     | VERIFIED   | [aidB NextGen][aidb-nextgen] |
| Label area per long side              | 240 × 30 mm (120), 240 × 130 mm (228)                                       | VERIFIED   | [aidB 120][aidb-12]          |
| Rim                                   | self-centring stacking rim all round, hollow underneath                     | VERIFIED   | [aidB NextGen][aidb-nextgen] |
| Foam insert that fits inside          | 560 × 360 × 105 mm (120), 560 × 360 × 205 mm (228)                          | VERIFIED   | [aidB 120][aidb-12]          |
| Inner floor width                     | at least 360 mm (the foam insert fits)                                      | DERIVED    | [aidB 120][aidb-12]          |
| Foot height into the box below        | about 10 mm (115 − 105, 215 − 205)                                          | DERIVED    | [aidB 120][aidb-12]          |
| Walls taper                           | yes; inserts fit only their own box height                                  | VERIFIED   | [aidB insert set][aidb-set]  |
| Rim overhang, foot width, taper       | not published by aidB or Müller & Sohn                                      | UNVERIFIED | roadmap 0004                 |
| N2G64-12 price                        | grey 10.55 € net each (≈ 12.55 €); 11.51 € net is a coloured-handle variant | DERIVED    | [aidB 120][aidb-12]          |
| N2G64-22 price                        | 15.39 € net each, 14.33 € net from 8 (≈ 18.31 €, 17.05 €)                   | DERIVED    | [aidB 228][aidb-22]          |
| Private shop, minimum order, shipping | private shop exists; no minimum; free shipping in DE from 126.05 €          | VERIFIED   | [aidB 228 private][aidb-22b] |

[aidb-12]: https://www.ab-in-die-box.de/b2bde/eurobox-nextgen-2-0-griffe-geschlossen-600-x-400-x-120-mm.html
[aidb-22]: https://www.ab-in-die-box.de/b2bde/eurobox-nextgen-2-0-griffe-geschlossen-600-x-400-x-220-mm.html
[aidb-22b]: https://www.ab-in-die-box.de/eurobox-nextgen-2-0-griffe-geschlossen-600-x-400-x-220-mm.html
[aidb-nextgen]: https://www.ab-in-die-box.de/b2bde/euroboxen/nextgen.html
[aidb-blog]: https://www.ab-in-die-box.de/blog/post/euroboxen-nextgen-sortimentsumstellung
[aidb-set]: https://www.ab-in-die-box.de/b2bde/einsatzkaesten-set-1-4-unterteilung-fuer-600x400x120.html

### Boxes: regular Euroboxes

| Fact                               | Value                                                                          | Status    | Source                                            |
| ---------------------------------- | ------------------------------------------------------------------------------ | --------- | ------------------------------------------------- |
| Auer EG 64/12 HG outer, inner      | 600 × 400 × 120, 570 × 370 × 115 mm, 103 mm usable when stacked                | SECONDARY | [esd.equipment][auer-12]                          |
| Auer EG 64/12 HG floor, weight     | smooth, closed; 1.26 kg                                                        | SECONDARY | [esd.equipment][auer-12]                          |
| Auer EG 64/22 outer, inner         | 600 × 400 × 220, 570 × 370 × 215 mm, 203 mm usable when stacked                | SECONDARY | [Auer datasheet][auer-22]                         |
| Auer EG 64/xx floor variants       | smooth closed or reinforced closed; open or closed handles                     | VERIFIED  | [Auer shop][auer-shop]                            |
| Auer EG 64/12 price                | 12.69 € each, 8.46 € per pallet (Auer shop); 12.44 € (esd)                     | VERIFIED  | [Auer shop][auer-shop]                            |
| Auer EG 64/22 HG price             | 17.77 € each, 11.85 € per pallet (Auer shop); 17.41 € (boxic24)                | VERIFIED  | [Auer shop][auer-shop]                            |
| Auer shop net prices               | EG 64/12 10.66 €, EG 64/22 HG 14.93 € net each; free shipping from 250 € net   | VERIFIED  | [Auer shop][auer-shop], [Auer freight][auer-ship] |
| Utz RAKO 120 outer, inner          | 600 × 400 × 120, 553 × 353 × 114 mm, 99 mm usable                              | VERIFIED  | [Utz 120][utz-12]                                 |
| Utz RAKO 220 inner, inner at floor | 558 × 358 mm top; 552–558 × 352–358 mm at the floor                            | VERIFIED  | [Utz catalog][utz-cat]                            |
| Utz RAKO prices                    | 120: 17.53 €; 220: 20.74 € (business shop)                                     | DERIVED   | [Utz 220][utz-22]                                 |
| SSI Schäfer EF 6220 inner, price   | 553 × 353 × 216 mm; 34.68 € + 5.89 € packaging                                 | SECONDARY | [Schäfer Shop][ssi-22]                            |
| Bito XL 64221 inner                | 568 × 368 × 216 mm                                                             | SECONDARY | [lagerprofis][bito]                               |
| A measured Auer 600 × 400          | 597 × 397 mm in one forum post, exactly 600 × 400 in another                   | SECONDARY | [tx-board][tx-board]                              |
| Standard                           | no "Euronorm"; only VDA KLTs (VDA 4500) have a standard, actual size 594 × 396 | SECONDARY | [Wikipedia KLT][klt]                              |
| VDA 4500 nesting depth             | 15 mm, heights 147.5 / 213 / 280 mm                                            | VERIFIED  | [VDA 4500][vda]                                   |
| Boxes that fail on floor support   | Wibo (Hornbach, Hagebau), keeeper/OKT Robusto: no continuous bottom edge       | VERIFIED  | [IDEA-Regale][idea]                               |

[auer-12]: https://esd.equipment/de/auer-eg-64-12-hg.html
[auer-22]: https://esd.equipment/dokumente/auer/datenblatt/euro-containers-solid-eg-64-22.pdf
[auer-shop]: https://www.auer-packaging.com/de/de/Eurobeh%C3%A4lter-geschlossen.html
[auer-ship]: https://www.auer-packaging.com/de/de/Frachtkosten.html
[utz-12]: https://www.utzgroup.de/geschlossener-eurobehaelter-2-griffloecher-600-400-120-mm/
[utz-22]: https://www.utzgroup.de/geschlossener-eurobehaelter-2-griffe-600-400-220-mm/
[utz-cat]: https://www.abena.ch/pdf/behaelter/rako-d.pdf
[ssi-22]: https://www.schaefer-shop.de/p/eurobox-ssi-schaefer-ef-6220-geschlossen-polypropylen-b-600-x-t-400-x-h-220-mm-43-5-l-10171501
[bito]: https://www.lagerprofis.de/bito-eurostapelbehaelter-xl-xl-64221-600x400x220-blau-p5974527
[tx-board]: https://tx-board.de/threads/reale-groesse-von-euroboxen.162659/
[klt]: https://de.wikipedia.org/wiki/Kleinladungstr%C3%A4ger
[vda]: https://www.vda.de/dam/jcr:e5306eaa-0f16-4422-b396-f839acab244b/2026-01-05_VDA_4500_Version_3.1_DE.pdf
[idea]: https://www.idea-regale.de/euro-norm-boxen/

### Inserts for 600 × 400

| Fact                                 | Value                                                                        | Status     | Source                                       |
| ------------------------------------ | ---------------------------------------------------------------------------- | ---------- | -------------------------------------------- |
| Auer EK 2/100                        | 563 × 183 × 100 mm, 7.49 € net (≈ 8.91 €)                                    | VERIFIED   | [Auer EK][auer-ek], [Auer EK DE][auer-ek-de] |
| Auer EK 4/100                        | 282 × 183 × 100 mm, 4.47 € net (≈ 5.32 €)                                    | VERIFIED   | [Auer EK][auer-ek], [Auer EK DE][auer-ek-de] |
| Auer EK 8/100                        | 183 × 141 × 100 mm, 3.31 € net (≈ 3.94 €)                                    | VERIFIED   | [Auer EK][auer-ek], [Auer EK DE][auer-ek-de] |
| Auer EK fit                          | up to 8 inserts per 60 × 40 Auer box; tile 564 × 366 mm, no fillers          | VERIFIED   | [Auer EK][auer-ek]                           |
| Auer EK in a NextGen box             | very likely (aidB's own set is 566 × 366 mm); not confirmed                  | UNVERIFIED | roadmap 0004                                 |
| Auer EK prices DE and AT             | the same net prices on both pages, both plus VAT                             | VERIFIED   | [Auer EK][auer-ek], [Auer EK DE][auer-ek-de] |
| Auer EK pallet prices                | EK 2/100 5.00 €, EK 4/100 2.98 €, EK 8/100 2.21 € net (220, 440, 880 pieces) | VERIFIED   | [Auer EK][auer-ek]                           |
| Auer EK x/50, x/150 in a 120 box     | x/50 and x/100 fit under 115 mm inner height; x/150 does not                 | DERIVED    | [Auer EK][auer-ek], [esd.equipment][auer-12] |
| Insert mix for the six 120 boxes     | 1 × EK 2, 10 × EK 4, 24 × EK 8; 131.63 € net (≈ 156.64 €)                    | DERIVED    | [Auer EK][auer-ek]                           |
| HPS divider wall, long               | 562 × 3 × 100 mm for 60 × 40 × 12; 3.45 € net (4.17 €)                       | VERIFIED   | [TBA wall][tba-wall]                         |
| HPS divider wall, short              | 370 × 3 × 100 mm; one long and one short wall needed                         | VERIFIED   | [TBA wall][tba-wall]                         |
| HPS short wall in a NextGen box      | 370 mm against 365 mm inner top width; fit open                              | UNVERIFIED | roadmap 0004                                 |
| aidB insert sets for 600 × 400 × 120 | 566 × 366 × 100 mm with 8 filler boxes 34 × 46 mm in the middle              | VERIFIED   | [aidB set][aidb-set]                         |
| Utz RAKO inserts                     | made for 558 × 358 mm; leave about 10 mm in other boxes                      | SECONDARY  | [brw.ch][utz-ek]                             |

[auer-ek]: https://www.auer-packaging.com/at/de/Einsatzk%C3%A4sten-f%C3%BCr-Eurobeh%C3%A4lter.html
[auer-ek-de]: https://www.auer-packaging.com/de/de/Einsatzk%C3%A4sten-f%C3%BCr-Eurobeh%C3%A4lter.html
[utz-ek]: https://www.brw.ch/de-CH/einsatzbehaelter-utz-547240
[tba-wall]: https://www.tbaplast.de/trennwand-fur-eurobehalter-60x40x12-cm--lang

### Racks that take every brand

| Fact                            | Value                                                               | Status   | Source                       |
| ------------------------------- | ------------------------------------------------------------------- | -------- | ---------------------------- |
| Gruber container rack 600 × 400 | 409 mm clear width, 604 mm deep, rails 596 mm, 26 mm height steps   | VERIFIED | [Gruber][gruber]             |
| profilzuschnitt24 Eurobox rack  | 410 mm inner width without slides, 442 mm with slides               | VERIFIED | [profilzuschnitt24][pz-rack] |
| MH-Regale Advance               | slide rails, 25 mm hole pattern, 35 kg per level, optional end stop | VERIFIED | [MH-Regale][mh]              |
| HOOKZ drawer 60 × 40            | 565 × 365 mm frame; excludes Auer boxes                             | VERIFIED | [HOOKZ][hookz]               |
| IDEA-Regale camper frames       | boxes run on their continuous bottom edge; Auer, RAKO fit           | VERIFIED | [IDEA-Regale][idea]          |
| Hochbeet-Hans FIT4BOX           | guide strips 20 × 45 × 600 mm; advise fixing to the wall            | VERIFIED | [Hochbeet-Hans][hh]          |

[gruber]: https://gruber-systeme.eu/de/de/esd/behaelterregal-esd/1142/grundregal-behaelterregal-fuer-eurobehaelter-esd-600-x-400-mm
[pz-rack]: https://www.profilzuschnitt24.de/eurobox-regalsystem-mit-3-auszuegen-400x900-mm-100-KG.html
[mh]: https://www.mh-regale.de/Lagerregale/Behaelterregale/Regal-fuer-Euronormbehaelter-Advance.html
[hookz]: https://hookz-systeme.de/produkt/eurobox-schublade-60x40-quer/
[hh]: https://hochbeet-hans.at/produkt/euroboxen-regale/

### Frame: 75 mm castors and panels

| Fact                                                | Value                                            | Status    | Source                                                |
| --------------------------------------------------- | ------------------------------------------------ | --------- | ----------------------------------------------------- |
| Castor 75 mm, back hole, brake, Dold                | 60 kg, 100 mm high, PU on PP, 11 mm hole, 5.36 € | VERIFIED  | [Dold 75 brake][dold-75b]                             |
| Castor 75 mm, back hole, no brake, Dold             | 60 kg, 5.40 €                                    | VERIFIED  | [Dold 75][dold-75]                                    |
| Castor 75 mm, back hole, motedis                    | 60 kg; 22.83 € (brake) and 19.75 € (plain) per 4 | VERIFIED  | [motedis 75][mo-75b]                                  |
| Castor 75 mm, back hole, motedis "NEU"              | 48 kg only, below the 60 kg the rack needs       | VERIFIED  | [motedis 75 NEU][mo-75b-neu]                          |
| Aluminium composite 3 mm, white                     | about 39–48 €/m²                                 | SECONDARY | [ws-onlineshop][acp-ws], [plattenzuschnitt24][acp-pz] |
| Aluminium composite 3 mm, white, plattenzuschnitt24 | 48.10 €/m² cut to size                           | VERIFIED  | [plattenzuschnitt24 ACP][p24-acp]                     |

[dold-75b]: https://www.dold-mechatronik.de/Lenkrolle-75-Rueckenloch-mit-Bremse
[dold-75]: https://www.dold-mechatronik.de/Lenkrolle-75-Rueckenloch-ohne-Bremse
[acp-ws]: https://www.ws-onlineshop.de/alu-verbundplatten/
[acp-pz]: https://www.plattenzuschnitt24.de/alu-verbundplatten/
[mo-75b]: https://www.motedis.com/de/Rolle-75-Rueckenloch-mit-Bremse
[mo-75b-neu]: https://www.motedis.com/de/Rolle-75-Rueckenloch-mit-Bremse-NEU
[p24-acp]: https://www.plattenzuschnitt24.de/Alu-Verbundplatte-weiss-3mm.html

## Superseded: the 125 mm castors

These facts served only the castors before roadmap 0014, which replaced them
on 2026-10-22 with Dold 69483 on castor plates (*Castor plates, open back*);
they are kept unchanged for reference.

| Fact                               | Value                                                            | Status     | Source                       |
| ---------------------------------- | ---------------------------------------------------------------- | ---------- | ---------------------------- |
| Castor 125 mm, back hole, brake    | motedis, 10.51 € each, 40.78 € per 4                             | VERIFIED   | [motedis 125 brake][mo-125b] |
| Castor 125 mm, back hole, no brake | motedis, 7.73 € each, 30.01 € per 4                              | VERIFIED   | [motedis 125][mo-125]        |
| Castor 125 mm, properties          | PU on PP, total lock, 11 mm hole, offset 41, 160 mm high, 100 kg | VERIFIED   | [motedis 125 brake][mo-125b] |
| Castor 125 mm, non-marking         | not stated                                                       | UNVERIFIED | [motedis 125 brake][mo-125b] |

[mo-125b]: https://www.motedis.com/de/Rolle-125-Rueckenloch-mit-Bremse
[mo-125]: https://www.motedis.com/de/Rolle-125-Rueckenloch-ohne-Bremse
