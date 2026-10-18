# 04 — Minotaur reference overhaul

V3 stage complete after two visual passes. Started after Slime Maiden commit1f493b6. Reference: V3 inline brown Minotaur card, no local filename. Existing class `MinotaurEntity`, ID `minotaur`, common renderer and native project inspected. Current gameplay includes close area melee and16-tick charge with per-target hit tracking; all runtime source, dimensions and timing remain unchanged. The old bone `axe` is retained for compatibility but its visual geometry becomes the reference-inspired hammer.

| Priority | Aspect | Existing → original V3 target |
| --- | --- | --- |
| 1 | Silhouette | Thin long trunk → broad bull barrel and shoulder hump |
| 1 | Proportions | Tall stretched waist → compact abdomen and massive upper body |
| 1 | Head | Long narrow shape → broad squared bovine skull |
| 1 | Face | Mask-like projection → dark projecting muzzle and articulated lower jaw |
| 2 | Eyes | Small bright marks → ivory sclera and dark pupils under heavy brows |
| 2 | Hair | Flat dark cap → stepped brown forelock and mane facets |
| 1 | Torso/limbs | Plain columns → pectorals, abdominal fur, thick biceps and bent shins |
| 1 | Hands/feet | Raised two-hand pose → connected gripping fingers, metal cuffs and split hooves |
| 1 | Species | Thin tall horns → paired ivory horns bending outward then upward/inward |
| 1 | Outfit | Long straight apron/belt → short layered magenta loincloth |
| 2 | Texture | Dark flat fur/wood-like lines → warm brown fur planes, ivory and gray metal |
| 1 | Weapon | Tall broad axe/maul obscuring face → short-shaft gray block hammer held through closed fist |

Baseline actual client passed and saved before changes. Pass1 rebuild:22 retained bones,108 cubes,ten original clips unchanged. Head/limb pivots adjusted for the new proportions; existing animation channel names retained. Original rear/tail construction remains conservative because only one reference angle exists. Final comparison and corrective pass completed.


Pass1 actual views found a long abdomen, overly upright narrow skull and hammer head near the shoulder. Pass2 compressed the abdomen, broadened the skull, added overlapping forelock/chest facets, lowered the hammer head and replaced thin fur scratches with broad painted patches. Final22 bones/115 cubes; all ten animation clips remain byte-identical. No emissive layer is used by the existing Minotaur renderer, so no unused glow texture is added.

Validation: baseline and both actual client runs passed; final all33 resource sets baked/synchronized, one selected creature presented. Front/side/three-quarter/back/distant, walking/running, attack and heavy at original24-tick impact, cast, hurt and death were inspected. The hammer remains attached to the closed right grip during the sampled impact poses; horns, tail and split hooves remain coherent. All20 asset/preservation tests passed. All gameplay Java/data/eggs,16 non-target species and the three finished creatures remain unchanged.

[Final actual state sheet](previews/minotaur-states.jpg) · [Released/final comparison](previews/minotaur-comparison.jpg). Remaining differences: original muscle/fur/horn construction and conservative unseen back; the reference is a hunched posed card while existing action timing and hitbox are preserved. Still samples do not certify every animation interpolation or a numerical similarity score.
