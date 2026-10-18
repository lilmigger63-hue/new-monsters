# CODEX MASTER PROMPT — MYTHIC REALMS CREATURE OVERHAUL V2

## PROJECT

Repository: https://github.com/lilmigger63-hue/new-monsters

- Minecraft: Java Edition 1.21.10
- Mod loader: Fabric
- Java: 21
- Animation system: GeckoLib 5
- Optional compatibility: Better Combat
- Task: Complete visual, model, rigging, and animation overhaul of 18 existing creatures.

This is a full implementation task, not a planning or documentation-only task.

**PRIMARY OBJECTIVE:** Transform the existing creatures into highly polished, visually appealing, rounded and organic fantasy mobs, with an aesthetic closer to Hytale NPCs and professionally designed fantasy games than ordinary Minecraft mobs.

Maintain the established identity, colors, personalities, abilities and descriptions of the existing creatures unless the specific changes below require otherwise.

Do not replace the mod or rebuild its gameplay systems.

---

# 1. GLOBAL VISUAL STYLE

## Hytale-inspired model overhaul

Visual reference (IMAGES ONLY):

https://hytalewiki.org/w/NPC

Study the images rather than the article text.

All 18 creatures must receive a shared visual upgrade featuring:

- More rounded-looking geometry.
- Less obvious Minecraft-style cubes and hard 90-degree edges.
- Improved anatomical proportions and silhouettes.
- More detailed but consistent facial designs.
- Better-shaped limbs, hands, feet, shoulders, joints and torsos.
- Smooth-looking transitions between body parts.
- Better texturing and material definition.
- Appropriate proportions for each creature's intended role.
- Natural and expressive animations.
- More convincing weight and momentum during movement.

Achieve this using compatible segmented geometry, bevel-like silhouettes, layered forms, textures and properly organized GeckoLib bones.

Avoid excessively tiny cubes that increase rendering costs without visible benefits.

**IMPORTANT:** Preserve a stylized fantasy voxel aesthetic. The goal is not photorealism. It is to make the creatures more organic, expressive, polished, and visually sophisticated than ordinary Minecraft mobs.

Use original models and textures. External images are visual references, not permission to copy third-party assets.

---

# 2. INDIVIDUAL CREATURE REQUIREMENTS

## GROUP A — FANTASY HUMANOIDS

### 1. Goblin Scout

Give the Goblin Scout a significantly more finished appearance.

Requirements:

- Improve facial geometry and expressions.
- Round out the head, torso, arms, legs and shoulders.
- Improve armor and clothing transitions.
- Improve body proportions while keeping the goblin small and agile.
- Correct how it holds its existing weapon.
- The weapon must be held naturally by the handle, not the blade or shaft's center.
- Align the weapon with the hand and wrist.
- Ensure the grip remains correct while walking, running and attacking.
- Eliminate stiff, robotic arm animations.
- Add subtle shoulder rotation, elbow bending, wrist movement and body follow-through.
- Preserve its established combat role.

The finished Goblin Scout must look nimble, threatening and professionally animated.

### 2. Goblin Shaman

Apply the same level of visual polish as the Goblin Scout.

Requirements:

- More finished body geometry and clothing.
- Better facial proportions.
- Improved magical details.
- Correct staff/weapon attachment directly to the hand at the handle.
- Natural arm and wrist motion.
- Expressive spellcasting movements.
- Less rigid idle and walking animations.
- Smooth magical casting transitions.
- Preserve existing magical attacks and effects.

Its staff must never appear to float or rotate independently of the gripping hand.

### 3. Orc Warrior

Give the Orc Warrior a complete visual refinement.

Requirements:

- Broader muscular silhouette.
- Rounded shoulders and better anatomical proportions.
- More detailed jaw, tusks and facial structure.
- Better-defined armor and equipment.
- Stronger, more convincing weapon-handling animations.
- Natural grip at the weapon handle.
- Heavy, powerful movement rather than stiff body rotation.
- Visible torso rotation and attack follow-through.

