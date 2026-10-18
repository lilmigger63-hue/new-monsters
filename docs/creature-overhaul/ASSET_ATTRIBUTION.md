# Asset attribution and source inspection

Audit date: 2026-10-18. Scope: the 18 requested refinements; Crystal Spider and Flame Imp remain outside this refinement.

No third-party model, rig, texture, material or animation was downloaded or integrated by this add-on audit. All six exact requested pages returned `<urlopen error Tunnel connection failed: 403 Forbidden>` from the environment proxy. TLS verification remained enabled. The failures occur before page content is available; archive links, exact file licenses, credits, geometry, rigs and materials therefore could not be inspected. No file SHA-256 exists for an undownloaded asset.

| Requested source | Result |
| --- | --- |
| [Quaternius Ultimate Monsters](https://quaternius.com/packs/ultimatemonsters.html) | Proxy tunnel HTTP 403; no files selected |
| [Quaternius Ultimate Animated Animals](https://quaternius.com/packs/ultimateanimatedanimals.html) | Proxy tunnel HTTP 403; no files selected |
| [Quaternius Ultimate RPG](https://quaternius.com/packs/ultimaterpg.html) | Proxy tunnel HTTP 403; no files selected |
| [Quaternius Cute Animated Monsters](https://quaternius.com/packs/cutemonsters) | Proxy tunnel HTTP 403; no files selected |
| [OpenGameArt Low Poly Goblin (Rigged)](https://opengameart.org/content/low-poly-goblin-rigged) | Proxy tunnel HTTP 403; no files selected |
| [Blockbench Workshop GeckoLib models](https://blockbenchworkshop.com/models/geckolib) | Proxy tunnel HTTP 403; no files selected |

The six independent requests are recorded in `asset-sources.json`. Raw request results are cached outside the repository at `/workspace/validation/refinement/source-assets/pages.json`. Existing workspace downloads were checked for cached packs; none of these source packs or exact-file licenses was found. Repeated identical requests were stopped after the shared proxy denial was diagnosed.

## Original replacement and licensing

Use the existing project creatures as the starting point: refine their geometry and palette, create original pixel materials and accessory details, and adjust their existing GeckoLib bone animation curves. Preserve silhouettes, species, signature equipment, relative size and gameplay. No Quaternius, OpenGameArt or Blockbench Workshop content is cleared for copying by this audit, and no generic replacement model is selected.

The repository already provides a CC0-1.0 license at [`LICENSE`](../../LICENSE). That license governs original project contributions to the extent permitted by its terms; it does not establish permissions for external assets. Exact source-file licenses, source URL, SHA-256 and required credit must be added here before any future external file is integrated.

## Fossils and Archeology

No Fossils and Archeology JAR was supplied among the current attachments or identified in workspace downloads. Its structures, rigs and textures were not inspected. No Fossils and Archeology assets were copied; the fallback is original anatomical and motion refinement.

## Existing study references

The pre-existing [`references.json`](references.json) records Wesnoth image studies and explicitly states that exact per-image licensing is unresolved and reuse is not authorized by that catalog. It is not evidence of legally reusable model/material files. No such image is added to runtime textures or traced into geometry by this source audit.
