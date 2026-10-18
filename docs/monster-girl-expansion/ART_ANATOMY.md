# Expansion anatomy artwork

Four original creature sets authored in `tools/generate_expansion_anatomy.py`. Rebuild with `python tools/generate_expansion_anatomy.py` from the repository root (Python, Pillow and installed NumPy for export-time corner transforms). Uses existing Model/clip/write_creature and native Blockbench serializer; no Java or shared pipeline edits.

| ID | Bones | Cubes | Clips | Size | Impact |
|---|---:|---:|---:|---|---|
| centaur | 30 | 100 | 8 | 1.25 × 2.15 | 10 ticks |
| holstaurus | 21 | 99 | 9 | .8 × 1.9 | 14 ticks |
| sahuagin | 25 | 107 | 10 | .7 × 1.85 | 10 ticks |
| werecat | 24 | 98 | 8 | .7 × 1.8 | 16 ticks |

Centaur: adult armored human upper torso, long dark scalp-covered hair, layered shoulders/bracers; connected brown horse withers, barrel, rounded hindquarters, four independently articulated upper/lower/hoof chains, fetlocks and long segmented tail. Sword handle intersects curled right palm, all sword components rigidly parented through hand/forearm/arm/chest. Horse diagonal gait uses independently phased limb rotation, swing lift, lower-joint bend and counter-rotating hoof orientation. No humanoid legs beneath the horse body.

Holstaurus: biped cow woman with two segmented horns, broad bovine ears, full lavender-gray hair, modest blue/slate clothing, cow-pattern sleeve/cuff/bodice panels, gold belt bell and tufted tail. Friendly arm/body motion and dedicated `hop` clip; no minotaur snout or quadruped anatomy.

Sahuagin: pale teal aquatic adult, full deep-blue hair, three-part head fins, forearm fin fans, segmented fin tail, ocean armor and trident gripped through right palm. Webbed feet and toe rays retain biped surface gait. Dedicated `swim` and `idle_swim` clips change torso orientation, alternate kicks, sweep arms, and move fins/hair/tail with lag.

Werecat: silver-gray full hair/scalp, two pointed furry ears with contrasting inner surfaces, red eyes, navy/slate armor and gauntlets, hand claws, segmented silver tail. Biped gait and Shaman-style two-handed casting gestures with wrist/elbow anticipation and recovery. **No wings**; ID is `werecat` following confirmed reference identification.

Artwork is original. Shared painted material base has hand-added armor chevrons, seams, rivets, embossed panels, individual cow patches, ocean-wave fin bands, equine coat strokes and feline shield motif. Every species has its own 128×128 RGBA palette and texture, embedded identically into its editable native project. Each also has an independently drawn 32×32 fantasy egg: horseshoe, horn/bell, fish-fin, or cat-mask symbol. No external asset pixels/models or Grimoire of Gaia files shipped. Referenced asset pack URLs were unavailable; no unverified licensed assets incorporated.

Outputs for each ID: `src/main/resources/assets/mythic_realms_creatures/geckolib/models/entity/<id>.geo.json`, `geckolib/animations/entity/<id>.animation.json`, `textures/entity/<id>.png`, `textures/item/<id>_spawn_egg.png`, and `tools/blockbench/<id>.bbmodel`.

Validation executed: built-in positive geometry/UV/atlas/frame/bone/native-element and animation-count checks; runtime/native atlas decoded pixel parity; 32×32 egg dimensions; correct four-legged Centaur and wingless Werecat hierarchy; authoritative impact frames and clip durations. Rest-pose geometry corners, including every bone/cube rotation, meet the floor. Death clips finish at .65 seconds and contain 27 sampled collapse rotations/positions with geometry-derived minimum floor lift; all sampled transformed corners are on or above ground. No root bounce is used in ground locomotion.

Not yet checked in this batch: runtime animation blending, exact foot contact throughout all gait phases, actual swimming AI, item/entity registration, spawn eggs summoning, client appearance or Gradle. Parent handles integration/build and actual client screenshot review. No claim of full runtime visual verification is made.

## Werecat tail continuity correction

Initial client side review prompted a numerical joint audit. The original proximal tail cube rotated around its center, leaving the distal tip pivot beyond its actual endpoint. Corrected proximal cube rotation pivot to the attached top; placed the distal bone at its exact transformed endpoint and rotated the distal cube around that joint with volume overlap. Mathematical inverse-transform checks confirm the shared joint lies inside both cube volumes, so distal animation rotations retain attachment. Werecat-only exports regenerated; native/UV/atlas and rest/death-floor checks passed. Counts remain 24 bones, 92 cubes, 8 clips. Fresh client review remains pending.

### Runtime convention follow-up

Fresh actual client screenshot `0200_creature-werecat-side.png` still showed a detached tip: the prior offline cube-angle transform did not reproduce GeckoLib's cube convention. Replaced the manual transformed endpoint with an authored parent/child joint inside both **unrotated** cube volumes, moving the two bend angles to the corresponding tail bones. This removes the cube-angle/sign dependency entirely and keeps shared-joint overlap under animation. Werecat-only native/runtime exports and floor checks passed again; a fresh client review is required before claiming visual closure.

## Werecat feline ear refinement

Reviewed actual `client-verified/screenshots/0200_creature-werecat-idle.png`: old tall parallel ear blocks read as rabbit posts. Rebuilt Werecat-only ears as low, broad, four-stage tapering feline triangles with slightly outward shifted tips: widths 2.2 / 1.6 / .95 / .3 model units and total height 2.4 units. Contrasting inner ear also narrows toward the tip. Full hair, connected bone-articulated tail and animation channels remain intact. Export validation and explicit taper/height/tail checks passed; count now 24 bones, 98 cubes, 8 clips. Parent will perform final actual client review.
