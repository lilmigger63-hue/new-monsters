# Existing-creature visual updates

All artwork is independently authored. The reference packs returned HTTP 403 in the parent task; no legally verified archive was available. Grimoire of Gaia artwork is not redistributed. Supplied screenshot descriptions guided species, colors and silhouette; these are original models/textures rather than copied pixels or meshes.

| Creature | Visual change | Cubes / bones |
| --- | --- | --- |
| Minotaur | Deep brown bovine fur, ivory curved horns, magenta waistcloth and a broad gray metal hammer with thick striking faces. Existing `axe` bone ID, shaft, rigid grip and support hand remain. Grounded cloven hooves retain their geometry. | 126 / 22 |
| Forest Dryad | Pale adult anime face and arms, pointed ears, full green scalp cap, long layered green hair, fitted leaf bodice and short layered leaf gown, tall light boots with grounded soles. Replaces the former wood-mask face. | 82 / 29 |
| Harpy | Brown feather palette, layered brown scalp hair/crest, pale face with a shallow pale nose, green-yellow bird shins and black talons. Modest feather outfit retained. Previously corrected natural arm-wings and folding preserved exactly. | 154 / 28 |
| Slime Maiden | Saturated green translucent jelly throughout, full green cap/hair and substantial overlapping side gel pigtails. Original continuous slime mound, subtle face and deformation retained; no flesh-colored torso. | 65 / 34 |

## Preservation and verification

Only the four species were exported through filtered calls to their existing original exporter. All four animation JSON files are **byte-identical** to the pre-task baseline: same clips, channels, keyframes, durations, combat timing and polished deaths (at most 0.65 seconds). All old bone names, parents and pivots remain. Minotaur has identical non-weapon geometry, including hooves and both gripping hands; Harpy wing and wingtip bones including their complete cubes remain byte-for-byte equivalent as JSON structures. No Java, registry, hitbox, AI, attributes, loot or spawning changes belong to this batch.

The three authoring modules compile. Export validation passed for runtime JSON, animation bone references, UV bounds, PNG atlas and matching editable Blockbench geometry/animation/embedded texture. Additional focused checks confirmed all animation keys remain within clip durations and slime alpha includes the established translucent value 202.

Fresh actual-game screenshot review, gameplay verification and the full build remain parent integration work. No claim is made here that those checks passed.

## Modified files

- `tools/generate_overhaul_group_a.py`
- `tools/generate_overhaul_group_b.py`
- `tools/generate_overhaul_group_d.py`
- `src/main/resources/assets/mythic_realms_creatures/geckolib/models/entity/forest_dryad.geo.json`
- `src/main/resources/assets/mythic_realms_creatures/geckolib/models/entity/harpy.geo.json`
- `src/main/resources/assets/mythic_realms_creatures/geckolib/models/entity/minotaur.geo.json`
- `src/main/resources/assets/mythic_realms_creatures/geckolib/models/entity/slime_maiden.geo.json`
- `src/main/resources/assets/mythic_realms_creatures/textures/entity/forest_dryad.png`
- `src/main/resources/assets/mythic_realms_creatures/textures/entity/forest_dryad_glowmask.png`
- `src/main/resources/assets/mythic_realms_creatures/textures/entity/harpy.png`
- `src/main/resources/assets/mythic_realms_creatures/textures/entity/harpy_glowmask.png`
- `src/main/resources/assets/mythic_realms_creatures/textures/entity/minotaur.png`
- `src/main/resources/assets/mythic_realms_creatures/textures/entity/slime_maiden.png`
- `src/main/resources/assets/mythic_realms_creatures/textures/entity/slime_maiden_glowmask.png`
- `tools/blockbench/forest_dryad.bbmodel`
- `tools/blockbench/harpy.bbmodel`
- `tools/blockbench/minotaur.bbmodel`
- `tools/blockbench/slime_maiden.bbmodel`
- `docs/monster-girl-expansion/EXISTING_VISUALS.md`

## Sixteen other original species: unchanged-byte proof

Before exporting, SHA-256 baselines covered 172 original species resource files. All 138 files belonging to the other 16 species were compared after export and remained byte-identical. This includes model/animation JSON, native projects, base textures, glow masks and applicable variants. For each row, the digest below hashes sorted `path + space + file SHA-256 + newline` entries; pre-export and post-export digests match.

| Species | Files | Matching manifest SHA-256 |
| --- | --- | --- |
| `ancient_treant` | 8 | `8a09e5933e3791cb3ed741f2b38040a26a42dc9f4b56493e9e12073c877dd1cd` |
| `cave_basilisk` | 8 | `645ea4e59d031031a4ee8058c65d785d4eb4a593a54672723f484b4f389842fd` |
| `crystal_spider` | 8 | `3cd00f398ffacab3529e0e2a83d0ba04bbbe8ef719488c2b383706e40923b5f9` |
| `demon_sorceress` | 8 | `1b96eea26204516c9c9200dd8623e3539a7c2304c6272e4d5ae7c3931c9dec88` |
| `dire_wolf` | 8 | `7d9701f0eaa924df88c781187f423e95e7b01e5ccc6aa6372b8ea5256c206c03` |
| `flame_imp` | 8 | `af7914eecca1007a09f5dbd702224a97991a2a934376fd6589d0cb91c9f0cb6a` |
| `frost_elemental` | 8 | `0dc3840033dfbc3e340d636efa05f10b0d0e3a533c5faad614bc93234b2b6cfc` |
| `goblin_scout` | 7 | `fb95f79df1b4c4cf5819dbaa3ef736a8f8b27cd04912f86aa452b974542c2e0e` |
| `goblin_shaman` | 8 | `aaa049b26d2785c8ec93600c9254ec1569f882b7c4761b7f1e46aea0f5a490ab` |
| `grave_knight` | 8 | `667cafebde8ecb6ae8cf42fe289509c2c6230c868acffde177942843644a70db` |
| `griffin` | 14 | `532353418fcd59992a0f6975a60e56c5c255d519ac08a671ec62feb231462806` |
| `moon_stag` | 10 | `7ebfcc0beb1793c9a28a788e0ab8268a17943a963d762d1780e073e3a8285f79` |
| `orc_warrior` | 7 | `7dc75cacd52826213f3d62392b69379f2673fd0143700e0b722e743cf0c29220` |
| `shadow_wraith` | 8 | `2243a8c922961d0aecc7ae2f446e3d1658b13ba3b48db617b06d2089bc5c00ce` |
| `stone_troll` | 8 | `624d3d79a7d046c06c8778125bbf88224eda33db8b6923d5c205642d62b9f03f` |
| `wild_wyvern` | 12 | `7f8744c8651b81838606563502c9cc7205b66315681f032fd43e717bc462abbb` |
