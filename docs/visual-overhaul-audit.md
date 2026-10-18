# Visual overhaul audit — 2026-10-18

Baseline: a1aa0f0 (rc.2), clean before work. Branch: feat/visual-overhaul; continues existing source instead of resetting main.

Minecraft 1.21.10; Loader 0.19.5; API 0.138.4+1.21.10; Loom 1.14.10; Java 21; Gradle 9.7.1; GeckoLib 5.3-alpha-3. Better Combat remains optional.

## Shared integration

Registration: `src/main/java/com/mythicrealms/creatures/registry/ModEntities.java`; attributes/hitboxes: `entity/CreatureKind.java`; spawn eggs/items: `registry/ModItems.java`. Paths below are relative to `src/main/resources/assets/mythic_realms_creatures/`.

Renderer/variants/glow/translucency: `src/client/java/com/mythicrealms/creatures/client/MythicRealmsClient.java`; animation controllers: `src/main/java/com/mythicrealms/creatures/entity/MythicCreature.java`; server attacks: per-species entities; rider logic: `entity/mount/`. Baked weapons are geometry, not duplicate held-item renderer layers.

| Species | Geometry | Texture/variants | Animation clips | Native project | New-pass gap |
|---|---|---|---|---|---|
| goblin_scout | `geckolib/models/entity/goblin_scout.geo.json` | goblin_scout.png | `geckolib/animations/entity/goblin_scout.animation.json`: idle, walk, run, attack, heavy, cast, hurt, death, sneak, dodge, guard | `tools/blockbench/goblin_scout.bbmodel` | Grip/cranial proof implemented; visual acceptance pending |
| goblin_shaman | `geckolib/models/entity/goblin_shaman.geo.json` | goblin_shaman.png, goblin_shaman_glowmask.png | `geckolib/animations/entity/goblin_shaman.animation.json`: idle, walk, run, attack, heavy, cast, hurt, death, ritual, guard | `tools/blockbench/goblin_shaman.bbmodel` | New brief acceptance review pending |
| orc_warrior | `geckolib/models/entity/orc_warrior.geo.json` | orc_warrior.png | `geckolib/animations/entity/orc_warrior.animation.json`: idle, walk, run, attack, heavy, cast, hurt, death, guard | `tools/blockbench/orc_warrior.bbmodel` | New brief acceptance review pending |
| minotaur | `geckolib/models/entity/minotaur.geo.json` | minotaur.png | `geckolib/animations/entity/minotaur.animation.json`: idle, walk, run, attack, heavy, cast, hurt, death, charge, guard | `tools/blockbench/minotaur.bbmodel` | New brief acceptance review pending |
| stone_troll | `geckolib/models/entity/stone_troll.geo.json` | stone_troll.png, stone_troll_glowmask.png | `geckolib/animations/entity/stone_troll.animation.json`: idle, walk, run, attack, heavy, cast, hurt, death, throw, guard | `tools/blockbench/stone_troll.bbmodel` | New brief acceptance review pending |
| ancient_treant | `geckolib/models/entity/ancient_treant.geo.json` | ancient_treant.png, ancient_treant_glowmask.png | `geckolib/animations/entity/ancient_treant.animation.json`: idle, walk, run, attack, heavy, cast, hurt, death | `tools/blockbench/ancient_treant.bbmodel` | New brief acceptance review pending |
| wild_wyvern | `geckolib/models/entity/wild_wyvern.geo.json` | wild_wyvern.png, wild_wyvern_glowmask.png, wild_wyvern_rare.png, wild_wyvern_rare_glowmask.png, wild_wyvern_tamed.png, wild_wyvern_tamed_glowmask.png | `geckolib/animations/entity/wild_wyvern.animation.json`: idle, walk, run, attack, heavy, cast, hurt, death, sit, rest, ride, tame, fly, hover, takeoff, landing | `tools/blockbench/wild_wyvern.bbmodel` | New brief acceptance review pending |
| dire_wolf | `geckolib/models/entity/dire_wolf.geo.json` | dire_wolf.png, dire_wolf_tamed.png | `geckolib/animations/entity/dire_wolf.animation.json`: idle, walk, run, attack, heavy, cast, hurt, death, sit, rest, ride, tame, jump | `tools/blockbench/dire_wolf.bbmodel` | New brief acceptance review pending |
| griffin | `geckolib/models/entity/griffin.geo.json` | griffin.png, griffin_tamed.png | `geckolib/animations/entity/griffin.animation.json`: idle, walk, run, attack, heavy, cast, hurt, death, sit, rest, ride, tame, fly, hover, takeoff, landing | `tools/blockbench/griffin.bbmodel` | New brief acceptance review pending |
| cave_basilisk | `geckolib/models/entity/cave_basilisk.geo.json` | cave_basilisk.png, cave_basilisk_glowmask.png | `geckolib/animations/entity/cave_basilisk.animation.json`: idle, walk, run, attack, heavy, cast, hurt, death | `tools/blockbench/cave_basilisk.bbmodel` | New brief acceptance review pending |
| frost_elemental | `geckolib/models/entity/frost_elemental.geo.json` | frost_elemental.png, frost_elemental_glowmask.png | `geckolib/animations/entity/frost_elemental.animation.json`: idle, walk, run, attack, heavy, cast, hurt, death | `tools/blockbench/frost_elemental.bbmodel` | New brief acceptance review pending |
| moon_stag | `geckolib/models/entity/moon_stag.geo.json` | moon_stag.png, moon_stag_glowmask.png, moon_stag_tamed.png, moon_stag_tamed_glowmask.png | `geckolib/animations/entity/moon_stag.animation.json`: idle, walk, run, attack, heavy, cast, hurt, death, sit, tame, ride, jump | `tools/blockbench/moon_stag.bbmodel` | New brief acceptance review pending |
| forest_dryad | `geckolib/models/entity/forest_dryad.geo.json` | forest_dryad.png, forest_dryad_glowmask.png | `geckolib/animations/entity/forest_dryad.animation.json`: idle, walk, run, attack, heavy, cast, hurt, death | `tools/blockbench/forest_dryad.bbmodel` | New brief acceptance review pending |
| shadow_wraith | `geckolib/models/entity/shadow_wraith.geo.json` | shadow_wraith.png, shadow_wraith_glowmask.png | `geckolib/animations/entity/shadow_wraith.animation.json`: idle, walk, run, attack, heavy, cast, hurt, death, fly, hover | `tools/blockbench/shadow_wraith.bbmodel` | New brief acceptance review pending |
| grave_knight | `geckolib/models/entity/grave_knight.geo.json` | grave_knight.png, grave_knight_glowmask.png | `geckolib/animations/entity/grave_knight.animation.json`: idle, walk, run, attack, heavy, cast, hurt, death, attack_two, guard | `tools/blockbench/grave_knight.bbmodel` | New brief acceptance review pending |
| slime_maiden | `geckolib/models/entity/slime_maiden.geo.json` | slime_maiden.png, slime_maiden_glowmask.png | `geckolib/animations/entity/slime_maiden.animation.json`: idle, walk, run, attack, heavy, cast, hurt, death | `tools/blockbench/slime_maiden.bbmodel` | New brief acceptance review pending |
| harpy | `geckolib/models/entity/harpy.geo.json` | harpy.png, harpy_glowmask.png | `geckolib/animations/entity/harpy.animation.json`: idle, walk, run, attack, heavy, cast, hurt, death, fly, hover, swoop | `tools/blockbench/harpy.bbmodel` | New brief acceptance review pending |
| demon_sorceress | `geckolib/models/entity/demon_sorceress.geo.json` | demon_sorceress.png, demon_sorceress_glowmask.png | `geckolib/animations/entity/demon_sorceress.animation.json`: idle, walk, run, attack, heavy, cast, hurt, death, levitate, teleport | `tools/blockbench/demon_sorceress.bbmodel` | New brief acceptance review pending |

Gameplay resources remain under `data/mythic_realms_creatures/{loot_table/entities,tags/worldgen/biome/spawns}/<id>.json`; equipment and spawn-egg textures remain unchanged. All 20 registrations retained, including excluded Crystal Spider and Flame Imp.

## Reference evidence

The supplied inventory lists 66 geometry files, 65 animation files and 572 entity textures, with paths for articulated quadrupeds (mammoth, megaloceros), flying reptiles (pteranodon, quetzalcoatlus) and reptiles (megalania). This establishes contextual asset organisation only, not anatomy or animation quality. The source JAR is absent. The requested wiki returned proxy CONNECT HTTP 403 on this run. No reference images or keyframes could be inspected from this pack; no third-party assets copied. Do not label the new work visually verified against unavailable references.

Original work uses the existing GeckoLib bone hierarchy with rigid item inheritance, controlled cuboid subdivision and existing UV tiles. Earlier inspected visual references remain documented in `creature-overhaul/REFERENCE_ATLAS.md`.
