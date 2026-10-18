# Creature overhaul reference atlas

Research date: 2026-10-18. All 60 entries below refer to real, successfully downloaded images that were visually inspected in four labeled contact sheets. Repeated images are deliberately analyzed for different design purposes. Artwork downloads remain outside the repository in `/workspace/validation/overhaul/references`; no reference pixels are shipped as game assets.

## Scope and limits

GitHub and raw GitHub were accessible. Wikimedia Commons, Met Museum and Art Institute endpoints returned proxy 403 responses; those restrictions were not bypassed. Consequently the research uses one accessible professional game-art collection. This satisfies three inspected relevant image studies per creature, but does **not** provide three direct species depictions per creature or a complete anatomical study. Minotaur, moon stag, frost elemental and slime maiden particularly rely on explicitly identified partial analogs. Additional bovine/deer anatomy and true crystal/gel material studies remain desirable. Do not interpret horse hooves as cloven hooves, fairy membranes as bird feathers, or a mineral-covered arthropod as actual crystals. Most portrait references are cropped, so full-body proportions are original design decisions.

## Credits and usage

Source: [The Battle for Wesnoth portrait collection](https://github.com/wesnoth/wesnoth/tree/master/data/core/images/portraits). Its [README licensing section](https://github.com/wesnoth/wesnoth/blob/master/README.md) states that most art is GPL v2+ and newer art contributions use CC BY-SA 4.0; the repository [COPYING](https://github.com/wesnoth/wesnoth/blob/master/COPYING) is GPL v2. The exact license of each selected image was not established. Treat these as study references only: no copying, tracing, asset extraction or redistribution. Original Minecraft assets use written observations, not reference pixels.

[Project artwork credits](https://github.com/wesnoth/wesnoth/blob/master/data/core/about.cfg) credit Emilien Rotival (LordBob) as portrait director focusing on loyalists, trolls and monsters; James Woo (Pickslide) for portraits with a major orc focus; and Kathrin Polikeit (Kitty) as portrait director focusing on mage/necromancer, elvish, naga, merfolk and troll trees. These are **collection credits**, not verified individual authorship for every selected file. Per-image artist attribution remains unestablished and is recorded that way.

## Visual translation rules

Retain the silhouette features below at gameplay distance. Use large material patches and three-value ramps, minimal noise, articulated appendages and selective emissive accents. Interpret anatomy and material principles; invent shapes, markings, outfits and palettes for this project.

## Goblin Scout — `goblin_scout`

**Palette:** `#596347` · `#382b22` · `#a8986d`. These are proposed original colors, not measured samples.

**Distance silhouette:** Low hunch, long ears, narrow shoulders and an offset blade.

1. [spearman.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/goblins/spearman.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/goblins/spearman.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Large ear, long pointed nose, sloping shoulders and rough leather create a wiry scavenger.
   - **Original translation:** Use stepped ear cuboids and a forward head pivot; keep leather in broad dark patches.
2. [rouser.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/goblins/rouser.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/goblins/rouser.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Cloth headband, layered shoulder mail and dangling trinkets distinguish rank without bulk.
   - **Original translation:** One torn scarf tail and two large bone beads; omit tiny chain detail.
3. [assassin.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/orcs/assassin.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/orcs/assassin.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Masked face, wrapped forearms and separated knives make readiness legible.
   - **Original translation:** Asymmetric wrist wrap and short side blade; preserve the small goblin proportions.

## Goblin Shaman — `goblin_shaman`

**Palette:** `#506936` · `#322e27` · `#7fe85f`. These are proposed original colors, not measured samples.

**Distance silhouette:** Bent caster with a tall crystal staff and hanging charms.

1. [rouser.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/goblins/rouser.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/goblins/rouser.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Aged face, head ties and dangling ceremonial objects suggest a tribal elder.
   - **Original translation:** Extend one head tie and enlarge three pendant silhouettes rather than copying the outfit.
2. [troll-shaman.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/trolls/troll-shaman.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/trolls/troll-shaman.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Paint bands, rope, beads and a bright magical hand contrast a stony dark torso.
   - **Original translation:** Reinterpret as sparse green paint and a luminous staff head, keeping goblin skin organic.
3. [dark-adept+female.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/humans/dark-adept+female.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/humans/dark-adept+female.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Raised open hand surrounds a small pale green magical orb beneath a dark hood.
   - **Original translation:** Animate fingers as a simple grouped hand and stage a green orb before release.

## Orc Warrior — `orc_warrior`

**Palette:** `#4f5739` · `#463c32` · `#b98142`. These are proposed original colors, not measured samples.

**Distance silhouette:** Broad trapezoid torso, projecting tusks and one oversized armored shoulder.

1. [warrior.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/orcs/warrior.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/orcs/warrior.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Open tusked mouth, broad neck, layered reddish armor and a lifted blade emphasize aggression.
   - **Original translation:** Separate jaw/tusk blocks and three large shoulder plates; retain a visible neck.
2. [warlord.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/orcs/warlord.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/orcs/warlord.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Heavy helmet, cloak, mail and warm metal edges convey command and mass.
   - **Original translation:** Offset helmet crest and one thick pauldron; reduce mail to grouped dark pixels.
3. [iron-mauler.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/humans/iron-mauler.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/humans/iron-mauler.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Rounded riveted plate, hard specular edges and dark joints separate steel from straps.
   - **Original translation:** Use three metal tones and sparse rivets, with darker flexible gaps at elbows.

## Minotaur — `minotaur`

**Palette:** `#513c2c` · `#997343` · `#d1bb87`. These are proposed original colors, not measured samples.

**Distance silhouette:** Bull-headed giant, lateral horns, deep chest and split hooves.

1. [troll-warrior.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/trolls/troll-warrior.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/trolls/troll-warrior.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Massive neck and shoulders carrying a large weapon demonstrate weight; this is not a bovine reference.
   - **Original translation:** Use the shoulder-to-waist contrast only, with original bull muzzle and paired horns.
2. [warlord.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/orcs/warlord.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/orcs/warlord.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Helmet and wrapped torso show how warm metal and leather can frame a threatening face.
   - **Original translation:** Build original bronze brow guards around, rather than over, the horn silhouette.
3. [great-horse.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/great-horse.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/great-horse.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Heavy quadruped legs and long muzzle show large ungulate mass; horse feet are not cloven hooves.
   - **Original translation:** Borrow lower-leg taper only; create explicitly split original hooves and bovine head proportions.

## Stone Troll — `stone_troll`

**Palette:** `#555f58` · `#899286` · `#566b38`. These are proposed original colors, not measured samples.

**Distance silhouette:** Unequal huge arms, boulder shoulders and a low stone head.

1. [troll-rocklobber.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/trolls/troll-rocklobber.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/trolls/troll-rocklobber.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Faceted gray shoulders and enormous throwing arm are balanced by a narrow waist and rope.
   - **Original translation:** Build asymmetrical shoulder boulders and a distinct throwing arm with elbow articulation.
2. [troll-warrior.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/trolls/troll-warrior.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/trolls/troll-warrior.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Rock plates have clear light upper planes and dark fissures between chunky forms.
   - **Original translation:** Use broad stone planes with sparse cracks, reserving green pixels for damp seams.
3. [troll-shaman.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/trolls/troll-shaman.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/trolls/troll-shaman.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Warm magic against muted gray stone demonstrates a restrained emissive contrast.
   - **Original translation:** Translate to a few dim mineral seams; keep most rock opaque and unlit.

## Ancient Treant — `ancient_treant`

**Palette:** `#382b22` · `#606537` · `#bed081`. These are proposed original colors, not measured samples.

**Distance silhouette:** Wide branching crown, narrow trunk waist and splayed root feet.

1. [wose.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/woses/wose.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/woses/wose.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** A dark gnarled trunk face sits beneath a broad irregular green canopy and hanging moss.
   - **Original translation:** Use unequal crown branches, a recessed face and separated root toes; avoid a solid leaf cube.
2. [druid.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/elves/druid.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/elves/druid.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Living vines and flowers curve around the arm and shoulders with localized green magic.
   - **Original translation:** Attach sparse vine strips and one fungus shelf, keeping bark the primary material.
3. [troll-rocklobber.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/trolls/troll-rocklobber.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/trolls/troll-rocklobber.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Oversized shoulder and hand provide a useful heavy guardian proportion analog, not wood anatomy.
   - **Original translation:** Turn the large hand into forked wooden fingers and make root recovery slow and deliberate.

## Forest Dryad — `forest_dryad`

**Palette:** `#47633d` · `#4d382a` · `#b5ce77`. These are proposed original colors, not measured samples.

**Distance silhouette:** Slender trunk limbs, leaf mantle and a branching crown.

1. [druid.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/elves/druid.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/elves/druid.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Leaf clothing, a wooden circlet and a flowering vine link humanoid anatomy to vegetation.
   - **Original translation:** Create original bark hips and forearms, with a layered leaf skirt and blossom accent.
2. [shyde.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/elves/shyde.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/elves/shyde.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** A raised arm, trailing sleeve and floating motes establish a graceful outward casting pose.
   - **Original translation:** Use leaf and vine movement instead of copying fairy wings; hands lead the cast arc.
3. [wose.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/woses/wose.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/woses/wose.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Gnarled branching and deep bark seams show the organic construction missing from a plain humanoid.
   - **Original translation:** Split crown branches at unequal heights and run broad bark grooves along limb direction.

## Griffin — `griffin`

**Palette:** `#594839` · `#e4d8b6` · `#b99b4e`. These are proposed original colors, not measured samples.

**Distance silhouette:** Hooked eagle head, layered wings, large chest and feline hindquarters.

1. [gryphon.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/gryphon.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/gryphon.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Hooked yellow beak, pale ruff and layered brown wings provide the direct hybrid design anchor; hindquarters are cropped.
   - **Original translation:** Build a pale stepped ruff, dark wing coverts and an original lion rear body.
2. [falcon.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/falcon.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/falcon.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Full airborne bird shows spread primary feathers, tucked legs and fanned tail.
   - **Original translation:** Use three articulated feather banks per wing; keep leg tucking separate from wingbeats.
3. [roc.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/roc.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/roc.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Huge lifted wing and heavy yellow talons emphasize lift and predatory reach.
   - **Original translation:** Give takeoff a strong upstroke silhouette and large visible talons; preserve saddle clearance.

## Dire Wolf — `dire_wolf`

**Palette:** `#494b49` · `#b4b5a5` · `#cfbd8a`. These are proposed original colors, not measured samples.

**Distance silhouette:** Deep ruff, long muzzle, raised shoulders and low sweeping tail.

1. [direwolver.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/goblins/direwolver.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/goblins/direwolver.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Gray wolf head, thick cheek fur and layered chest ruff frame the rider.
   - **Original translation:** Use stepped mane blocks around a long jaw and keep saddle above the shoulder line.
2. [wolf-rider.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/goblins/wolf-rider.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/goblins/wolf-rider.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Brown-gray wolf muzzle and shaggy cheek create an alert face beneath practical riding straps.
   - **Original translation:** Add broad cheek fur and a thin optional harness; avoid covering the ear silhouette.
3. [great-horse.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/great-horse.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/great-horse.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Full-body weight-bearing stance helps compare mounted quadruped mass; it does not supply canine gait anatomy.
   - **Original translation:** Borrow clear leg spacing and saddle-zone mass only; preserve digitigrade wolf hindlegs.

## Wild Wyvern — `wild_wyvern`

**Palette:** `#49633b` · `#9ba66a` · `#526788`. These are proposed original colors, not measured samples.

**Distance silhouette:** Two wing arms, two hindlegs, long counterbalancing tail and narrow head.

1. [wyvern.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/wyvern.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/wyvern.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** A long neck curls below enormous green membranes carried by jointed wing arms.
   - **Original translation:** Retain two-leg anatomy, with elbow and wrist wing bones plus a segmented balancing tail.
2. [fire-dragon.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/fire-dragon.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/fire-dragon.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Broad belly plates, teeth and horn placement separate reptile surfaces from membrane.
   - **Original translation:** Use original scale blocks and a muted throat stripe; do not add dragon forelegs.
3. [glider.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/drakes/glider.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/drakes/glider.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Folded wings rise into a narrow tall silhouette; pale scales and blue cloth separate surfaces.
   - **Original translation:** Use folding wing pivots and desaturated blue rare-variant membranes, with no copied clothing.

## Cave Basilisk — `cave_basilisk`

**Palette:** `#3e4f3b` · `#7b8061` · `#cad26a`. These are proposed original colors, not measured samples.

**Distance silhouette:** Low reptilian body with armored back, crown crest and a clear gaze point.

1. [crocodile.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/crocodile.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/crocodile.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Low sprawling limbs, long toothed snout and raised dorsal scutes show convincing reptile mass.
   - **Original translation:** Build a low belly, elbowed legs and three broad back ridges; eyes must remain visible.
2. [skirmisher.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/saurians/skirmisher.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/saurians/skirmisher.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Crested reptile head and grouped bright scales give a readable brow and neck silhouette.
   - **Original translation:** Create an original stone crown above the eye line and larger scale groupings.
3. [wyvern.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/wyvern.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/wyvern.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Narrow aggressive head and horn clusters frame a focused eye beneath angular brows.
   - **Original translation:** Borrow head direction and horn rhythm only; keep basilisk wingless and ground-bound.

## Crystal Spider — `crystal_spider`

**Palette:** `#3d294f` · `#865bb2` · `#c9a5e2`. These are proposed original colors, not measured samples.

**Distance silhouette:** Eight clear leg spokes around a raised faceted abdomen.

1. [giant-spider.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/giant-spider.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/giant-spider.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Separated cephalothorax and round abdomen, with eight jointed legs, supply the anatomical anchor.
   - **Original translation:** Keep eight independent articulated legs and a clear narrow connection between body masses.
2. [jumping-spider.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/jumping-spider.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/jumping-spider.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Large forward eyes and blue-violet limb bands demonstrate focal face contrast and segmented color.
   - **Original translation:** Use two dominant bright eyes and a few amethyst joint accents rather than painting every segment.
3. [scorpion-rock.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/scorpion-rock.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/scorpion-rock.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Pale mineral nodules cover a dark arthropod shell; this is not a spider or crystal growth reference.
   - **Original translation:** Replace round nodules with original angular crystals on the abdomen only, leaving leg joints clear.

## Shadow Wraith — `shadow_wraith`

**Palette:** `#252731` · `#555167` · `#9b9dd1`. These are proposed original colors, not measured samples.

**Distance silhouette:** Floating hood and ragged hem with separated hanging forearms.

1. [wraith.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/undead/wraith.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/undead/wraith.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Blue spectral blade and smoky shredded robe contrast with a dark skeletal face.
   - **Original translation:** Use a few pale eye pixels and an opaque dark robe core with restrained edge wisps.
2. [spectre.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/undead/spectre.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/undead/spectre.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Muted green-gray armor fades into haze and thin shredded cloth beneath a raised weapon.
   - **Original translation:** Separate shoulder armor from the tapering lower body; keep strong opacity in the face.
3. [nightgaunt.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/undead/nightgaunt.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/undead/nightgaunt.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Faceless polished helmet and torn diagonal mantle produce an ominous silhouette without facial detail.
   - **Original translation:** Use a recessed hollow face and asymmetric cloth strips; avoid copying the helmet outline.

## Grave Knight — `grave_knight`

**Palette:** `#35373c` · `#79624e` · `#a0babc`. These are proposed original colors, not measured samples.

**Distance silhouette:** Heavy helmet, unequal plate shoulders, long sword and a broken cape edge.

1. [death-knight.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/undead/death-knight.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/undead/death-knight.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Exposed ribs, worn shoulder plates and a tattered cloak make age and undeath legible.
   - **Original translation:** Keep armor coverage heavier, revealing only a narrow cursed eye slit and broken heraldry.
2. [draug.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/undead/draug.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/undead/draug.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Dark spikes, a damaged shield and isolated pale highlights make a powerful ruined soldier.
   - **Original translation:** Use one broken pauldron silhouette and three large chips rather than uniform noise.
3. [iron-mauler.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/humans/iron-mauler.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/humans/iron-mauler.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Strong plate highlights and deep joint shadows explain readable heavy armor construction.
   - **Original translation:** Reserve brightest pixels for upper plate edges; darken cloth and articulation gaps.

## Flame Imp — `flame_imp`

**Palette:** `#512b27` · `#b54c29` · `#ffce6a`. These are proposed original colors, not measured samples.

**Distance silhouette:** Small horned head, broad bat wings and a hooked tail.

1. [bat-red.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/bat-red.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/bat-red.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Red fur, broad wing membranes and finger-supported silhouettes provide the airborne anatomy analog.
   - **Original translation:** Use two wing folds per side and a small heavy head, leaving hands visually separate.
2. [fire_guardian.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/fire_guardian.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/fire_guardian.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Bright branching flame edges against a dark center suggest a readable contained heat source.
   - **Original translation:** Place warm emissive pixels at eyes and chest cracks; use short ember trails.
3. [fire_wraith_A.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/fire_wraith_A.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/fire_wraith_A.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Dark armor embedded in orange flames demonstrates material separation in an infernal palette.
   - **Original translation:** Keep skin charcoal and set bright seams around horn roots and wrists, avoiding full-body glow.

## Frost Elemental — `frost_elemental`

**Palette:** `#344e66` · `#79b2ce` · `#d9f1eb`. These are proposed original colors, not measured samples.

**Distance silhouette:** Jagged broad shoulders around a narrow bright core and separated shard limbs.

1. [big-icemonax.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/big-icemonax.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/big-icemonax.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Lavender-white shell nodules and bright edge facets provide cold mineral contrast, not an ice golem.
   - **Original translation:** Replace rounded nodules with angular original shoulder shards and reserve white for upper edges.
2. [yeti.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/yeti.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/yeti.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Broad pale shoulders, dark face and raised heavy arms demonstrate cold-creature mass and focal contrast.
   - **Original translation:** Borrow upper-body weight distribution only, replacing fur with chunky ice planes.
3. [wraith.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/undead/wraith.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/undead/wraith.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Cyan glow concentrated on a weapon and surrounding haze shows cold emissive staging.
   - **Original translation:** Concentrate cyan in a chest core and sparse fissures; add a low-budget cold mist effect.

## Moon Stag — `moon_stag`

**Palette:** `#abbac1` · `#d8e4dd` · `#8caacc`. These are proposed original colors, not measured samples.

**Distance silhouette:** Slim quadruped, long neck and a huge open branching antler crown.

1. [white-horse.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/white-horse.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/white-horse.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Pale blue-white coat and darker cool mane show restrained moonlit quadruped shading; not deer anatomy.
   - **Original translation:** Use cool light coat bands with dark lower-leg accents; keep original slender deer proportions.
2. [great-horse.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/great-horse.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/great-horse.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Clearly separated four-leg standing pose and rounded chest help check mounted quadruped balance.
   - **Original translation:** Borrow grounded hoof spacing only; narrow the muzzle and make the legs more gracile.
3. [wose.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/woses/wose.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/woses/wose.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Open asymmetrical branching against the dark canopy provides a natural crown rhythm.
   - **Original translation:** Create paired but nonidentical luminous antlers with empty space between tines; omit foliage.

## Slime Maiden — `slime_maiden`

**Palette:** `#2b7d79` · `#69c4b1` · `#c4f1d7`. These are proposed original colors, not measured samples.

**Distance silhouette:** Soft pear-shaped body, looping liquid hair and rounded arm ends.

1. [mudcrawler.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/mudcrawler.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/mudcrawler.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Rounded sagging lobes and smooth drips show deformable substance; its brown rocky surface is not translucent gel.
   - **Original translation:** Translate lobe overlap and dripping edge rhythm into aqua rounded cuboids with coherent highlight bands.
2. [cuttlefish.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/cuttlefish.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/cuttlefish.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Cool teal mantle, smooth wet highlight and curling tentacles show liquid-like contour flow.
   - **Original translation:** Create two broad hair curls and curved arm poses, using sparse pale highlights instead of copied anatomy.
3. [dark-adept+female.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/humans/dark-adept+female.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/humans/dark-adept+female.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Readable feminine face and open-hand orb pose supply a humanoid casting gesture, not slime anatomy.
   - **Original translation:** Use an original friendly face with larger expressive eyes and a grouped liquid casting hand.

## Harpy — `harpy`

**Palette:** `#4b414f` · `#907e81` · `#c4b6a2`. These are proposed original colors, not measured samples.

**Distance silhouette:** Humanoid head and torso merging into large feather wings and taloned legs.

1. [falcon.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/falcon.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/falcon.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Full spread wings, extended talons and fanned tail establish predatory avian movement.
   - **Original translation:** Build stepped primary feather banks and downward-facing talons; articulate wing wrists.
2. [roc.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/monsters/roc.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/monsters/roc.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Raised layered wing presents a powerful dark feather silhouette and striking yellow claws.
   - **Original translation:** Use overlapping dark feather bands and a clear light claw tip at gameplay distance.
3. [shyde.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/elves/shyde.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/elves/shyde.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Humanoid raised arm integrated with wide wings provides a pose composition analog; these are insect wings.
   - **Original translation:** Borrow torso balance only; use original feathered arm-wings and no transparent insect membranes.

## Demon Sorceress — `demon_sorceress`

**Palette:** `#322a3d` · `#79517b` · `#cf7168`. These are proposed original colors, not measured samples.

**Distance silhouette:** Tall horned crown, flowing robe tiers and open floating casting hands.

1. [necromancer+female.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/humans/necromancer+female.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/humans/necromancer+female.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** Dark fitted robe, pale face, curved skull-staff horns and violet smoke establish a strong caster focal hierarchy.
   - **Original translation:** Create original swept head horns and a hovering rune focus, keeping face and hands distinct.
2. [sorceress.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/elves/sorceress.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/elves/sorceress.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** An extended palm and loose hair lead the eye toward fine rising magic beside a wooden staff.
   - **Original translation:** Animate an open-palm anticipation and layered robe panels with dark infernal materials.
3. [nightgaunt.webp](https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/undead/nightgaunt.webp) · [source page](https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/undead/nightgaunt.webp). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.
   - **Observed:** High dark collar, pointed shoulder shapes and shredded trailing cloth offer threatening negative space.
   - **Original translation:** Use two unequal robe tails and a sharp shoulder silhouette without copying the armored face.
