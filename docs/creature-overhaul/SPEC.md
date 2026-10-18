# MYTHIC REALMS: CREATURES — ULTIMATE DARK FANTASY OVERHAUL

## PROJECT

Repository: https://github.com/lilmigger63-hue/new-monsters

Mod: Mythic Realms: Creatures

Target: Minecraft Java Edition 1.21.10, Fabric, Java 21, GeckoLib 5.

## PRIMARY MISSION

Perform a complete, professional-quality visual and gameplay overhaul of **all 20 existing fantasy creatures**.

First, research and collect high-quality visual reference images for EVERY creature. Then use those references to redesign and improve the actual in-game models, textures, animations, special effects, combat behavior, and presentation.

**IMPORTANT: Do not simply write a plan. Inspect the repository, research references, and make actual implementation changes.**

The final result should feel like a professionally developed dark fantasy Minecraft creature expansion.

Visual inspiration:
- Dark Souls and Elden Ring: imposing silhouettes, mysterious magic, ancient monsters.
- The Witcher: believable fantasy anatomy, folklore creatures, organic textures.
- World of Warcraft: recognizable silhouettes and expressive animations.
- High-quality Minecraft fantasy mods: readable pixel art and designs that belong in Minecraft.

Use these only as aesthetic inspiration. Create original artwork rather than copying protected designs or textures.

The creatures should be detailed, intimidating, beautiful, or mysterious depending on their nature, while preserving the Minecraft visual language.

**The ZIP that contains this file includes four original illustration references:**
- `images/01_ancient_treant.png`
- `images/02_grave_knight.png`
- `images/03_moon_stag.png`
- `images/04_demon_sorceress.png`

Review those images as a moodboard, **not** as final Minecraft textures/models. They are illustrative concepts, not reference research for all 20 species. Find additional real sources for each species as required below.

---

# PHASE 1 — REPOSITORY INSPECTION

Before modifying anything:

1. Inspect the entire repository and read README.md, docs/PROGRESS.md, Gradle configuration, Java source files, asset generators, and testing scripts.
2. Locate every registered creature, its model, textures, glowmasks, animation files, renderer, AI, combat controller, attributes, loot, and spawning configuration.
3. Inspect existing GeckoLib bone hierarchies and Blockbench models.
4. Identify graphical weaknesses, broken animation transitions, unconvincing silhouettes, repetitive textures, and missing creature-specific details.
5. Record the current working build and test results.
6. Create a separate working branch and preserve existing functionality.

Important existing architecture:

- Assets use namespace `mythic_realms_creatures`.
- GeckoLib geometry and animations are under `src/main/resources/assets/mythic_realms_creatures/geckolib/`.
- Creature PNG textures are under `textures/entity/`.
- Groups A/B have Python asset generators.
- Groups C/D have generated assets and editable Blockbench projects in `tools/blockbench/`.
- Existing resources use 128×128 textures, including special variants and glowmasks.
- Server-authoritative combat and mount behavior must be preserved.

Understand which assets are generated and which files are the source of truth. Update generators and editable sources when necessary so regeneration does not erase the overhaul.

---

# PHASE 2 — FIND REAL REFERENCE IMAGES FOR ALL 20 CREATURES

Use available web browsing and image search tools.

Search sources such as ArtStation, Pinterest, DeviantArt, OpenGameArt, Wikimedia Commons, professional fantasy concept-art portfolios, and publicly available bestiaries.

For EACH creature:

1. Find at least 3 relevant, genuinely existing images, ideally including a full-body design, an anatomical or silhouette reference, and a color/material or VFX reference.
2. Record exact source URLs and artist credits when available.
3. Prefer images that show clear anatomy, character proportions, distinctive body features, armor, clothing, wings, horns, claws, or magical effects.
4. Explain what makes each reference useful.
5. Describe how to translate the visual features into original Minecraft-compatible geometry and textures.
6. Identify which design features must remain recognizable at Minecraft gameplay distances.
7. Record the image's license or usage restrictions when discoverable.
8. Never invent URLs, authors, image licenses, or claim that an image was inspected when it was not.

