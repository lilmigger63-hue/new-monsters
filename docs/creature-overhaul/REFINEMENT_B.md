# Existing-design refinement: exporter group B

Forest Dryad follows the add-on's adult anime fantasy category; the other four follow organic anatomy. These exporter groups are not the add-on's stylistic groups.

The actual client baseline images were inspected: Treant/Dryad idle, Griffin/Wyvern side, and the corrected Dire Wolf stance side capture in `/workspace/validation/overhaul/stance-base/screenshots`. These showed square facial planes, unbridged limb transitions, and broad flat wing surfaces. No new in-game screenshot is claimed by this document.

| Creature | Before | Implemented refinement | Cubes / clips |
| --- | --- | --- | --- |
| Ancient Treant | Long bark planes with abrupt shoulder/elbow/knee transitions | Overlapping bark joints, root knuckles, trunk knot lips and brow ridges; slightly lighter secondary bark grain; crown motion trails locomotion | 91 / 8 |
| Forest Dryad | Bare rectangular face, small glowing eyes, simple rear leaves | Stepped adult jaw, nose/mouth, ivory sclera, green irises/dark pupils, highlights and lashes; side-parted leaf bangs, two articulated leafy hair locks; overlapping leaf bodice and waist sash; warmer skin and directional hair material | 101 / 8 |
| Griffin | Flat wing layers, straight beak and abrupt leg/paw joints | Hooked beak tip, staggered lesser coverts, shoulder/haunch overlaps, hock/metacarpal bridges and fleshy toe roots connecting claws; warmer ivory feather atlas; wing-tip idle breathing and paw flex | 129 / 16 |
| Dire Wolf | Corrected stance retained, box muzzle and abrupt hocks/paws | Cheek planes, dark nose cap/eye focus, shoulder/haunch volume, hock bridges and toe roots connecting claws; lighter underfur, ear flicks and paw flex | 89 / 13 |
| Wild Wyvern | Two legs/two wings, flat membrane panels, abrupt hock/paw join | Wing wrist knuckles, narrow trailing membrane ribs, hock/metatarsal and toe bridges; subtly warmer membrane material; wing-tip idle breathing and paw flex | 106 / 16 |

All old bone names, parents and pivots are preserved. Tail/tail-tip connection pivots and rotations, wolf stance leg geometry, ground soles, relative dimensions, saddle seat geometry and rider heights remain as authored. Only Dryad hair bones are added. Secondary motion uses existing clip timing; all death clips export at 0.65 seconds through the existing shared exporter. Existing attack/cast impact timings remain unchanged. No gameplay/Java/dependency/pipeline/test changes were made by this task.

## Sources and permissions

All refinements are original procedural geometry and material work. The source-verification agent reported proxy tunnel HTTP 403 for all six requested pages, with TLS verification retained; no source packs or exact-file licenses could be inspected. No third-party mesh, texture or animation was copied. This follows the add-on's original fallback allowance. Consult the central attribution document for the six exact URLs and access evidence. Fossils/Archeology is visual/structural reference only; no JAR assets were transferred.

## Verification

- `python tools/generate_overhaul_group_b.py`: all five native Blockbench/GeckoLib/UV/PNG exports verified.
- `python scripts/test-assets.py`: 2 tests passed.
- `python scripts/test-overhaul-assets.py`: 4 tests passed (repository-wide assets at the time of execution).
- Direct comparison against HEAD: every pre-existing bone ID, parent and pivot preserved across all five species; death <=0.65 seconds; Wyvern has no foreleg arm bones.
- Gradle and fresh in-game rendering are reserved for the integrating agent. The changes above describe implemented geometry/materials, not a claim that a fresh client screenshot has already confirmed every view or clip.
