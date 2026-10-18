# Mythic Realms: Creatures implementation record

Target: the complete [Fabric 1.21.10 specification](REQUIREMENTS.md), continuing the existing working branch.

- [x] Initialize the Java 21/Fabric project, resolve actual published dependencies, compile and boot the dedicated test server.
- [x] Build reusable server-authoritative combat, AI, magic, configuration, synced animation and rendering systems.
- [x] Complete all four five-creature groups with distinct geometry, textures, animations, behavior, spawning, loot and eggs.
- [x] Provide persistent taming, owner-safe targeting, four rideable species and bounded flying mounts using vanilla server input packets.
- [x] Add four terrain-relative jigsaw structures, structure sets, persistent inhabitants and usable loot.
- [x] Add twenty-six progression items, fourteen recipes and optional Better Combat presets.
- [x] Run clean build, five JUnit tests, two asset tests and thirty-four server GameTests. Test server and actual graphical client with/without Better Combat, including real keyboard-controlled Griffin flight.
- [x] Package the remapped playable JAR, source JAR and complete editable source; document validation limits.

Detailed commands, reports, defects resolved and historical milestones are in [PROGRESS.md](PROGRESS.md). External multi-player latency, long-session balance/performance and Terralith/Tectonic installations remain untested. These limitations do not replace implemented content with stubs.