Create:

`docs/creature-overhaul/REFERENCE_ATLAS.md`

Include every creature's name, image URLs, artist/source credits, visual analysis, color palette, silhouette description, and proposed improvements.

Create a structured machine-readable reference file too.

For images without a compatible reuse license, store only the URL, credit, and your own written analysis. Do not commit unauthorized copies.

If image generation is available, optionally produce ORIGINAL front/side/back concept sheets inspired by the research. Otherwise create precise model specifications and diagrams.

**Do not begin arbitrary redesigns without considering the reference research.**

---

# PHASE 3 — INDIVIDUAL CREATURE OVERHAUL

Every creature must receive a unique design and a meaningful upgrade.

## 01. Goblin Scout — `goblin_scout`

Reference searches: dark fantasy goblin scout, medieval goblin raider, goblin rogue concept art.

Visual direction:
- Small, wiry, hunched anatomy.
- Oversized ears, sharp nose, asymmetrical teeth.
- Torn leather armor, rope bindings, scavenged metal plates.
- Rusty daggers, pouches, bone ornaments.
- Dirty moss-green skin with scars and markings.

Animations:
- Sneaking and scouting.
- Fast irregular running.
- Sideways dodging and circling.
- Quick stabbing attack sequences.
- Startled, hurt, and death reactions.

Gameplay improvements: smarter pack cooperation and flanking with clear, fair attack warnings.

## 02. Goblin Shaman — `goblin_shaman`

Reference searches: dark fantasy goblin witch doctor, tribal shaman, green necromancer.

Visual direction:
- Hunched mystical spellcaster.
- Wooden staff with glowing green crystal.
- Hanging skulls, feathers, bones, and talismans.
- Torn robes and mystical face paint.
- Glowing eyes and corrupted magical ornaments.

Animations:
- Complex staff casting.
- Floating green runes.
- Healing rituals.
- Summoning-like hand gestures.
- Magical anticipation and recovery.

VFX: layered green spell circles, swirling particles, glowing staff crystal, and distinctive healing effects.

## 03. Orc Warrior — `orc_warrior`

Reference searches: dark fantasy armored orc warrior, brutal orc berserker, medieval orc concept.

Visual direction:
- Massive muscular frame, broad shoulders.
- Large tusks, scars, fierce facial expression.
- Heavy asymmetrical iron armor.
- Fur, leather straps, battle trophies.
- Oversized brutal weapon.

Animations:
- Weighty footsteps.
- Heavy swings and powerful recovery poses.
- Blocking, battle roars, stagger reactions.
- More realistic upper-body movement.

Combat: threatening but readable attack patterns and improved defensive behavior.

## 04. Minotaur — `minotaur`

Reference searches: dark fantasy minotaur, labyrinth beast, armored bull monster.

Visual direction:
- Huge muscular bull-headed humanoid.
- Distinct horns, large hooves, thick neck.
- Realistic bovine anatomy adapted to Minecraft.
- Ancient bronze armor and battle damage.
- Heavy double-handed weapon.

Animations:
- Head lowering before charging.
- Violent running and impact.
- Wide weapon sweeps.
- Heavy breathing and intimidation.
- Strong knockback animations.

VFX: ground dust, debris, charge trails, and impact shockwaves.

## 05. Stone Troll — `stone_troll`

Reference searches: fantasy cave troll, mossy stone giant, Nordic rock troll.

Visual direction:
- Enormous irregular rocky body.
- Uneven proportions and oversized arms.
- Moss, cracked stone, ancient mineral deposits.
- Jagged rocky shoulders and spine.
- Subtle glowing cracks.

Animations:
- Heavy asymmetric walking.
- Boulder throwing.
- Ground slams.
- Body-weight shifts and slow recovery.

VFX: falling rock fragments, ground dust, cracks, and impact debris.

## 06. Ancient Treant — `ancient_treant`

