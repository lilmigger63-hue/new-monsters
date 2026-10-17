# CODEX TASK — Build a Complete Fantasy Creatures Mod for Minecraft Fabric 1.21.10

## 1. Main objective

You are an experienced Minecraft Fabric mod developer, Java programmer, AI behavior designer, 3D model creator, and game designer.

Your task is to **CREATE AND IMPLEMENT a complete, playable Minecraft Fabric 1.21.10 mod** called **Mythic Realms: Creatures**.

Do not simply describe how to make this mod. Actually create, modify, and implement the source code, resources, models, animations, configurations, and build files.

The mod must introduce **20 original fantasy creatures** into Minecraft, with a cohesive combination of:

- High fantasy creatures
- Dark fantasy monsters
- Medieval fantasy enemies
- Magical forest creatures
- Mythical beasts
- Anime-inspired fantasy creatures

The overall atmosphere should be mysterious, immersive, magical, and slightly dark, like a fantasy RPG world.

**Bosses are NOT required.** Prioritize creature quality over bosses. Do not spend development time implementing boss fights, boss bars, or boss-specific progression.

All visible text, item descriptions, configuration names, and documentation must be in English.

## 2. Technical requirements

Target environment:

- Minecraft: **1.21.10 EXACTLY**
- Mod loader: **Fabric**
- Programming language: Java
- Java version: 21
- Fabric API: compatible 1.21.10 release
- Fabric Loom: compatible version
- Animation library: GeckoLib 5, using a compatible Fabric 1.21.10 release
- Better Combat: compatibility with the 1.21.10 Fabric release
- Multiplayer: dedicated-server compatible

Use official Mojang mappings consistently unless an existing repository already uses another mapping set and migration would introduce unnecessary risk.

Use the official Fabric example mod/template as the reference for creating Gradle files.

Resolve actual published dependency versions before inserting them into the Gradle configuration. Do not invent Maven coordinates or version strings.

The 1.21.10 GeckoLib release is based on an alpha API. Inspect the documentation for that exact version instead of using outdated GeckoLib 4 examples.

The mod must work without Better Combat installed. Better Combat integration should enhance the experience when detected.

Avoid unnecessary Mixins and avoid modifying vanilla player attack timing or input handling.

## 3. The 20 creatures

Implement exactly these 20 creatures initially.

Each must have its own registry ID, meaningful visual identity, behavior, stats, loot, spawn conditions, and animations.

| # | Creature | Behavior and special abilities |
|---|---|---|
| 1 | Goblin Scout | Fast, weak enemy using daggers; attempts to flank players |
| 2 | Goblin Shaman | Ranged magical goblin using green fireballs and healing |
| 3 | Orc Warrior | Armored melee creature with heavy weapon swings and shield behavior |
| 4 | Minotaur | Large labyrinth creature with charging and sweeping attacks |
| 5 | Stone Troll | Slow, powerful creature with rock-throwing and ground-smash attacks |
| 6 | Ancient Treant | Giant living tree that throws roots and protects forests |
| 7 | Forest Dryad | Magical humanoid forest spirit with healing and vine attacks |
| 8 | Griffin | Tameable flying creature that can carry a player |
| 9 | Dire Wolf | Large tameable wolf that can be ridden and assist in combat |
| 10 | Wild Wyvern | Dangerous flying reptile with poison breath; rare tameable variant |
| 11 | Cave Basilisk | Cave predator that applies slowing and petrification-like effects |
| 12 | Crystal Spider | Glowing spider that creates crystal projectiles and webs |
| 13 | Shadow Wraith | Undead spectral enemy that phases visually and uses dark magic |
| 14 | Grave Knight | Undead armored warrior with sword combos and defensive stances |
| 15 | Flame Imp | Small flying demon that launches fire projectiles |
| 16 | Frost Elemental | Ice creature using frost waves and ice spikes |
| 17 | Moon Stag | Rare, peaceful, magical deer that can be tamed and ridden |
| 18 | Slime Maiden | Anime-inspired slime spirit with bouncing movement and magical abilities |
| 19 | Harpy | Flying humanoid monster with aerial swoops and ranged feather attacks |
| 20 | Demon Sorceress | Dark fantasy magical enemy using purple energy, curses, and teleportation |

