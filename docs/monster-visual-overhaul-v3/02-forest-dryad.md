# 02 — Forest Dryad reference overhaul

V3 stage complete after four visual passes. Reference: inline V3 Dryad image, no supplied local filename. Harpy was validated and committed as84ec9ce before Dryad work began.

Technical mapping: `ForestDryadEntity`, registry `forest_dryad`, shared `CreatureRenderer`, runtime `forest_dryad.geo.json`/PNG/glow/animation, native `tools/blockbench/forest_dryad.bbmodel`. All eight clip durations are preserved; seven clips remain byte-identical. Only the cosmetic death support curve is adapted. Hands cast existing vine magic; no handheld weapon is depicted or added.

| Priority | Aspect | Released art → intended V3 original art |
| --- | --- | --- |
| 1 | Silhouette | Thin straight body → broader head, full hair, fitted leaf outfit and substantial boots |
| 1 | Proportions/height | Small head and long stick-like legs → larger adult head and shorter visible boots; hitbox remains unchanged |
| 1 | Head | Narrow green cap → broad pale face framed by leaf-green hair |
| 2 | Face | Flat small facial plane → shaped jaw and shallow nose/mouth |
| 2 | Eyes | Tiny bright eyes → readable green irises and dark upper lashes |
| 1 | Hair | Flat rear sheet → separate overlapping long green locks, side volume and sweeping fringe |
| 1 | Torso/limbs | Thin column and arms → leaf bodice, pale waist opening and fuller bare arms |
| 1 | Hands/feet | Thin finger sticks and narrow boots → palms/articulated fingers and broad pale boot volumes |
| 2 | Ears/accessory | Small ears/crown → pointed pale ears and a restrained leaf/flower ornament |
| 1 | Outfit | Short plain green shape → overlapping front/side leaf panels and green shoulder caps |
| 2 | Texture | Uniform green → layered botanical greens, pale face/arms and off-white boot separation |
| — | Weapon | None; preserve existing unarmed vine casting |

Pass1: rebuilt geometry in the existing29-bone hierarchy,110 cubes. New original128×128 texture uses leaf-like color planes and green hair shading. Existing geometry/native/UV/atlas checks passed; actual comparison and corrections pending. Rear hair and garment construction are conservative because the supplied card shows only one angle.

Pass1 review found a flat hair outline, barely visible ornament and plain white boot columns. Pass2 added stepped rear locks, lower sweeping bangs, a visible yellow-green shoot, shoulder cuff edges and boot seams/bands/painted panels. Pass3 extended the pointed ears beyond the hair silhouette. Front/side/three-quarter/back review confirmed the ears and coherent original botanical silhouette. Final:29 bones,124 cubes,eight clips.

Death regression: the old root curve ended at Y=-2 with no geometry support; under the new model about6.96 pixels lay beneath ground. It made partially buried limbs look disconnected. A new asset regression test failed on the original curve, then passed after a geometry-derived129-sample support curve was exported. Pass4 confirmed the full body above the floor in the actual client. Root rotation and0.65-second duration are unchanged; all attack/cast/heavy and locomotion clips remain untouched. The old expansion preservation test now accepts only explicitly listed V3 cosmetic clip adaptations, while checking authentic original baselines, clip names/durations/loop flags and byte-equivalent content of every other clip.

Validation: final real client build/run passed with all33 resource sets baked and synchronized; focused Dryad views, attack/cast/hurt/death and locomotion playback were inspected. All19 asset/preservation tests passed. All main gameplay Java, loot/spawn data and eggs remain byte-identical to baseline. The16 non-target species and completed Harpy assets were not changed.

[Final actual state sheet](previews/forest_dryad-states.jpg) · [Matched-camera pass1/final comparison](previews/forest_dryad-comparison.jpg). Remaining differences are original leaf/hair construction rather than proprietary geometry, reference-card versus game lighting, and conservatively inferred hidden back details. Still frames do not certify every interpolation, dynamic foot IK or a numerical similarity percentage.

Modified: Dryad geometry, texture/glow, cosmetic death support and native project; selected-species authoring/report source and the new offline floor regression utility. No runtime gameplay source or server mechanics changed.
