# Persistent progress — 2026-10-17

## Current milestone

Early five-creature alpha, Minecraft 1.21.10 / Fabric / Java 21. Not the complete 20-creature mod.

## Implemented

- Working Gradle build, source and distributable JARs. Stable Loom 1.14.10 resolves on Java 21; the initial template's newer Loom snapshot required Java 25 and was replaced.
- Fabric Loader 0.19.5, Fabric API 0.138.4+1.21.10, GeckoLib 5.3-alpha-3 (verified published Modrinth version 7qjQQSWv).
- Shared server attack timeline, AI pursuit/cooldowns, ranged retreat, animation triggers and bounded-lifetime projectiles.
- Five distinct entities: Goblin Scout (flanking), Goblin Shaman (poison projectile and ally healing), Orc Warrior (heavy swings and directional shield), Minotaur (charge/sweep), Stone Troll (boulder/smash).
- Per-species block geometry, pixel atlas, animations, spawn eggs, English names, loot tables and natural biome spawning.
- Validated JSON configuration for difficulty and per-species spawn settings; data-pack biome tags.
- Client render registration isolated from common/server code.

## Evidence

- `python3 scripts/cloud-gradle.py build`: passed, including JUnit combat test (14 assertions).
- `python3 scripts/cloud-gradle.py runGametest`: passed, 5 custom tests plus Minecraft's built-in test. Covers all five species' server registration, health, eggs and loaded loot; scout windup/impact; shaman projectile damage.
- `python3 scripts/test-assets.py`: passed for five distinct nonempty models, linked animation bones/states, PNG dimensions, eggs and loot resources.
- GameTests load the dedicated server and world, apply biome modifications, and shut down automatically. An external Minecraft-services public-key request failed due to direct DNS; local GameTests still completed successfully. This does not verify online player authentication.

## Incomplete / unverified

- Client code compiled, but visual model/animation quality has not been observed in a graphical game client.
- Real-player multiplayer, optional Better Combat, Terralith and Tectonic are not tested.
- 15 creatures remain: Ancient Treant, Forest Dryad, Griffin, Dire Wolf, Wild Wyvern, Cave Basilisk, Crystal Spider, Shadow Wraith, Grave Knight, Flame Imp, Frost Elemental, Moon Stag, Slime Maiden, Harpy, Demon Sorceress.
- Mount/taming/flight, structures, progression items, expanded configuration, custom audio and editable Blockbench projects remain planned.
- First-group gameplay needs deeper tests of shield direction, charge/sweep, boulder/smash, shaman healing, natural spawning density and reload persistence.

## Next execution

1. Review the current alpha visually in Minecraft 1.21.10 and expand first-group behavioral GameTests.
2. Continue core systems and Groups B–D from REQUIREMENTS.md without restarting the project or counting names/assets as complete creatures.
3. Implement mounts, structures, progression and the complete compatibility test matrix.

Use the current isolated checkout. Original user authorization: implement inline, maintain progress, commit meaningful groups. Do not claim all 20 creatures are done.

## Review and reusable setup
- Independent review found Minotaur/Troll retaliation excluded non-player targets. Two GameTests failed before the fix and passed after including valid primary targets in area attacks.
- Model death animation now supplies the death roll without a second renderer roll.
- Updated install_script and start_skill saved to the cloud configuration draft. Review/save and publish the environment to retain these updates for later tasks.
