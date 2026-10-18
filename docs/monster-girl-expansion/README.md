# Monster Girl Expansion — 1.2.0-rc.1

Fabric / Minecraft 1.21.10 / Java 21. Loader, Fabric API, GeckoLib and optional Better Combat versions remain unchanged. This candidate adds 13 entities to the existing 20; it does not replace or rename saved original entities.

## Species and gameplay

| New species / ID | Initial reusable AI | Natural habitats |
| --- | --- | --- |
| Ender Dragon Girl `ender_dragon_girl` | Demon caster | end_highlands, end_midlands, small_end_islands |
| Vampire `vampire` | Scout melee | dark_forest, taiga |
| Holstaurus `holstaurus` | Slime guardian | plains, sunflower_plains, meadow |
| Centaur `centaur` | Scout melee | savanna, plains, forest |
| Sahuagin `sahuagin` | Scout melee | ocean, lukewarm_ocean, deep_ocean, river |
| Valkyrie `valkyrie` | Scout melee | jagged_peaks, frozen_peaks, stony_peaks |
| Nine-Tailed Fox Spirit `fox_spirit_girl` | Shaman caster | cherry_grove, old_growth_pine_taiga, forest |
| Anubis `anubis` | Scout melee | desert, badlands |
| Kobold `kobold` | Scout melee | dripstone_caves, lush_caves, windswept_gravelly_hills |
| Cyclops `cyclops` | Scout melee | windswept_hills, stony_peaks |
| Dhampir `dhampir` | Scout melee | dark_forest, old_growth_spruce_taiga |
| Succubus `succubus` | Demon caster | crimson_forest, soul_sand_valley |
| Werecat `werecat` | Shaman caster | taiga, snowy_taiga, grove |

Ender Dragon Girl uses the End; Succubus uses the Nether; the other new species use the Overworld. Hostile light/difficulty checks and configured rarity apply. Sahuagin uses water placement, amphibious paths and underwater breathing. Holstaurus uses a neutral guardian profile. Scout-based species remain melee combatants; decorative weapons do not imply an unimplemented ranged attack. Winged caster presentation is adapted to the existing Demon caster profile, rather than introducing new aerial boss AI.

Only **Forest Dryad** and **Slime Maiden** of the original 20 retain natural spawning. All 13 new species have eligible biome registrations. The other 18 original species have empty habitat tags, no biome registration and an explicit natural/chunk-generation reason guard even with legacy configuration flags. Generated structure inhabitants follow the same rule. Existing saved creatures, eggs, summons, taming and other original mechanics remain available. Structure blocks and loot remain intact.

## Art and references

All 13 species have original optimized cube rigs, UV textures, GeckoLib animation JSON, custom symbolic eggs and editable Blockbench files. The four existing visual revisions preserve their original animation files byte for byte. Crystal Spider, Flame Imp and the remaining original visuals are preserved. The Werecat has no wings, following the explicit reference clarification. Harpy uses the separately supplied wing image for wing anatomy while retaining her adult feminine form. Fox Spirit has nine articulated tails; Cyclops has one central eye; Centaur has four horse legs.

[Shared-system optimization and measurements](OPTIMIZATION.md) · [Complete asset sources and license audit](ASSET_INVENTORY.md) · [AI implementation](AI.md) · [Original preservation evidence](EXISTING_VISUALS.md) · [User specification](REQUEST.md)

The seven requested external pack pages were blocked by the environment proxy before origin access. No downloadable pack or license could be inspected, so no external pack files were integrated. The supplied Grimoire JAR has all-rights-reserved assets and is reference-only. All delivered new artwork was authored in this repository under its CC0 license.

## Validation

The final optimized build passed **51 server GameTests without Better Combat and 51 with Better Combat**. All **16 asset/export tests** and **14 standalone attack-timeline checks** passed. The shipped JAR contains 76 Java 21 classes and 33 complete entity resource sets, with no reference/test classes or proprietary Gaia files.

Actual graphical verification rendered and synchronized **all 33 species** after optimization. A separate full 17-species expansion run passed with Better Combat; a final optimized Werecat run also passed with Better Combat. Captures cover idle, side, back, distant, attack, walk, run, heavy, cast, hurt and held death, plus sampled flight phases for winged species, real mount flight/corpse removal and Sahuagin water poses. The final Werecat ear silhouette and connected tails were checked in the actual client. [Recorded test outcomes](../test-results/1.2.0-rc.1-validation.txt).

Initial diagnostic runs exposed missing glow-mask references, detached wing decorations/tails and overly fast Sahuagin swimming. These were corrected and retested; the initial failed images are not final approval. All four original animation files remain byte-identical, original attributes/IDs are preserved, and all 138 art files of the other 16 original species remain unchanged.

[Actual in-game contact sheets](previews/) show all 13 new and four revised species. Fox Spirit has nine articulated tail chains in the baked/native hierarchy; tail overlap prevents counting all nine independently in a single still. Harpy's preserved death pose holds her body above her low wing extremity; this existing pose was not re-authored. The source-JAR audit and external pack failures are documented separately.

Still-frame inspection cannot certify every animation interpolation frame, dynamic foot contact, all hardware or arbitrary modpacks. Gameplay tests use a local server; a long multiplayer survival session was not performed. Shared-cache optimizations retain visual detail, attacks and particle counts; the measured kernel result is not a global FPS claim.

## Rebuilding and editing

Use `python3 scripts/cloud-gradle.py --no-configuration-cache build` in the configured cloud workspace, or Java 21 with the checked-in Gradle wrapper elsewhere. The three `tools/generate_expansion_*.py` scripts recreate owned new assets; Pillow and NumPy are offline art-tool dependencies, not Minecraft runtime dependencies. Do not regenerate unrelated art when editing one species.