Reference searches: ancient treant, dark forest guardian, living tree monster, ancient ent.

Visual direction:
- Ancient walking tree with twisted roots.
- Branching antlers and crown-like canopy.
- Bark-covered face, glowing eyes.
- Moss, vines, fungi, leaves.
- Giant wooden hands and root-like feet.

Animations:
- Slow, deliberate walking.
- Branch and leaf movement.
- Root attacks emerging from the ground.
- Ancient guardian awakening.
- Nature magic preparation.

VFX: roots, drifting leaves, spores, faint forest lights.

## 07. Forest Dryad — `forest_dryad`

Reference searches: forest dryad concept art, woodland spirit, dark fantasy nature guardian.

Visual direction:
- Elegant supernatural forest spirit.
- Natural wooden anatomy combined with organic humanoid features.
- Flowing leaf-and-vine clothing.
- Branching horns or a natural wooden crown.
- Luminous eyes, small flowers, and magical growth.

Animations:
- Graceful walking and idle movement.
- Living vines extending from arms.
- Floating leaves and healing gestures.
- Expressive environmental interactions.

VFX: living vines, magical green runes, healing blossoms, glowing pollen.

## 08. Griffin — `griffin`

Reference searches: realistic fantasy griffin, eagle lion hybrid, armored griffon mount.

Visual direction:
- Powerful eagle/lion hybrid.
- Detailed feathered head and neck.
- Large layered wings.
- Muscular feline body.
- Talons, beak, elegant tail.
- Distinct saddle and tamed-state details.

Animations:
- Wing folding and unfolding.
- Walking, running, takeoff, flight, hovering.
- Gliding and landing.
- Aerial claw attacks.
- Perching and resting.

Ensure ridden animations and rider positioning work correctly.

## 09. Dire Wolf — `dire_wolf`

Reference searches: dark fantasy dire wolf, giant ancient wolf, armored fantasy wolf.

Visual direction:
- Large predatory wolf anatomy.
- Thick layered fur.
- Powerful shoulders, legs, and jaws.
- Scarred face and intimidating eyes.
- Optional tasteful tamed-state equipment.

Animations:
- Quadruped walk and gallop.
- Growling and sniffing.
- Pouncing, biting, shaking prey.
- Lying down and resting.
- Mount sprinting and jumping.

Keep riding stable and natural.

## 10. Wild Wyvern — `wild_wyvern`

Reference searches: dark fantasy wyvern, two-legged dragon anatomy, fantasy wyvern concept sheet.

Visual direction:
- Proper wyvern silhouette with two rear legs and two large wings.
- Extended reptilian neck and powerful tail.
- Horns, scales, claws, teeth.
- Jagged wing membranes.
- Distinct rare blue and tamed variants.

Animations:
- Natural wingbeats.
- Smooth gliding, hovering, takeoff, landing.
- Tail movement and poison attacks.
- Ground movement and threat displays.
- Proper rider alignment.

VFX: toxic breath, venom droplets, poison clouds and subtle magical eye glow.

---

## 11. Cave Basilisk — `cave_basilisk`

Reference searches: fantasy basilisk reptile, medieval basilisk creature, petrifying cave monster.

Visual direction:
- Sinister reptilian body with a distinctive crown or crest.
- Heavy scales and rocky growths.
- Sharp claws, predatory head.
- Glowing petrifying eyes.

Animations: stalking, coiling, staring, lunging, and recovering.

VFX: focused gaze beam, stone-colored magic, subtle petrification buildup.

Keep its existing gaze gameplay and telegraph readable.

## 12. Crystal Spider — `crystal_spider`

Reference searches: fantasy crystal spider, gemstone arachnid, magical cave spider.

Visual direction:
- Eight individually articulated legs.
- Accurate spider body proportions.
- Crystal clusters growing from its exoskeleton.
- Amethyst-like color palette.
- Glowing crystal abdomen and mandibles.

Animations: eight-leg gait, wall climbing, crystal casting, web attacks.

VFX: crystal fragments, prismatic particles, glowing web traps, crystal projectile trails.

