# Monster girl expansion asset and reference inventory

Inventory scope: 13 delivered original species, four existing visual revisions, the supplied reference JAR and seven requested asset-source URLs. No proprietary reference asset or third-party asset-pack archive was incorporated. File-level provenance and completed artwork records follow the source audit below.

## Supplied JAR

`GrimoireOfGaia4-1.20.1-4.0.0-alpha.12.jar` is a Forge reference, not a runtime dependency. SHA-256: `cb3e635dfa8779f32c1fe7810e6c38b983d733988b0298001ef6332eb167b56b`. Its 1,498 archive entries include `assets/grimoireofgaia/textures/entity`, JSON block/item models, Patchouli documentation, Forge biome modifiers and compiled `gaia/client/model/*.class` / renderer classes. Entity geometry is represented by Java model classes rather than ready-to-import GeckoLib geometry.

`META-INF/mods.toml` explicitly declares `license="Assets: ARR, Code: Creative Commons 0"`. Assets are all rights reserved. The code license does not authorize redistribution of textures/models/audio. Only isolated texture viewing and model part-name metadata inspection were used. No implementation code was copied or decompiled.

Reference-only local inspection files live outside the checkout in `/workspace/validation/monster-girl-expansion/references/`. They include archive-entry index, metadata, enlarged Werecat/Nine Tails textures and a texture contact sheet. These proprietary images must remain excluded from distributables and repository resources.

## Reference mapping

The task screenshots were supplied conversationally and were not available as individual files to this audit. Matches below use the parent agent's image descriptions and isolated JAR inspection. A matching species name establishes an available reference, not an exact screenshot match.

| Requested creature | JAR reference key | Evidence / limitation |
| --- | --- | --- |
| Ender Dragon Girl | ender_dragon_girl | same-name texture and model |
| Vampire | unresolved | no vampire-named entity texture/model in supplied version |
| Holstaurus | unresolved | no holstaurus-named entity texture/model; do not silently substitute Minotaurus |
| Centaur | centaur | two female/male texture sets present |
| Sahuagin | unresolved | no sahuagin-named entity texture/model; do not silently substitute Siren or Mermaid |
| Valkyrie | valkyrie | same-name texture and model |
| Fox Spirit Girl | nine_tails | high-confidence described visual match; Nine Tails silhouette used for original art |
| Anubis | anubis | female and male textures present |
| Kobold | kobold | two numbered textures present |
| Cyclops | cyclops | same-name texture and model |
| Dhampir | unresolved | no dhampir-named entity texture/model; hunter is distinct and unconfirmed |
| Succubus | succubus | female and male textures present |
| Werecat (temporary Ashen Wing Girl name) | werecat / werecat01 | gray/red-eyed reference identified; user explicitly requested wingless anatomy |
| Existing Harpy | harpy / harpy01 | brown-feather variant fits described reference |
| Existing Minotaur | minotaurus versus minotaur unresolved | both distinct references exist; screenshot confirmation required for exact mapping |
| Existing Slime Maiden | slime_girl | green texture plus separate hair layer present |
| Existing Forest Dryad | dryad | two green variants; precise variant not confirmed |

The described fox has a strong Nine Tails match: gold hair, green eyes, red tunic, fox ears and gold tails. `NineTailsModel` names nine two-segment tail chains in top/middle/bottom rows.

The silver-gray, red-eyed figure has a strong **Werecat (werecat01)** match: its isolated texture has gray hair, red eyes, pale silver details and navy limb pieces. `WerecatModel` identifies two ears and `tail1`/`tail2`; it has no wing-named parts. The head protrusions and rear appendage fit ears and tail. The screenshot itself was not directly examined by this audit, so use the Werecat identity with the user-confirmed wingless silhouette. Do not add wings merely because the temporary name contains “Wing”.

## External source checks

One attempt at every exact URL was made concurrently in a single batch. Every attempt failed during HTTPS proxy CONNECT with `403 Forbidden`; no origin HTTP response was received. Therefore no pages, legitimate download links, archives, individual file contents or licenses could be verified. Licenses remain **unknown**, including sources commonly described elsewhere as permissively licensed. No archive hashes can be reported because none was downloaded.

