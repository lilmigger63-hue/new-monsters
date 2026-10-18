# V2 Group D implementation

Source: `tools/generate_overhaul_group_d.py`. Export with `python tools/generate_overhaul_group_d.py` (Python + Pillow). No Java, entity, gameplay, attachment offsets, shared exporter, or balancing changes.

| Species | Bones | Cubes | Clips | Visible changes |
|---|---:|---:|---:|---|
| Frost Elemental | 36 | 66 | 8 | Continuous faceted feminine ice torso, proportionate covered bust and waist, connected narrow casting arms, embedded sternum rune, nonhuman angular ice-mask slit, complete icehair scalp and nine long animated locks. |
| Moon Stag | 21 | 107 | 12 | Deep deer chest, strong sloped throat/neck, enormous low lateral palmate paddles with upward distal tines and embedded luminous crystals. |
| Slime Maiden | 34 | 60 | 8 | Cohesive modest jelly bust, narrowed waist, continuous full-scalp long slimehair, overlapping secondary gel deformation. |
| Harpy | 28 | 154 | 11 | Adult clothed bust/waist, integrated long scalp hair, preserved broad overlapping reference feather helper, folded wing-arms and delayed wrist/feather follow-through during flight and attacks. |
| Demon Sorceress | 42 | 111 | 10 | Tailored modest bust and corseted waist, full layered scalp hair with secondary motion, retained elegant horn chains and clothing, coordinated wrists and casting torso. |

All old bones and clip IDs remain; original attack landmarks and clip lengths remain. Exported death clips finish at 0.65 seconds using the existing exporter normalization. The Moon Stag saddle geometry, limb pivots, and 65-sample numeric hoof IK tracks are unchanged; added head/neck counter-motion stays above the locomotion rig. Its antler structure stays rigidly parented to the skull.

## Evidence and limits

The coordinator inspected the user's actual supplied Megaloceros image during this V2 task and relayed its anatomical features: broad low outward paddles with distal upward tines, deep deer chest and long neck. The updated stag follows that supplied visual evidence, retaining the lunar palette rather than the reference's brown coloration. Other original geometry uses the task's written visual descriptions and existing original material atlases. External reference sites were blocked and no Forge reference JAR was available. No third-party pixels or geometry were copied.

Exporter passed its native/UV/PNG checks for all five creatures. Focused Python validation additionally passed: old rig/clip IDs, original non-death clip lengths, death limit, finite and bounded keyframes, native cube/clip/embedded-texture parity, <=180-cube budget, full scalp long-lock animation channels, no extra Harpy arms, translucent slime alpha, glowmask alpha, tamed Stag texture existence, and exact unchanged Stag walk/run/ride hoof IK channel values. Validation script used: `/tmp/validate_group_d_v2.py` (session-local). `python -m py_compile tools/generate_overhaul_group_d.py` passed.

Generated paths per species: `src/main/resources/assets/mythic_realms_creatures/geckolib/models/entity/<id>.geo.json`, `geckolib/animations/entity/<id>.animation.json`, existing entity PNG/glowmask paths, and `tools/blockbench/<id>.bbmodel`. Original atlas material painting and supported slime alpha were reused; native projects embed exactly the runtime base texture. Tamed Stag textures remain supported.

The coordinator owns Gradle/build and actual-game screenshot review; these checks do not establish in-game clipping or appearance verification by themselves.
