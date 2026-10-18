# Graphical client validation

The optional `clientGametest` source set is a separate test mod and is not included in the release JAR. It uses Fabric's client GameTest runner to create a real singleplayer world. It does not start a dedicated server or accept the Minecraft server EULA.

## Run

```sh
./scripts/client-smoke-install.sh  # Debian 13 cloud instance, local install without root
./scripts/client-smoke.sh
```

The installer uses Debian's signed package index and APT's package checksum verification. Display tools are retained under `/workspace/toolchains/client-display`; system package files are unchanged. The runner uses Mesa software rendering with Xvfb when no `DISPLAY` is set. Java 21 and the Gradle dependency cache follow the repository cloud environment defaults.

The build must contain `apply from: 'scripts/client-smoke.gradle'`. This creates `runClientSmoke`, `compileClientGametestJava`, and an isolated `build/client-smoke` game directory.

## Scope

For every `CreatureKind`, the test checks GeckoLib's baked model and animation caches, the required locomotion/combat clips and every animation declared by each species, texture resource presence, an actual GeckoLib renderer, and synchronized entities in a singleplayer world. It positions the camera in front of each creature, lets idle animation run, then triggers the networked attack animation and captures another frame. Assertions and the runner's exit status determine the result; screenshots are evidence for manual visual review, not an automated artistic-quality comparison.

Screenshots are saved in `build/client-smoke/screenshots/`; the command log, Xvfb log, and OpenGL capabilities are saved in `build/client-smoke-evidence/`. A successful current run includes a `CLIENT_SMOKE_PASS` log line with the number of creature types. It also mounts a real integrated-server player on an owned, saddled Griffin, presses forward/jump through the client input helper, and verifies those packets move and raise the server-authoritative mount. The test does not validate combat balance, playback of every animation state, every rare/tamed texture, all mount species, external multiplayer latency, or long-session performance.

## Current cloud evidence

Display prerequisite probe: Xvfb starts successfully; Mesa 25.0.7 llvmpipe exposes OpenGL 4.5 core/compatibility profiles. The installer was executed twice successfully. All 4,403 unique Minecraft 1.21.10 asset objects were downloaded over HTTPS and verified against the SHA-1 values in Mojang's verified asset index (438 MB retained in the Loom cache). The harness compiles with Java 21 against the cached mapped Minecraft/Fabric/GeckoLib dependencies. Both `bash scripts/client-smoke.sh` and `bash scripts/client-smoke.sh -PwithBetterCombat` pass for all twenty species and actual keyboard-controlled Griffin flight. Each captures forty-one screenshots. Successful evidence is automatically copied outside `build/` to `/workspace/validation/client-base` or `/workspace/validation/client-better-combat`, so a clean build preserves it.

Fabric 0.138.4's test network synchronizer stalls during integrated spawn preparation in this environment. The harness uses its documented `fabric.client.gametest.disableNetworkSynchronizer` flag and explicitly waits for real client-side entity state. Use `-PclientSmokeSynchronizedNetwork` only to diagnose the original synchronized runner.