Preserve the original Orc Warrior identity and equipment.

### 4. Minotaur

Improve the existing model considerably.

Requirements:

- Stronger and more imposing silhouette.
- More organic head and snout.
- Improved horns with better shape transitions.
- Powerful chest and shoulders.
- More detailed legs and hooves.
- Natural muscular proportions.
- Heavy, convincing movement.
- Better weapon grip and attack animations.

Avoid turning the Minotaur into an ordinary humanoid with a cow head.

Its anatomy should feel genuinely monstrous.

### 5. Stone Troll

Redesign the Stone Troll's proportions while preserving its original stone-creature identity.

Requirements:

- Make the creature noticeably larger and more intimidating.
- Increase torso mass and shoulder width.
- Develop thicker arms and heavier hands.
- Replace the existing face with a monster-like structure dominated by one enormous lower jaw.
- Remove the eyebrows completely.
- Eliminate recognizable human facial proportions.
- Keep any necessary eyes small and deeply recessed, without brow ridges resembling human eyebrows.
- The oversized jaw should create an unmistakable monstrous silhouette.
- Add asymmetrical rocky protrusions.
- Build layered stone plates around the shoulders and back.
- Improve stone textures and cracks.
- Give the monster heavy, weighty animations.

Ensure its enlarged model does not clip into the ground.

Adjust render scale, collision dimensions and eye height only where necessary.

The Stone Troll should look terrifying, massive and ancient.

---

## GROUP B — ORGANIC FANTASY CREATURES

### 6. Ancient Treant

Give the Ancient Treant a significant visual refinement.

Requirements:

- Make the creature wider.
- Increase the width of its torso and shoulders.
- Replace the human-like face with an intimidating nonhuman tree-monster face.
- Integrate its facial features into twisted bark and wooden structures.
- Use deep cracks, knot cavities and jagged wooden formations.
- Make its arms resemble massive branches.
- Add convincing roots and tree-like lower limbs.
- Improve bark, moss and foliage detailing.
- Give the creature an ancient and imposing appearance.
- Improve heavy movement and attack animations.

It must look like a living ancient monster-tree, not a human covered in wood.

### 7. Griffin

Make the Griffin more monstrous and predatory.

Requirements:

- Improve overall anatomy and proportions.
- Give it a more aggressive head and stronger beak.
- Increase the definition of the neck and shoulders.
- Improve feather layering.
- Make the claws and talons more threatening.
- Improve wing proportions.
- Preserve its recognizable griffin anatomy.
- Add more convincing flight and ground movement.
- Ensure wings fold naturally at rest.

The result should look like a dangerous mythical predator rather than a friendly bird-like animal.

### 8. Dire Wolf

Maintain the Dire Wolf's established identity.

Requirements:

- Make the eyebrows angle upward.
- Ensure the brow shape creates an expressive, intimidating wolf appearance.
- Better integrate the brows into the forehead and eye sockets.
- Improve the muzzle, ears, neck, shoulders and tail.
- Add more natural wolf anatomy.
- Improve leg joints and paw geometry.
- Use expressive head movements.
- Improve running, attacking and idle animations.
- Preserve existing colors and behavior.

Do not exaggerate the eyebrows until they resemble artificial human eyebrows.

### 9. Wild Wyvern

Give the Wild Wyvern a major visual overhaul.

**Body and wing reference (IMAGES ONLY):**

https://ice-and-fire-mod.fandom.com/wiki/Dragons

**Head reference (IMAGES ONLY):**

https://fossilsarcheology.wiki.gg/wiki/Ceratosaurus

Requirements:

