# 01 — Harpy reference overhaul

V3 stage complete after six visual iterations; known differences and validation limits are recorded below. Reference: first inline V3 image, adult brown Harpy. Original image filename is unavailable. The separately supplied bird-wing image remains wing-anatomy context. New Grimoire JAR SHA256 is identical to the previously audited ARR-assets reference; no pixels or model data are copied.

Technical mapping: `HarpyEntity`, registry `harpy`, shared `CreatureRenderer`, `harpy.geo.json`, `harpy.animation.json`, `harpy.png`/`harpy_glowmask.png`, native `tools/blockbench/harpy.bbmodel`. Wings are arms; there is no handheld weapon. `wing_*` → `wingtip_*` articulation and all original animation IDs/timing are retained. Gameplay baseline is recorded separately.

| Priority | Aspect | Released model → intended original V3 art |
| --- | --- | --- |
| 1 | Silhouette | Tall narrow body / spiky pale wings → compact adult bird woman with broad layered brown feather fans |
| 1 | Height/proportion | Small head / long thin torso → broad head, shorter waist, fuller feathered hips; hitbox unchanged |
| 1 | Head | Narrow square mask → wider cheeks and shaped jaw |
| 2 | Face | Flat center plane → shallow nose/mouth and framed pale face |
| 2 | Eyes/expression | Gold bright eyes → red-brown irises, dark lashes, pale sclera |
| 1 | Hair | Straight long curtain → swept brown bangs, side tufts, short filled rear locks and crest |
| 1 | Torso/limbs | Straight column / shoulder-heavy armor → pale chest/waist openings, layered brown feather bodice, adult silhouette |
| 1 | Hands/feet | Thin stick-like claws → olive segmented shins, three grounded black toes and rear toe; wings replace hands |
| 1 | Wings/tail | Light blade-like feathers → overlapping brown tapered primaries/coverts and coherent feathered tail |
| 2 | Clothing | Broad dark block bodice → feathered chest, shoulder bands, scalloped hip plumage |
| 2 | Texture | Pale yellow wing accents / uniform hair → original warm umber feathers, lighter brown feather edges, pale skin, olive legs |
| — | Weapon | None in reference or model |

Pass1: rebuilt geometry, anatomy and atlas from original source; 28 existing bones,162 cubes,11 original clips. Existing exporter/native/UV/PNG checks and16 asset suites passed. Actual client review pending. Largest differences will be recorded from real pass1 captures before pass2. Hidden back/inner-wing details are conservative original interpretations. No numerical resemblance score is claimed.

Pass2: narrowed the eye border, replaced the five upright hair posts with a single tapered crest, added crossing bodice straps and a deliberately painted broad-patch feather atlas. Added an explicit grounded-reference animation probe to the test harness: the original NoAI Harpy capture automatically chose hover because the test entity was airborne. Grounded stills are presentation probes, not evidence of changed flight AI.

Pass3: widened/lengthened the primary fan, exposed the pale upper arms and reduced the forehead fringe overhang. Reviewed front, side, three-quarter, held death and sampled flight. Remaining top issues: the fan still collapsed inward, the resting wing outline was too narrow and the feather tips lacked lateral separation.

Pass4: corrected the feather cube Z rotation direction for GeckoLib's mirrored coordinate convention. This directly addresses the three fan-readability issues without changing clips, damage timing or AI. Actual client review pending. No numerical similarity score or exhaustive continuous-motion certification is claimed.

Pass5: lowered the wing rest angle20degrees through the appearance rig, matching the reference's lower feather fan while retaining original flap tracks. Pass6: introduced two ankle bones to counter-rotate the flat toes beneath the newly bent avian hocks. Final rig:30 bones,162 cubes,11 byte-identical original animation clips.

Final validation: real Minecraft client resource bake/synchronization of all33 species, focused Harpy presentation and actual server attack/held movement/hurt/death/fly/hover probes passed; front/side/three-quarter/back/distant and four flight samples inspected. The final client build passed. All18 asset/preservation tests passed. Main gameplay Java, loot/spawn data and eggs match the baseline byte for byte; all16 non-target species art remains unchanged.

[Final actual state sheet](previews/harpy-states.jpg) · [Matched-camera pass2/final comparison](previews/harpy-comparison.jpg). These compare original project renders, not a numerical similarity metric against proprietary reference pixels.

Remaining differences: the original swept hair/crest is an interpretation rather than copied proprietary geometry; the supplied reference is a posed card while the game uses animated wing gestures; the preserved held death pose supports the elevated torso at the lower wing extremity. Rear feather layering is conservative because the reference does not show the back. Still images/sample phases do not certify every interpolation frame or dynamic foot IK. No blocking missing textures, detached anatomy or broken clips were observed in the inspected frames.

Modified: Harpy runtime geometry, base/glow PNGs, native project; original V3 authoring source/baseline and this report. Shared test-only camera/grounded-idle probes and preservation/report tooling were added for the remaining sequential stages. No runtime Java changed.
