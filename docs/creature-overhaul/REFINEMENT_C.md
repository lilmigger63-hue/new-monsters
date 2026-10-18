# Basilisk, Wraith and Knight refinement

All changes are original geometry, material-role assignments and motion authored for these existing creatures. Entity IDs, colors, world dimensions, gameplay and the shared exporter are unchanged. Crystal Spider and Flame Imp are finished assets and were excluded from export; a SHA-256 guard verified all 38 files bearing those names remained byte-identical.

| Creature | Inspected actual client baseline | Refined result |
| --- | --- | --- |
| Cave Basilisk | `0110_creature-cave_basilisk-idle.png`: broad flat snout and jaw, flat flank transitions, abrupt leg/foot junctions. | Retains low green reptile silhouette, existing eyes, teeth, dorsal ridge and tail. Adds inset nostrils, lower mandible rim, cheek shields, staggered flank scales, ankle cuffs, visible joint pads and progressively smaller tail scutes. Scale material now continues across cheeks/joints. Counter-moving feet and restrained neck/jaw motion add secondary anatomy movement without changing attack windup. |
| Shadow Wraith | `0132_creature-shadow_wraith-idle.png`: blank dark hood interior with two glowing bars; uninterrupted cloth chest. | Retains original floating shroud, hood, spectral claws, wisps and cool palette. Recessed tapered adult female spectral face has bounded teal eyes, pupils, brow expression, subtle nose/mouth and layered silver-blue hair. Folded neckline, waist seam and side pleats refine cloth transitions. Hair and terminal wisps move gently during floating; shroud/hair follow attacks with a small lag. No human legs, unrelated costume or ordinary human skin is introduced. |
| Grave Knight | `0143_creature-grave_knight-idle.png`: full bar visor masks identity; large unsegmented breastplate and gauntlets. | Retains helmet/crown, plate silhouette, sword, forearm guard and split cape. Existing helmet becomes an open visor recess containing an adult female anime-inspired cool ivory face, defined mint eyes, pupils/brows and restrained expression. Silver hair sits within cheek guards and moves subtly. Overlapping waist lames, gauntlet fingers and shin inlays refine armor transitions. Hair/cape action follow-through preserves sword hierarchy and original attack windups. |

Baseline screenshots are in `/workspace/validation/overhaul/client-base/screenshots`. Those images describe the pre-refinement client state; they are not presented as proof of new in-game appearance. New exports still require client screenshot review for subjective readability and animation clipping under all poses.

## Source use and fallback

The source audit reports proxy CONNECT HTTP 403 for all six requested source sites; no file-level licensed download was available. Consequently no downloaded model, texture, animation, copyrighted jar geometry or external pixels were copied into this group. These are independently authored refinements of the existing builders. See `ASSET_ATTRIBUTION.md` and `asset-sources.json` for the repository-wide source audit. This follows the user's explicit original replacement fallback when downloads or legal reuse are blocked.

## Export and validation

Only the three assigned builders were exported with the existing pipeline. The checked-in group C entry point has matching per-creature material roles, so future regeneration reproduces them. Existing shared functions and Spider/Imp builders were untouched.

- Cave Basilisk: 15 bones, 73 cubes, 8 clips.
- Shadow Wraith: 23 bones, 50 cubes, 10 clips.
- Grave Knight: 17 bones, 75 cubes, 10 clips.
- Native Blockbench geometry, embedded texture and animation parity validated by the exporter and existing tests.
- `python scripts/test-overhaul-assets.py`: 4 tests passed.
- `python scripts/test-assets.py`: 2 tests passed.
- All three exported death clips finish at 0.65 seconds through the existing exporter. Existing primary attack contact timing is preserved; follow-through is secondary motion only.
- Crystal Spider/Flame Imp: 38-file byte guard passed.

No Java, dependencies, Gradle settings, gameplay or tests were edited. No Gradle or new in-game run was performed by this asset-only task.

Final integration: both actual client profiles and both40-test server profiles passed. Fresh visual samples were reviewed; see [refinement validation](REFINEMENT_VALIDATION.md) for scope and remaining manual checks.
