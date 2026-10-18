# Group A refinement

Original geometry and texture work only. The source audit reported proxy HTTP 403 for all six requested sources; no downloaded geometry, animation, texture, or third-party license is incorporated. Existing repository attribution remains applicable.

Inspected the five actual baseline idle screenshots in `/workspace/validation/overhaul/client-base/screenshots/` before editing. These showed flat cheek planes, low eye definition, straight fingers and broad armor slabs; the troll eyes were largely hidden behind its forward head shell.

| Creature | Before → after cubes | Visible refinement |
|---|---:|---|
| goblin_scout | 40 → 64 | Layered eye planes and cheeks, opposing thumbs and curled finger fronts, cuff/boot seams, rolled pauldron edge, dagger grip/pommel, pouch flap stitching. |
| goblin_shaman | 46 → 74 | Defined glowing eyes and cheeks, gripping thumb/fingers, wrapped staff grip, sewn robe hems and talisman edge. |
| orc_warrior | 43 → 72 | Ivory eye planes with dark pupils, cheeks and thumbs, stepped breastplate rim, shield side bindings/rivets, cleaver grip and pommel. |
| minotaur | 49 → 75 | Readable eyes and cheeks above unchanged muzzle, horn root rings, muzzle lip, brass armor lips, axe grip and hand finishing. |
| stone_troll | 58 → 80 | Forward eye planes recover eyes previously hidden by head shell; chiseled lids/cheeks, knuckle facets, wrist strata, stone jaw edge and moss seam transitions. |

All original bones, clips, palettes, equipment and world dimensions remain. Held dagger/staff/cleaver/axe/boulder stay descendants of `hand_right`; the shield stays on `forearm_left`. Weapon geometry is never independently translated during motion. Narrow layered surfaces use explicit depth offsets. Palettes are unchanged; the atlas adds directional skin/fur highlights, leather seam stitches, metal edge reflections and stone chisel highlights using shades of existing tile colors.

Locomotion now includes ankle articulation and delayed accessory motion; orc/minotaur weapon arms use a steadier carry. Attack/heavy/cast accessory follow-through lags the impact and settles in recovery. Gameplay impact keys remain at 0.35/0.8/0.9/1.2/1.1 seconds respectively, and authored death is exactly 0.65 seconds. Existing special clips remain.

Validation: `python tools/generate_overhaul_group_a.py` exported and verified all five native projects, UVs and PNGs. `python scripts/test-overhaul-assets.py` passed all four tests. No Java, gameplay, shared pipeline, dependencies, or Gradle changes. Runtime visual review of the new exports is delegated to the parent integration pass; baseline images alone do not establish new in-game clipping coverage.

Files: `tools/generate_overhaul_group_a.py`; five species files in `src/main/resources/assets/mythic_realms_creatures/geckolib/models/entity/*.geo.json`, `geckolib/animations/entity/*.animation.json`, `textures/entity/*.png`; shaman/troll glowmasks; and `tools/blockbench/{goblin_scout,goblin_shaman,orc_warrior,minotaur,stone_troll}.bbmodel`.