- Make the Wild Wyvern larger.
- Develop a more powerful dragon-like torso.
- Improve its neck and chest.
- Rebuild its wings with anatomy inspired by the dragon images in Ice and Fire.
- Use convincing wing membranes, long wing supports, strong shoulder attachment and articulated folding.
- Develop a larger, stronger tail.
- Redesign the head using the Ceratosaurus images as inspiration.
- Give the head a recognizable predatory dinosaur silhouette.
- Use a strong elongated muzzle, reptilian jaws and appropriate horn/crest features.
- Avoid making the head simply a copy of an Ice and Fire dragon.
- Maintain the creature's original wyvern identity.
- Keep the correct number of limbs for its existing species design.
- Improve takeoff, landing, walking, flight and attack animations.
- Add natural wing folding and extension.
- Give the tail secondary follow-through motion.

The result should combine a powerful dragon-like body and wings with a dinosaur-inspired predatory head.

Preserve the original abilities, including existing flight and combat mechanics.

### 10. Cave Basilisk

Preserve the Cave Basilisk's existing appearance and species identity.

Required change:

**Give the Cave Basilisk a fedora.**

Requirements:

- Create a properly proportioned fedora with a recognizable crown and brim.
- Fit it naturally to the Basilisk's head.
- Ensure it does not float.
- Avoid severe clipping during head rotation.
- Attach it to the appropriate head bone.
- Match its colors and material treatment to the creature's overall design.
- Keep the fedora visible during normal movement.

Also refine the creature's geometry and animation while preserving its original anatomy.

The fedora is a permanent part of this creature's visual identity.

---

## GROUP C — FEMININE ANIME FANTASY CHARACTERS

All characters in this group should have expressive, feminine adult fantasy designs.

General requirements:

- More anatomically coherent feminine proportions.
- Visible but proportionate bust geometry.
- Better-defined waist, shoulders, torso and hips.
- Improved facial design where a humanoid face is intended.
- Long, properly shaped hair where requested.
- Hair must cover the entire top of the head rather than looking like a small attached block.
- Hair must be integrated with the skull and head shape.
- Use layered hair sections with natural flow.
- Add subtle secondary hair animation.
- Preserve clothing, armor, modesty and established fantasy themes.
- Avoid distorted anatomy or exaggerated proportions that harm animation or readability.

These characters should look like mature anime-inspired fantasy characters while remaining recognizable as their original species.

### 11. Forest Dryad

Requirements:

- Make the face less human-like.
- Add visible feminine bust geometry appropriate to the adult character.
- Blend feminine anatomy with her original plant-like design.
- Create more organic facial structures using wood, bark, leaves or plant-inspired forms.
- Keep the creature beautiful and mysterious while remaining distinctly nonhuman.
- Improve body geometry and foliage.
- Add subtle foliage or hair movement.
- Preserve her established colors and nature-themed abilities.

### 12. Shadow Wraith

Requirements:

- Give the creature a more feminine silhouette.
- Add visible bust geometry.
- Remove the existing human-like face.
- Replace it with a mysterious supernatural face or shadow-like facial structure.
- Add long hair that completely covers the top of the head.
- Create full layered hair with natural length and volume.
- Blend the hair into the overall ghostly appearance.
- Keep the character visibly supernatural rather than turning it into a normal human.
- Preserve the original dark magical style.
- Improve floating and attack animations.
- Add gentle secondary hair and clothing movement.

### 13. Grave Knight

Requirements:

- Give the character a clearly feminine armored silhouette.
- Add proportionate bust geometry integrated with its armor.
- Improve armor fitting around the torso.
- Add long hair covering the entire top of the head.
- Improve hair layering and silhouette.
- Ensure the sword is held correctly by its handle.
- Correct the attachment bone and grip orientation.
- Improve the sword's alignment with the palm, fingers and wrist.
- Fix stiff attacking and walking animations.
- Add body rotation, natural arm movement and sword follow-through.
- Preserve its existing dark knight identity and armor theme.

The sword must stay correctly attached throughout every animation.

### 14. Frost Elemental

Requirements:

