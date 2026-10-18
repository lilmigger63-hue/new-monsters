# Creature overhaul V2 — candidate 1.1.0-rc.3

Source of truth: [user V2 specification](visual-overhaul-input/MASTER_PROMPT_V2.md). The existing Fabric 1.21.10 / Java 21 / GeckoLib 5.3-alpha-3 project is extended, not replaced. Crystal Spider and Flame Imp are excluded and byte-preserved.

## References actually available

The coordinator visually inspected the four supplied conversation images: dinosaur head (Wyvern head only), broad layered bird wing (Harpy wings only), Megaloceros (Stag anatomy/antlers), and dark airborne dragon (Wyvern body/wings/tail). The dragon image is dim/cropped; invisible anatomy was not treated as known. Species colors and lunar crystals are retained rather than copying image palettes. V2 additionally authorizes the Harpy torso/hair changes; the earlier wing-only image remains a wing reference.

All five requested reference websites returned proxy CONNECT HTTP 403 on a single batched attempt. No page images were inspected. Exact audit: [reference access](test-results/v2-reference-access.json). No Fossils & Archeology Forge reference JAR is present. The supplied rc.2 JAR is this original mod and matches the pre-overhaul source assets, apart from the later Scout proof. No third-party code, pixels or geometry were copied. Existing original painted texture atlases are reused with new geometry/UV allocations; no new texture layers or runtime dependencies.

## Compact manifest and visual changelog

Every row has modified runtime model, animation JSON and matching native Blockbench project. Geometry lives under `src/main/resources/assets/mythic_realms_creatures/geckolib/models/entity/<id>.geo.json`, animation under `geckolib/animations/entity/<id>.animation.json`, texture under `textures/entity/<id>.png`, native project at `tools/blockbench/<id>.bbmodel`. Authoring groups A/B/C/D are `tools/generate_overhaul_group_<group>.py`. Existing registries/renderers/gameplay mapping is in [audit](visual-overhaul-audit.md).

| Creature ID | Authoring group | Before → after cubes | Bones | Changes |
|---|---|---:|---:|---|
| goblin_scout | A | 64 → 95 | 20 | Faceted nimble anatomy; enclosed dagger socket; elbow/wrist/torso follow-through |
| goblin_shaman | A | 74 → 102 | 24 | Faceted anatomy/robes; rigid staff handle; wrist-driven ritual/casting |
| orc_warrior | A | 72 → 102 | 19 | Broader muscular armor silhouette; closed cleaver grip; weighted attacks |
| minotaur | A | 75 → 120 | 22 | Bovine muzzle/dewlap, shoulder mass/hooves; two-hand carry and support release during swing |
| stone_troll | A | 80 → 96 | 17 | Wider stone giant; enormous lower jaw, tiny recessed eyes, no brows; layered rocks |
| ancient_treant | B | 91 → 95 | 17 | Wider trunk/shoulders; nonhuman bark cavity face; root/branch limbs and weighted motion |
| griffin | B | 129 → 129 | 22 | Hooked beak/orbital scowl, predatory chest/talons; layered wings and flight lag |
| dire_wolf | B | 89 → 95 | 20 | Rising integrated brow facets, muzzle/haunch/tail refinement; bite/gait articulation |
| wild_wyvern | B | 106 → 127 | 18 | User dinosaur head plus long dragon torso/tail, broad supported membrane wings; tucked flight legs |
| cave_basilisk | C | 73 → 82 | 16 | Permanent head-attached fedora, refined flanks and reptile gait |
| forest_dryad | B | 101 → 91 | 29 | Nonhuman botanical face, clothed adult foliage bodice/waist; hair/vine follow-through |
| shadow_wraith | C | 50 → 57 | 27 | Supernatural void/fissure face, clothed feminine silhouette; full long spectral hair |
| grave_knight | C | 75 → 100 | 22 | Fitted protective armor, full long hair; enclosed handle and upward carry sword; combos |
| frost_elemental | D | 55 → 66 | 36 | Nonhuman ice mask, feminine ice silhouette; full scalp ice strands and casting motion |
| moon_stag | D | 81 → 107 | 21 | User Megaloceros proportions/palmate lateral antlers with crystals; deer anatomy and original hoof IK |
| slime_maiden | D | 45 → 60 | 34 | Coherent translucent clothed jelly silhouette; full long gel hair, squish/secondary motion |
| harpy | D | 73 → 154 | 28 | User layered feather wings; adult covered torso, full long hair; wing-arm fold/follow-through |
| demon_sorceress | D | 94 → 111 | 42 | Tailored covered silhouette, full long layered hair; horn/casting/hand refinement |

Detailed authoring notes: [A](v2-group-a.md), [B](v2-group-b.md), [C](v2-group-c.md), [D](v2-group-d.md).

## Validation and acceptance

