# CODEX — COMPLETE SEQUENTIAL MONSTER VISUAL OVERHAUL V3

## PROJECT

Repository:
https://github.com/lilmigger63-hue/new-monsters

Target:
- Minecraft Fabric 1.21.10
- Java 21
- Existing GeckoLib animation architecture
- Existing Mythic Realms: Creatures project

## MAIN OBJECTIVE

Perform an extremely high-quality visual overhaul of ALL 17 specified creatures.

**CRITICAL: Work on exactly ONE creature at a time. Finish its complete visual overhaul, validate it, save the changes, and only THEN begin the next creature.**

Do not generate all models at once.

Do not make superficial color changes and call the work finished.

Use the 17 supplied reference images as the primary visual design source and the existing repository as the technical foundation.

The goal is the maximum achievable resemblance to the supplied images, including anatomy, body proportions, facial features, clothing, colors, accessories, and species-specific characteristics.

Aim for at least 90% visual similarity wherever technically feasible, but never report a numerical similarity percentage unless supported by an actual documented evaluation method.

Prioritize final visual quality over speed.

## 1. EXACT CREATURE ORDER

Process these creatures sequentially, in this order:

### Existing creatures — appearance changes only

1. Harpy
2. Forest Dryad
3. Slime Maiden
4. Minotaur

These four must keep their original AI, health, damage, combat mechanics, registry IDs, hitboxes, natural spawning configuration, and gameplay.

Their models, UVs, textures, and appearance-related animations may be improved only as necessary for visual accuracy.

### Newly added monster girls

5. Vampire
6. Valkyrie
7. Succubus
8. Ender Dragon Girl
9. Centaur
10. Fox Spirit Girl
11. Anubis
12. Kobold
13. Cyclops
14. Dhampir
15. Sahuagin
16. Holstaurus
17. Ashen Wing Girl

Use the existing registry names from the repository. The names above are reference labels and must not cause unnecessary renaming or duplicate registrations.

If the supplied images reveal different official names for Fox Spirit Girl or Ashen Wing Girl, record those names in the documentation, but preserve already existing registry IDs.

## 2. MANDATORY ONE-CREATURE-AT-A-TIME WORKFLOW

For each creature, perform ALL of these steps before proceeding.

### STEP A — Inspect

Identify:
- Entity class.
- Existing model.
- Current geometry and rig.
- Textures and UV mapping.
- Animation files.
- Renderer.
- Weapon attachment points.
- Matching reference image.

Inspect the reference image carefully.

Do not infer details from unrelated character designs.

### STEP B — Analyze visual differences

Document differences in:

1. Overall silhouette.
2. Body height and proportions.
3. Head shape and size.
4. Facial geometry.
5. Eyes and expression.
6. Hair shape, color, and volume.
7. Chest, torso, arms, and legs.
8. Hands and feet.
9. Wings, ears, horns, tails, and other anatomy.
10. Outfit, armor, and accessories.
11. Texture colors, shading, and materials.
12. Weapon design and positioning.

Rank differences by their impact on visual similarity.

### STEP C — Rebuild or improve model

Implement the most important geometry changes first.

Requirements:
- Faithful silhouette.
- Recognizable anatomy.
- Detailed facial structures.
- Properly proportioned limbs.
- Distinct hairstyles.
- Correct clothing shapes.
- Layered armor where necessary.
- Anatomically coherent wings and tails.
- Correct feet placement.
- Appropriate weapon grip.

Avoid oversimplified box-only representations when the reference clearly contains more detail.

Use additional geometry and bones whenever they materially improve appearance.

Optimize unnecessarily dense models without removing essential reference details.

### STEP D — Improve textures

Create original, high-quality textures matching the reference.

Requirements:
- Accurate palette.
- Clear eyes and facial expressions.
- Detailed hair shading.
- Clothing folds and material separation.
- Readable armor details.
- Species-specific markings.
- Correct UV mapping.
- No missing or stretched textures.

Do not directly copy third-party copyrighted textures or models.

### STEP E — Improve animations

Create or refine appropriate animations:

- Idle.
- Walking.
- Running.
- Melee attacks.
- Ranged attacks.
- Magic casting.
- Hurt.
- Death.
- Flying where applicable.
- Swimming where applicable.
- Wing articulation.
- Tail movement.
- Hair secondary motion.

