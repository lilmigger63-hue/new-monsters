# 10 — Fox Spirit Girl / Nine Tails reference overhaul

V3 stage complete after 3 visual passes. Started after Centaureed5aeb. Primary reference: supplied golden Nine Tails with green eyes and red/white outfit. ID `fox_spirit_girl` and existing `FoxSpiritGirlEntity` Shaman-profile spells/behavior preserved. Existing46-bone/nine-tail two-joint rig, eight clips, UV, renderer and native project inspected. No weapon is depicted or added; all gameplay, hitboxes, spawn data and eggs preserved.

| Priority | Aspect | Released → original V3 target |
| --- | --- | --- |
| 1 | Silhouette | Drooping ivory-tipped tail cluster → raised full golden nine-tail fan |
| 1 | Proportions | Small head/thin sleeves → broad adult face and full white sleeves |
| 1 | Head | Narrow golden face → broader pale framed head |
| 2 | Face | Small mouth/jaw → enlarged adult planes |
| 2 | Eyes | Green → retained readable green irises |
| 1 | Hair | Thin blonde locks → wider golden scalp/fringe and side volume |
| 1 | Torso/limbs | All-red sleeve silhouette → red bodice, white sleeves, dark waist |
| 1 | Hands/feet | Pale palms/brown shoes → black gloves/shoes and white stocking legs |
| 1 | Species | Small ivory points → golden ears and nine full tapered golden tails |
| 1 | Outfit | Red skirt/ivory trim → red/white sleeves, black waist and stocking charm patches |
| 2 | Texture | Orange/ivory tails → golden fur planes, warm hair, white cloth and dark accents |
| — | Weapon | None; preserve magic gesturing |

Baseline actual client passed. Pass1:147 cubes/46 bones, eight original clips unchanged. Head/ears/hair enlarged, tail rest/cube X rotations corrected upward, all nine original anchors retained with fuller middle volumes and golden tips, sleeves/hands/stockings rebuilt. Actual corrective comparison completed. Nine tails must be judged from back/rear-quarter because the reference card exposes only part of its fan.


Pass1 review found prong-like ears, an overly long red lower garment and a suspended corpse. Pass2 rebuilds tapered golden ears, short black skirt/waist and black collar, removes the old waist jewel, adds a small red hairpin and broad golden fur/hair painting. Geometry-derived death support reduces the height, but the spread fan still leaves2.2 model pixels of body/arm clearance. Pass3 gradually collects the nine tail anchors near the back during death and recalculates support with the animated rotations. The prior2.2-pixel clearance violates the new1.5-pixel body-contact threshold; the revised pose passes. Seven clips remain unchanged; death duration/root rotation remain unchanged. Final client review completed.


Final pass3 actual corpse rests on the body/arms with the tail fan relaxed behind it. Final46 bones/150 cubes; seven clips remain byte-identical and death-only collection/support is explicitly adapted.

Validation: baseline and three graphical runs passed; final all33 resource sets baked/synchronized and one species presented. Front/side/three-quarter/back/rear-quarter/distant, nine retained tail chains, golden ear/tip alignment, walk/run/action/impact and grounded corpse inspected. All22 asset/preservation tests pass. Gameplay/data/eggs,16 non-target species and nine completed creatures unchanged.

Remaining differences: original fur/tail/garment construction, conservative hidden details and game lighting. Tail overlap varies during motion; all nine anchors are retained, but every tail is not visible from every angle. Stills do not certify every interpolation or numerical similarity.

[Final actual state sheet](previews/fox_spirit_girl-states.jpg) · [Released/final comparison](previews/fox_spirit_girl-comparison.jpg).
