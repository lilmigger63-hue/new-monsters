# Anubis — V5.3 stage8

Reference: latest inline image11. Existing `anubis` ID, dimensions, AI, guard/combat mechanics, equipment, sounds and spawning unchanged. Original project CC0 artwork; unchanged actual1.3.0 baseline views reused.

Five principal baseline differences: rectangular ears, a dense gold collar, flat headcloth ends, plain linen mapping and weak waist/blade definition. Pass1 tapers the jackal ears, flares the black/gold cloth ends, reorganizes the collar into a calmer segmented shape, adds separate gold apron plates and allocates more existing atlas texels to linen folds. The successful blue eyes, black head covering and established forward/down khopesh grip are preserved.

Actual pass1 review identified an overly massive upper collar, identical folds on both legs and a square hooked blade. Pass2 slims the collar, maps the left linen panel to a separately painted fold region and bevels the existing hooked blade on its original hilt. Idle/walk/run cloth-tip motion is refined with exact existing clip lengths; attack/heavy/cast/hurt/guard clips remain unchanged. Death support is recomputed for the new silhouette.

Validation: both focused client runs and all35 asset/source/preservation checks pass. Inspected front/side/three-quarter/back/distant, ears/headcloth/blue eyes, gold collar/apron/arm bands, separate linen folds and black footwear, weapon seating and attack/heavy impact, walk/run/cast/hurt and side-lying corpse. Milestone8 full Java21 build and51 dedicated-server GameTests pass, zero failures/skips; archived results are in `test-results/`. Seven completed models, the20 originals, five pending targets and production gameplay/audio/renderer remain unchanged.

Remaining differences: original collar, cloth/apron layout, ear shapes, rear construction and retained project khopesh rather than an exact copy of the reference weapon. The reference does not expose every rear surface. Stills sample real playback and do not certify every interpolation or physical GPU performance. No numerical likeness claim.

Final model: 29 bones / 164 cubes. Actual reviewed baseline plus 2 corrective client runs; each corrective run bakes/syncs all33 resource sets and presents one selected species.

[Actual final states](previews/anubis-states.jpg) · [Actual baseline/final comparison](previews/anubis-comparison.jpg).
