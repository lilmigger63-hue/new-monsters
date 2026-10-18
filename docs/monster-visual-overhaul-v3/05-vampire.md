# 05 — Vampire reference overhaul

V3 stage complete after two visual passes. Started after Minotaur9391176. Inline blonde Vampire V3 card is the primary visual reference; no local reference filename. `entity/expansion/VampireEntity`, existing common renderer,28-bone rig, PNG, UV, nine clips and native project inspected. Existing inherited Scout-profile melee/cooperation, registry `vampire`, attributes, spawning, eggs, collision dimensions and action timing are preserved. Existing dagger is retained even though the card does not clearly show a weapon.

| Priority | Aspect | Released → original V3 target |
| --- | --- | --- |
| 1 | Silhouette | Thin short jacket → long flared black/crimson layered coat |
| 1 | Proportions | Small head/long exposed legs → broad adult head and full lower garment |
| 1 | Head | Narrow dark-haired face → broad pale blonde-framed head |
| 2 | Face | Small angular mask → adult jaw/nose/mouth planes |
| 2 | Eyes | Large staring marks → red eyes beneath dark lashes |
| 1 | Hair | Black hair → blonde stepped scalp, fringe and rear locks with red bow |
| 2 | Torso/limbs | Straight small waistcoat → shaped red waistcoat and substantial black sleeves |
| 1 | Hands/feet | Bare palms/tall exposed boots → crimson gauntlets and restrained dark shoes |
| 2 | Species/accessories | Small ruff → high dark collar and pale pleated ruff |
| 1 | Outfit | Short red coat → layered black tails, red hems and gold fastenings |
| 1 | Texture | Blue-black/purple → charcoal, burgundy, blonde, pale skin and red accents |
| 2 | Weapon | Existing short dagger → retained closed grip and aligned blade |

Baseline actual graphical client passed. Pass1: rebuilt116 cubes in28 retained bones, nine original animation clips unchanged. Full layered coat, high collar, ruff, red bow, blonde locks, gloved hands and original dagger. Actual comparison/correction completed. Hidden rear garment construction is conservative original artwork.


Pass1 review found flat hair, a small bow and a narrow straight cape. Pass2 introduced swept overlapping blonde locks with broad painted clusters, a larger asymmetric red bow, shoulder edges and flared black/crimson mantle panels. Final28 bones/138 cubes; all nine clips remain byte-identical. Only red irises use the glow tile; clothing/bow remain normally lit.

Validation: baseline and two actual graphical runs passed, all33 resource sets baked/synchronized and one species presented. Front/side/three-quarter/back/distant and locomotion/action/impact/death views inspected. Dagger grip remains connected in sampled actions, coat and hair stay attached and corpse remains above floor. All20 asset/preservation tests passed; gameplay/data/eggs,16 non-target species and four completed creatures unchanged.

[Final actual state sheet](previews/vampire-states.jpg) · [Released/final comparison](previews/vampire-comparison.jpg). Remaining differences: original hidden back/hem interpretation and existing dagger retained despite cropped reference; still samples do not prove every interpolation or any numerical similarity percentage. The skirt uses jointed rigid voxel panels rather than cloth simulation.
