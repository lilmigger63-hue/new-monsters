# Asset refinement validation — 1.1.0-rc.2

Base:29cc858, branch `feat/asset-refinement`. [Changes by creature](REFINEMENT_CHANGES.md) · [Before preview](CLIENT_PREVIEW.jpg) · [Updated in-game preview](REFINEMENT_PREVIEW.jpg) · [Source/permission audit](ASSET_ATTRIBUTION.md).

| Check | Result |
|---|---|
| Existing and overhaul asset/export suites | 6 PASS |
| Dedicated server, base | 40/40 PASS |
| Dedicated server, Better Combat | 40/40 PASS |
| Actual base client | PASS,20 species/222 fresh screenshots, real mounted flight and server death/removal |
| Actual Better Combat client | PASS,20 species/222 fresh screenshots, real mounted flight and server death/removal |
| Final clean build and JUnit | PASS, all 11 tasks executed;5 JUnit tests pass |
| Frozen gameplay/renderers and finished Spider/Imp assets | 156 files byte-identical to base |
| Legacy generator reproduction | 346 files byte-identical before/after regeneration |
| Rig/clip preservation | All 20old bone IDs and clip names retained |
| Intended normal textures | All 18changed;2 finished creatures unchanged |
| Model complexity | Maximum129 cubes |

All 20 species were visually reviewed across front/side/back/distant, attack, and six playback probes (walk/run/heavy/cast/hurt/death). No clear new face clipping, detached parts or weapon attachment defects were found in sampled frames. Moon Stag's full idle images show hooves meeting the ground; Sorceress casting sigils remain visible. Static samples do not certify every transition, jitter-free full animation cycles or all riding/terrain combinations. Authoring notes distinguish original baseline inspection from this fresh integration review.

No Java gameplay/renderer, entity IDs, attributes, spawning/loot/recipes, ownership, sounds, effects or dependency changes were needed. The version property is the only build-configuration change. Stag's original idle saddle/attachment is retained; its new visual leg rig compensates hoof orientation. Existing attack timings and0.65 second death lengths remain.

Evidence: `/workspace/validation/refinement/` contains raw server/client logs, screenshots under `client-base`/`client-better-combat`, `review-sheets`, `visual-review.md`, `baseline.json`, `guard-results.json`, `model-diff.json` and `regeneration.json`. Final concise transcripts/XML are stored in `docs/test-results/1.1.0-rc.2-*`.

Executed workflow: `python3 scripts/test-assets.py`; `python3 scripts/test-overhaul-assets.py`; `python3 scripts/cloud-gradle.py --no-configuration-cache build runGametest` (also `-PwithBetterCombat`); `bash scripts/client-smoke.sh` (also `-PwithBetterCombat`). Final delivery uses `python3 scripts/cloud-gradle.py --no-configuration-cache clean build` after preserving client evidence.

## Source limits

All six supplied source pages were blocked by proxy CONNECT 403 before content/license inspection. No external model, animation, texture or accessory was downloaded, copied or claimed to have a verified license. The explicit original-replacement fallback was used for all 18 refinements. No Fossils and Archeology JAR was attached/found, so its internals were not inspected/copied. Source details and null file-license/hash fields are recorded in `asset-sources.json`.

Xvfb/software OpenGL establishes real in-game rendering, not hardware FPS. Mojang online services and an audio device are unavailable. Long-duration survival, unusual terrain, large creature packs and unrelated mod combinations remain manual checks. Stable `main` is preserved; this candidate is provided on its feature branch.

Candidate archive checks passed: JAR version1.1.0-rc.2,54Java21classes byte-identical to rc.1, all packaged Spider/Imp resources identical,20native projects in source ZIP, CRC-valid archives and three-JAR dependency bundle. Required dependency SHA512 hashes were verified against the existing authoritative metadata; SHA256 sums accompany all downloads.