### Creature quality rules

Every creature must feel like a distinct species, not simply a reskinned zombie.

Implement:

- Unique health, damage, speed, size, and defense
- Appropriate movement and navigation
- Aggressive, neutral, or peaceful behavior
- Distinct idle and movement animations
- Combat animations where applicable
- Appropriate death animation or death-state visuals
- Attack cooldowns and telegraphs
- Functional loot tables
- Spawn egg
- English display name
- Natural biome spawning
- Appropriate sounds and particles
- Multiplayer-safe behavior

Create actual functional implementations for all 20 creatures.

Do not satisfy this requirement by registering 20 names that all use the same unchanged model or AI.

## 4. Custom 3D models and visual design

Create actual Minecraft-compatible 3D creature assets.

Use a coherent style inspired by medieval fantasy, high fantasy, and dark fantasy.

Models should look professional while retaining the block-based Minecraft visual style.

### Model requirements

- Unique silhouette for every creature
- Correct proportions, pivot points, UV mapping, and texture coordinates
- Distinct heads, limbs, bodies, and creature-specific details
- Animated body parts with properly defined bones
- Correct entity shadow sizes and visual scales
- No missing-texture purple/black placeholders
- Proper lighting and transparent texture handling
- Normal and emissive textures where appropriate

Create real GeckoLib model JSON files, animation JSON files, and texture PNG files.

Prefer providing editable Blockbench project files as well.

Models must not be empty placeholders.

Use shared model-building utilities or reusable geometry templates where appropriate, but individual models must remain visually distinct.

### Visual effects

Examples:

- Goblin Shaman: swirling green particles
- Treant: falling leaves and moving roots
- Griffin: feather particles while flying
- Wyvern: poisonous breath clouds
- Crystal Spider: glowing crystal particles
- Wraith: dark smoke and spectral transparency
- Flame Imp: flame particles
- Frost Elemental: ice shards and cold mist
- Demon Sorceress: purple runes and magic circles

Particles should use performant, distance-aware emission and must not overwhelm the client.

## 5. Animation system

Use the GeckoLib API compatible with Minecraft 1.21.10.

Implement the following animation states where relevant:

- Idle
- Walk
- Run
- Fly
- Hover
- Attack
- Heavy attack
- Magic casting
- Taking damage
- Death
- Sleeping
- Sitting
- Taming
- Riding

Not every creature needs every animation, but every creature needs appropriate functioning animations.

Create smooth transitions and sensible animation priorities.

Important:

**Do not merely name animations in Java that do not exist in the assets.**

Ensure all animation references resolve to actual files and animation definitions.

Animations should synchronize correctly in multiplayer.

Avoid restarting animations on every entity tick.

## 6. Combat and Better Combat integration

The mod must work alongside Better Combat for Fabric 1.21.10.

Important technical distinction:

Better Combat primarily modifies player weapon combat. Do not assume that installing Better Combat automatically provides custom attack animations for every new mob.

Implement creature combat using supported Fabric/Minecraft entity APIs, with GeckoLib for creature-specific attack animations.

Ensure:

- Creatures can be hit correctly by Better Combat weapons
- Entity hitboxes are accurate
- Knockback works
- Damage sources are handled correctly
- Combat does not interfere with Better Combat player animations
- Mob damage is performed server-side
- Attack visuals correspond to actual hit timing
- Friendly creatures do not accidentally attack their owners
- Better Combat is optional rather than required

If the mod includes creature weapons that players can obtain, add supported Better Combat weapon-attribute JSON definitions with appropriate presets for swords, spears, axes, and staffs.

Use the weapon-attribute format appropriate for the installed Better Combat version.

Do not implement incompatible custom player combo systems.

Test with and without Better Combat installed.

## 7. Intelligent creature AI

Build reusable AI components rather than duplicating large sections of code for every mob.

Implement behaviors such as:

