# Overhaul progress

Newer candidate **1.1.0-rc.2** refines18existing designs while preserving Spider/Imp: [changes](REFINEMENT_CHANGES.md) · [validation](REFINEMENT_VALIDATION.md) · [updated preview](REFINEMENT_PREVIEW.jpg).

Candidate **1.1.0-rc.1** implemented and verified on `feat/creature-overhaul`. All20art sets, native sources and runtime integration are complete. Both server profiles pass40tests; both graphical profiles pass, with focused stance reruns. [Validation](VALIDATION.md) · [In-game preview](CLIENT_PREVIEW.jpg). Main merge and GitHub Release remain pending.

| Creature | Research | Model | Textures | Animation | VFX | Behavior | Tests |
|---|---|---|---|---|---|---|---|
| goblin_scout | 3 inspected refs | exported/native parity | original materials | integrated | physical windup | preserved/refined | assets/server/client pass |
| goblin_shaman | 3 inspected refs | exported/native parity | original materials | integrated | bounded effects | preserved/refined | assets/server/client pass |
| orc_warrior | 3 inspected refs | exported/native parity | original materials | integrated | physical windup | preserved/refined | assets/server/client pass |
| minotaur | 3 inspected refs | exported/native parity | original materials | integrated | bounded effects | preserved/refined | assets/server/client pass |
| stone_troll | 3 inspected refs | exported/native parity | original materials | integrated | bounded effects | preserved/refined | assets/server/client pass |
| ancient_treant | 3 inspected refs | exported/native parity | original materials | integrated | bounded effects | preserved/refined | assets/server/client pass |
| forest_dryad | 3 inspected refs | exported/native parity | original materials | integrated | bounded effects | preserved/refined | assets/server/client pass |
| griffin | 3 inspected refs | exported/native parity | original materials | integrated | bounded effects | preserved/refined | assets/server/client pass |
| dire_wolf | 3 inspected refs | exported/native parity | original materials | integrated | physical windup | preserved/refined | assets/server/client pass |
| wild_wyvern | 3 inspected refs | exported/native parity | original materials | integrated | bounded effects | preserved/refined | assets/server/client pass |
| cave_basilisk | 3 inspected refs | exported/native parity | original materials | integrated | bounded effects | preserved/refined | assets/server/client pass |
| crystal_spider | 3 inspected refs | exported/native parity | original materials | integrated | bounded effects | preserved/refined | assets/server/client pass |
| shadow_wraith | 3 inspected refs | exported/native parity | original materials | integrated | bounded effects | preserved/refined | assets/server/client pass |
| grave_knight | 3 inspected refs | exported/native parity | original materials | integrated | physical windup | preserved/refined | assets/server/client pass |
| flame_imp | 3 inspected refs | exported/native parity | original materials | integrated | bounded effects | preserved/refined | assets/server/client pass |
| frost_elemental | 3 inspected refs | exported/native parity | original materials | integrated | bounded effects | preserved/refined | assets/server/client pass |
| moon_stag | 3 inspected refs | exported/native parity | original materials | integrated | bounded effects | preserved/refined | assets/server/client pass |
| slime_maiden | 3 inspected refs | exported/native parity | original materials | integrated | bounded effects | preserved/refined | assets/server/client pass |
| harpy | 3 inspected refs | exported/native parity | original materials | integrated | bounded effects | preserved/refined | assets/server/client pass |
| demon_sorceress | 3 inspected refs | exported/native parity | original materials | integrated | bounded effects | preserved/refined | assets/server/client pass |

Next: review/play the downloadable candidate and review the feature branch before merging/releasing. All346generated art/gameplay files reproduce byte-for-byte. Visual defects in tail joints, spider stance, death timing and remote mount stance were corrected and verified.
