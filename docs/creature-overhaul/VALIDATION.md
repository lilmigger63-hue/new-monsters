# Overhaul validation

Candidate **1.1.0-rc.1**, branch `feat/creature-overhaul`, Minecraft/Fabric1.21.10, Java21. Stable1.0.0/main and its published downloads remain intact. [Actual in-game preview](CLIENT_PREVIEW.jpg).

| Check | Result |
|---|---|
| Final clean build (`--no-configuration-cache clean build`) | PASS, all11tasks executed |
| JUnit: combat timing and mount flight | 5PASS |
| Asset/export suites | 6PASS, including all20native sources |
| Dedicated server, base | 40/40PASS |
| Dedicated server, Better Combat3.0.0 | 40/40PASS |
| Real graphical client, base | PASS, all20species;222screenshots |
| Real graphical client, Better Combat | PASS, all20species;222screenshots |
| Focused remote Wolf/Stag stance regression, both modes | PASS;24fresh screenshots per mode |
| Real integrated-player keyboard-controlled Griffin flight | PASS in all client runs |
| Actual server death and vanilla corpse removal | PASS in all final client runs |
| Legacy asset-generator regeneration | 346files byte-identical |
| Download JAR/archives | Version,54Java21classes,20models/animations, test-mod exclusion, dependency SHA512 and SHA256 checks verified |

Commands: `python3 scripts/cloud-gradle.py --no-configuration-cache clean build`; `python3 scripts/cloud-gradle.py --no-configuration-cache runGametest` (also `-PwithBetterCombat`); `python3 scripts/test-assets.py`; `python3 scripts/test-overhaul-assets.py`; `bash scripts/client-smoke.sh` (also `-PwithBetterCombat`). For focused stance checks add `-PclientSmokeMountStanceOnly`.

## Evidence and scope

Server XML, JUnit XML and concise graphical transcripts are committed under `docs/test-results/1.1.0-rc.1-*`. Full logs/screenshots are preserved outside build under `/workspace/validation/overhaul/`: `client-base`, `client-better-combat`, `stance-base`, `stance-better-combat`, `final-base-40.log`, `final-better-combat-server.log`, `final-delivery-build.log` and `final-regeneration.json`. The preview uses final focused images for Wolf/Stag and the full suite for the other18species.

The graphical suites check actual GeckoLib resource reload/baking of every declared clip, textures, renderers and all20synchronized entities. Full suites capture front/side/back/distant, server-triggered attack, and six animation playback probes:walk/run/heavy/cast/hurt/death. Test-only playback probes establish actual rendering/pose integrity, not natural AI selection. Authoritative combat, ownership, spawning, loot and mounting are exercised separately by GameTests. Real keyboard input reaches the integrated server and moves/raises the Griffin; real death preserves vanilla removal.

Visual review of all200initial creature stills exposed detached three-species tails and floating spider feet. Corrected joints and stance were re-rendered; regression tests cover eight transformed soles and101samples per gait. Death clips finish within0.65s, leaving a5tick blend margin. A fresh graphical assertion reproduced a stationary remote Wolf using `jump` with `onGround=false, velocity=0`; vertical-velocity gating now passes both mode-specific stance reruns.

A deterministic server regression reproduced vanilla's expanding projectile collision margin swallowing the ray start, so `AABB.clip` missed an overlapping target. A server-only fallback during margin growth reuses existing target filters and deflection handling, requires an unobstructed block ray, and passes both an explicit overlap case and a solid-wall obstruction case. Eight successive stationary-target bubbles also pass. Failed diagnostic runs were investigated; none is counted as passing.

Baseline6fb834f passed5JUnit and34GameTests before edits. An early combined clean/launch hit Loom's stale cached argument-file path; running clean separately and using `--no-configuration-cache` restored launch preparation.

## Limits

Software OpenGL/Xvfb establishes real in-game rendering, not hardware FPS. No audio device or Mojang online-service access is available; expected audio/auth/Realms warnings do not prevent local-world tests. Long-duration survival, varied terrain/large packs and unrelated mod combinations still need manual testing. No main merge or GitHub Release has been created.

Research records60inspected entries/42unique images, exact URLs and licensing caveats in REFERENCE_ATLAS.md/references.json. Some anatomy studies are explicitly partial analogues. Third-party reference pixels are not included in mod textures; reference downloads remain outside Git.
