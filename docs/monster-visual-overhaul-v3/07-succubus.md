# 07 — Succubus reference overhaul

V3 stage complete after four visual passes. Started after Valkyriec2f14b6. Primary reference: V3 inline adult blonde Succubus with curled brown horns, black outfit/gauntlets/boots and red membrane wings. Existing `SuccubusEntity` inherits Demon-profile behavior;37-bone model,13 clips, renderer/atlas/native project inspected. All gameplay, ID, hitbox, eggs and spawning preserved. No weapon is depicted or added.

| Priority | Aspect | Released → original V3 target |
| --- | --- | --- |
| 1 | Silhouette | Long gown/tall horns/large wings → black boots, curled horns and compact red wings |
| 1 | Proportions | Small head over long skirt → broader adult head and separate booted legs |
| 1 | Head | Narrow face → enlarged pale framed head |
| 2 | Face | Thin mask → broader jaw/nose/mouth planes |
| 2 | Eyes | Light pink → muted red irises and dark lashes |
| 1 | Hair | Long straight gold locks → short layered blonde head/shoulder framing |
| 1 | Torso/limbs | Full black abdomen → fitted bodice, pale waist and dark waist straps |
| 1 | Hands/feet | Thin gloves/hidden feet → broad black gauntlets, fingers and boot soles |
| 1 | Species | Upright prongs → thick curled brown horns; compact articulated bat wings |
| 1 | Outfit | Full floor-length gown → black fitted hip outfit and tall boots |
| 2 | Texture | Burgundy ornamental → charcoal leather, warm blonde, brown horn and red membrane |
| — | Weapon | None; preserve unarmed magic casting |

Baseline actual client passed. Pass1:142 cubes/37 retained bones; all13 original animation clips unchanged. Gown removed in favor of articulated boot/hip forms; horns rebuilt, head/hair structurally resized, membrane span compacted, gauntlets/waist rebuilt. Actual corrective comparison completed. Existing tail is retained as species anatomy; reference does not expose its full rear construction.


Pass1 actual review found separated membrane strips and a corpse propped above the floor by spread wings. Pass2 rebuilt continuous overlapping membrane bays and adapted cosmetic support using the actual death wing transforms. Pass3 folded the wings more closely, but a new torso/arm contact check still failed with a2.29-pixel gap; the final correction folds the wing planes fully along the back. Only death is explicitly whitelisted; root rotation/duration and all other12 clips remain unchanged. The offline floor evaluator now includes numeric non-root death rotations instead of only rest geometry. Final client/check completed.


Final pass4 actual corpse is grounded with wings folded along the back; body/arm geometry clearance is0.1 model pixels in the offline check. New regression protects both full-model and body/arm floor contact. All21 asset/preservation checks pass. Baseline and four graphical runs passed; final all33 resource sets baked/synchronized, one species presented. Front/side/three-quarter/back/distant, action/impact, walking/running, fly/hover/phases and corpse inspected. Gameplay/data/eggs,16 non-target species and six finished creatures unchanged.

[Final actual state sheet](previews/succubus-states.jpg) · [Released/final comparison](previews/succubus-comparison.jpg). Remaining differences: original horn/membrane construction, conservative hidden tail/back, game lighting and rigid voxel surfaces. Sampled poses do not certify every interpolation or numerical similarity. Final136 cubes/37 bones;12 clips byte-identical, death-only cosmetic folding/support adapted.
