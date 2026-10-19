# Centaur — V5.3 stage4

Reference: latest inline image15. Registry `centaur`, server dimensions, AI and movement physics remain unchanged. Original project CC0 artwork. The unchanged recorded1.3.0 all33 graphical run supplies actual baseline views.

Five principal baseline differences: a bench-like barrel, straight post-like hindlegs, gold irises, stacked shoulder bands and a rigid tail tip. Pass1 rebuilds the horse shoulder/barrel/tucked belly/croup, adds broad haunches and distinct hocks on the original three-joint hindleg chains, refines the shoulder plates and assigns a small unused atlas region to muted green irises. Individual forelegs, silver front cuffs and all four hooves remain. The existing sword's forward/down grip is retained.

Pass1 side comparison showed an overlong trunk and a stepped rear topline. Pass2 compacts the horse body, hindleg geometry/pivots and tail together, softens the croup transition and adds layered dark fringe/temple details. The new four-beat cosmetic walk offsets the four leg phases; its existing cycle duration stays1.2 seconds. Foot-angle compensation remains. The existing fast diagonal trot and every combat clip remain unchanged. Idle tail-tip lag and geometry-based death support are cosmetic only.

Validation: three new focused client runs pass, with final geometry unchanged between passes2 and3. Pass3 extends only the isolated client test camera to show side-biased motion and additional walk/run phases. Actual frames expose the four leg chains, hocks, hoof orientations and tail through several gait phases. Front/side/three-quarter/back/distant, chest/waist transition, eye colors, sword grip and attack impact, cast/hurt and side-lying corpse are inspected. All35 asset/source/preservation checks pass. The full milestone4 Java21 build and51 dedicated-server GameTests pass with zero failures/skips; archived results are in `test-results/`.

The original489-file baseline is retained. Exactly one test-only class has an explicit reviewed SHA override for the added Centaur camera; production renderer/gameplay/audio, all20 original creatures, the three completed models and nine pending targets remain unchanged. The client test class is excluded from the playable JAR.

Remaining differences: original horse coat/haunch construction, clothing seams, hair and unseen rear details. Gait probes play real animations on the stationary test fixture; they do not measure terrain traversal or foot slip at every server velocity. Shadow placement is not used as a contact measurement; numeric support guards the sampled final corpse bounds. Stills do not certify every interpolation, and software rendering is not a GPU benchmark.

Final model: 30 bones / 135 cubes. Actual reviewed baseline plus 3 corrective client runs; each corrective run bakes/syncs all33 resource sets and presents one selected species.

[Actual final states](previews/centaur-states.jpg) · [Actual baseline/final comparison](previews/centaur-comparison.jpg).
