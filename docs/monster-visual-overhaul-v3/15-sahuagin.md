# 15 — Sahuagin reference overhaul

V3 stage complete after 3 visual passes. Started after Dhampir1b48c87. Primary reference: V3 pale adult aquatic figure with dark teal hair, golden eyes, blue fins/gauntlets/webbed feet and blue/white top. The card's hand object is unclear; existing trident is retained instead of inventing a replacement. `SahuaginEntity` amphibious navigation, real vertical swimming, water breathing and existing Scout combat remain unchanged.25-bone rig/ten clips/native/UV/renderer inspected; IDs/hitbox/spawns/eggs preserved.

| Priority | Aspect | Released → original V3 target |
| --- | --- | --- |
| 1 | Silhouette | Teal armored humanoid → pale torso, dark teal hair and blue finned limbs |
| 1 | Proportions | Small head/thin arms → broader adult head and substantial fin gauntlets |
| 1 | Head | Narrow teal face → broad pale framed head |
| 2 | Face | Green skin → pale jaw/nose/mouth planes |
| 2 | Eyes | Gold → retained muted golden irises |
| 1 | Hair | Blue narrow locks → expanded dark teal scalp/hair |
| 1 | Torso/limbs | Covered teal torso/thighs → pale waist/thighs with blue top/straps |
| 1 | Hands/feet | Small fins/white claws → blue gloves, broad webbed toes and dark blue claws |
| 1 | Species | Turquoise spikes → blue head/forearm fins, jointed fish tail and retained swim rig |
| 1 | Outfit | Teal full armor → blue/white top, dark teal hip wrap and blue leg bands |
| 2 | Texture | Turquoise → dark teal/blue/pale skin with subdued metal |
| 1 | Weapon | Unclear reference object → retain original trident and grip |

Baseline graphical run passed. Pass1:118 cubes/25 bones, all ten clips unchanged. Head/hair/fins resized, body/chest/limb material boundaries rebuilt, gauntlets/leg bands and webbed foot coloration adapted. Actual land/water corrective comparison pending. Hidden tail/back retains conservative original construction.


Pass1 review found an occluded trident, weak tail-joint overlap and small leg fins. Pass2 presents the trident forward/down, rebuilds overlapping tail beams around their shared joint, adds lower-leg fin plates and layers the fringe. Pass3 changes only the test camera: underwater side views from inside the tank with test-only night vision show the whole horizontal swim pose without foreground glass bars. The upright idle close view crops part of the head; head/fin alignment was separately inspected in land views. Final25 bones/125 cubes; all ten clips remain byte-identical.

Validation: baseline and three graphical runs passed; all33 resource sets baked/synchronized and one selected species presented. Land front/side/three-quarter/back/distant, trident grip at sampled impact, tail/fin/webbed foot alignment, walk/run/death and actually submerged idle/swim playback inspected. All22 asset/preservation checks pass. Gameplay/data/eggs,16 non-target species and fourteen completed creatures unchanged. Amphibious AI is unchanged; these NoAI presentation probes are not a claim of new AI validation.

Remaining differences: original fin/tail/armor construction, conservative hidden details, existing trident retained because the card's hand object is unclear, and water lighting. Stills do not certify every swimming interpolation or numerical similarity.

[Final actual state sheet](previews/sahuagin-states.jpg) · [Released/final comparison](previews/sahuagin-comparison.jpg).
