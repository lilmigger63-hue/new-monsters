# V5.3 visual overhaul · 1.4.0-rc.1

All thirteen expansion creatures received original reference-inspired geometry, texture and cosmetic animation refinements, one creature at a time, each with a separate reviewed commit. The twenty original creatures, all gameplay and sound resources, and the production renderer are preserved from1.3.0-rc.1 (`1704f67`). This is the task iteration V5.3; the mod release version is1.4.0-rc.1.

[Inventory and exact registry mappings](../monster-girl-v5-3-inventory.md) · [Sequential progress and commits](../monster-girl-v5-3-progress.md) · [Provenance](PROVENANCE.md) · [Original request](REQUEST.md).

[View all thirteen final Minecraft models](previews/all-thirteen.jpg).

## Individual visual evidence

Each report links actual Minecraft baseline/final images and sampled animation states. Initial1.3.0 art is authenticated by cached asset hashes; most baseline screenshots reuse the actual previous all 33 client run. Final corrective runs present exactly one species while baking and synchronizing all 33 resource sets. No synthetic render is presented as Minecraft evidence.

| Creature / ID | Bones / cubes | Corrective client runs | Report |
| --- | ---: | ---: | --- |
| `ender_dragon_girl` | 35 / 120 | 3 | [Changes, evidence and remaining differences](ender_dragon_girl.md) |
| `vampire` | 30 / 131 | 3 | [Changes, evidence and remaining differences](vampire.md) |
| `holstaurus` | 22 / 112 | 2 | [Changes, evidence and remaining differences](holstaurus.md) |
| `centaur` | 30 / 135 | 3 | [Changes, evidence and remaining differences](centaur.md) |
| `sahuagin` | 25 / 122 | 2 | [Changes, evidence and remaining differences](sahuagin.md) |
| `valkyrie` | 32 / 167 | 2 | [Changes, evidence and remaining differences](valkyrie.md) |
| `fox_spirit_girl` | 46 / 167 | 3 | [Changes, evidence and remaining differences](fox_spirit_girl.md) |
| `anubis` | 29 / 164 | 2 | [Changes, evidence and remaining differences](anubis.md) |
| `kobold` | 31 / 177 | 2 | [Changes, evidence and remaining differences](kobold.md) |
| `cyclops` | 30 / 156 | 1 | [Changes, evidence and remaining differences](cyclops.md) |
| `dhampir` | 29 / 170 | 1 | [Changes, evidence and remaining differences](dhampir.md) |
| `succubus` | 37 / 134 | 1 | [Changes, evidence and remaining differences](succubus.md) |
| `werecat` | 24 / 134 | 1 | [Changes, evidence and remaining differences](werecat.md) |

## Preservation and rendering cost

The 489-file protected initial manifest authenticates production code, renderer, gameplay/data/audio, original artwork and test sources. One explicitly hashed client-test exception adds Centaur phase views and an underwater Sahuagin FOV restored after use; this test mod is excluded from the production JAR. Completed art hashes are frozen, pending stages were required to match their starting hashes, and only the active species could differ.

All existing animation clip names, lengths and loops are preserved. Attack, heavy, cast, hurt, teleport, guard and hop clips remain identical. Secondary hair, tail, cloth, wing and swimming movement changes are cosmetic. Root death support is recalculated where geometry changes. IDs, hitboxes, AI, attributes, physics, cooldowns, equipment, saved data, loot, eggs, recipes, taming/riding, structures and spawning are unchanged. Only Forest Dryad and Slime Maiden from the original twenty spawn naturally; the expansion habitats remain unchanged.

Every creature stays within the existing180-cube budget with128×128 material atlases; native Blockbench projects retain editable geometry/UVs/animations. Species-specific details are kept. Three existing unused emissive-pass optimizations remain intact, including non-emissive Kobold. There are no production Java or renderer changes, no dependency upgrades and no new runtime systems. These are verified resource budgets and preservation checks, not a measured hardware FPS improvement.