**Melee enemies**
- Search for valid targets
- Chase and attack
- Respect attack cooldowns
- Use melee range appropriate to model size
- Navigate around obstacles
- Avoid permanently getting stuck

**Ranged enemies**
- Maintain suitable attack distance
- Aim at targets
- Cast projectiles
- Retreat or reposition when threatened
- Respect line of sight

**Flying creatures**
- Fly over obstacles
- Approach and leave targets
- Land when appropriate
- Avoid uncontrolled endless circling
- Handle unloaded chunks safely

**Neutral creatures**
- Wander naturally
- React to nearby threats
- Defend themselves
- Return to normal behavior afterward

**Tamed creatures**
- Follow their owner
- Sit or stay when commanded
- Defend their owner
- Avoid targeting allies
- Remember their owner after world reload

Use stable, performant AI goals and avoid executing expensive world searches every tick.

## 8. Taming, mounts, and riding

Implement a complete creature taming and riding system.

Primary tameable mounts:

1. Griffin
2. Dire Wolf
3. Moon Stag
4. Rare tameable Wyvern

Each mount should have its own taming item or method.

Features:

- Taming success chance
- Owner UUID persistence
- Tamed/untamed visual distinction
- Follow and stay commands
- Healing with appropriate food
- Mount interaction
- Mount health and damage
- Rideable movement
- Dismounting
- Safe rider positioning
- Multiplayer synchronization

### Flying mounts

For Griffins and tameable Wyverns, implement controllable flight.

Required:

- Takeoff
- Landing
- Ascend and descend controls
- Forward movement and turning
- Reasonable acceleration and speed
- Fall-damage handling
- Server-validated flight controls

Flying mounts must not provide unrestricted client-controlled teleportation or movement.

Keep mounted movement compatible with normal multiplayer gameplay.

## 9. Magic system

Implement a lightweight internal creature-magic system.

This should support:

- Fire projectiles
- Ice projectiles
- Poison breath
- Dark energy
- Healing
- Root attacks
- Crystal attacks
- Magical shields
- Area attacks
- Teleportation

Create reusable spell/action classes and visual-effect utilities.

Each magical attack should include:

1. Cast condition
2. Windup
3. Animation
4. Particle effect
5. Sound
6. Server-side effect
7. Cooldown

Balance attack power against vanilla survival.

Avoid excessive particle spawning and unnecessary networking traffic.

## 10. Spawning and world-generation compatibility

Creatures should spawn naturally in suitable biomes.

Suggested distribution:

| Environment | Creatures |
|---|---|
| Forests | Treants, Dryads, Dire Wolves |
| Plains | Goblins, Moon Stags |
| Mountains | Griffins, Minotaurs |
| Caves | Trolls, Basilisks, Crystal Spiders |
| Swamps | Slime Maidens, Goblin Shamans |
| Dark forests | Wraiths, Grave Knights |
| Snowy biomes | Frost Elementals |
| Nether | Flame Imps, Demon Sorceresses |
| High cliffs and mountains | Harpies, Wyverns |

Use biome tags and data-driven spawn configuration where possible.

Compatibility goals:

- Vanilla world generation
- Tectonic
- Terralith
- Other biome and terrain mods

Do not hardcode assumptions about terrain height or biome placement that would break Tectonic terrain generation.

Make spawning configurable:

- Enable/disable each creature
- Spawn weights
- Minimum/maximum groups
- Spawn frequency
- Dimension restrictions
- Biome restrictions
- Rare-creature settings

Do not create excessively dense hostile spawning.

## 11. Structures and dungeons

Add exploration structures without requiring boss encounters.

Implement at least four structure concepts:

**Abandoned Goblin Watchtower**
- Found in suitable overworld biomes
- Goblin Scout and Shaman inhabitants
- Small loot containers

**Forgotten Forest Shrine**
- Overgrown magical structure
- Dryad or Treant encounters
- Magical ingredients and ancient relics

**Ruined Grave Crypt**
- Underground or partially buried structure
- Wraiths and Grave Knights
- Undead-themed loot

