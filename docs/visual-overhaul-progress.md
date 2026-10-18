# Current V2 progress — 1.1.0-rc.3

All 18 requested model/rig/animation updates are implemented. Latest specification: [V2](visual-overhaul-input/MASTER_PROMPT_V2.md); [per-creature changes, references and evidence](overhaul-v2.md).

- Four independent original asset batches integrated, existing IDs/abilities/mounts retained.
- All five requested weapon attachments verified structurally; staff and sword no longer animate separately from palms. Minotaur support hand releases during attack and rejoins on recovery.
- Supplied images used for Wyvern dinosaur head + dragon body, Harpy feather wings and Megaloceros Stag antlers.
- Crystal Spider/Flame Imp unchanged. All 18 runtime model/animation hashes differ from uploaded rc.2 baseline; texture atlases reused as original painted materials.
- Structural review fixed buried Knight carry sword. Actual-game review fixed Harpy death burial and Griffin resting wing fold. Fresh target captures confirmed corrections.
- 12 asset checks passed; base and optional Better Combat builds/server runs passed 40 game tests each. Five JUnit checks passed.
- Base client presented all 20 species; corrective Better Combat client presented four targets and baked all 20 resource/animation sets. 237 combined latest screenshots, 18 before/after comparison images.
- Performance: matched unthrottled software runs captured 100 samples each; longer 40-sample Harpy repeat showed no reproduced regression. Hardware FPS and all continuous transitions are not certified.

Final artifact is built from these source/assets and packaged under `releases/1.1.0-rc.3/`. No further species implementation is intentionally deferred. Art direction remains subject to user review; the inaccessible external websites were not falsely claimed as inspected.
