# Mythic Realms: Creatures

An early Fabric **Minecraft 1.21.10** alpha with five fantasy creatures. This is the first playable-content milestone of the [20-creature specification](docs/REQUIREMENTS.md), not the completed mod. The JAR builds and dedicated-server tests pass; client visuals and hands-on survival balance still need in-game review.

## Install

1. Use Minecraft Java Edition **1.21.10**, Java **21**, and Fabric Loader **0.19.5 or newer**.
2. Put `mythic-realms-creatures-0.1.0-alpha.1.jar` in your instance's `mods` folder.
3. Also install **Fabric API 0.138.4+1.21.10** and **GeckoLib Fabric 1.21.10 5.3-alpha-3**. These dependencies are not bundled into the mod JAR.
4. Start the game. Spawn eggs appear in the Spawn Eggs creative tab. A dedicated server needs the same three mods; clients need them too.

Better Combat is optional. This mod changes no player combat inputs or timing. Better Combat runtime compatibility has not yet been tested; no player weapons are included in this alpha.

## Creatures

| Creature | Health | Damage | Behavior | Natural habitat | Loot |
| --- | ---: | ---: | --- | --- | --- |
| Goblin Scout | 18 | 3 | Fast melee attacks; circles to flank | Plains and forests | Iron nuggets |
| Goblin Shaman | 24 | 4 | Green poison bolts; heals nearby wounded allies | Swamps | Slime balls |
| Orc Warrior | 40 | 7 | Telegraphs heavy swings; shields frontal damage between swings | Forests and hills | Iron ingots |
| Minotaur | 65 | 9 | Charges distant targets; sweeps at close range | Mountains | Leather |
| Stone Troll | 80 | 11 | Throws boulders; smashes nearby players | Below sea level minus eight blocks in the Overworld | Cobblestone |

Attacks run on the server with windup and recovery. All species have distinct block geometry, pixel textures, idle/walk/attack/death animations, English names, spawn eggs, loot and configurable natural spawning. Vanilla sound effects are reused.

Use commands with cheats/operator permission:

```mcfunction
/summon mythic_realms_creatures:goblin_scout
/summon mythic_realms_creatures:goblin_shaman
/summon mythic_realms_creatures:orc_warrior
/summon mythic_realms_creatures:minotaur
/summon mythic_realms_creatures:stone_troll
/give @p mythic_realms_creatures:goblin_scout_spawn_egg
```

Natural spawning follows vanilla hostile darkness/difficulty rules. The troll uses the world's sea level rather than a fixed terrain-height assumption.

## Configuration

On first start, `config/mythic_realms_creatures.json` is created. Restart the game/server after editing.

- `difficultyMultiplier`: health and damage multiplier, from 0.25 to 4.
- `spawning.<species>.enabled`: toggles natural spawning; summon commands and eggs remain available.
- `weight`: relative spawn weight, from 0 to 100; zero disables natural spawning.
- `minGroup` / `maxGroup`: group sizes from 1 to 6, with minimum no greater than maximum.
- `frequency`: spawn-candidate acceptance, one in this many attempts; from 1 to 1000.

Invalid configuration uses defaults and logs an error while preserving the original file. Biome restrictions are data-pack tags under `data/mythic_realms_creatures/tags/worldgen/biome/spawns/`. All current species spawn naturally only in Overworld biomes. Additional configuration from the full specification remains planned.

## Build and test

Use a full JDK 21. Gradle 9.7.1 is checksum-pinned; Loom 1.14.10 uses official Mojang mappings.

```sh
./gradlew build
./gradlew runGametest
python3 scripts/test-assets.py
./gradlew runClient
./gradlew runServer
```

The normal distributable JAR and editable source JAR are produced in `build/libs`. Do not install the `-sources.jar` as the mod.

For this cloud environment, which requires the platform HTTPS proxy:

```sh
bash scripts/setup-tools.sh
python3 scripts/cloud-gradle.py build
python3 scripts/cloud-gradle.py runGametest
```

The cloud helper uses system TLS trust and the injected proxy without saving credentials. GameTests use an isolated, automatically stopped test server. Running a normal Minecraft server requires separately reviewing Minecraft's EULA.

Verified: build; one JUnit test exercising 14 combat assertions; five custom server GameTests for registration/attributes/eggs/loot, delayed melee damage projectile damage and non-player retaliation; five-species asset consistency checks. The GameTest runner additionally executes Minecraft's built-in `always_pass` test. Visual quality, multiplayer with real players, terrain mods and Better Combat remain unverified.

## Editable assets and remaining work

Geometry and animations are normal GeckoLib 5 JSON under `assets/mythic_realms_creatures/geckolib/`. Textures are PNG. `tools/generate_group_a_assets.py` regenerates the assets with Pillow; Pillow is a development tool only. No Blockbench project files are supplied yet.

Remaining: 15 creatures, taming and mounts, exploration structures, progression items, expanded configuration, deeper balancing and full multiplayer/client compatibility testing. See [progress](docs/PROGRESS.md) and [implementation plan](docs/IMPLEMENTATION_PLAN.md).

Dependency provenance: official Fabric template branch `1.21.10`, published Fabric Maven artifacts, and Modrinth's exact Fabric 1.21.10 GeckoLib release (`7qjQQSWv`, verified against its published SHA-512). GeckoLib APIs were checked against its matching 1.21.10 / 5.3-alpha-3 source.

License: CC0-1.0, inherited from the Fabric example template. Third-party dependencies retain their own licenses.
