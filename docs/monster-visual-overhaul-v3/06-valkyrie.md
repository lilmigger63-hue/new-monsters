# 06 — Valkyrie reference overhaul

V3 stage complete after three visual passes. Started after Vampire054cbfd. Primary reference: inline silver-armored Valkyrie card. Existing expansion Valkyrie uses Scout-profile melee/cooperation; renderer,32-bone model,13 clips, texture/UV and native project inspected. Combat, ID `valkyrie`, attributes, eggs, spawning and hitbox preserved. Sword and shield remain attached to their existing wrist/forearm bones.

| Priority | Aspect | Released → original V3 target |
| --- | --- | --- |
| 1 | Silhouette | Thin armored body → larger winged helmet, layered shoulders and black wing fan |
| 1 | Proportions | Small head/light boots → broad helmeted adult head and substantial greaves |
| 1 | Head | Small silver cap → brow/cheek plates and swept helmet winglets |
| 2 | Face | Small facial area → enlarged pale adult planes |
| 2 | Eyes | Blue glow → restrained red irises |
| 1 | Hair | Silver-gray locks → blonde framing under helmet |
| 2 | Torso/limbs | Light armor → stacked silver shoulder/greave plates with dark joints |
| 1 | Hands/feet | Narrow boots → broad metal toes and segmented shins |
| 1 | Species | Low inward folded feather tips → distinct black feathers fanning upward from back |
| 1 | Outfit | Muted gray → silver/charcoal armor and short red central tabard |
| 2 | Texture | Blue-gray ornamental tiles → neutral metal planes and dark feather shading |
| 1 | Weapon | Sword/shield → preserve closed grip and attachment under attack/flight |

Pass1 adapts existing detailed geometry with structural head/helmet expansion, new metal winglets, greave/shoulder plating and feather rest-rotation correction. All13 original clips retained, with no timing changes. Actual comparison/corrections completed. Hidden armor/back details remain conservative original artwork.


Pass1 real client passed but review found oversized wings and exposed blonde scalp above the helmet. The geometry-budget regression also correctly failed:195 cubes exceeded the existing180 limit. Pass2 removes20 superseded helmet/shin/foot plates, adds a fitted helmet crown and compacts the feather span/rest angles. Final32 bones/176 cubes; budget test passes without changing the limit. Actual final review completed.


Pass2 side review exposed the original sword pointing behind the palm. Pass3 mirrors only the sword geometry along local Z, preserves the closed grip and adds a solid silver front crown. Final32 bones/177 cubes, all13 original animation clips byte-identical. Final side and sampled impact views confirm the forward blade; walking/running, fly/hover and three additional flight phases show attached wing chains. Death remains coherent. No server behavior was changed.

Validation: baseline and three graphical client runs passed; final all33 resource sets baked/synchronized and one selected creature presented. All20 asset/preservation checks pass, including the unchanged180-cube budget. Gameplay/data/eggs,16 non-target creatures and five finished creatures remain unchanged.

[Final actual state sheet](previews/valkyrie-states.jpg) · [Released/final comparison](previews/valkyrie-comparison.jpg). Remaining differences: original helmet/feather construction, conservative hidden back and rigid segmented armor. Existing action/flight loops are retained, with sampled poses rather than exhaustive interpolation or numerical similarity claims.
