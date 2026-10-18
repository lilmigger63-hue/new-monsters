# 13 — Cyclops reference overhaul

V3 stage complete after 2 visual passes. Started after Koboldf8f4bb8. Primary reference: earlier supplied blue/gold Cyclops card with black hair, one central eye and a large brown-gold weapon. Existing oversized two-handed poleaxe remains the agreed technical weapon interpretation; no dual-weapon gameplay is invented. `CyclopsEntity` existing profile,30-bone rig, nine clips, native/UV/renderer inspected. Gameplay/IDs/hitbox/eggs/spawning preserved.

| Priority | Aspect | Released → original V3 target |
| --- | --- | --- |
| 1 | Silhouette | Small gold-haired helmet → broad black-haired helmet and blue crest |
| 1 | Proportions | Tiny head above broad armor → larger head and prominent single-eye opening |
| 1 | Head | Narrow gold cap → blue/black helmet framing |
| 1 | Face | Small tan planes → enlarged pale adult jaw/nose |
| 1 | Eyes | One bright blue eye → one centered muted iris/sclera; no extra eyes |
| 1 | Hair | Gold → black scalp/locks |
| 2 | Torso/limbs | Teal plate → blue/gold layered armor |
| 1 | Hands/feet | Bare palms/brown shoes → blue gauntlets and armored blue/gold feet |
| 1 | Species | Single eye maintained → larger unobstructed central ocular opening |
| 1 | Outfit | Teal/silver greaves → blue greaves, blue plume and restrained gold bands |
| 2 | Texture | Cyan/gold hair → blue/black/gold and brown-bronze weapon |
| 1 | Weapon | Bright block head → dark bronze/brown head with gold edges; both original solved grips preserved |

Baseline graphical run passed. Pass1:150 cubes/30 bones, nine clips unchanged. Head/helmet/hair/plume resized, lower armor/gauntlets rebuilt, weapon recolored to bronze/brown. Both arm/grip chains remain geometrically unchanged to retain their original cross-body support poses. Actual corrective comparison completed. Hidden armor/back details remain conservative original artwork.


Pass1 review found overly broad armor and gold cheek framing. Pass2 narrows the fitted armor/rig/haft together while retaining both rigid shared-chest grip chains, darkens the helmet frame and adds a thin gold brow. Original action clips contain no independent arm channels, so the shared carry remains attached. Death alone turns the held weapon along the body and recalculates support. Final30 bones/151 cubes; eight clips byte-identical, death duration/root rotation preserved.

Validation: baseline and both graphical runs passed; all33 resource sets baked/synchronized and one species presented. Front/side/three-quarter/back/distant, exactly one eye, plume/armor alignment, both palms on the shaft at sampled impact, walk/run and coherent grounded corpse inspected. All22 asset/preservation tests pass. Gameplay/data/eggs,16 non-target species and twelve completed creatures unchanged.

Remaining differences: original fitted armor/helmet and the existing oversized two-handed polearm interpretation, which is retained instead of inventing separate dual-weapon gameplay from the posed card. Hidden back is conservative; stills do not certify every interpolation or numerical similarity.

[Final actual state sheet](previews/cyclops-states.jpg) · [Released/final comparison](previews/cyclops-comparison.jpg).
