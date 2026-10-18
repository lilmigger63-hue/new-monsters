# Sequential monster visual overhaul V3

Baseline: `50dfab973a053e6c6761f45771e72c898f3963d4`. Completed: **Harpy**. Next: **Forest Dryad** (not started until the Harpy commit). Work remains sequential; no later creature is started until the active one is validated and committed.

Reference labels below follow the requested order, not physical attachment filenames: inline images have no supplied filenames. Cyclops uses the earlier conversation image (blue armor, one eye, polearm); that image was not repeated in the latest message. Fox reference is Nine Tails; Ashen Wing Girl is Werecat (confirmed wingless), preserving IDs `fox_spirit_girl` and `werecat`.

| Order | Creature / ID | Reference | Stage | Model | Texture | Animation | Visual review | Build/test | Commit | Remaining issues |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | harpy | conversation image1; no local filename | Complete | 162 cubes/30 bones | Original128×128 | 11 clips; timing unchanged | Six passes; final states inspected | Client/build +18 asset tests pass | subject: Visual overhaul: Harpy reference accuracy | Hair/posed-reference and still-frame limits documented |
| 2 | forest_dryad | conversation image 2 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |
| 3 | slime_maiden | conversation image 3 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |
| 4 | minotaur | conversation image 4 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |
| 5 | vampire | conversation image 5 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |
| 6 | valkyrie | conversation image 6 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |
| 7 | succubus | conversation image 7 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |
| 8 | ender_dragon_girl | conversation image 8 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |
| 9 | centaur | conversation image 9 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |
| 10 | fox_spirit_girl | conversation image 10 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |
| 11 | anubis | conversation image 11 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |
| 12 | kobold | conversation image 12 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |
| 13 | cyclops | conversation image 13 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |
| 14 | dhampir | conversation image 14 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |
| 15 | sahuagin | conversation image 15 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |
| 16 | holstaurus | conversation image 16 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |
| 17 | werecat | conversation image 17 (no local filename) | Not started | pending | pending | pending | pending | pending | — | pending |

Next step: Commit Harpy, then inspect Forest Dryad; no other creature has been edited.
