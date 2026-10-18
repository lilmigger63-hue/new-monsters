# 03 — Slime Maiden reference overhaul

V3 stage complete after three visual passes. Reference: inline V3 green Slime Girl image, no supplied local filename. Dryad was completed and committed as23fb1e2 before this stage began.

Technical mapping: `SlimeMaidenEntity`, registry `slime_maiden`, existing translucent `CreatureRenderer`, runtime `slime_maiden` geometry/PNG/glow/animation and matching native project. Existing neutral guardian targeting, slowing slime bubble,35-tick server hop, attributes/hitbox/spawning remain unchanged. No weapon is depicted or added.

| Priority | Aspect | Released art → intended original V3 art |
| --- | --- | --- |
| 1 | Silhouette | Pear/blob bottom → clearly humanoid green gel figure with separate legs |
| 1 | Proportions | Small head above mound → adult shaped torso/waist/hips and larger gel-framed head |
| 2 | Head | Narrow little face → broader gel cheeks/jaw |
| 2 | Face | Bright staring face → tiny dark eyes, subtle mouth and restrained reference-inspired cheek tint |
| 2 | Eyes | Large glowing eyes → dark gel eyes with small green catchlights |
| 1 | Hair | Uneven clumps → two broad hollow-topped gel pigtail loops with tapering side masses |
| 1 | Torso/limbs | Stacked pudding lobes → coherent adult torso, long gel arms and articulated legs |
| 1 | Hands/feet | Mittens/blob base → soft finger tips and two broad gel pads |
| 1 | Species anatomy | Floating decorative cubes → continuous gel body/pigtails; remove unused external bubble rig |
| 2 | Outfit | Gel body already uniform → unified green bodice/hip form without human flesh-colored torso |
| 1 | Texture | Dark saturated green → original lighter green jelly palette with translucent shading |
| — | Weapon | None; existing ranged slime-bubble mechanics retained |

Pass1:33 bones,80 cubes,eight clips. Seven unused bubble bones and their idle tracks removed; six leg/knee/ankle bones added. Original attack/heavy/cast/hurt content remains byte-identical. Idle, walk/run and death are explicitly permitted cosmetic adaptations; clip durations/loops are preserved. New sampled leg tracks create a soft humanoid gait while original torso gel squash remains. Cosmetic death height is adapted to the new geometry. Existing exporter/native/UV checks passed; actual client comparison subsequently completed.

Hidden rear gel construction and feet below the cropped reference are conservative original interpretations. No numerical similarity score or exhaustive motion certification is claimed.


Pass1 actual views exposed narrow upright pigtail tops, arms visually merging with the torso and excessive glass-like seams. Pass2 broadened the caps/lobes, separated the arms and used broad gel shading at alpha228. Pass3 curled the outer pigtail lobes outward. The focused test scene now hides other fixtures during reference views; their emissive layers can still appear as distant ghosts, but the selected creature is clear. The final three-quarter/distant views and state sheet were inspected. No weapon, wings or tail applies to this creature.

Validation: three successful actual graphical client runs; final client/build passed with all33 resource sets baked/synchronized and one selected species presented. All20 asset/preservation tests passed. The temporary expired global Minecraft metadata lookup was resolved using retained, checksum-verified original1.21.10 metadata and Loom's supported custom metadata override; final run was offline. This was an environment failure, not a creature test failure. Original attack/heavy/cast/hurt clips, gameplay Java, data, eggs and16 non-target species remain unchanged.

[Final actual state sheet](previews/slime_maiden-states.jpg) · [Pass1/final comparison](previews/slime_maiden-comparison.jpg). Remaining differences: original gel construction, conservatively inferred cropped feet/back, and reference-card versus game lighting. No numerical similarity or exhaustive animation certification is claimed.