Every creature must move naturally for its anatomy.

Weapon-holding creatures must grip weapons correctly instead of having weapons floating beside the hands.

Preserve existing combat and damage timing.

Do not change server-authoritative mechanics.

### STEP F — Visual validation

Render the model using appropriate available tools.

Compare the updated creature with its assigned reference image.

Use matched camera angles, scale, and lighting wherever possible.

Inspect:
- Front view.
- Side view.
- Three-quarter view.
- Animated movement.

When reference images only show one angle, infer hidden geometry conservatively and document uncertainty.

Identify the three largest remaining differences.

Fix those differences before proceeding.

Perform at least two visual improvement passes when comparison renders are available and further corrections are warranted.

Do not invent screenshots or claim visual inspection when rendering is unavailable.

### STEP G — Technical validation

Before moving to the next creature:

- Validate geometry.
- Validate UVs and texture references.
- Validate animation JSON.
- Validate renderer compatibility.
- Verify the existing entity ID is unchanged.
- Verify unchanged hitbox dimensions.
- Verify AI and attributes are unchanged.
- Verify spawning behavior is unchanged.
- Compile or run focused validation where practical.

Do not continue with a known blocking error.

### STEP H — Save progress

Create a separate logical commit for the creature when the environment permits.

Use a descriptive commit message, for example:

`Visual overhaul: Harpy reference accuracy`

Document:
- Modified files.
- Visual improvements.
- Animation improvements.
- Validation completed.
- Remaining differences.

Only now may the next creature begin.

## 3. SPECIAL CREATURE REQUIREMENTS

### Harpy

Match the supplied feathered Harpy design.

Focus on:
- Wing shape and feather structure.
- Face and hairstyle.
- Feathered arms.
- Legs and talons.
- Clothing and colors.
- Coordinated wing movement.

### Forest Dryad

Match the supplied green fantasy Dryad.

Focus on:
- Face.
- Hair.
- Nature-inspired clothing.
- Body silhouette.
- Green coloration and botanical details.

### Slime Maiden

Match the green Slime Girl reference.

Focus on:
- Slime-like hairstyle.
- Translucent-looking shading where feasible.
- Facial details.
- Body proportions.
- Soft organic silhouette.

### Minotaur

Match the supplied Minotaur reference.

Focus on:
- Horn shape.
- Head proportions.
- Muscular torso.
- Hooves.
- Fur coloration.
- Large hammer and natural weapon grip.

### Vampire and Dhampir

Prioritize:
- Gothic clothing.
- Accurate hairstyles.
- Facial features.
- Accessories.
- Black and red color palettes.

### Valkyrie

Prioritize:
- Wing anatomy.
- Feather layers.
- Helmet.
- Armor.
- Sword attachment.
- Strong but natural combat poses.

### Succubus

Prioritize:
- Horns.
- Wings.
- Hairstyle.
- Facial features.
- Demon-inspired outfit.
- Tail where present in the reference.

### Ender Dragon Girl

Prioritize:
- Black dragon wings.
- Horns.
- Purple eyes.
- Dark clothing.
- Wing joints.
- Dragon anatomy.

### Centaur

Prioritize:
- Horse body proportions.
- Four-leg locomotion.
- Hooves.
- Tail.
- Upper-body integration.
- Natural torso movement.

### Fox Spirit Girl

Prioritize:
- Fox ears.
- Individually modeled tails.
- Hairstyle.
- Outfit.
- Natural tail movement.

### Anubis

Prioritize:
- Jackal ears.
- Facial design.
- Egyptian-inspired accessories.
- Black and gold armor.
- Correct weapon grip.

### Kobold

Prioritize:
- Reptilian face.
- Snout.
- Scales.
- Horns/ears.
- Tail.
- Armor.
- Small body proportions.

### Cyclops

Prioritize:
- One central eye.
- Head geometry.
- Outfit.
- Armor.
- Weapon positioning.

### Sahuagin

Prioritize:
- Aquatic body details.
- Fins.
- Hairstyle.
- Clothing.
- Swimming animation.

### Holstaurus

Prioritize:
- Cow ears.
- Horns.
- Hair.
- Body proportions.
- Cow-pattern details.
- Outfit.

### Ashen Wing Girl

Prioritize:
- Silver-gray hairstyle.
- Red eyes.
- Dark wing-like features.
- Clothing.
- Overall silhouette.