- Give the elemental a more feminine silhouette.
- Add visible, proportionate bust geometry.
- Remove the human-like face.
- Replace it with a nonhuman magical ice-elemental facial design.
- Add long hair covering the entire upper head.
- Make the hair resemble magical ice, frost strands or other appropriate elemental materials.
- Use layered shapes with natural movement.
- Improve icy surfaces, crystals and material transitions.
- Keep the creature unmistakably elemental.
- Preserve its existing ice magic and combat abilities.
- Improve floating, movement and casting animations.

### 15. Moon Stag

Redesign the Moon Stag to look like a majestic royal mythical mount.

**Visual reference (IMAGES ONLY):**

https://fossilsarcheology.wiki.gg/wiki/Megaloceros

Requirements:

- Create a majestic king-of-steeds appearance.
- Use the Megaloceros images as the main anatomical and antler reference.
- Develop a more powerful, elegant body.
- Improve the neck, chest, shoulders and legs.
- Create enormous majestic antlers.
- Integrate magical crystals into the antlers.
- Make the crystals look naturally embedded or grown within the antler structure.
- Add subtle magical glow effects.
- Preserve the original lunar fantasy aesthetic.
- Give the creature a regal, powerful presence.
- Improve walking, running and idle animations.
- Ensure the antlers and crystals remain stable during movement.

Maintain its identity as a Moon Stag. Do not replace its deer anatomy with a normal horse model.

Preserve all existing riding and taming functionality where applicable.

### 16. Slime Maiden

Requirements:

- Give the character a more feminine body shape.
- Add proportionate bust geometry.
- Add long hair covering the entire top of the head.
- Create layered hair that fits the existing slime aesthetic.
- Make the hair look like a cohesive part of the slime body.
- Improve transparent/translucent-looking material treatment using supported rendering techniques.
- Preserve the slime identity.
- Improve body deformation and animation.
- Add subtle secondary motion to hair and slime surfaces.
- Prevent major clipping and detached geometry.

### 17. Harpy

**Wing reference (IMAGES ONLY):**

https://fossilsarcheology.wiki.gg/wiki/Confuciusornis

Requirements:

- Give the Harpy a more feminine adult body.
- Add proportionate bust geometry.
- Add long hair covering the entire top of the head.
- Rebuild the wings using the Confuciusornis images as anatomical inspiration.
- Ensure the wings have convincing feather shapes and proportions.
- Scale the wings to fit the Harpy's torso.
- Make wing attachments anatomically consistent with the existing body.
- Improve wing folding and extension.
- Create natural feather layering.
- Improve flying, landing and attacking animations.
- Preserve the Harpy's existing fantasy identity.

The wings must look physically integrated rather than attached like decorative flat panels.

### 18. Demon Sorceress

Requirements:

- Give the character a more feminine adult silhouette.
- Add proportionate bust geometry.
- Add long, full hair covering the entire top of the head.
- Improve layered hair volume and shape.
- Maintain recognizable demon characteristics.
- Improve horns and facial expressions where appropriate.
- Improve clothing and magical accessory geometry.
- Add natural arm, hand and finger-equivalent posing for casting.
- Improve spellcasting animation.
- Add subtle hair movement.
- Preserve all existing abilities and magical effects.

The finished character should look like a polished anime-inspired demon sorceress rather than a standard blocky Minecraft humanoid.

---

# 3. ANIMATION OVERHAUL

All creatures must receive animation improvements appropriate to their anatomy.

Focus on:

- Natural head and torso rotation.
- Correct joint pivots.
- More expressive idle movement.
- Better walking and running cycles.
- Attack anticipation and follow-through.
- Natural recovery after attacks.
- Smooth wing motion for flying creatures.
- Secondary hair and tail movement where applicable.
- Reduced stiffness.
- Consistent animation timing.

Do not replace attack timing in ways that desynchronize server-side combat logic.

## Weapon attachment system

For Goblin Scout, Goblin Shaman, Orc Warrior, Minotaur and Grave Knight:

