# V2: Basilisk, Wraith and Grave Knight

Authoring manifest: `tools/generate_overhaul_group_c.py`; runtime geometry and clips live in `src/main/resources/assets/mythic_realms_creatures/geckolib/{models,animations}/entity/`; editable matching native projects live in `tools/blockbench/`. There is no `assets/native` directory. Existing original painted material atlases, palettes and glow maps are retained.

- **Cave Basilisk:** 82 cubes, 16 bones, 8 clips. Permanent head-parented felt fedora has an overlapping stepped brim, crown, pinched crown ridge and contrasting green band. Its bottom intersects the skull crown slightly, eliminating a floating seam. Broad reptilian jaw, four sprawling legs, claws and segmented tail remain; angled flank masses soften the torso. Walking includes shoulder roll, alternating articulated feet and neck counter-motion. Bite keeps its existing 1.0-second impact with torso and tail-tip follow-through.
- **Shadow Wraith:** 57 cubes, 27 bones, 10 clips. Removed pallid face, nose, lips, pupils and brows; replaced them with a deep shadow cavity and three irregular luminous magical fissures. Covered adult bodice uses paired shaped chest panels, a tapered waist and wider hips. An overlapping fixed scalp cap covers the full skull; long side locks and four back layers overlap the shoulders/shroud. Floating shroud, hands and hair receive secondary motion. Existing translucency remains enabled. Attacks retain their existing 0.9-second impact.
- **Grave Knight:** 100 cubes, 22 bones, 10 clips. Fitted protective chest plates, tapered waist and overlapping hip lames define an adult feminine armored silhouette. Full scalp cap and six long side/back hair layers replace the short locks. Sword handle passes through a new palm socket, with curled fingers and an opposing thumb around it. `sword` is a rigid child of `arm_1_hand`, itself a child of the original forearm; no animation independently transforms the sword. Walk/run add torso weight transfer, alternating knee flexion and elbow motion. Both combo strikes, heavy/cast, guard and death remain; existing attack impact is 0.6 seconds.

## Verification

`python tools/generate_overhaul_group_c.py` passed the shared exporter's native Blockbench, UV, atlas and animation validation. Focused Python checks confirmed:

- All original bone names retained; all animated bones exist; all key times fit clip bounds.
- All three remain below 180 cubes and exported deaths finish within 0.65 seconds.
- Fedora is parented to `head`; knight sword is parented to the hand socket and has no independent animation channel in any clip.
- Crystal Spider and Flame Imp authoring functions are unchanged; SHA-256 checks verified all 16 associated generated files stayed byte-identical.
- Python compilation passes.

External visual reference pages were unavailable in the parent task. These are independently authored designs based on the supplied descriptions and established original art; no third-party geometry, pixels or animation were copied. Native/runtime exports share the same authoring data. Fresh actual-game screenshots, gameplay tests, full build and measured performance remain the parent integration checks; this batch does not claim those checks have passed.