## 13. Shadow Wraith — `shadow_wraith`

Reference searches: dark fantasy wraith, spectral knight spirit, ghostly reaper.

Visual direction:
- Floating spectral silhouette.
- Torn robes and fragmented armor.
- Hollow face, supernatural eyes.
- Wispy limbs and fading edges.
- Dark mist surrounding its body.

Animations: eerie hovering, floating turns, casting, appearing and dissipating.

VFX: shadow smoke, cursed particles, spectral afterimages, subtle translucent effects.

Ensure translucency depth sorting remains acceptable in the actual renderer.

## 14. Grave Knight — `grave_knight`

Reference searches: cursed knight dark fantasy, undead medieval armor, black knight concept art.

Visual direction:
- Heavy medieval plate armor.
- Damaged helmet, worn cape.
- Rust, ancient engravings, broken heraldry.
- Glowing supernatural eyes.
- Terrifying dark knight silhouette.

Animations:
- Realistic three-hit sword combinations.
- Shield/guard stance.
- Heavy final strike.
- Weapon weight and recovery.
- Dramatic death animation.

VFX: sparks, dust, dark energy accents, clear heavy-attack anticipation.

## 15. Flame Imp — `flame_imp`

Reference searches: fantasy fire imp, small infernal demon, mischievous fire elemental.

Visual direction:
- Small demonic flying creature.
- Horns, bat-like wings, tail.
- Clawed hands, mischievous expression.
- Burnt skin and glowing molten accents.

Animations: erratic flight, mischievous hovering, fire casting, wing flaps, evasive maneuvers.

VFX: ember trails, fiery projectiles, glowing eyes, small smoke wisps.

## 16. Frost Elemental — `frost_elemental`

Reference searches: fantasy frost elemental, living ice golem, ancient ice spirit.

Visual direction:
- Body composed of angular ice and frozen stone.
- Floating crystalline components where technically practical.
- Glowing blue magical core.
- Jagged frost-covered shoulders.
- Cold mist and fractured surfaces.

Animations: floating shards, ice attacks, frost nova, heavy movement.

VFX: detailed ice spikes emerging from the ground, crystalline projectiles, freezing shockwaves, snow and frost particles.

## 17. Moon Stag — `moon_stag`

Reference searches: mystical moon stag, celestial deer spirit, enchanted forest deer.

Visual direction:
- Elegant deer anatomy.
- Massive branching luminous antlers.
- Silvery fur, celestial patterns.
- Moonlight-inspired eyes.
- Subtle supernatural markings.

Animations: graceful walking, galloping, jumping, resting and head movement.

VFX: drifting moonlight particles, delicate healing rings, soft antler glow.

Protect taming and riding functionality.

## 18. Slime Maiden — `slime_maiden`

Reference searches: fantasy slime girl character design, translucent slime elemental girl, cute fantasy gelatinous spirit.

Visual direction:
- Distinct feminine humanoid slime silhouette.
- Original expressive face and hairstyle.
- Translucent gelatinous body.
- Liquid-like hair and clothing forms.
- Small floating bubbles inside the body.
- Aquamarine or emerald glowing accents.

Animations:
- Squash-and-stretch bouncing.
- Gelatinous secondary motion.
- Expressive idle poses.
- Liquid arm casting.
- Slime bubble attacks.

VFX: floating bubbles, liquid splashes, elastic impacts, soft translucent glow.

Avoid making the model appear like a rigid rectangular humanoid. Prioritize charming, expressive animation and believable slime motion.

## 19. Harpy — `harpy`

Reference searches: dark fantasy harpy, bird woman monster concept, mythological harpy creature sheet.

Visual direction:
- Distinct humanoid-avian anatomy.
- Large feathered wings integrated into the body.
- Taloned legs and sharp claws.
- Wild flowing hair or feather crests.
- Layered feathers and rugged fantasy accessories.

Animations:
- Dynamic wing flapping.
- Midair hovering.
- Rapid swooping attacks.
- Talon strikes.
- Feather projectiles.
- Perching and landing.

