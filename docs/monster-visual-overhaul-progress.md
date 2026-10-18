# Sequential monster visual overhaul V3

Baseline: `50dfab973a053e6c6761f45771e72c898f3963d4`. Completed in order: **harpy, forest_dryad, slime_maiden, minotaur, vampire, valkyrie, succubus, ender_dragon_girl, centaur**. Last completed: **Centaur**. Continue the next requested creature only after committing this stage.

Reference labels below follow the requested order, not physical attachment filenames: inline images have no supplied filenames. Cyclops uses the earlier conversation image (blue armor, one eye, polearm); that image was not repeated in the latest message. Fox reference is Nine Tails; Ashen Wing Girl is Werecat (confirmed wingless), preserving IDs `fox_spirit_girl` and `werecat`.

| Order | Creature / ID | Reference | Stage | Model | Texture | Animation | Visual review | Build/test | Commit | Remaining issues |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | harpy | conversation image1; no local filename | Complete | 162 cubes/30 bones | Original128×128 | 11 clips; timing unchanged | Six passes; final states inspected | Client/build +18 asset tests pass | 84ec9ce | Hair/posed-reference and still-frame limits documented |
| 2 | forest_dryad | conversation image2; no local filename | Complete | 124 cubes/29 bones | Original128×128 | Eight clips; cosmetic death support fixed | Four passes inspected | Client/build +19 asset tests pass | 23fb1e2 | Original hidden-back/lighting and still-frame limits |
| 3 | slime_maiden | conversation image3; no local filename | Complete | 80 cubes/33 bones | Original green gel atlas | Cosmetic gait/death; timing preserved | Three passes inspected | Client/build +20 asset tests pass | 1f493b6 | Original cropped-foot/back and still-frame limits |
| 4 | minotaur | conversation image 4 (no local filename) | Complete | 115 cubes/22 bones | Original brown fur/metal | Ten clips unchanged | Two passes +impact poses inspected | Client/build +20 asset tests pass | 9391176 | Posed-reference/hidden-back and still-frame limits |
| 5 | vampire | conversation image 5 (no local filename) | Complete | 138 cubes/28 bones | Original blonde/crimson atlas | Nine clips unchanged | Two passes +impact poses inspected | Client/build +20 asset tests pass | 054cbfd | Rigid coat/hidden-back and still-frame limits |
| 6 | valkyrie | conversation image 6 (no local filename) | Complete | 177 cubes/32 bones | Original silver/blonde/black feather | 13 clips unchanged | Three passes +flight/impact inspected | Client/build +20 asset tests pass | c2f14b6 | Original hidden back/rigid armor and still-frame limits |
| 7 | succubus | conversation image 7 (no local filename) | Complete | 136 cubes/37 bones | Original blonde/black/red membrane | Cosmetic death folded; 12 clips unchanged | Four passes +flight/impact inspected | Client/build +21 asset tests pass | fbeff26 | Original membrane/back and still-frame limits |
| 8 | ender_dragon_girl | conversation image 8 (no local filename) | Complete | 131 cubes/35 bones | Original black/gray/pale/violet | Death-only cosmetic adaptation | Two passes +flight/impact inspected | Client/build +21 asset tests pass | 4ff1c9f | Original membrane/back and still-frame limits |
| 9 | centaur | conversation image 9 (no local filename) | Complete | 131 cubes/30 bones | Original V3 atlas | Eight clips unchanged | 2 passes inspected | Client/build +21 asset tests pass | Visual overhaul: Centaur reference accuracy | Original hidden-back/lighting and still-frame limits |
| 10 | fox_spirit_girl | conversation image 10 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |
| 11 | anubis | conversation image 11 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |
| 12 | kobold | conversation image 12 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |
| 13 | cyclops | conversation image 13 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |
| 14 | dhampir | conversation image 14 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |
| 15 | sahuagin | conversation image 15 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |
| 16 | holstaurus | conversation image 16 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |
| 17 | werecat | conversation image 17 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |

Next step: commit this validated stage, then inspect the next creature in the requested order. No later creature has been edited.

Cloud resume: run Gradle/client commands with `--offline --init-script /workspace/toolchains/retained-minecraft-metadata.gradle`; `/workspace/toolchains/prepare-retained-minecraft.py` verifies the retained original metadata and artifacts. Run only one Gradle process at a time.
