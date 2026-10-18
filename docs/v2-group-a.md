# Group A V2 implementation

Original authored geometry; no external models, textures or animation copied.
Generator: `tools/generate_overhaul_group_a.py`.

| Creature | Bones | Cubes | Clips | Visible change |
|---|---:|---:|---:|---|
| Goblin Scout |20|95|11|Faceted torso, skull, shoulder/limb transitions; wrist/elbow phase offsets, torso follow-through; existing enclosed dagger socket seated higher in palm, pommel above ground.|
| Goblin Shaman |24|102|10|Faceted anatomy, shoulder caps, clothing preserved; enclosed palm/staff handle socket; all independent staff animation removed, casting and ritual tilt moved to wrist; expressive free elbow/hand.|
| Orc Warrior |19|102|9|Broader layered chest/shoulders and faceted limbs/skull; short actual cleaver hilt inside closed palm; steel blade/guard retained in identity; elbow, wrist and torso attack follow-through.|
| Minotaur |22|120|10|Barrel muzzle, dewlap, horn transitions, split grounded hoof lobes, broad muscular torso; two actual palms on long axe handle in carry poses; separate cross-chest support elbow geometry. Support releases during attack windup for an elbow/wrist-powered swing and returns during recovery.|
| Stone Troll |17|96|10|Wider 21.6-pixel torso, larger shoulder/back plate silhouette, 12.6-pixel enormous lower jaw versus 8.6-pixel skull; asymmetric plates, minute recessed eyes; every previous eyebrow/lid/ridge removed; broad feet remain at y=0.|

Changed generated paths for each of the five IDs above:

- `src/main/resources/assets/mythic_realms_creatures/geckolib/models/entity/<id>.geo.json`
- `src/main/resources/assets/mythic_realms_creatures/geckolib/animations/entity/<id>.animation.json`
- `tools/blockbench/<id>.bbmodel`

Existing original palette/material painting is reused. Export regenerates the original PNGs and matching embedded native atlas; no additional texture/material/controller layers were added.

## Checks

`python tools/generate_overhaul_group_a.py` passes all five export validators (geometry, animation references, native/UV/PNG parity). Existing focused Scout rigid-socket and all-native-project parity tests pass (2 tests, parity restricted to these five IDs). Additional direct checks passed for four rigid `hand_right -> grip_right -> weapon` chains, seven enclosing finger/thumb cubes per grip, absence of weapon/socket animation transforms, unchanged attack/heavy/cast server-impact keys, Troll head's exact seven brow-free elements, lower jaw wider than skull and both foot minima exactly zero.

Minotaur support rest geometry is solved in the frontal plane: shoulder `(7,29,0)`, two segments of length 8, support target `(-7,25,0)`; palm overlaps handle at z=-1.8. Both arms remain on the handle throughout idle/walk/run/charge/guard by moving their common chest ancestor. During attacks the support intentionally releases and rejoins at recovery; it is not claimed to remain a two-hand grip through every attack frame. No runtime IK or floating attachment is introduced.

Troll raw, unrotated model extents: x `[-0.985,1.099]`, y `[0,3.446]`, z `[-0.821,0.738]` blocks. Enlargement comes from torso/shoulder/jaw geometry rather than uniform render scale. Collision dimensions, eye height, render scale and all gameplay code remain unchanged; root integration owns assessment of necessary renderer/dimension changes.

## Limits

Export tests establish structure and parity, not rendered artistic quality. This subtask ran no Gradle, game client, performance benchmark or screenshot review; root integration handles those. Ground contact during leg swing is approximate, not a runtime foot IK solution. Existing clip names, bone names, registry IDs and impact times are preserved. Crystal Spider and Flame Imp untouched.