| Exact URL | Observed result | Verified license | Incorporated |
| --- | --- | --- | --- |
| https://quaternius.com/packs/ultimatemodularwomen.html | proxy CONNECT 403; origin unavailable | unknown | none |
| https://quaternius.com/packs/ultimatemonsters.html | proxy CONNECT 403; origin unavailable | unknown | none |
| https://quaternius.com/packs/modularcharacteroutfitsfantasy.html | proxy CONNECT 403; origin unavailable | unknown | none |
| https://quaternius.com/packs/ultimateanimatedanimals.html | proxy CONNECT 403; origin unavailable | unknown | none |
| https://quaternius.com/packs/universalanimationlibrary2.html | proxy CONNECT 403; origin unavailable | unknown | none |
| https://vediagames.itch.io/characters-fantasy-voxel-pack | proxy CONNECT 403; origin unavailable | unknown | none |
| https://kenney.nl/assets/particle-pack | proxy CONNECT 403; origin unavailable | unknown | none |

See `source-audit.json` for machine-readable outcomes. Response bodies and hashes are absent because the CONNECT tunnel was rejected before an origin response. Do not describe these attempts as successful downloads or assert an asset license from a provider's reputation. If access becomes available later, verify the actual individual asset license, archive SHA-256 and file contents before any integration recommendation.

## Integration requirement

Use original independently authored models, textures, eggs and effects. General creature concepts and broad palette/species cues can guide new art; proprietary pixels, geometry and exact character designs are not project inputs. Any future third-party inclusion needs its own verified file-level provenance and compatible license. This audit makes no claim about runtime rendering or artistic quality of the implementation.

## Incorporated original artwork

No third-party asset pack files were incorporated. All 13 new models, UV layouts, painted PNG textures, native Blockbench files, GeckoLib animation tracks and symbolic spawn-egg icons were authored within this project under its [CC0 license](../../LICENSE). Shared export helpers and the four existing visual revisions derive from this repository, not the reference JAR. Runtime particles use vanilla Minecraft particle types. No FBX animation was imported or assumed compatible.

| Original assets | Authoring source | Additional record |
| --- | --- | --- |
| Vampire, Dhampir, Cyclops, Anubis, Kobold | `tools/generate_expansion_humanoids.py` | [Humanoid art notes](ART_HUMANOIDS.md) |
| Ender Dragon Girl, Succubus, Valkyrie, Nine-Tailed Fox Spirit | `tools/generate_expansion_winged.py` | [Winged art notes](ART_WINGED.md) |
| Centaur, Holstaurus, Sahuagin, Werecat | `tools/generate_expansion_anatomy.py` | [Anatomy notes](ART_ANATOMY.md) |
| Existing Harpy, Minotaur, Slime Maiden, Forest Dryad visual revisions | Existing group A/B/D generators | [Preservation record](EXISTING_VISUALS.md) |

Each new species has `tools/blockbench/<id>.bbmodel`, `geckolib/models/entity/<id>.geo.json`, `geckolib/animations/entity/<id>.animation.json`, `textures/entity/<id>.png` and `textures/item/<id>_spawn_egg.png`. Resource paths are relative to `src/main/resources/assets/mythic_realms_creatures/`. Optional glow masks exist only where the renderer enables them.

All 17 conversational screenshots were available to the implementation review after the later Ender Dragon Girl and Dryad submissions. The source-JAR table above records archive availability, not a missing design reference. The gray/red-eyed reference follows the confirmed **wingless** Werecat silhouette; the fox follows a nine-tail silhouette. Harpy retains her adult feminine body and uses the separately supplied bird-wing image only for wing shape and feathers. Moon Stag and Wyvern references belong to the preceding V2 overhaul, which remains preserved outside the four explicitly revised originals.

The [file-level asset manifest](asset-manifest.json) records every incorporated species asset path, SHA-256, geometry count, authoring script and CC0 provenance. The manifest includes the four preserved original animation files to make the visual-only boundary reviewable.
