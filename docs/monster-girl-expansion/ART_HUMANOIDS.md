# Five original humanoid expansion artworks

Generator: `tools/generate_expansion_humanoids.py`.

All geometry, pixel motifs, palettes, equipment, eggs and animation poses were independently authored for this project. No proprietary Grimoire asset, implementation, reference pixel or third-party pack was incorporated. The existing project exporter/material-paint foundation is reused under the authorized original-project workflow. The unavailable external packs remain unused; their licenses are not inferred.

| Species | Bones | Cubes | Clips | Authored identity |
|---|---:|---:|---:|---|
| Vampire | 28 | 139 | 9 | Adult gothic silhouette, fitted dark-red coat with black lapels and split animated tails, ivory ruff, red eyes, fangs, bat-themed embroidery, ruby clasp, layered full-cap dark hair, short dagger. |
| Dhampir | 29 | 144 | 9 | Broad shaped black hat, red crest and articulated feather, black long coat, shoulder scarf, red patterned trousers with crossing leather braids, long guarded poleblade. |
| Cyclops | 30 | 138 | 9 | Exactly one large central eye, gold helmet arch leaving the eye unobstructed, plume, blue/gold cuirass and articulated tassets, massive cross-body poleaxe gripped by both palms. |
| Anubis | 29 | 147 | 9 | Tall black jackal ears with warm inset planes, warm non-European skin palette, full black/gold hair lappets, broad gold/turquoise collar, scarab jewel, light linen panels, segmented curved khopesh. |
| Kobold | 31 | 152 | 9 | Small adult reptilian anatomy, scale-painted muzzle/nostrils and cheeks, pointed reptile ears, digit claws, short two-segment scaled tail, layered gray/lavender brigandine, articulated hip plates, small sword. |

## Files

For exactly `vampire`, `dhampir`, `cyclops`, `anubis`, `kobold`:

- `src/main/resources/assets/mythic_realms_creatures/geckolib/models/entity/<id>.geo.json`
- `src/main/resources/assets/mythic_realms_creatures/geckolib/animations/entity/<id>.animation.json`
- `src/main/resources/assets/mythic_realms_creatures/textures/entity/<id>.png`
- `src/main/resources/assets/mythic_realms_creatures/textures/entity/<id>_glowmask.png`
- `src/main/resources/assets/mythic_realms_creatures/textures/item/<id>_spawn_egg.png`
- `tools/blockbench/<id>.bbmodel`

Each editable native project embeds the exact distributed 128x128 original atlas and animations. Atlas painting includes intentional fabric brocade, directional skin planes, chased metal, hair filaments and scales, plus distinct vampire bat, hunter thorn-cross, cyclopean meander, jackal lotus and kobold diamond motifs. Five 32x32 transparent fantasy relic eggs have distinct outline profiles and actual species icon artwork, not vanilla speckle recolors.

Each model has a fully covered faceted scalp cap, overlapping fringe, temple locks, long back locks and secondary hair sections. Clothed chest and hip geometry is proportionate and integrated with clothing/armor. There are no exposed body details or copied outfits.

## Animation and attachment

Every species exports `idle`, `walk`, `run`, `attack`, `heavy`, `cast`, `hurt`, `guard`, `death`.

Walk/run use opposing hip/shoulder phases, articulated knees/feet, delayed elbows/wrists, counter-rotating chest/head and delayed cloth/hair/tail movement. Attacks include preparation, an exact server-impact landmark, torso follow-through, wrist/elbow action and recovery. Vampire emphasizes a quick forward dagger strike; Anubis uses a khopesh sweep; the Cyclops uses a heavy torso/chest-driven two-hand sweep. Casting presents the free arm/hand. Impact landmarks are Vampire 7, Dhampir 9, Cyclops 18, Anubis 10 and Kobold 7 ticks.

Weapons are rigid descendants of `hand_right -> grip_right -> weapon`. Each socket contains three bent finger pairs and an opposing thumb (seven cubes), with the actual handle crossing the enclosed palm. No animation rotates a weapon or grip independently. Cyclops also has `hand_left -> grip_left`; the continuous horizontal haft passes through both palms. Cyclops arm/wrist animation overrides are deliberately omitted so every clip maintains its two-hand constraint; motion comes through the shared chest/body, bracing legs and secondary clothing/hair. This is an authored rigid two-hand rig, not runtime IK.

All five death clips finish at 0.65 seconds. They rotate around all three axes and lift the complete silhouette according to its rotated support envelope. The calculation includes every cube corner, cube-local rotations, rest bone hierarchy, hats, ears, weapons and tail. Lift is densely sampled at 129 keys; independent quarter/mid/three-quarter samples between keys verify the interpolated floor envelope.

Authored models are fitted to their explicit species heights (1.85, 1.85, 2.05, 1.95, 1.3 blocks respectively) using the complete 3D rest silhouette. All rest soles are exactly y=0; weapons clear the ground. New gameplay dimensions and registration remain root integration responsibilities.

## Verification

Passed:

- `python tools/generate_expansion_humanoids.py`: all five geometry/UV/PNG/native exports, bone references, rigid grip checks, exact impact landmarks and 3D floor checks.
- Rest minimum y is 0 for all five.
- Every dense interpolated death floor sample clears the ground by at least 0.0999 model pixels.
- Existing `test_all_editable_projects_match_distributed_png_geometry_and_clips`, scoped to these five new IDs: 1 test passed, five native-project parity subtests.
- Five egg PNGs are 32x32 RGBA with transparent borders, visible artwork and five distinct SHA-256 hashes.
- Original local offline geometry contact sheet was rendered and visually inspected for distinct silhouettes, central Cyclops eye, two-hand haft placement, hats/ears, reptile muzzle, clothing/armor separation and overall proportions. This preview used solid material colors; it is not an in-game texture/animation validation.

No Java, shared pipeline, existing generator, existing creature, registration, gameplay, test or global documentation file was changed by this art subtask. No Gradle, game client or git operation was run. Root integration owns actual Minecraft rendering, texture/animation screenshot review, egg registration, behavior and build verification. Walking foot contact is authored approximation rather than a runtime IK system; no FPS benchmark is claimed.
