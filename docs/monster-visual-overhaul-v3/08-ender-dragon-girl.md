# 08 — Ender Dragon Girl reference overhaul

V3 stage complete after two visual passes. Started after Succubusfbeff26. Primary reference: supplied Ender Dragon Girl with black hair/wings/outfit, gray horns and purple eyes. `EnderDragonGirlEntity` inherits Demon-profile spells/behavior;35-bone rig,13 clips, native project/renderer/UV inspected. Registry, combat/spell timing, eggs, spawning, hitbox and existing entities preserved. Clawed hands are unarmed.

| Priority | Aspect | Released → original V3 target |
| --- | --- | --- |
| 1 | Silhouette | Tall white forward horns/large broken wings → paired gray horns and compact black membrane wings |
| 1 | Proportions | Small head/thin limbs → broad adult face and fuller clawed extremities |
| 1 | Head | Narrow dark mask → broader pale face framed in black |
| 2 | Face | Gray-purple planes → restrained pale jaw/nose/mouth |
| 2 | Eyes | Purple stare → retained violet irises beneath black lashes |
| 1 | Hair | Thin long strips → fuller widened black scalp and locks |
| 1 | Torso/limbs | Full covered purple-black gown → pale waist/chest opening and black straps |
| 1 | Hands/feet | Thin pale claws/small toes → connected black claws and broad black foot pads |
| 1 | Species | Ivory prongs → substantial swept gray horns, continuous black wing bays and jointed tail |
| 1 | Outfit | Purple trim/long robe → charcoal split lower garment and black limb covering |
| 2 | Texture | Purple decorative → dark charcoal scales/membrane with gray horn facets |
| — | Weapon | None; existing claws/magic preserved |

Baseline client passed. Pass1:128 cubes/35 retained bones. Head/hair/horns structurally rebuilt/resized, waist and clawed hands/feet rebuilt, black membranes assembled as overlapping continuous bays. Death-only cosmetic fold/support adapted using the proven grounded-wing approach;12 other original clips unchanged. Corrective comparison completed. Hidden rear/tail details use conservative original construction.


Pass1 review found overlong hair, an inherited purple chest jewel and overly bright membrane edges. Pass2 shortens the black locks, removes the jewel, adds dark chest framing and paints low-contrast membrane/hair planes. Final35 bones/131 cubes. Twelve clips remain byte-identical; death-only wing folding/support is explicitly adapted without changing its duration/root rotation.

Validation: baseline and two graphical runs passed; final all33 resource sets baked/synchronized, one selected species presented. Front/side/three-quarter/back/distant, tail/horn/claw alignment, walking/running/actions/impact, flight/hover/phases and grounded corpse inspected. All21 asset/preservation checks pass. Gameplay/data/eggs,16 non-target species and seven completed creatures unchanged.

[Final actual state sheet](previews/ender_dragon_girl-states.jpg) · [Released/final comparison](previews/ender_dragon_girl-comparison.jpg). Remaining differences: original horn/membrane/garment construction and conservative hidden rear details. Rigid voxel wing bays retain their existing jointed flight loops; still samples do not establish exhaustive interpolation or numerical similarity.
