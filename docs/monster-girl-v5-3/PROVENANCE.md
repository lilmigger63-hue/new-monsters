# V5.3 provenance and environment

V5.3 builds on the project's original CC0 artwork at commit `1704f678b51d528fa9a27f727d55eb035985c45c`. Reference images are supplied inline by the user; they are visual direction, not imported texture/model data. Hidden surfaces and design details remain original project artwork. No sound work is performed.

The supplementary repository https://github.com/Silentine/GrimoireOfGaia was inspected at `ccb25833ab984652c9696b266247629f6d172f81`. Its `LICENSE.md` states: “Code (aside from /models) is public domain under Creative Commons0” and “Textures and models (Art Assets) remain under the ownership of the original creator, Silentine.” Its artwork is not imported. No Gaia code is needed for this task. Repository metadata and license were inspected in a separate temporary checkout; model/texture content was not used as authoring input.

All V5.3 geometry/UV/texture painting and cosmetic keyframes are original project source in `tools/generate_v5_3.py`. Runtime assets and native editable Blockbench projects are generated one selected active species at a time. Baseline geometry/animation and small texture snapshots support review without duplicating embedded native-project data; the original native projects are recorded by SHA256 instead. Completed stages are frozen in `state.json`.

The prior V3 tests intentionally check archived V3 geometry/textures/animation and original native hashes for these thirteen superseded artworks; the V5.3 preservation suite checks live files, the single active species and completed-stage hashes. Unrelated legacy tests continue checking live assets.

The retained Java21/Gradle/Fabric client environment is reused. `prepare-retained-minecraft.py` verifies the exact cached official1.21.10 metadata/client/server/asset index, and the existing supported offline Loom init supplies its immutable metadata URL. No dependency versions, TLS verification or checksums are changed. Client evidence is captured through Xvfb/llvmpipe; this does not measure physical GPU FPS or sound playback. Existing saved startup instructions remain applicable.