- 12 asset checks passed: 2 baseline resource checks, 5 geometry/native/UV/grounding checks, 5 V2 release contracts. All 18 model/animation hashes differ from the supplied rc.2 assets; excluded Spider/Imp resource/native hashes match. Weapon sockets are rigid, staff/sword have no independent animation channels; Fedora follows head.
- Independent structural review checked bone hierarchy, animation keyframe/death bounds, full scalp coverage, mask/texture parity and excluded assets. It found a buried Knight sword; blade orientation was corrected above the guard while handle/palm inheritance stayed rigid. Sampled blade ground clearance is >=0.88 blocks in idle/walk/run.
- Full `build runGametest`: passed; five JUnit checks and 40 server game tests. Optional `-PwithBetterCombat` build/server profile: passed, 40 game tests. [XML and client evidence](test-results/1.1.0-rc.3/).
- Base graphical smoke: all 20 species presented, 232 real screenshots. Review found a buried Harpy death pose and raised slab-like Griffin resting wings; both corrected. Harpy death support was recomputed from all model corners and wing feathers lengthened/tapered; Griffin shoulder/wrist folding now follows flanks.
- Fresh corrective smoke with Better Combat: all 20 resources/animation sets baked, four target species presented with 61 screenshots, actual Griffin rider-input flight and authoritative death/removal passed. Independent review confirmed the two visual defects resolved. This is not a fresh 20-species presentation run with Better Combat.
- Latest combined evidence: 237 actual captures; all 18 models reviewed in front/side/back/distant/attack and six playback probes, plus four flight phases for Wyvern/Harpy/Griffin. [Actual-game overview](overhaul-v2-preview.jpg); per-species before/after captures below.
- Four exporters regenerated deterministically: 347 resource/native files byte-identical. No additional runtime controllers/render layers or Java gameplay changes.
- Matched software-rendering performance comparison: uploaded rc.2 assets, same current smoke harness, Xvfb/llvmpipe OpenGL 4.5, 1280×720, render distance 3, FOV50, vsync off, cap260. Twenty species share one world; each fixed idle camera settles20ticks then captures5samples at5tick intervals. Baseline median 54.5 FPS versus V2 62.0 FPS, 100 samples each with throttle reason NONE. The initial comparison was discarded after detecting vanilla AFK throttling; both sides were rerun with identical idle-only work. A separate 40-sample Harpy-only repeat measured baseline 24.5 FPS versus V2 37.0 FPS. Run-to-run variation is substantial: the earlier short Harpy sample was lower, but that drop did not reproduce in the longer repeat. No overall or reproducible Harpy regression was observed; these results are not a speedup guarantee. Raw samples and methods are retained in the evidence directory. This is a controlled local software workload, not hardware FPS certification.

## Limits to report honestly

Grounded locomotion outside Spider/Stag is authored approximation rather than dynamic foot IK. Minotaur support hand intentionally releases for attack and returns at recovery. In-game stills and sampled flight phases cannot certify every transition/extreme collision or multiplayer network condition. Enlarged rock/wing/antler silhouettes overhang existing collision boxes; no gameplay dimension/eye/seat changes are made without a demonstrated need. Full Hytale visual fidelity cannot be verified against unavailable website images.

## Actual before/after captures

Wyvern camera distance increased from 4 to 6 blocks and the final Stag corrective camera also widened for large antlers; these images are appearance comparisons, not calibrated size measurements.

- [goblin_scout](overhaul-v2-previews/goblin_scout-comparison.jpg)
- [goblin_shaman](overhaul-v2-previews/goblin_shaman-comparison.jpg)
- [orc_warrior](overhaul-v2-previews/orc_warrior-comparison.jpg)
- [minotaur](overhaul-v2-previews/minotaur-comparison.jpg)
- [stone_troll](overhaul-v2-previews/stone_troll-comparison.jpg)
- [ancient_treant](overhaul-v2-previews/ancient_treant-comparison.jpg)
- [griffin](overhaul-v2-previews/griffin-comparison.jpg)
- [dire_wolf](overhaul-v2-previews/dire_wolf-comparison.jpg)
- [wild_wyvern](overhaul-v2-previews/wild_wyvern-comparison.jpg)
- [cave_basilisk](overhaul-v2-previews/cave_basilisk-comparison.jpg)
- [forest_dryad](overhaul-v2-previews/forest_dryad-comparison.jpg)
- [shadow_wraith](overhaul-v2-previews/shadow_wraith-comparison.jpg)
- [grave_knight](overhaul-v2-previews/grave_knight-comparison.jpg)
- [frost_elemental](overhaul-v2-previews/frost_elemental-comparison.jpg)
- [moon_stag](overhaul-v2-previews/moon_stag-comparison.jpg)
- [slime_maiden](overhaul-v2-previews/slime_maiden-comparison.jpg)
- [harpy](overhaul-v2-previews/harpy-comparison.jpg)
- [demon_sorceress](overhaul-v2-previews/demon_sorceress-comparison.jpg)
