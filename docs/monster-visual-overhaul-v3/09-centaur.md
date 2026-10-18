# 09 — Centaur reference overhaul

V3 stage complete after 2 visual passes. Started after Ender Dragon Girl4ff1c9f. Reference: V3 inline dark-haired armored Centaur, brown horse barrel/four legs/tail and sword. Existing `CentaurEntity` Scout-profile melee,30-bone rig, eight clips, native project, UV and renderer inspected. No bow mechanic is added: existing gameplay, registry, collision box, eggs and spawn data are preserved.

| Priority | Aspect | Released → original V3 target |
| --- | --- | --- |
| 1 | Silhouette | Small human above thin horse plank → adult upper body over full horse barrel/croup |
| 1 | Proportions | Small head → broader pale face and full dark hair |
| 1 | Head | Narrow face → larger adult skull/jaw |
| 2 | Face | Small eye/mouth marks → enlarged existing facial planes |
| 2 | Eyes | Gold dots → muted olive irises and dark lashes |
| 1 | Hair | Narrow rear cap → full black-green scalp/long locks |
| 1 | Torso/limbs | Blue thin armor → gray layered shoulders and a defined human/horse junction |
| 1 | Hands/feet | Small hands/plain hooves → closed sword grip and distinct four hooves with front metal cuffs |
| 1 | Species | Long thin barrel → rounded horse belly/withers/croup; four original three-joint chains preserved |
| 1 | Outfit | Blue torso → gray/charcoal armor, dark red front panels and restrained leather details |
| 2 | Texture | Noisy brown/blue → warm horse coat, gray metal and dark hair |
| 1 | Weapon | Upright sword → forward/down sword with visible continuous handle and finger wrap |

Baseline client passed. Pass1:128 cubes/30 retained bones, all eight clips unchanged. Horse barrel/transition, head/hair proportions, shoulder plates/front cuffs and sword geometry/closed grip adapted. Actual corrective comparison completed. Hidden back/harness construction remains conservative original artwork.


Pass1 review found thin underlegs, flat fringe/tail and noisy horse shading. Pass2 widens underlegs, layers fringe/side hair/tail brush, paints broad warm coat planes and removes five superseded barrel cubes. Final30 bones/131 cubes; all eight clips remain byte-identical.

Validation: baseline and both graphical runs passed; all33 resource sets baked/synchronized, one selected species presented. Front/side/three-quarter/back/distant, four-leg walk/run pose, hoof/cuff alignment, tail connection, sword grip/impact and coherent grounded death inspected. All21 asset/preservation tests passed. Gameplay/data/eggs,16 non-target species and eight completed creatures unchanged.

Remaining differences: original horse/armor/hair construction, conservative rear/harness and game lighting. Existing melee behavior remains; reference bow metadata does not add gameplay. Stills do not certify every hoof interpolation or numerical similarity.

[Final actual state sheet](previews/centaur-states.jpg) · [Released/final comparison](previews/centaur-comparison.jpg).