1. Find the existing weapon attachment system.
2. Identify the correct hand bones.
3. Align each weapon's actual handle with the gripping palm.
4. Correct position, rotation and scale.
5. Keep the grip consistent during all animations.
6. Use appropriate arm and wrist rotations.
7. Prevent the weapon from floating, clipping through hands or appearing stuck to the forearm.
8. Ensure Better Combat compatibility remains intact where relevant.

Test idle, walking, attacking, casting and recovery poses.

Never fake weapon attachment with an unrelated floating transform.

---

# 4. MODEL AND TEXTURE IMPLEMENTATION

Use the current mod architecture and GeckoLib version.

Where possible, update existing:

- `.geo.json` model files.
- `.animation.json` animation files.
- `.png` textures.
- Renderer code and render states.
- Attachment transforms and animation controllers.

Use Blockbench-compatible geometry.

For rounded-looking bodies, use a controlled combination of layered shapes, sensible geometry segmentation, texture shading and model-part transitions.

Do not introduce a high-poly system that performs poorly inside Minecraft.

For enlarged creatures, consider visual scale, collision dimensions, navigation, rider offsets, camera clipping, shadow size and interaction reach. Do not alter gameplay balance unnecessarily.

Avoid unnecessary changes to Java entity logic.

---

# 5. PERFORMANCE OPTIMIZATION

The overhaul must not cause a significant FPS reduction.

Requirements:

- Reuse existing textures and materials where practical.
- Minimize unnecessary individual model cubes.
- Avoid excessive animation controllers.
- Reduce unnecessary per-frame calculations.
- Reuse efficient animation patterns where appropriate.
- Avoid excessive translucent geometry.
- Minimize render-layer changes.
- Keep particle effects within reasonable limits.
- Avoid allocating new objects unnecessarily during rendering.
- Keep visual improvements focused on noticeable details.

Use a measured performance baseline where testing is available.

Do not sacrifice major visual requirements merely to reduce file sizes.

---

# 6. CODEX TOKEN AND CREDIT OPTIMIZATION

## Efficiency protocol: `CREATURE_OVERHAUL_EFFICIENT`

Follow these instructions throughout development:

### A. Inspect once, reuse findings

Perform one focused inspection of the repository.

Identify the relevant model, animation, texture, renderer and entity files.

Create a compact working manifest listing the paths and responsibilities of each creature.

Do not repeatedly inspect files whose contents and structure are already known unless they have changed.

### B. Work in focused batches

Process the overhaul in the following order:

1. Shared visual and animation infrastructure.
2. Goblin Scout and Goblin Shaman.
3. Orc Warrior, Minotaur and Stone Troll.
4. Ancient Treant, Griffin, Dire Wolf and Wild Wyvern.
5. Cave Basilisk and Moon Stag.
6. Forest Dryad, Shadow Wraith and Grave Knight.
7. Frost Elemental, Slime Maiden, Harpy and Demon Sorceress.
8. Final testing and corrections.

Complete actual model and animation work in every batch.

Do not stop after producing a plan.

### C. Avoid wasteful operations

- Do not repeatedly summarize the entire project.
- Do not regenerate unchanged files.
- Do not run full builds after every minor modification.
- Do not perform unnecessary web searches.
- Do not download the same reference assets repeatedly.
- Do not produce excessive progress messages.
- Do not repeatedly rewrite the same model from scratch without identifying a defect.
- Do not change unrelated files.
- Do not recreate existing infrastructure unnecessarily.

### D. Reuse proven solutions

When one creature receives a working weapon-handling solution, reuse the underlying approach for other compatible humanoids.

When one rigging technique works, adapt it to related creatures where appropriate.

Use shared helper code only when it genuinely reduces duplication.

Do not force anatomically different creatures to use identical rigs.

### E. Efficient testing

After each major batch:

- Validate model and animation JSON.
- Check model bone references.
- Check resource paths.
- Run focused tests where available.

Run a full Gradle build at meaningful milestones and after the final batch.

Do not run the entire test suite repeatedly without a reason.

### F. Concise reporting