**Wyvern Nest**
- Rare elevated nest in mountain biomes
- Wyvern encounters
- Rare eggs or taming-related resources

Use proper Minecraft world-generation structures and structure sets.

Respect existing terrain and other structures.

Do not generate entire structures using expensive chunk-load callbacks.

All loot must be functional and reasonably balanced.

## 12. Items and progression

Introduce a modest collection of creature-related items:

- Monster materials
- Magical essences
- Rare creature drops
- Taming foods
- Griffin saddle
- Wyvern saddle or harness
- Magical crafting components
- A small number of fantasy weapons
- Decorative trophies or relics

Every item must have:

- Valid registered ID
- Texture and model
- English name
- Appropriate creative-tab access
- Functional recipe or loot source where relevant

Do not add hundreds of unnecessary items.

Prioritize quality over quantity.

## 13. Architecture and code organization

Use a maintainable architecture.

Suggested package structure:

`com.mythicrealms.creatures`

- `registry` — entities, items, sounds, particles, blocks, attributes
- `entity` — individual creature classes
- `entity.ai` — reusable AI goals and behaviors
- `entity.combat` — attack helpers, damage and cooldown logic
- `entity.mount` — taming, riding, movement
- `magic` — spell system and projectiles
- `client` — client initialization
- `client.model` — GeckoLib model classes
- `client.renderer` — creature renderers
- `client.animation` — animation utilities
- `client.particle` — visual effects
- `network` — server/client packets and handlers
- `world` — biome spawning and structures
- `config` — configuration loading and validation
- `compat` — optional Better Combat integration
- `util` — shared utilities

Separate common/server code from client-only classes.

Dedicated servers must never attempt to initialize client renderers or Minecraft client classes.

Create resource directories for:

- Creature geometry
- Animations
- Textures
- Sounds and sound registration
- Language files
- Loot tables
- Recipes
- Tags
- Structures
- World generation
- Better Combat weapon attributes

All resources must follow the actual loading conventions for Fabric 1.21.10 and the chosen GeckoLib version.

## 14. Gradle and project setup

Create all necessary project files:

- `settings.gradle`
- `build.gradle`
- `gradle.properties`
- `gradlew`
- `gradlew.bat`
- Gradle wrapper files
- `fabric.mod.json`
- `README.md`
- `.gitignore`
- `LICENSE`
- Source and resource directories

Use appropriate dependency repositories.

Declare:

- Minecraft 1.21.10
- Fabric Loader
- Fabric API
- GeckoLib for Fabric 1.21.10
- Optional Better Combat integration

Ensure the generated source JAR and normal distributable mod JAR are correctly configured.

Do not include optional development dependencies as mandatory runtime requirements.

## 15. Networking and multiplayer

All gameplay-critical systems must be authoritative on the server.

Implement safe synchronization for:

- Creature attack states
- Magic casting
- Taming
- Owner information
- Mount movement
- Mount commands
- Special effects
- Creature animation triggers

Use the networking APIs supported by Fabric 1.21.10.

Validate client packets.

Never trust unvalidated client-provided entity IDs, positions, targets, attack damage, or permissions.

Avoid sending large amounts of data every tick.

Test with a dedicated server as well as singleplayer.

## 16. Configuration and performance

Create editable configuration for:

- Creature spawn rates
- Individual creature enable/disable settings
- Creature difficulty multipliers
- Magic particle intensity
- Mount movement speed
- Mount flight speed
- Taming difficulty
- Structures
- AI update intervals

Provide reasonable defaults.

Prioritize smooth gameplay with 20 different creature types active.

Do not use expensive global entity scans every tick.

Use appropriate tracking distances, AI scheduling, entity cleanup, and client-side animation management.

Optimize without removing visual quality.

## 17. Implementation workflow — mandatory

You are not allowed to stop after producing an architecture plan.

Follow this implementation process:

### Phase 1 — Project initialization

1. Inspect the repository and existing files.
2. If the repository already contains a mod, preserve unrelated work.
3. If it is empty, create a complete Fabric project.
4. Resolve dependency versions.
5. Configure Gradle.
6. Create mod initialization and registrations.
7. Run the build and fix errors.

