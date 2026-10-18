# Mythic Realms: Creatures

**Development candidate 1.3.0-rc.1 · Fabric · Minecraft Java Edition 1.21.10 · Java 21**

Candidate 1.3.0-rc.1 completes the sequential visual overhaul of 17 creatures, with original species-specific geometry, textures and individually inspected in-game animations. Gameplay and spawning rules are preserved. Three unused emissive render passes are removed. See the [visual validation report](docs/monster-visual-overhaul-v3/README.md).

[Download candidate JAR](releases/1.3.0-rc.1/mythic-realms-creatures-1.3.0-rc.1.jar?raw=true) · [Candidate with required dependencies](releases/1.3.0-rc.1/mythic-realms-creatures-1.3.0-rc.1-with-dependencies.zip?raw=true) · [Candidate source](releases/1.3.0-rc.1/mythic-realms-creatures-1.3.0-rc.1-source.zip?raw=true)

[Download the stable mod JAR](releases/1.0.0/mythic-realms-creatures-1.0.0.jar?raw=true) · [Download with required dependencies](releases/1.0.0/mythic-realms-creatures-1.0.0-with-dependencies.zip?raw=true) · [Editable source](releases/1.0.0/mythic-realms-creatures-1.0.0-source.zip?raw=true)

Thirty-three fantasy creatures, four rideable species, four exploration structures, and a compact survival progression with 26 items and 14 recipes. Creatures use distinct block models, textures, GeckoLib animations, server-controlled attacks, biome spawning, spawn eggs, and loot tables. Better Combat adds optional player weapon animations.

## Installation

Install these mods on both clients and the dedicated server:

| Component | Required version |
| --- | --- |
| Minecraft Java Edition | **1.21.10 exactly** |
| Java | **21** |
| Fabric Loader | **0.19.5 or newer** |
| Mythic Realms: Creatures | `mythic-realms-creatures-1.3.0-rc.1.jar` (candidate) or stable `1.0.0` |
| Fabric API | **0.138.4+1.21.10** |
| GeckoLib, Fabric | **5.3-alpha-3 for Minecraft 1.21.10** |

Put the mod JAR and dependencies in the instance's `mods` directory. Dependencies are separate downloads; the `-sources.jar` contains editable source and is not the playable mod. Spawn eggs appear in the Spawn Eggs creative tab. Materials, foods, weapons, and mount equipment appear in their corresponding vanilla creative tabs.

### Optional Better Combat

The base mod runs without Better Combat. For its sword, axe, spear, and staff animations, add the following Fabric releases and their required dependencies:

