# Release progress — 2026-10-18

Version **1.0.0** completes the twenty-creature content specification for Minecraft **1.21.10**, Fabric and Java 21. This continues the existing mod and preserves its original ten species.

## Implemented content

- All twenty species have registered attributes, distinct articulated GeckoLib geometry, 128×128 pixel textures, English names, spawn eggs, loaded survival loot and biome spawn entries. All declared animation clips bake in the actual client. Running, hurt, casting, death, flight and mount states are supplied where applicable.
- Groups C/D add petrifying Basilisk gaze; wall-climbing Crystal Spider with crystal bolts and breakable temporary webs; translucent Wraith curses; guarded Grave Knight combos; flying fire Imps; frost novas and ice spikes; tameable Moon Stag with nighttime owner healing; neutral bouncing Slime Maiden; swooping Harpy; and teleporting Demon Sorceress.
- Four owner-persistent rideable species share taming, healing, follow/stay, saddles, owner protection and server-controlled movement. Griffin and rare Wyvern flight uses vanilla player-input packets with bounded acceleration/speed, loaded-chunk and ceiling checks. Moon Stag and Dire Wolf use ground riding.
- Four real jigsaw structures and structure sets contain persistent inhabitants and usable chest loot: Goblin Watchtower, Forest Shrine, Grave Crypt and Wyvern Nest. Placement follows terrain height and village exclusion. Configuration can disable individual structure sets.
- Twenty-six items and fourteen recipes provide creature materials, taming foods, Griffin saddle, Wyvern harness, four weapons and a relic. Frostbound Staff has a server cooldown, durability cost and resistance spell. Optional Better Combat presets resolve to real weapon categories and attack animations.
- Configuration covers per-species spawning, groups, frequency, dimension/biome restrictions, per-species/global difficulty, rare Wyverns, taming, ground/flight speed, particle intensity, structures and pathfinding update intervals. Older configurations preserve settings and acquire missing defaults in memory.
- Asset generators reproduce resources; C/D also include ten native editable Blockbench projects. Magical creatures use emissive layers; Wraith and Slime Maiden use translucent rendering. Vanilla sounds are reused.

## Executed verification

- **34 dedicated-server GameTests pass without Better Combat and with Better Combat 3.0.0**: 33 custom tests plus Minecraft's built-in test. Reports are in [test-results](test-results/).
- Server checks cover all twenty registrations/attributes/eggs/loaded loot, natural biome spawn entries and rejected dimensions, delayed combat, distinct magic effects, temporary webs, frost reach, combos, guardian healing, taming, owner/state reload, owner-safe targeting, normal-tick rider inputs and bounded flight, all four generated jigsaws/inhabitants/chests, material sources, real crafting, staff cooldown/durability and live Better Combat presets.
- **Two graphical client runs pass**, with and without Better Combat, under Xvfb/Mesa llvmpipe OpenGL 4.5. Each loads all twenty models and every declared animation, verifies synchronized entities and Geo renderers, captures idle/attack frames, and uses real local-player keyboard packets to move and ascend on the authoritative Griffin. Selected screenshots were visually inspected. Forty-one screenshots per run are retained outside build output under `/workspace/validation/client-base` and `/workspace/validation/client-better-combat`.
- **Two resource tests pass** across twenty species: distinct nonempty geometry, bone/state references, PNG size, alternate mount textures, loot, eggs and English names.
- Every retained dependency JAR was rechecked against the published Modrinth SHA-512 and Minecraft 1.21.10 compatibility metadata. Exact versions/hashes are recorded in [the dependency report](test-results/1.0.0-dependencies.json).
- **`python3 scripts/cloud-gradle.py clean build` passes**, with all eleven tasks executed. Five JUnit tests pass: one attack-timeline test and four bounded flight-motion tests. The final remapped JAR is Java 21 bytecode, version 1.0.0; all source resources match the packaged bytes, and isolated test mods are excluded. It contains twenty models/animation files, fourteen recipes, four NBT structures and four optional weapon presets.

## Defects resolved during integration

- Minecraft 1.21.10 emits no jigsaw pieces at depth zero. Structure definitions now use depth one, and the placement test reads the depth from each actual decoded structure definition before asserting mobs and loot.
- Frost nova selection now matches its affected region; targets outside it receive ice projectiles. Temporary webs are pickable and break on damage.
- Grave Knight heavy animation starts during its windup, before the finisher hits. Registered animation names resolve for the relevant species, and damage reactions avoid interrupting active windups.
- Ranged enemies retain their retreat navigation during recovery. Magical particles share a configurable, bounded, distance-aware emission helper.
- Fabric's client test network synchronizer stalled initial world loading. The isolated harness uses its documented asynchronous-network option and explicitly waits for actual synchronized client entities. The gameplay mod is unchanged by this test setting.
- Loom development runs omit embedded optional-mod libraries. The Better Combat development flag now loads the exact nested libraries from its published distributions. Ordinary Fabric installations load these automatically; no optional library is bundled in the mod.
- Durability/Peaceful tests now use a genuine Survival mock where required; the deprecated server mock reports Creative mode even after changing its game mode.

## Validation limits

Dedicated-server gameplay tests and an integrated real client are verified. External multi-player sessions, network latency/packet loss, long survival balance/performance sessions and Terralith/Tectonic installations were not exercised. Biome tags and terrain-relative structures support those compatibility goals; this is not a claim of tested terrain-mod integration. Audio hardware was unavailable in the headless client, and offline Mojang profile lookups/X11 cursor warnings were logged without failing gameplay/render tests.

## History

- Group A: first five-creature alpha, commit `270a0d3`.
- Group B: ten-creature alpha with guardians and safe mounts, commit `45ebd3e`.
- Version 1.0.0 completes Groups C/D, structures, progression, configuration and the client/optional-combat validation above.