### Phase 2 — Core systems

Implement the reusable entity framework, registries, AI, magic, spawning, networking, renderers, configuration, and taming infrastructure.

Compile before proceeding.

### Phase 3 — Creature implementation

Implement all 20 creatures.

Work in manageable groups:

- Group A: Goblin Scout, Goblin Shaman, Orc Warrior, Minotaur, Stone Troll
- Group B: Ancient Treant, Forest Dryad, Griffin, Dire Wolf, Wild Wyvern
- Group C: Cave Basilisk, Crystal Spider, Shadow Wraith, Grave Knight, Flame Imp
- Group D: Frost Elemental, Moon Stag, Slime Maiden, Harpy, Demon Sorceress

For each group:

1. Implement entities and AI.
2. Create distinct model and texture assets.
3. Create appropriate animations.
4. Add spawn rules and loot.
5. Register spawn eggs.
6. Test asset loading and compilation.
7. Fix detected issues before continuing.

Do not mark a creature complete until its code and necessary resources exist.

### Phase 4 — Gameplay systems

Implement:

- Magic attacks
- Taming and ownership
- Riding controls
- Flying mounts
- Creature drops
- Crafting
- Better Combat integration

### Phase 5 — World generation

Implement biome spawning, structures, loot tables, and compatibility-sensitive world generation.

### Phase 6 — Integration and testing

Run:

`./gradlew clean build`

Also use the appropriate development client and server tasks when available.

Test at minimum:

- Game initialization
- Entity registration
- Spawn eggs for all 20 creatures
- Natural spawning
- Entity AI and combat
- Renderer/model loading
- Animation transitions
- Taming and saving/loading
- Riding and flying
- Projectiles and damage
- Loot tables
- Structure generation
- Compatibility with Better Combat
- Dedicated-server startup

If the environment cannot launch Minecraft, complete all runnable static/build tests and state which runtime tests remain unverified.

Fix compilation errors rather than leaving them for the user.

## 18. Quality standards and acceptance criteria

The mod is complete only when:

- All 20 creatures are registered and have meaningful functionality.
- Each creature has a distinct actual 3D model and texture.
- Appropriate animations load without errors.
- Creature AI functions.
- Magic attacks work.
- Mounts can be tamed and ridden.
- Flying mounts have safe, controllable movement.
- Natural spawning works in appropriate biomes.
- Structures generate and contain functional loot.
- The mod can load without Better Combat.
- Better Combat compatibility has been implemented and tested wherever the environment allows.
- The project compiles for Fabric 1.21.10.
- No unresolved references or missing assets remain.
- All game content is in English.
- The README explains installation, dependencies, commands, and configuration.

Never report an untested feature as verified.

## 19. Deliverables

Provide:

1. Complete editable source code.
2. All required assets.
3. Functional Gradle project.
4. Compiled distributable JAR in `build/libs`, if the build succeeds.
5. README with installation instructions.
6. Creature reference list.
7. Configuration instructions.
8. Test results.
9. List of known limitations, if any.

If the repository is connected to GitHub, make changes directly in the working branch. Commit changes in meaningful groups and provide a summary of changed files.

Do not overwrite unrelated files without reason.

If the work is too large for a single execution, implement the project in working phases. Maintain a persistent progress document and continue from the last verified state rather than restarting the project.

Do not replace unfinished systems with fake stubs just to satisfy a build.

## 20. Final instruction

**START IMPLEMENTING NOW.**

Do not respond with only suggestions, a roadmap, or pseudocode.

Inspect the actual environment, establish the working Fabric 1.21.10 project, write the required source and asset files, run the available build/test commands, fix failures, and continue implementing the 20-creature mod.

Prioritize professional quality, distinct creature designs, reliable gameplay, performance, and multiplayer compatibility.

Bosses are not necessary. Spend that development effort on making the 20 normal creatures significantly better.

Only report completion when the corresponding files and functionality genuinely exist.