## Validation

Milestone builds after stages4 and8 passed, each with 51 dedicated-server GameTests and zero failures/skips. Logs, authentic XML results and hash summaries are in [test-results](test-results).

All 35 asset/source/preservation checks passed after stage13. The14 combat timeline checks also passed. These cover all 33 resource sets, native projects/UVs/animation rig compatibility, original IDs/attributes/spawn rules, render budgets, authentic baselines, completed-art immutability, exact combat clips/timing, generated source reconstruction and supported corpse positions. Historical V3 source/freeze tests deliberately validate archived V3 assets for the thirteen superseded artworks; V5.3 checks the live replacements. Legacy Fox and Succubus corpse-body contact regressions continue checking live art.

Final Fabric1.21.10 release build passed; five JUnit test cases passed. Dedicated-server GameTests passed 51/51 without Better Combat and 51/51 with Better Combat, zero failures/errors/skips. All 76 production `.class` files in the release JAR are byte-identical to1.3.0-rc.1. The392 protected packaged resources match both1.3.0-rc.1 and current source bytes, and all thirteen packaged art sets match the reviewed live files. A separate filesystem audit rejects added production source/resources outside the original manifest and thirteen art paths. [Binary/scope audit](test-results/final-preservation.json).

The independent read-only review found no critical or important blockers; [scope and limits](test-results/review.md).

The final graphical client with Better Combat passed all 33 baked/synchronized resource sets and presented all 33 species, including reference angles, sampled combat/motion/corpse states and species-specific flight/swimming views. Actual run:5m7s. [Client result](test-results/final-client.json) · [Actual log](test-results/final-client.log). Across the sequential process,26  focused corrective runs were reviewed before this final combined run.

## Limits and deliberate differences

The references guide original project art. Gaia artwork is not imported or redistributed; its metadata and license were inspected, and no Gaia code is needed. Rear surfaces, texture clusters, garment seams and some silhouettes remain original interpretations; see each species report. Cyclops keeps the existing agreed two-handed polearm, Sahuagin keeps its trident, and Valkyrie keeps its established shield. The request alias “Ashen Wing Girl” maps to `werecat`, which remains wingless following the user's explicit image-based choice.

The actual development client runs through Xvfb/llvmpipe software rendering. Sampled stills and animation phases do not certify every interpolated frame, terrain foot sliding or physical GPU performance. No percentage likeness or benchmark FPS is claimed. Audio is preserved by hashes rather than an audio-hardware playback test. The cloud client reports no OpenAL sound device, unavailable optional online account/key lookups and software-rendering tick lag; local graphical/animation tests continue independently of those services. These warnings are retained in the actual logs and are not claimed as successful audio or performance tests. The retained cloud instance and saved setup workflow were reused; a newly published cloud snapshot was not tested.

## Rebuilding and authoring

Use Minecraft1.21.10 exactly, Java21, Fabric Loader0.19.5+, Fabric API0.138.4+1.21.10 and GeckoLib5.3-alpha-3. Optional Better Combat3.0.0 integration uses the unchanged existing presets and dependencies documented in the root README.

`tools/generate_v5_3.py <registry-id>` reconstructs only one explicitly active species. Completed stages are intentionally frozen; the source-reconstruction test evaluates all thirteen builders read-only. Do not re-enable a completed stage just to regenerate unrelated art. Baseline snapshots are project-owned input data and source archives include them.

Cloud validation uses `scripts/cloud-gradle.py --offline --no-configuration-cache --init-script /workspace/toolchains/retained-minecraft-metadata.gradle build runGametest`. The init supplies the checksum-verified immutable official1.21.10 metadata through Loom's supported override; it does not bypass TLS or checksums. Outside the retained cloud, normal Gradle setup may download the pinned official dependencies. Client validation uses `scripts/client-smoke.sh` with the same offline init; add `-PwithBetterCombat` for optional integration and `-PclientSmokeGroundedReference` for the reference poses.