VFX: feather trails, gusts of wind, air-slicing effects.

## 20. Demon Sorceress — `demon_sorceress`

Reference searches: dark fantasy demon sorceress, infernal witch character, horned demon mage, cursed fantasy enchantress.

Visual direction:
- Powerful supernatural female demon mage.
- Elegant but sinister silhouette.
- Distinct horns and glowing eyes.
- Intricate dark robes or infernal armor.
- Magical tattoos, runes and ornaments.
- Floating magical accessories where feasible.

Animations:
- Expressive hand and finger casting poses.
- Floating spell circles in front of the hands.
- Dark magical projectiles.
- Teleporting and reappearing.
- Levitation and intimidating idle poses.

VFX: layered purple/red magic circles, infernal flames, swirling sigils, shadow bolts and teleport distortion.

Make her visually recognizable as a dangerous, highly skilled magical creature.

---

# PHASE 4 — PROFESSIONAL 3D MODELS

For each creature:

- Create a detailed, distinctive GeckoLib-compatible model.
- Improve silhouette, anatomy, proportions, geometry and pivots.
- Use additional articulated bones when they meaningfully improve movement.
- Make wings, tails, ears, horns, hair, clothing and other important features animate correctly.
- Avoid unnecessary geometry and overlapping faces.
- Preserve the correct world scale, collision dimensions, movement and rider positioning.
- Check models from front, side, back and multiple gameplay distances.
- Use Blockbench-compatible editable source files.
- Keep the game performance reasonable when multiple creatures spawn.

Do not use identical generic humanoid models for unrelated creatures.

Each creature must be recognizable from its silhouette alone.

# PHASE 5 — HIGH-QUALITY PIXEL ART TEXTURES

Create handcrafted-looking, original creature textures informed by the research.

Improve:
- Material separation.
- Subtle pixel shading.
- Fur, feathers, scales, skin, wood, stone, metal and fabric.
- Faces, eyes and expressions.
- Natural color variation.
- Damage, scars, armor, ornaments and magical markings.

Retain 128×128 where suitable, or upgrade resolution only when a demonstrated visual improvement justifies it.

Avoid noisy random-colored procedural textures masquerading as detailed artwork.

Check UV mapping carefully, including any alternate variants and glowmasks.

Create coherent color palettes across the mod while giving each species its own identity.

# PHASE 6 — ADVANCED GECKOLIB ANIMATIONS

Redesign existing animations into polished, creature-specific movements.

Support existing states such as idle, walk, run, attack, cast, hurt, death, fly, hover, tame, sit and ride wherever applicable.

Add appropriate secondary motion and transitions, including:

- Breathing and natural idle movement.
- Weight shifts and anticipation.
- Tail, wing, cloth, ear and hair movement.
- Distinct turning and locomotion.
- Attack recovery and reaction poses.
- Species-specific magical casting.
- Environmental details such as treant branch movement and slime deformation.

Animation must respect the existing actual GeckoLib 5 runtime and supported APIs.

Synchronize important hit frames with server-authoritative combat timing. Do not move damage logic to the client.

Avoid animation snapping, extreme clipping, floating feet, sliding quadrupeds and invalid bone references.

# PHASE 7 — MAGICAL VISUAL EFFECTS

Give magical creatures unique and impressive VFX.

Prioritize:
- Magic circles that appear at the correct hand or staff positions.
- Glowing symbols, layers and rune rotation.
- Element-specific particles.
- Projectile trails.
- Ground eruptions and area effects.
- Teleportation effects.
- Good cast anticipation and impactful hits.

Use emissive textures and transparent rendering where supported.

Keep effects synchronized to real game actions.

Add appropriate distance culling, particle budgets and configurable intensity.

Never create excessive client particles or expensive per-tick allocations.

# PHASE 8 — IMPROVE AI AND COMBAT

Review each creature's current combat design before modifying it.

