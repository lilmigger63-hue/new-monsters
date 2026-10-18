# Incorporated assets and rights

All 17 V3 creature models, textures and native editable models are original project artwork distributed under the repository CC0 license. No Grimoire of Gaia model, texture, animation, sound or code is incorporated. The supplied Gaia JAR declares its artwork ARR and is used only as reference metadata. Reference images guide species anatomy and broad appearance; hidden surfaces are original interpretations.

The complete per-file SHA256 inventory is [asset-inventory.json](asset-inventory.json). It includes runtime geometry, textures, animations and native editable assets for each species. Authoring source is `tools/generate_visual_overhaul_v3.py`, with original project rig baselines in `tools/visual_v3_baselines/` and geometric death support in `tools/visual_v3_geometry.py`. Pillow and NumPy are offline authoring dependencies, not mod dependencies.

Harpy, Forest Dryad, Slime Maiden, Minotaur and Vampire use rebuilt geometry on the existing project animation skeletons. The remaining twelve adapt the project's existing species-specific rigs and geometry with newly authored anatomy, equipment, clothing and texture details. Wings, arm-wings, horse body, horns, fins, nine jointed tails and feline/reptilian details are modeled in this source; no downloaded generic character model substitutes for species anatomy. Existing animations are retained except the cosmetic clips explicitly listed in [animation-adaptations.json](animation-adaptations.json). Clip names, timing and gameplay stay preserved.

The following requested foundations were attempted during the preceding expansion work but downloads were blocked by the network proxy (CONNECT403). Their downloadable contents and licenses could not be inspected, so **none were incorporated**:

- https://quaternius.com/packs/ultimatemodularwomen.html
- https://quaternius.com/packs/ultimatemonsters.html
- https://quaternius.com/packs/modularcharacteroutfitsfantasy.html
- https://quaternius.com/packs/ultimateanimatedanimals.html
- https://quaternius.com/packs/universalanimationlibrary2.html
- https://vediagames.itch.io/characters-fantasy-voxel-pack
- https://kenney.nl/assets/particle-pack

See the [preceding asset audit](../monster-girl-expansion/ASSET_INVENTORY.md) for download attempts and existing dependency licensing. Fabric API and GeckoLib are separate runtime dependencies; optional Better Combat is not bundled. No FBX animation is assumed to work directly in GeckoLib.

## Runtime dependencies in the optional installation bundle

The existing dependency JARs were inspected through `fabric.mod.json` and their embedded license files; the packaging script verifies their SHA512 against the recorded dependency manifest before copying them unchanged.

| Dependency | Source declared in JAR | License | Embedded license |
| --- | --- | --- | --- |
| Fabric API0.138.4+1.21.10 | https://github.com/FabricMC/fabric | Apache-2.0 | `LICENSE-fabric-api` |
| GeckoLib5.3-alpha-3 Fabric1.21.10 | https://github.com/bernie-g/geckolib | MIT | `LICENSE_GeckoLib 5` |

These libraries provide runtime APIs and animation/rendering support; their character artwork is not used. Their original JAR contents and notices remain intact. Minecraft and Fabric Loader are not bundled.
