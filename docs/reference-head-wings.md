# Initial user-reference checkpoint — superseded by V2

Historical two-creature increment before the full V2 prompt. Current implementation, counts and test results: [overhaul V2](overhaul-v2.md).

## Baseline and reference scope

The user supplied `mythic-realms-creatures-1.1.0-rc.2.jar`, SHA-256 `c2eeb862ca006f13e4fc3a0594cba847c468e1e880220194f50e596e2fc33c27`. Its resource assets match the working source except the later Scout geometry; that completed grip proof is retained. No binary decompilation or dependency/version migration was needed.

Reference 1 (user-provided screenshot): broad, blunt reptilian skull, pale squared muzzle, separate tooth-lined jaw, side-set eyes and low dorsal crest. Used only for Wild Wyvern head design. Reference 2: broad flat wing with overlapping stepped flight feathers and coverts. The user explicitly confirmed this image guides the Harpy's wings only. Her adult female face, body, costume and talons remain unchanged.

Both reference images were visually inspected in the conversation. New geometry and UV assignments are original; no third-party pixels, models or animations were extracted or shipped. The previously blocked wiki is not a prerequisite for these supplied references.

## Implemented

- Wild Wyvern: rebuilt head/jaw geometry, faceted cranium and muzzle, short crest replacing tall horns, nostrils, side eyes, upper and lower teeth. 17 bones, 129 cubes, 16 existing clips retained.
- Harpy: broad overlapping secondary feathers, two depth-separated covert layers, stepped primary tips and a restrained light/dark feather pattern from existing atlas materials. Wing-arms retained without extra humanoid arms. 19 bones, 115 cubes, 11 existing clips retained.
- Exported matching native Blockbench files. All existing head/jaw/wing bone names, parents, pivots and rest rotations preserved. Existing mount seat, hitboxes, attack timing, skins and glow masks retained. No Java gameplay or renderer changes. All 54 compiled runtime class files are byte-identical to the supplied JAR.
- Client smoke now also renders fly/hover playback probes for these two creatures. Probes demonstrate animation rendering, not natural AI transition behavior.

## Modified authoring/runtime files

- `tools/generate_overhaul_group_b.py` and `tools/generate_overhaul_group_d.py`
- `tools/blockbench/{wild_wyvern,harpy}.bbmodel`
- `src/main/resources/assets/mythic_realms_creatures/geckolib/models/entity/{wild_wyvern,harpy}.geo.json`
- `src/clientGametest/java/com/mythicrealms/creatures/clienttest/CreatureClientSmokeTest.java`
- Version in `gradle.properties`: 1.1.0-rc.3. Minecraft 1.21.10 / Fabric / Java 21 / GeckoLib 5.3-alpha-3 unchanged.

Texture and animation JSON bytes did not need alteration: revised geometry uses existing painted UV materials and existing articulated motion.

## Validation

- `python3 scripts/test-assets.py`: 2 passed.
- `python3 scripts/test-overhaul-assets.py`: 5 passed.
- `python3 scripts/cloud-gradle.py --no-configuration-cache build runGametest`: passed; 40 required server game tests. Five JUnit checks passed in this build.
- Export comparison against previous source: only Wyvern `head`/`jaw` cubes and Harpy four wing bones changed. All other model bones and all bone transforms unchanged.
- Repeat both exporters: all 347 resource/native files byte-identical.
- Full fresh base-client smoke: passed, 20 entity presentations and 226 screenshots including fly/hover probes for both changed creatures; authoritative death/removal and Griffin mount input/flight also passed.
- A focused rerun is checking wider Wyvern framing and four flight phases for both targets.
- Evidence directory: `/workspace/validation/reference-head-wings/`.

## Remaining limits

This completes only the two supplied-reference geometry changes. Full 18-creature artistic acceptance, exhaustive gait/transition review and hardware performance certification are not claimed. Optional Better Combat has not yet been rerun for this candidate.