Improve:
- Target selection.
- Navigation and attack positioning.
- Melee range and timing.
- Telegraphs for dangerous attacks.
- Creature-specific combat identity.
- Fair damage and cooldown balance.
- Group tactics where appropriate.
- Flying enemy behavior.
- Guardians' defensive behavior.

Preserve existing taming, ownership, riding, spawning, loot and config behavior.

Do not introduce overpowered abilities or break peaceful/neutral interactions.

Any new mechanic should reinforce the creature's established identity and have appropriate tests.

# PHASE 9 — IMPLEMENTATION ORDER

Work in manageable batches:

Batch A:
Goblin Scout, Goblin Shaman, Orc Warrior, Minotaur, Stone Troll.

Batch B:
Ancient Treant, Forest Dryad, Griffin, Dire Wolf, Wild Wyvern.

Batch C:
Cave Basilisk, Crystal Spider, Shadow Wraith, Grave Knight, Flame Imp.

Batch D:
Frost Elemental, Moon Stag, Slime Maiden, Harpy, Demon Sorceress.

For each batch:
1. Complete reference research and document image URLs.
2. Improve models and editable source files.
3. Create improved textures and variants.
4. Upgrade animations.
5. Upgrade relevant VFX and combat behavior.
6. Build, test and visually inspect.
7. Fix problems before moving on.
8. Save progress with a clear Git commit.

Continue until every batch is complete, subject to available tools, time and usage limits.

# PHASE 10 — TESTING AND VISUAL VALIDATION

Use the repository's existing commands, including:

Windows:
`gradlew.bat clean build`

`gradlew.bat runGametest`

`gradlew.bat -PwithBetterCombat runGametest`

`python scripts/test-assets.py`

Use the available graphical client smoke-test workflow or runClient to validate real in-game rendering.

Check all 20 creatures and their animations. Capture screenshots where graphical testing is available.

Test:
- GeckoLib model loading.
- Missing textures, models or animations.
- Broken bones and UV mappings.
- Emissive layers and transparency.
- Movement and attack animation timing.
- Spawn eggs, loot and biome spawning.
- Multiplayer-safe authoritative behavior.
- Tameable creature ownership and mounts.
- Optional Better Combat compatibility.
- Client and dedicated-server stability.

Do not claim that a test passed unless it actually ran and passed.

Fix regressions introduced by the overhaul.

# PHASE 11 — SAVE REFERENCES, PROGRESS AND RESULTS

Create and maintain:

`docs/creature-overhaul/REFERENCE_ATLAS.md`

`docs/creature-overhaul/DESIGN_GUIDE.md`

`docs/creature-overhaul/PROGRESS.md`

`docs/creature-overhaul/VALIDATION.md`

The progress document must show each creature's status for reference research, model, textures, animations, VFX, behavior, and testing.

Update these documents as work is completed, not just at the end.

If interrupted by context limits or usage allowance exhaustion, preserve completed work, document the exact next unfinished step, and make the task resumable without repeating already completed work.

Do not attempt to bypass usage limits or falsely claim automatic continuation.

# FINAL QUALITY REQUIREMENTS

The result should be:

- Visually impressive.
- Cohesive dark fantasy.
- Highly distinctive for every creature.
- Professionally animated.
- Faithful to each creature's original identity.
- Technically clean and maintainable.
- Stable on Fabric 1.21.10.
- Optimized for reasonable gameplay performance.
- Compatible with the existing mod systems.

**Critical rules:**

Do not stop after creating documentation.

Do not replace detailed models with simplified placeholders.

Do not erase existing features to make the build easier.

Do not fabricate reference links or validation results.

Do not change Minecraft version or break required mod compatibility.

Do not perform destructive repository operations without approval.

Use research to inform ORIGINAL assets.

Prioritize actual visible improvements over cosmetic code refactoring.

Start immediately by auditing the repository and collecting reference images for all 20 creatures, then implement the overhaul batch by batch.

**The task is only complete when all 20 creatures have received their upgrades and the final build, asset tests, and supported gameplay tests have been verified.**
