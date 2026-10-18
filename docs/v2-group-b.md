# V2 organic creature batch

Original geometry using the existing 128×128 painted material atlas and GeckoLib/native Blockbench export pipeline. No third-party asset data copied. Existing head screenshot interpretation in `reference_wyvern_head` is preserved.

| Creature | Bones | Cubes | Clips | Visible changes |
|---|---:|---:|---:|---|
| Ancient Treant | 17 | 95 | 8 | 32% wider upper trunk/joints, branching shoulder masses, irregular dark knot cavity with split bark and recessed luminous slits; weighted trunk sway, forebranch lag and impact recoil |
| Forest Dryad | 29 | 91 | 8 | Bark-framed nonhuman face, luminous angled eyes, full foliage crown, modest volumetric leaf bodice and tapered waist; hair/vine spell and attack follow-through |
| Griffin | 22 | 129 | 16 | Strong pectoral/shoulder mass, descending hooked beak and orbital scowl; articulated wing spars, overlapping primary/coverts, foot plants and flight/tail lag |
| Dire Wolf | 20 | 95 | 13 | Rising integrated brow facets, reinforced muzzle, scapular fur and fuller tail; grounded body compression, joint articulation, ear anticipation and bite recoil |
| Wild Wyvern | 18 | 127 | 16 | Strong chest/neck, enlarged tail plus distal segment, longer supported membrane fan; preserved blunt dinosaur head/pale muzzle/teeth/low crest, exactly two legs and two wings; flight body lag, tail follow-through, takeoff tuck and landing leg compression |

The wyvern saddle seat remains at model Y=22 (seat cube starts at Y=21 and is 1.2 units tall). Existing bones and limb parent hierarchy retained; only `tail_end` added. Registry/gameplay/Java files unchanged. Grounded run/ride root bounce removed to prevent a persistent hovering offset.

Validation run: `python tools/generate_overhaul_group_b.py`; all five passed built-in positive geometry, 128×128 atlas/UV, bone reference, frame interval, native element/clip count, and embedded texture decoding assertions. Additional checks confirmed all HEAD bone names retained, attack/heavy/cast impact timestamps (1.2/.8/.6/.35/1.0 seconds) and durations unchanged, wyvern limb count and exact seat cube preserved.

Limits: no Gradle or client launch performed in this batch; parent task owns build and actual client screenshot assessment. Visual quality, extreme-pose clipping, wing membrane silhouette and foot contact under blended runtime controllers require that assessment. References unavailable to this batch were not retried; models are original interpretations of the provided descriptions and existing screenshot head implementation.

## Supplied wyvern body image follow-up

Parent inspected the newly supplied nighttime dragon body reference: nearly horizontal long airborne torso, strong integrated shoulder, tall broad wings with long spars and generous membrane chord, long tapering spined tail, tucked hindlegs. Applied those silhouette cues to the original green/rare-blue wyvern without copying red palette or any asset data. Torso now extends four model units farther rearward, wing wrist spars extend to 41 units from center with broader finger membranes (24-unit root chord tapering outward), and distal tail tapers to model Z=54 with small dorsal spines. Flight uses a nearly horizontal torso, higher shoulder recovery stroke, lagged wrist motion and tucked hindlegs with bent lower joints. Dinosaur screenshot head and saddle cube are unchanged. Only wyvern was regenerated during this follow-up; other four species exports remain finalized. Export validation passed again: 18 bones, 127 cubes, 16 clips.

## Griffin client fold correction

Reviewed actual client side screenshot `0078_creature-griffin-side.png`: old shoulder yaw folded the fan forward, while extreme wrist roll raised the primaries above the head as slabs. Griffin-only rest now yaws wings rearward along flanks (78 degrees), with shallow downward shoulder roll and a nearly aligned wrist. Ground clips explicitly keep compact wing scale (0.55 span/chord) and neutral fold offsets; feather chord shortened 28% and shifted outward to reduce cross-body overlap. Flight restores full span and cancels the new rest angles before applying flap and wrist lag. Takeoff/landing interpolate shoulder angle, wrist angle and compact/full scale. This keeps connected wing-parent transforms, saddle, attack times and all original bones; native validation and explicit grounded/flight scale, hierarchy and saddle checks passed. Counts unchanged (22 bones, 129 cubes, 16 clips). A fresh actual client fold/flight review remains necessary; no other species was regenerated.
