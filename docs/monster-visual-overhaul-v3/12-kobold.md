# 12 — Kobold reference overhaul

V3 stage complete after 2 visual passes. Started after Anubis87c3599. Primary reference: inline gray armored Kobold with pale short muzzle, swept crest, brown belt/scarf, sword and tail. Existing `KoboldEntity` Scout-profile melee,31-bone rig, nine clips, renderer/UV/native project inspected. Small1.3-block gameplay height, attributes, collision box, eggs, spawn data and registry preserved.

| Priority | Aspect | Released → original V3 target |
| --- | --- | --- |
| 1 | Silhouette | Thin purple reptile → larger gray head, crest and layered armor |
| 1 | Proportions | Small head → broader species head above compact armored body |
| 1 | Head | Narrow purple cap → gray scalp/crest and broader pale muzzle |
| 2 | Face | Dark snout → pale short reptilian muzzle with retained jaw/nostrils |
| 2 | Eyes | Gold → small dark irises |
| 1 | Hair | Dark purple strips → gray hair/scalp with swept two-step crest |
| 1 | Torso/limbs | Narrow purple armor → layered gray shoulder/shin plates |
| 1 | Hands/feet | Small extremities → retained gripping fingers/claws with defined toe plates |
| 1 | Species | Wide lateral ears → compact reptile ear fins, muzzle and original jointed scaled tail |
| 1 | Outfit | All-purple armor → gray armor with brown neck wrap/belt |
| 2 | Texture | Violet → neutral/lavender-gray scale/steel and brown leather |
| 1 | Weapon | Upright blade → forward/down shortsword and grip rotating as one |

Baseline graphical run passed. Pass1:166 cubes/31 bones, nine original clips unchanged. Head/hair/ear geometry resized, crest/armor/belt/scarf added and grip presentation corrected. Eyes are intentionally non-emissive; the glow mask addresses an unused tile. Actual corrective comparison completed. Hidden scaled back remains conservative original artwork.


Pass1 review found short hip plates, brown feet and a bright blade. Pass2 lengthens/widens the gray hip plates, adds a defined brown front pouch/clasp, makes the foot armor gray and darkens the blade metal. Gray hair receives broad painted clusters. Final31 bones/168 cubes; all nine clips remain byte-identical.

Validation: baseline and both graphical runs passed; all33 resource sets baked/synchronized and one selected species presented. Front/side/three-quarter/back/distant, short muzzle/ear/crest, scaled tail, walk/run, closed grip at sampled impact and coherent grounded corpse inspected. All22 asset/preservation checks pass. Gameplay/data/eggs,16 non-target species and eleven completed creatures unchanged.

Remaining differences: original reptilian muzzle/armor/hair construction, conservative rear and game lighting. Existing small size is preserved. Stills do not certify every animation interpolation or numerical similarity.

[Final actual state sheet](previews/kobold-states.jpg) · [Released/final comparison](previews/kobold-comparison.jpg).
