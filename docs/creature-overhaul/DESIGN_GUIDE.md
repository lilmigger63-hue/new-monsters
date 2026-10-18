# Dark-fantasy creature overhaul design

Binding brief: [SPEC.md](SPEC.md). User authorized immediate execution; existing release1.0.0 and the main branch stay intact. Work occurs on `feat/creature-overhaul` from `6fb834f`.

Keep Minecraft1.21.10 exactly, Java21, Fabric and GeckoLib5.3-alpha-3, all20 registered IDs, stats, collision dimensions, taming/owner persistence, safe flight, spawning, recipes, structures and optional Better Combat. Upgrade art and presentation against inspected reference research. Reference artwork is studied; its pixels are not copied into mod textures. Copyrighted reference downloads remain outside Git; only exact URLs, available credits, restrictions and original analysis enter the atlas.

## Visual language

Readable block silhouettes at4–24blocks; muted moss/bark/iron/bone colors, selective saturated magical accents, material-specific directional pixel work instead of random noise. Retain128×128 RGBA atlases. Use articulated wrists, jaws, wing tips, tails, ears, fabric panels and antlers where relevant. Avoid excess overlapping slabs, indistinguishable humanoids, flat rectangular robes and visual size drift.

GroupA: hunched asymmetric goblins, broad tusked plated orc, bovine-headed bronze minotaur, irregular mineral troll. GroupB: root-legged branching treant; vine-draped dryad; layered eagle/lion Griffin; canine digitigrade wolf; two-legged/two-winged wyvern. GroupC: crested low reptile, eight-legged crystal spider, tattered spectral wraith, damaged plate/cape knight, small bat-winged ember imp. GroupD: articulated icy shards/core; elegant antlered quadruped stag; asymmetrical expressive deformable slime; feathered wing-arm harpy; horned robed caster with original sigils.

## Implementation boundaries

One shared offline asset pipeline validates geometry/UVs, paints controlled material tiles, writes matching GeckoLib resources and native Blockbench projects. Four independently owned generators build groupsA–D; original generator entry points invoke the relevant overhaul exporters last so regeneration preserves these edits. Exporters touch creature art only, never gameplay data/loot/items/lang. All20 native sources embed exactly the distributed normal PNG and corresponding animations; variants and masks keep the same UV layout.

Keep damage on the server; attack/cast/heavy impact keys match CreatureKind.windup/20. Existing action triggers retain attack/cast/hurt/heavy semantics. Runtime presentation supplies speed-appropriate locomotion, guarded/combo poses and bounded cast/impact effects. Any AI adjustment must have a reproducing server test and preserve owner/neutral rules.

## Validation

Record baseline before edits. Per-batch: validate source/export correspondence, all bone hierarchies/UVs/PNG variants, collision/model scale and actual rendered front/side/back/gameplay-distance images. Finish with clean build, all server tests with/without Better Combat and graphical client tests including owner riding/flight. Particle amounts obey intensity and nearby-player distance, with strict per-event/ring budgets. Never claim a phase complete from generated file counts alone.
