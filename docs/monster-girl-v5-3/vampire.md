# Vampire — V5.3 stage2

Reference: latest inline image17. Registry `vampire`, hitbox, AI, sounds and spawning preserved. Original CC0 project artwork.

Five baseline differences: long slab-like blonde hair, a narrow dark mantle, repeated metallic horizontal waist bars, ladder-like rectangular skirt borders and a shallow white ruff. The revised model shortens and layers the bob; replaces the narrow cape with a wider burgundy-lined mantle; adds two articulated lower cape panels; replaces front bars with a small clasp; and builds vertical pleats and a darker hem. Original collar, eyes and red/black materials are retained where successful.

Pass1 review prioritized the fringe, hair accessory and white neck detail. Pass2 adds swept overlapping locks, a dimensional red rosette, layered jabot and broad dark fabric shading clusters. Weapon inspection then revealed the original dagger pointing into the forearm. Pass3 rotates only the visual dagger bone to put the blade forward/down through the hand grip. Actual idle and attack-impact views now show the hilt seated in the hand and the blade clear of the forearm. Cape secondary motion is cosmetic idle/walk/run; death support is recomputed for the new silhouette. All attack/heavy/cast/hurt keyframes, clip names, durations, loops and server behavior remain unchanged.

Validation: actual baseline and three valid corrective client runs pass. Inspected front/side/three-quarter/back/distant, hair/rosette/ruff, red eyes, mantle and skirt, idle/walk/run, attack/heavy impact, cast/hurt and grounded corpse. All35 asset/source/preservation checks pass. The completed Ender artwork, all20 original species and eleven pending targets are frozen unchanged. One earlier export failed because a rounded walk keyframe exceeded its exact existing duration by0.00000122 seconds; its prematurely started client run was discarded and is not counted. Endpoint clamping fixes the authoring bug without changing duration, and an automated source regression covers it.

Remaining differences: original pleat layout, rosette, mantle folds and hidden rear construction; lighting and pose differ from the reference. The original dagger is retained rather than inventing a new gameplay weapon. Actual stills sample playback and do not certify every interpolated frame. No likeness percentage or measured GPU performance claim.

Final model: 30 bones / 131 cubes. Actual baseline and 3 corrective client runs; all33 resource sets baked/synced, one selected species presented per run.

[Actual final states](previews/vampire-states.jpg) · [Actual baseline/final comparison](previews/vampire-comparison.jpg).
