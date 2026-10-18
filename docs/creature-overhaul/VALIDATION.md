# Overhaul validation

Work remains on `feat/creature-overhaul`; stable1.0.0/main and its downloads are unchanged. Candidate:1.1.0-rc.1, Fabric/Minecraft1.21.10, Java21.

## Verified so far

- Baseline6fb834f: build,5JUnit tests and34server GameTests PASS.
- Original asset suite:2tests PASS; overhaul exporter suite:4tests PASS, including all20 native Blockbench/PNG/clip/geometry parity, deterministic materials, invalid hierarchy/UV checks, attached tail joints, death blend/lifetime margin and eight-foot spider grounding across101samples per gait.
- All three legacy generator entrypoints regenerate346 creature-art, native-source and gameplay-data files byte-for-byte. Evidence:`/workspace/validation/overhaul/final-regeneration.json`.
- Clean build compiled candidate and passed5JUnit tests. Loom's configuration cache retained a launch argument-file path removed by `clean`; rerunning `--no-configuration-cache build runGametest` regenerated it and passed all37server tests. Run `clean` separately before launch tasks in this environment.
- First actual graphical run passed all20species resource loading, declared GeckoLib animation baking, client entity synchronization, renderer/texture checks and real integrated-player keyboard-controlled Griffin flight.201screenshots:four views plus attack/walk/run/cast/hurt/death playback. All200creature frames were visually reviewed; evidence:`/workspace/validation/overhaul/client-initial` and `review-sheets`.
- Review found detached tail tips on Griffin/Dire Wolf/Wyvern and floating Crystal Spider feet. Joint pivots and articulated stance were corrected, with reproducing regression checks. Death clips now finish within0.65s, leaving5controller-blend ticks before vanilla20tick removal. Mount flight transitions resolve once per AI tick to avoid restarting both takeoff/landing in the same tick.

## Final checks in progress

Final actual client rerun includes fresh four-view shots, six held/looping playback probes, server-triggered attacks/cast particles, a real server-death/corpse-removal check, and real player-controlled Griffin flight. Its animation probes intentionally select clips in the test client; they establish actual rendering and pose integrity, not natural AI state selection. Server GameTests exercise authoritative gameplay separately.

Optional Better Combat server/client runs and final artifact checks remain pending. A repeated stationary-target projectile regression is being investigated after one early integration run intermittently missed the Slime Maiden's projectile effect; the following37-test run passed. No failed run has been treated as a pass.

## Limits

Software OpenGL/Xvfb provides real in-game rendering, not a hardware FPS benchmark. This machine has no audio device and cannot reach Mojang online services; expected audio/auth/Realms warnings do not prevent local worlds. Manual long-duration survival, varied terrain/large packs and unrelated mod combinations remain outside the automated checks.

Reference research uses60inspected entries/42unique images with exact URLs and licensing caveats in REFERENCE_ATLAS.md/references.json. Some anatomy studies are explicitly partial analogues; no unvisited specialist references or copied third-party textures are claimed. Reference downloads remain outside the repository.