After each completed batch, report only:

- Creatures completed.
- Important files changed.
- Tests performed.
- Outstanding issues.

Do not output large unchanged files in chat when modifications are already saved in the repository.

### G. Accuracy over artificial token limits

Minimize redundant reasoning and tool calls.

However, never skip necessary implementation, debugging, validation or safety checks merely to save tokens.

If context is nearly exhausted, save a concise implementation checkpoint containing completed creatures, changed paths, test status and next actions.

Resume from that checkpoint instead of restarting the entire analysis.

The objective is maximum useful implementation per credit, not minimum token usage at the expense of quality.

---

# 7. REFERENCE HANDLING

These links are visual references:

Hytale NPCs:
https://hytalewiki.org/w/NPC

Ice and Fire dragons:
https://ice-and-fire-mod.fandom.com/wiki/Dragons

Fossils and Archeology Ceratosaurus:
https://fossilsarcheology.wiki.gg/wiki/Ceratosaurus

Fossils and Archeology Megaloceros:
https://fossilsarcheology.wiki.gg/wiki/Megaloceros

Fossils and Archeology Confuciusornis:
https://fossilsarcheology.wiki.gg/wiki/Confuciusornis

**Only analyze the visual images on these reference pages. Ignore the page articles and unrelated information.**

Do not copy proprietary models, textures or animations from those mods.

If a page cannot be accessed, document the limitation and continue using the provided visual design descriptions and available original assets. Do not spend excessive tokens repeatedly retrying inaccessible pages.

Any previously provided reusable asset packs may be used only after verifying the individual asset license.

The supplied Fossils and Archeology Forge JAR, if present in the workspace, may be inspected for visual reference and structural ideas. Do not treat it as a Fabric dependency or copy its proprietary assets.

---

# 8. PRESERVE EXISTING FUNCTIONALITY

Do not break:

- Creature spawning.
- AI behaviors.
- Combat abilities.
- Server-controlled attacks.
- Magic projectiles.
- Existing loot tables.
- Biome configuration.
- Taming systems.
- Mount riding and controls.
- GeckoLib integration.
- Better Combat compatibility.
- Multiplayer synchronization.
- Dedicated server startup.

Keep existing creature registry IDs and saved-world compatibility.

Do not add unrelated mobs or major gameplay systems.

---

# 9. TESTING REQUIREMENTS

Before declaring completion:

1. Validate all 18 creature models.
2. Validate every changed animation.
3. Check all model and texture paths.
4. Verify that weapons are attached correctly.
5. Check all enlarged creature dimensions.
6. Check wing folding and flight animations.
7. Check hair positioning and secondary motion.
8. Check the Cave Basilisk's fedora.
9. Confirm that original entity behavior remains intact.
10. Run the Gradle build.
11. Run available relevant tests.
12. Perform in-game checks where the environment allows.

If client-side visual testing is unavailable, do not falsely claim that every model has been visually verified.

Provide a clear list of what has and has not been tested.

---

# 10. FINAL DELIVERABLES

Implement the changes directly in the existing repository.

Deliver:

- All 18 updated creature models.
- Updated textures as needed.
- Updated GeckoLib animation files.
- Fixed weapon attachment transforms.
- Updated rendering code where necessary.
- Improved performance where practical.
- Successful build results.
- Testing results.
- A concise visual changelog covering every creature.

Do not submit only an implementation plan.

Finish with a brief completion report showing which requirements were met.

## FINAL EXECUTION DIRECTIVE

Begin inspecting the existing repository immediately, then implement the overhaul in the specified batches.

Do not ask for repeated confirmations between batches.

Respect existing creature identities and functionality while fully applying the specific appearance changes.

Prioritize visible quality, functional correctness, stable performance and efficient Codex token usage.

**The final result should look like an original high-quality fantasy creature mod with polished Hytale-inspired styling, better anatomy and dynamic GeckoLib animations, while remaining completely functional on Fabric 1.21.10.**