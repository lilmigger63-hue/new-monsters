# Visual overhaul progress

## Phase 1 — Goblin Scout proof

Implemented a named rigid `grip_right` socket under `hand_right`, with dagger child attachment and three curled fingers plus opposing thumb around the handle. Shortened hilt remains under the guard, with pommel below the fingers. Rebuilt cranial cap and temple planes using original geometry and existing painted UV tiles. Existing 11 clips, attack impact at 7 ticks, gameplay, hitbox and palette preserved. Model: 20 bones / 67 cubes. Exported matching native Blockbench project.

Texture and animation files are unchanged: this is a grip/head proof, not a claim of a completed new species redesign. Existing arm/wrist animation drives the entire attachment without independent socket drift.

## Remaining

- Scout front/side/back/attack screenshots inspected: no visible new detached dagger or missing geometry. Full-cycle gait, foot plants and final art acceptance remain open.
- Phase 2: remaining Group A; particularly two-handed Minotaur axe and weight-bearing foot plants.
- Phase 3: seven organic species; assess ground contact and flight transitions against supplied requirements.
- Phase 4: six distinct adult female species and hair/cloth motion.
- Phase 5: full variants/optional Better Combat regression, per-species acceptance grid, fresh release artifact.
- All 18 retain their earlier rc.2 assets except this Scout proof. Crystal Spider and Flame Imp remain untouched.

## Reference limitation

Full uploaded brief and metadata preserved in `visual-overhaul-input/`. Source Forge JAR not supplied; linked wiki blocked by proxy HTTP 403. Inventory used only for technical context, never treated as inspected visual evidence. No copied third-party assets or new dependency.

## Checks

- `python3 scripts/test-assets.py`: 2 PASS.
- `python3 scripts/test-overhaul-assets.py`: 5 PASS, including rigid grip hierarchy protection.
- Repeat Group A export: 347 resources/native files byte-identical.
- `python3 scripts/cloud-gradle.py --no-configuration-cache build runGametest`: PASS; 5 JUnit tests and 40 required server game tests.
- Before/after actual-game comparison: [Scout comparison](visual-overhaul-scout-comparison.jpg).
- Base client smoke: PASS, all 20 entities, 222 fresh screenshots, server death/removal and actual Griffin mount flight. Evidence: `/workspace/validation/visual-overhaul/client-base/`.
- Better Combat was not rerun for this checkpoint; earlier rc.2 evidence does not certify this change.
- Static views do not establish full-cycle gait or transition quality. No final release artifact created for this partial checkpoint.