| Mod | Version | Published Modrinth version |
| --- | --- | --- |
| [Better Combat](https://modrinth.com/mod/better-combat/version/qaOWa2t6) | **3.0.0+1.21.10-fabric** | `qaOWa2t6` |
| [Cloth Config API](https://modrinth.com/mod/cloth-config/version/qMxkrrmq) | **20.0.149+fabric** | `qMxkrrmq` |
| [Player Animation Library](https://modrinth.com/mod/player-animation-library/version/p8nawkdm) | **1.1.3** | `p8nawkdm` |

Player Animation Library's published file is named `PlayerAnimationLibFabric-1.1.3+mc.1.21.9.jar` and explicitly supports 1.21.10. Existing Fabric API supplies its resource-loader and command modules. Use a consistent mod set between clients and the server.

Integration uses Better Combat 3.0.0's supported `data/<namespace>/weapon_attributes/<item>.json` parent presets: `bettercombat:sword`, `bettercombat:axe`, `bettercombat:spear`, and `bettercombat:staff`. Creature attacks remain controlled by the server and GeckoLib; the mod adds no player combo or input hooks.

## Creature reference

Values are base attributes at difficulty multipliers of 1. Health and damage use Minecraft points; two health points equal one heart. Speed is the movement attribute, and armor is armor points. Individual attacks can apply additional effects or damage multipliers. The original-species habitat column records their historical habitats. In 1.2.0, only Forest Dryad and Slime Maiden from this table spawn naturally; the other 18 require eggs, commands or existing saved entities. New species habitats are listed in the expansion documentation.

| Creature / registry ID | Health | Damage | Speed | Armor | Behavior | Habitat | Drops |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| Goblin Scout `goblin_scout` | 18 | 3 | 0.32 | 1 | Fast melee; circles to flank | Plains, sunflower plains, forests | Iron nuggets, Goblin Scrap |
| Goblin Shaman `goblin_shaman` | 24 | 4 | 0.24 | 1 | Green fire bolts; heals wounded hostile allies | Swamps, mangrove swamps | Slime balls, Forest Essence |
| Orc Warrior `orc_warrior` | 40 | 7 | 0.23 | 7 | Heavy swings; guards frontal damage between attacks | Forests, hills | Iron ingots, Orc Steel |
| Minotaur `minotaur` | 65 | 9 | 0.27 | 5 | Charges distant targets; close sweeps | Mountains | Leather, Minotaur Horn |
| Stone Troll `stone_troll` | 80 | 11 | 0.17 | 10 | Boulder throws and ground smashes | Overworld caves, below sea level minus eight | Cobblestone, Troll Heartstone |
| Ancient Treant `ancient_treant` | 100 | 8 | 0.16 | 8 | Neutral guardian; slowing root projectiles | Forests | Oak logs, Living Wood |
| Forest Dryad `forest_dryad` | 28 | 3 | 0.26 | 2 | Neutral guardian; vine attacks and healing | Forests | Glow berries, Forest Essence |
| Griffin `griffin` | 48 | 6 | 0.28 | 3 | Flying mount; defends its owner | Mountains | Feathers, Griffin Feather |
| Dire Wolf `dire_wolf` | 36 | 5 | 0.34 | 2 | Fast ground mount; defends its owner | Forests | Leather, Dire Fang |
| Wild Wyvern `wild_wyvern` | 64 | 7 | 0.25 | 5 | Flying poison predator; rare blue variant is tameable | Mountains | Amethyst shards, Wyvern Scale |
| Cave Basilisk `cave_basilisk` | 34 | 5 | 0.25 | 4 | Telegraphs a slowing, mining-fatigue gaze | Dripstone and lush caves, below sea level minus eight | Spider eyes, Basilisk Scale |
| Crystal Spider `crystal_spider` | 28 | 4 | 0.29 | 3 | Climbs walls; crystal bolts create temporary slowing webs | Dripstone and lush caves, below sea level minus eight | Amethyst shards, Crystal Shard |
| Shadow Wraith `shadow_wraith` | 30 | 5 | 0.25 | 1 | Translucent hovering spirit; weakening dark bolts | Dark forests | Phantom membranes, Shadow Essence |
| Grave Knight `grave_knight` | 46 | 6 | 0.24 | 9 | Three-hit melee sequence; heavy finisher and frontal guard | Dark forests, old-growth spruce taiga | Iron nuggets, Orc Steel |
| Flame Imp `flame_imp` | 16 | 4 | 0.28 | 0 | Small flying fire caster; fire immune | Nether biomes | Blaze powder, Infernal Ember |
| Frost Elemental `frost_elemental` | 42 | 6 | 0.20 | 5 | Close frost wave; distant ice spikes | Snowy plains, ice spikes, frozen peaks | Snowballs, Frost Essence |
| Moon Stag `moon_stag` | 32 | 3 | 0.32 | 1 | Peaceful ground mount; heals its nearby owner at night | Forests, cherry groves | Leather, Forest Essence |
| Slime Maiden `slime_maiden` | 30 | 4 | 0.24 | 1 | Neutral bouncing guardian; slowing slime bubbles | Swamps, mangrove swamps, lush caves | Slime balls, Slime Pearl |
| Harpy `harpy` | 26 | 4 | 0.30 | 2 | Aerial swoops and fast feather projectiles | Mountains, windswept hills | Feathers, Griffin Feather |
| Demon Sorceress `demon_sorceress` | 40 | 6 | 0.25 | 3 | Cursing dark bolts; retreats by bounded teleport; fire immune | Nether wastes, crimson forests | Glowstone dust, Shadow Essence, Infernal Ember |

Overworld hostile species use darkness and difficulty checks. Nether casters require a non-Peaceful difficulty. Guardians and peaceful mounts use daylight and suitable ground checks. Natural spawns obey biome tags, dimension restrictions, configurable weights, and group limits. Forest guardians retaliate and attack monsters; they do not hunt peaceful players. Newly generated structures retain their blocks and loot, but only the Forest Shrine retains its Dryad inhabitant. Existing saved creatures are preserved.

All IDs use the namespace `mythic_realms_creatures`. With operator permission:

```mcfunction
/summon mythic_realms_creatures:crystal_spider
/summon mythic_realms_creatures:moon_stag
/give @p mythic_realms_creatures:demon_sorceress_spawn_egg
/give @p mythic_realms_creatures:frostbound_staff
```

## Taming, commands, and riding

| Mount | Custom taming and healing food | Also accepted for taming | Other healing food | Saddle |
| --- | --- | --- | --- | --- |
| Griffin | Sunseed Biscuit | Raw rabbit | Raw rabbit | Griffin Saddle or vanilla saddle |
| Dire Wolf | Hearty Meat | Bone | Raw beef | Vanilla saddle |
| Moon Stag | Moonblossom | Golden carrot | Glow berries, golden carrot | Vanilla saddle |
| Rare blue Wyvern | Venomous Morsel | Fermented spider eye | Fermented spider eye | Wyvern Harness or vanilla saddle |

Feed an untamed creature using the main hand. Default taming success is one in three attempts. The default randomized Wyvern variant has a one-in-twenty chance of being blue and tameable; ordinary Wyverns reject taming food without consuming it. Bones tame Dire Wolves but do not heal them. Healing food restores six health points and is consumed only when healing is needed.

The owner can equip a saddle by right-clicking, then mount a saddled adult with an empty hand. Shift-right-click beside an unmounted pet toggles stay/follow; flying pets must land first. The owner UUID, saddle state, stay command, and Wyvern variant persist across saves. Pets defend their owner and avoid attacking the owner or pets owned by the same player.

Use **WASD** and your view direction to steer. **Space** jumps on ground mounts. On Griffins and Wyverns, **Space** takes off or ascends, the **Sprint key** descends, and releasing vertical input hovers. Descend to the ground to land. **Shift dismounts**; land before dismounting at height. The server calculates bounded flight movement from vanilla input booleans and checks loaded chunks and the build ceiling.

## Structures

Four exploration structures generate through vanilla jigsaw structures, structure sets, biome tags, and NBT templates. Heights follow the generated terrain; the crypt begins five blocks below its surface placement. Structure sets exclude nearby vanilla villages and apply conservative random-spread spacing. Exploration loot uses normal chest loot tables.

| Structure / ID | Location | Inhabitants | Notable loot |
| --- | --- | --- | --- |
| Abandoned Goblin Watchtower `goblin_watchtower` | Plains, forests, savannas | Goblin Scouts and a Goblin Shaman | Goblin Scrap, arrows, food, iron nuggets |
| Forgotten Forest Shrine `forest_shrine` | Forests | Forest Dryad and Ancient Treant | Forest Essence, Living Wood, rare Twilight Relic |
| Ruined Grave Crypt `grave_crypt` | Dark forests, pale gardens, taiga | Grave Knight and Shadow Wraith | Shadow Essence, iron, spectral arrows, rare echo shard |
| Wyvern Nest `wyvern_nest` | Mountains | Wild Wyvern | Venomous Morsels, Wyvern Scales, saddle, rare diamonds |

New generation appears in unexplored chunks. Use `/locate structure mythic_realms_creatures:forest_shrine` or `/place structure mythic_realms_creatures:forest_shrine` with operator permission. Structure enable switches control natural generation; templates and administrative placement remain available.

## Items and survival progression

The **26 progression items** comprise 15 materials, four taming foods, two mount equipment items, four weapons, and one decorative relic. The 20 spawn eggs are additional creature access items.

Materials come from the creature drops listed above: **Goblin Scrap, Orc Steel, Minotaur Horn, Troll Heartstone, Living Wood, Forest Essence, Griffin Feather, Dire Fang, Wyvern Scale, Basilisk Scale, Crystal Shard, Shadow Essence, Frost Essence, Infernal Ember, and Slime Pearl**. Structure chests provide additional sources for selected materials and taming foods.

Fourteen crafting recipes are available in the recipe book after collecting a relevant ingredient. Food and material conversion recipes are shapeless; equipment recipes are shaped and use the arrangement shown in the recipe book.

| Recipe / output | Ingredients | Output count |
| --- | --- | ---: |
| Sunseed Biscuit | 2 wheat, golden carrot, sunflower | 4 |
| Hearty Meat | Cooked beef, sweet berries, cooked chicken | 3 |
| Moonblossom | Glow berries, sweet berries, lily of the valley | 3 |
| Venomous Morsel | Rotten flesh, spider eye, fermented spider eye | 3 |
| Griffin Saddle | 2 Griffin Feathers, 4 leather, 2 iron ingots | 1 |
| Wyvern Harness | 2 Wyvern Scales, 3 leather, Slime Pearl, 2 iron ingots | 1 |
| Crystal Fang Sword | Crystal Shard, Dire Fang, iron ingot | 1 |
| Orc War Axe | 3 Orc Steel, Infernal Ember, stick | 1 |
| Basilisk Spear | Minotaur Horn, 2 Basilisk Scales, 2 sticks | 1 |
| Frostbound Staff | 2 Frost Essences, Crystal Shard, 2 Living Wood | 1 |
| Twilight Relic | 4 gold ingots, 2 Shadow Essences, 2 Forest Essences, Troll Heartstone | 1 |
| Salvaged iron ingot | 9 Goblin Scrap | 1 |
| Oak planks | Living Wood | 8 |
| Bone meal | Forest Essence, bone meal | 8 |

The Crystal Fang Sword has 720 durability; the Orc War Axe has 480 and supports vanilla axe interactions; the Basilisk Spear has 420; the Frostbound Staff has 260. Repair them with Crystal Shard, Orc Steel, Basilisk Scale, and Frost Essence respectively. Weapon tags support relevant vanilla enchantments. With Better Combat, the spear and staff use their supported two-handed presets.

Right-click the **Frostbound Staff** for Resistance I for five seconds, with a twelve-second cooldown and three durability per cast. This defensive spell works without Better Combat. The **Twilight Relic** is a rare decorative keepsake available through crafting or shrine exploration.

## Configuration

The first start creates `config/mythic_realms_creatures.json`. Restart after changing settings. Invalid configuration logs an error, preserves the file, and uses defaults. Existing files retain their settings; missing species and fields receive defaults in memory. Valid numeric values must also be finite.

| Field | Default | Accepted values / effect |
| --- | --- | --- |
| `difficultyMultiplier` | `1` | `0.25`–`4`; global creature health and damage multiplier |
| `magicParticleIntensity` | `1` | `0`–`2`; scales creature spell particles; `0` disables these emissions |
| `aiUpdateInterval` | `10` | `2`–`40` ticks; cadence for scheduled combat navigation updates |
| `mountSpeedMultiplier` | `1` | `0.25`–`2`; ridden ground speed |
| `flightSpeedMultiplier` | `1` | `0.25`–`2`; ridden flight speed |
| `tamingDifficulty` | `3` | `1`–`100`; taming chance is one in this many attempts |
| `rareWyvernChance` | `20` | `1`–`1000`; natural blue-Wyvern chance is one in this many |
| `structuresEnabled` | `true` | Global natural structure generation switch |
| `structures.<structure_id>` | `true` | Individual switches for `goblin_watchtower`, `forest_shrine`, `grave_crypt`, `wyvern_nest` |
| `spawning.<species>.enabled` | `true` | Natural spawning switch for eligible species; disabled original species cannot be re-enabled; eggs and summon commands stay available |
| `spawning.<species>.weight` | Species-specific, `1`–`12` | `0`–`100`; relative biome spawn weight; `0` disables natural spawning |
| `spawning.<species>.minGroup` | `1` | `1`–`6`; minimum group size |
| `spawning.<species>.maxGroup` | `2` | Minimum through `6`; maximum group size |
| `spawning.<species>.frequency` | `1` | `1`–`1000`; accept one in this many eligible spawn attempts |
| `spawning.<species>.difficultyMultiplier` | `1` | `0.25`–`4`; multiplies global health and damage scaling for this species |
| `spawning.<species>.dimensions` | `["minecraft:overworld"]` | Dimension-ID allowlist; Flame Imp and Demon Sorceress default to `["minecraft:the_nether"]`; empty list disables natural spawning |
| `spawning.<species>.biomes` | `[]` | Optional biome-ID / `#biome_tag` allowlist; empty list imposes no further biome restriction |

Biome configuration **narrows the species' existing spawn tag**. It does not inject spawning into additional biomes. To expand biome support, extend `data/mythic_realms_creatures/tags/worldgen/biome/spawns/<species>.json` in a data pack, then allow the intended dimensions and optional biome whitelist. Structure biome tags are under `tags/worldgen/biome/has_structure/`. The 18 retired original natural-spawn tags are empty and the registration policy also blocks their natural/chunk-generation spawn reasons, including legacy configurations with enabled=true.

The global and species difficulty multipliers multiply together. For example, global `1.5` and species `2` produce three times that species' base health and damage. Enabling a dimension alone does not remove biome or ground checks.

## Build and verification

Use a full JDK 21. The wrapper pins Gradle 9.7.1; Fabric Loom 1.14.10 uses official Mojang mappings.

```sh
./gradlew clean build
./gradlew runGametest
python3 scripts/test-assets.py
./gradlew -PwithBetterCombat runGametest
./gradlew runClient
./gradlew -PwithBetterCombat runClient
./gradlew runServer
```

`-PwithBetterCombat` adds the three published optional runtime dependencies listed above. It does not make Better Combat a release requirement. The distributable JAR and editable source JAR are in `build/libs`.

For this cloud workspace, the setup helper installs the pinned JDK/Gradle tooling and the Gradle helper configures the platform HTTPS proxy without saving credentials:

```sh
bash scripts/setup-tools.sh
python3 scripts/cloud-gradle.py clean build
python3 scripts/cloud-gradle.py runGametest
python3 scripts/cloud-gradle.py -PwithBetterCombat runGametest
python3 scripts/test-assets.py
```

GameTests run in a separate, automatically stopped dedicated server. A normal playable server requires reviewing Minecraft's EULA. The tests cover entity and item registrations, crafting and drops, attack timing and spell effects, ownership and mounts, structure placement and loot, and optional Better Combat weapon resolution.

The graphical smoke workflow launches an actual Minecraft client, renders creatures in a singleplayer world, and writes screenshots and logs:

```sh
bash scripts/client-smoke-install.sh  # Debian cloud workspace: local Xvfb/display tools
bash scripts/client-smoke.sh
bash scripts/client-smoke.sh -PwithBetterCombat
```

The wrapper uses an existing display or starts its local Xvfb, requires `CLIENT_SMOKE_PASS`, and stores evidence in `build/client-smoke-evidence/` and `build/client-smoke/screenshots/`. With an existing desktop environment, `./gradlew runClientSmoke` runs the same isolated client test mod.

**See [docs/PROGRESS.md](docs/PROGRESS.md) for executed checks.** Hands-on survival balance, multiplayer network latency, and integration with Terralith and Tectonic have not been verified. Automated client rendering does not establish those gameplay outcomes.

## Architecture and editable assets

- `registry/`: creature types, projectiles, spawn eggs, progression items, and creative-tab access.
- `entity/`, `entity/ai/`, `entity/combat/`: distinct species, shared hostility/guardian/aerial behavior, and server attack windup/impact/recovery timelines.
- `entity/mount/`: persistent ownership, stay/follow commands, rider validation, and bounded flight movement from vanilla input packets.
- `magic/`: spell effects and temporary web traps; `CreatureProjectile` handles server-authoritative projectile impacts.
- `world/`: structure resource conditions; vanilla world generation loads jigsaw structures, template pools, templates, and loot data.
- `config/` and `compat/`: validated configuration and optional Better Combat detection. Integration references no mandatory Better Combat classes.
- `src/client/`: GeckoLib renderers and models, separated from common/server classes.
- `src/test/`, `src/gametest/`, `src/clientGametest/`: unit tests, dedicated-server tests, and a separate graphical test mod. Test mods are excluded from the release JAR.

GeckoLib geometry and animations live under `assets/mythic_realms_creatures/geckolib/`; textures are PNG; items use the 1.21.10 item-definition and model format. Data directories use the target game's singular `recipe`, `loot_table`, `structure`, and `advancement` conventions. Vanilla sounds are reused. Editable Blockbench projects for Groups C/D are in `tools/blockbench/`.

Rebuild generated assets with these scripts; creature and item texture generation requires Pillow as a development dependency:

```sh
python3 tools/generate_group_a_assets.py
python3 tools/generate_group_b_assets.py
python3 tools/generate_groups_cd_assets.py
python3 tools/generate_progression.py
python3 tools/generate_structures.py --minecraft-jar /path/to/minecraft-extracted_server.jar
python3 tools/integrate_content.py
python3 scripts/test-assets.py
```

Run the integration script after regeneration to merge English language fragments and restore survival material drops. The structure generator reads the actual target Minecraft JAR's `DataVersion`; it uses Python's standard library. Creature model silhouettes, pivots, textures, and animation tracks remain editable in their source JSON and generators.

Dependency provenance: the official Fabric 1.21.10 template, published Fabric Maven artifacts, GeckoLib's exact 1.21.10 release ([`7qjQQSWv`](https://modrinth.com/mod/geckolib/version/7qjQQSWv)), and the Better Combat dependency versions linked above. The GeckoLib API and Better Combat attribute schema were inspected against those exact releases.

License: **CC0-1.0**, inherited from the Fabric example template. Third-party dependencies retain their own licenses. The [requirements](docs/REQUIREMENTS.md) and [progress log](docs/PROGRESS.md) describe scope and validation evidence.
