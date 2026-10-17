# Mythic Realms: Creatures Implementation Plan

Goal: implement the complete Fabric 1.21.10 mod specified in REQUIREMENTS.md.
Architecture: common server-authoritative entities and reusable combat/magic/mount systems; isolated client GeckoLib renderers; data-pack world generation.
Constraints: Java 21, official Mojang mappings, GeckoLib 5 exact-version API, optional Better Combat, English content, no bosses, no fake completion.
Execution: inline on the existing working branch, as requested.

- [ ] Phase 1: initialize from official Fabric 1.21.10 template, resolve published dependencies, compile and boot dedicated server.
- [ ] Phase 2: tested combat clock, config, registries, AI, spells, networking and renderer framework. Compile before creature work.
- [ ] Phase 3A–D: four five-creature groups in request order; each includes distinct geometry, textures, animations, behavior, spawning, loot and eggs. Build and check asset references per group.
- [ ] Phase 4: persistent taming, owner-safe combat, authoritative riding and bounded flight inputs; multiplayer tests.
- [ ] Phase 5: four proper structures and structure sets, loot and terrain placement checks.
- [ ] Phase 6: materials, taming foods, equipment, recipes and optional Better Combat weapon data.
- [ ] Phase 7: client and server tests, all 20 creatures, with/without Better Combat, packaged JAR and honest limitations.

Review focus: malformed configuration; allied/owner targeting; invalid/replayed mount packets; dedicated-server class loading; missing assets and terrain-mod compatibility.
Verification: ./gradlew build; dedicated-server startup and gameplay smoke tests; client visual checks; focused Java combat tests. Never equate static tests with gameplay validation.
