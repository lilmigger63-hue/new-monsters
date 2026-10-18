# Monster visual overhaul V3 — 1.3.0-rc.1

Seventeen creatures were completed sequentially, visually checked in the actual Minecraft 1.21.10 Fabric client, and committed individually. The [progress table](../monster-visual-overhaul-progress.md) links the stage order and commits; individual numbered stage reports and `previews/` contain actual before/final comparisons and animation-state sheets.

Original artwork follows the supplied anatomy and broad visual references: Harpy arm-wings and bird feet; green leaf Dryad; fully green humanoid gel Slime Maiden; bovine Minotaur; blonde crimson Vampire; armored black-winged Valkyrie; curled-horn Succubus; horned black Ender Dragon Girl; four-legged Centaur; nine-tailed Fox Spirit; jackal-eared Anubis; reptilian Kobold; single-eyed Cyclops; broad-hatted Dhampir; finned amphibious Sahuagin; cow-eared Holstaurus; and silver feline Werecat. Werecat deliberately has no wings, following the user's clarification. Cyclops retains the existing two-handed polearm; Sahuagin retains its trident because the pictured hand object is unclear.

## Preservation and optimization

All server gameplay Java, data, attributes, AI, hitboxes, damage timing, saved entity identifiers, loot and spawn eggs match the recorded baseline. Only Forest Dryad and Slime Maiden naturally spawn among the original twenty species; thirteen added species keep their habitat rules. Six species have explicitly documented cosmetic animation adaptations; every other clip remains unchanged. Frozen art hashes protect all 17 completed creatures and all 16 non-target species.

A whole-roster audit covers all 33 models in [render-budget.json](render-budget.json). Wild Wyvern, Slime Maiden and Kobold had glow masks whose opaque pixels map to no model face. Their redundant full-model emissive passes are removed without altering geometry, textures or animations. This avoids submitting 375 cubes / 2250 cube faces across one instance of each of these three species, before GPU culling. The remaining emissive-species set is allocated once instead of once per renderer construction. Existing texture caching, gameplay tick rates and detail are preserved. No hardware FPS improvement is claimed.

The final source review found and fixed an accidental Fox-only correction block in the Vampire generator. Read-only reconstruction now matches its frozen geometry; no final artwork was regenerated.

## Validation

- 27 Python checks: asset validity, all33 rig/native/UV contracts, expansion preservation, frozen artwork/gameplay hashes, corpse support emissive UV coverage and read-only reconstruction of all17 models/textures.
- 14 standalone attack timeline checks.
- Full Java21 build passes. Dedicated-server GameTests: 51/51 pass without Better Combat and 51/51 with Better Combat, zero skips. XML results are in `test-results/`; final client and artifact details are recorded in `validation.json`.
- Each of the 17 species has actual focused client evidence with multiple viewing angles, relevant movement/actions, attack-impact poses and death. Winged species include flight phases; Sahuagin is actually submerged; Holstaurus includes hop and landing. Each run also bakes/synchronizes all33 resource sets. Final shared-renderer validation also passes: all33 species presented with Better Combat, including actual mount input and server death checks. Wild Wyvern, Slime Maiden and Kobold were visually inspected again after removing their unused glow passes; see [final render checks](previews/render-optimization-check.jpg).

These are inspected frames from real animation playback, not a certification of every interpolation frame. Tests use Xvfb/llvmpipe software rendering, so they do not establish physical-GPU performance. Reference images do not expose every rear surface, and hidden details are original interpretations. Sahuagin's close upright underwater frame crops part of the head; its full land head and horizontal swim are inspected separately. No numerical likeness score is claimed. The headless client has no audio device, and offline authentication-key requests fail; sound playback and online authentication are not certified by these runs.

## Assets and rebuilding

See [ASSET_INVENTORY.md](ASSET_INVENTORY.md) and [asset-inventory.json](asset-inventory.json) for incorporated files, origins, rights and requested pack download limitations. All V3 artwork is original CC0 project work; proprietary Gaia assets are not shipped.

Build with Java21, Minecraft1.21.10, Loader0.19.5, FabricAPI0.138.4+1.21.10 and GeckoLib5.3-alpha-3. `scripts/cloud-gradle.py build runGametest` runs the normal build/server suite; add `-PwithBetterCombat` for the optional integration. `scripts/client-smoke.sh` launches the graphical suite. Author a single species using `python3 tools/generate_visual_overhaul_v3.py <species>`; do not overwrite reviewed assets without intentional review and new validation.