## 4. STRICT GAMEPLAY PRESERVATION

This is not a gameplay overhaul.

DO NOT change:
- Entity registry IDs.
- AI profiles.
- Health.
- Damage.
- Combat logic.
- Attack cooldowns.
- Movement speeds.
- Loot tables.
- Existing spawn eggs.
- Natural spawning configuration.
- Saved-world entity identities.
- Better Combat integration.

CRITICAL SPAWNING REQUIREMENT:

Among the 20 original creatures, ONLY Forest Dryad and Slime Maiden may spawn naturally.

All other original creatures must remain disabled from natural spawning.

The 13 new monster girls retain their intended natural spawning behavior.

Do not accidentally reactivate old creature spawning while editing renderer, assets, or entity registrations.

Preserve existing persistent entities, spawn egg usage, and summon commands.

## 5. REFERENCE-ONLY DESIGN POLICY

Only use:
- User-supplied creature reference images.
- Existing repository code and assets.
- Standard Minecraft/Fabric/GeckoLib development resources.

No external model packs are required.

Create original geometries and texture artwork.

Do not substitute generic models that visibly differ from the references.

Do not copy proprietary Grimoire of Gaia assets into the distributable mod without explicit appropriate permission.

Where the reference does not show enough information, create conservative, visually coherent details.

## 6. QUALITY CONTROL

Do not declare a creature visually finished just because its model loads.

A creature is ready for the next stage only when:
- It compiles and loads correctly where testing is available.
- The model has the correct reference-inspired silhouette.
- Major facial, hair, outfit, and anatomical features are represented.
- There are no obvious missing textures.
- The animation rig works.
- Gameplay has not been unintentionally altered.
- Remaining visual differences are documented.

If visual validation tooling is not available, clearly mark the creature as requiring manual visual review rather than claiming it matches the reference.

For difficult creatures, prioritize faithful geometry over cosmetic extras.

Do not spend excessive effort on secondary details while the main silhouette is still wrong.

## 7. PROGRESS TRACKING AND RESUMABILITY

Create a file:

`docs/monster-visual-overhaul-progress.md`

Maintain a progress table containing:
- Creature name.
- Reference image filename.
- Current stage.
- Model status.
- Texture status.
- Animation status.
- Visual review status.
- Build/test status.
- Commit reference.
- Remaining issues.

Update this file after each creature.

If execution limits interrupt the task:

1. Save all completed source changes.
2. Record the active creature and exact next step.
3. Mark unfinished work honestly.
4. Commit stable progress where possible.
5. Leave the project ready to resume.

On the next Codex run, inspect the progress file and continue from the first unfinished creature.

Never skip creatures silently.

Never overwrite already finished improvements without a clear reason.

## 8. PERFORMANCE

Maintain efficient rendering.

Avoid:
- Excessive model bones.
- Excessively complex geometry without visual benefit.
- Unnecessary animation calculations.
- Per-tick allocation-heavy effects.
- Expensive renderer operations.
- Excessive texture memory usage.

Prefer meaningful geometric detail over arbitrary complexity.

## 9. FINAL VERIFICATION

When all 17 creatures are complete:

1. Build the complete mod.
2. Run automated tests.
3. Verify the mod targets Fabric 1.21.10.
4. Check all 17 model and texture registrations.
5. Check all animation registrations.
6. Check all original entity IDs.
7. Verify gameplay attributes were preserved.
8. Verify spawning restrictions.
9. Verify existing spawn eggs still work.
10. Test dedicated server startup if possible.
11. Produce a visual comparison report.
12. Report remaining known limitations.

Do not claim tests or visual checks that were not performed.

## 10. DELIVERABLES

Deliver:
- Updated repository.
- Improved models for all 17 creatures.
- Improved original textures.
- Updated GeckoLib animations.
- Progress tracking file.
- Per-creature changelog.
- Final buildable JAR.
- Test results.
- Reference comparison images where available.
- Known limitations report.

## START IMMEDIATELY

Begin with Creature 1: Harpy.

Complete its entire visual improvement cycle, validate the implementation, save progress, and then proceed to Forest Dryad.

Continue sequentially through all 17 creatures without requesting confirmation between them, unless a critical ambiguity or blocking issue requires user input.

Do not stop after producing an implementation plan.

Make the actual changes.