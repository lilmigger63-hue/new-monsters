# CODEX V5.3 — ULTIMATE REFERENCE FIDELITY VISUAL OVERHAUL

## PROJECT INFORMATION

Target repository:
https://github.com/lilmigger63-hue/new-monsters

Grimoire of Gaia reference repository:
https://github.com/Silentine/GrimoireOfGaia

Target platform:
- Minecraft Java Edition 1.21.10
- Fabric
- Java 21
- Existing GeckoLib architecture

## 1. PRIMARY OBJECTIVE

Perform the highest-quality practical VISUAL-ONLY overhaul of the 13 newly added monster girls in the existing Mythic Realms: Creatures mod.

The objective is to make every monster girl resemble its supplied reference images as closely as legally, technically, and artistically possible.

Prioritize:

1. Legally permissible reference fidelity.
2. Accurate overall silhouette.
3. Detailed and coherent anatomy.
4. Accurate facial features and hairstyles.
5. Species-specific body geometry.
6. Clothing, armor, and accessories.
7. High-quality original textures.
8. Natural GeckoLib animations.
9. Correct rendering and performance.
10. Efficient token and credit usage.

Visual quality takes priority over implementation speed.

Do not settle for superficial texture changes when significant geometry improvements are necessary.

However, do not spend time rewriting already successful work without a concrete visual reason.

This task is VISUAL ONLY.

DO NOT CREATE, REPLACE, REMOVE, OR MODIFY SOUNDS.

DO NOT MODIFY GAMEPLAY.

## 2. INITIAL REPOSITORY INSPECTION

Before modifying files:

1. Inspect the latest committed repository state.
2. Verify the correct Minecraft and dependency versions.
3. Identify all 13 target entities and their actual registry IDs.
4. Locate their models, renderers, textures, and animation files.
5. Identify reusable GeckoLib systems.
6. Identify reference image files available in the workspace.
7. Record relevant current gameplay configurations.
8. Create a separate development branch.

Perform shared project analysis only once.

Create:

`docs/monster-girl-v5-3-inventory.md`

Include:
- Entity name.
- Registry ID.
- Model path.
- Texture path.
- Animation path.
- Renderer path.
- Reference image path.
- Current visual limitations.

Avoid repeatedly scanning the whole project for each creature.

If a reference image is unavailable, request it before making reference-dependent changes.

## 3. EXACT CREATURE SCOPE

Improve ONLY the following 13 existing new creatures:

1. Ender Dragon Girl
2. Vampire
3. Holstaurus
4. Centaur
5. Sahuagin
6. Valkyrie
7. Fox Spirit Girl
8. Anubis
9. Kobold
10. Cyclops
11. Dhampir
12. Succubus
13. Ashen Wing Girl

Map these display names to the actual entity registry IDs.

Do not create replacement entities or duplicate registrations.

Do not rename existing entity IDs.

All 20 original creatures are outside the scope of this project.

## 4. REFERENCE AND COPYRIGHT POLICY

Use the user-provided reference images as the primary artistic direction.

Use the Grimoire of Gaia repository only as a supplementary reference for aesthetic concepts and legally reusable technical information.

Important:

- The Grimoire of Gaia code is CC0 except for protected artwork.
- Models and textures remain owned by their creator.
- Publicly available assets are not automatically free to redistribute.
- Do not copy or redistribute proprietary assets without appropriate permission.
- Do not assume manually rebuilding a copyrighted model makes an exact reproduction legal.
- Create original character models, UV maps, and textures unless explicit permission covers reuse.
- Do not use unlicensed third-party sound or art assets.
- Record asset origin and licensing where applicable.

When exact reproduction is not authorized, preserve the fantasy species, aesthetic direction, and broadly recognizable design qualities while introducing sufficient original character design choices.

Maintain maximum lawful reference fidelity without falsely claiming copyrighted material can be reused freely.

## 5. MANDATORY SEQUENTIAL WORKFLOW

Work on EXACTLY ONE creature at a time.

Complete that creature's model, textures, animation improvement, visual validation, and technical validation before proceeding to the next.

Do not make large uncontrolled changes across multiple creatures simultaneously.

For EACH creature:

### STAGE A — Focused inspection

Inspect:
- Existing geometry.
- Existing UV mapping.
- Existing textures.
- Existing GeckoLib animations.
- Existing renderer.
- Matching reference images.

Identify the five most important remaining visual differences.

Focus on changes that materially improve reference fidelity.

Avoid lengthy repeated analysis.

### STAGE B — Geometry improvement

Improve or rebuild the model where necessary.

Priorities:

- Overall silhouette.
- Head and face geometry.
- Eye shape and position.
- Hair volume and layering.
- Neck, shoulders, torso, and hips.
- Arms, hands, legs, and feet.
- Species-specific wings, tails, horns, ears, fins, or claws.
- Clothing and armor geometry.
- Accessories.
- Weapon grips and attachment positions.

Use additional geometry and bones when necessary for meaningful visual improvements.

Do not preserve a poor existing model merely to save implementation time.

If the existing geometry fundamentally prevents accurate representation, rebuild the affected model while retaining its current entity compatibility.

Avoid wasteful geometry that provides no visible benefit.

### STAGE C — Texture overhaul

Improve original textures to match the reference-inspired visual design.

Requirements:

- Accurate and consistent fantasy color palettes.
- Detailed but readable facial features.
- Improved eyes and expressions.
- Layered hair shading.
- Species-appropriate fur, skin, scales, or other material patterns.
- Fabric, leather, and metal differentiation.
- Improved clothing and armor details.
- Proper UV alignment.
- No missing texture faces.
- No unintended stretching or obvious seams.

Choose texture resolution based on visible benefit and model complexity.

Do not increase resolution without a meaningful quality gain.

### STAGE D — Cosmetic animation overhaul

Refine existing GeckoLib animations.

Where appropriate:

- Idle.
- Walking.
- Running.
- Existing melee attacks.
- Existing ranged or magical attacks.
- Hurt.
- Death.
- Flying.
- Swimming.
- Wing articulation.
- Tail movement.
- Hair secondary motion.

Important:

- Preserve existing combat and gameplay timing.
- Preserve all attack triggers.
- Preserve movement physics.
- Avoid stiff limbs.
- Avoid unnatural joint movement.
- Minimize foot sliding.
- Correct weapon alignment.
- Prevent obvious clipping.
- Maintain existing server-client synchronization.

Do not implement new skills or combat mechanics.

### STAGE E — Visual comparison and refinement

When rendering or Minecraft client inspection is available:

1. Render the improved model.
2. Reproduce the reference camera angle as closely as practical.
3. Compare silhouettes and proportions.
4. Compare faces, hairstyles, and anatomy.
5. Compare outfits, armor, colors, and accessories.
6. Identify the three largest remaining legally correctable differences.
7. Implement targeted improvements.
8. Render and compare again.

Continue refinement while substantial visible differences remain and improvements are demonstrably useful.

Avoid endless minor adjustments that provide no meaningful progress.

For token efficiency, prioritize major shape and facial differences before small texture details.

Do not invent similarity percentages.

Do not claim visual validation without actual renders or client inspection.

### STAGE F — Technical validation

Verify:
- Valid geometry and model JSON.
- Valid texture paths and UV coordinates.
- Valid GeckoLib animation data.
- Correct renderer registration.
- Existing entity ID preserved.
- Existing hitbox unchanged.
- AI and gameplay preserved.
- Existing spawning preserved.
- Existing sounds unchanged.

Run focused tests first.

Build the complete mod whenever necessary to validate integration or investigate errors.

Fix blocking failures before proceeding.

### STAGE G — Commit and continue

After a creature is complete:

1. Save modified source and assets.
2. Document key visual improvements.
3. Record unresolved reference differences.
4. Record actual validation results.
5. Commit stable changes where practical.
6. Update the progress file.
7. Begin the next creature.

Never silently skip a creature.

## 6. SPECIES-SPECIFIC DESIGN PRIORITIES

### Ender Dragon Girl
- Distinctive dragon wings.
- Dark fantasy silhouette.
- Horns.
- Purple eyes.
- Detailed hairstyle.
- Layered clothing.
- Natural wing articulation.

### Vampire
- Elegant gothic silhouette.
- Hair and facial details.
- Dark red and black costume.
- Accessories and layered fabric.

### Holstaurus
- Correct cow ears and horns.
- Hairstyle and face.
- Species-specific markings.
- Faithful fantasy clothing and proportions.

### Centaur
- Coherent humanoid and horse anatomy.
- Four correctly proportioned horse legs.
- Hooves and tail.
- Correct torso connection.
- Natural quadrupedal locomotion.

### Sahuagin
- Aquatic anatomy.
- Fins and distinctive facial features.
- Hair and marine-themed clothing.
- Swimming motion.

### Valkyrie
- Large feathered wings.
- Distinct armor silhouette.
- Helmet.
- Hair and face.
- Sword-holding pose.
- Coordinated wing animation.

### Fox Spirit Girl
- Fox ears.
- Multiple individually shaped tails.
- Correct tail placement.
- Hairstyle and clothing.
- Natural secondary tail movement.

### Anubis
- Jackal-inspired features.
- Facial structure.
- Egyptian-inspired costume and accessories.
- Black and gold materials.
- Correct weapon pose.

### Kobold
- Reptilian facial structure.
- Snout.
- Horns or ears as appropriate.
- Tail.
- Small body proportions.
- Armor details.

### Cyclops
- Exactly one central eye.
- Correct facial geometry.
- Armor and clothing.
- Proper weapon attachment.

### Dhampir
- Gothic hat.
- Hairstyle.
- Face.
- Red and black outfit.
- Weapon positioning.

### Succubus
- Horns.
- Demon wings.
- Hairstyle and facial details.
- Dark fantasy clothing.
- Wing motion.

### Ashen Wing Girl
- Silver-gray hair.
- Red eyes.
- Distinct silhouette.
- Pale clothing.
- Dark wing-like features.

## 7. STRICT GAMEPLAY AND AUDIO PRESERVATION

DO NOT CHANGE:

- Sounds or sound resources.
- Sound registrations.
- AI or target selection.
- Entity IDs.
- Health.
- Damage.
- Armor.
- Movement speed.
- Movement physics.
- Combat mechanics.
- Attack cooldowns.
- Projectile behavior.
- Hitbox dimensions.
- Natural spawning.
- Spawn weights.
- Loot.
- Spawn eggs.
- Items or recipes.
- Taming or riding.
- Structures or world generation.
- The 20 original creatures.
- Better Combat integration.

Only Forest Dryad and Slime Maiden among the original 20 may spawn naturally.

The other 18 original species must retain disabled natural spawning.

All 13 new species must retain their existing spawning behavior.

Do not modify protected gameplay systems simply to improve rendering.

If a visual change would require a gameplay change, choose a visual-only alternative and document the limitation.

## 8. CREDIT AND TOKEN OPTIMIZATION

Maintain high visual quality while reducing redundant operations.

Use:
- One initial repository inventory.
- Focused file reads.
- Existing GeckoLib infrastructure.
- Shared utilities where appropriate.
- Targeted changes instead of unnecessary rewrites.
- Concise progress reports.
- Static asset validation.
- Integration builds at meaningful milestones.

Avoid:
- Repeated full project scans.
- Rewriting working entity systems.
- Duplicating models unnecessarily.
- Excessively verbose intermediate reports.
- Running a full Gradle build after trivial changes.
- Unnecessary external searches.
- Recreating completed work.
- Editing unrelated code.
- Any audio work.

Perform full builds after creatures 4, 8, and 13, plus whenever technical correctness requires it.

Never omit necessary tests solely to conserve credits.

Visual quality, compatibility, and correctness remain more important than token minimization.

## 9. PROGRESS TRACKING

Create:

`docs/monster-girl-v5-3-progress.md`

Track:

- Creature.
- Actual registry ID.
- Reference file.
- Model status.
- Texture status.
- Animation status.
- Visual comparison status.
- Validation results.
- Remaining differences.
- Commit ID.
- Next required action.

If the task is interrupted:

1. Save all stable changes.
2. Commit finished creatures where practical.
3. Record exactly where work stopped.
4. Do not claim unfinished work is complete.

On a future Codex run, inspect this progress document and resume from the first unfinished step.

Do not automatically redo completed creatures.

## 10. FINAL VALIDATION

After all 13 creatures are complete:

1. Build the complete mod for Fabric 1.21.10.
2. Run relevant automated tests.
3. Validate all 13 model registrations.
4. Validate all textures and UV maps.
5. Validate all GeckoLib animations.
6. Test rendering in a Minecraft development client where available.
7. Confirm all 33 entities remain registered.
8. Confirm registry IDs and hitbox dimensions are unchanged.
9. Confirm AI, combat, and gameplay attributes are unchanged.
10. Confirm natural spawning rules are unchanged.
11. Confirm original sound resources and registrations are unchanged.
12. Test dedicated-server startup where available.
13. Document the actual results.
14. Report unresolved visual differences and technical limitations.

Do not fabricate visual comparison results or test outcomes.

## 11. FINAL DELIVERABLES

Deliver:

- Improved original 3D models for all 13 new monster girls.
- Improved texture artwork.
- Corrected UV mapping.
- Refined cosmetic GeckoLib animations.
- Necessary client-side renderer improvements.
- Updated code and assets in the existing repository.
- Progress documentation.
- Per-creature changelog.
- Asset provenance and licensing notes.
- Visual comparison screenshots where possible.
- Buildable Minecraft Fabric 1.21.10 JAR.
- Honest build and test report.

No sound modifications.

No gameplay modifications.

No changes to the 20 original creatures.

## 12. EXECUTION

Begin with the latest committed state of the existing repository.

Create a separate development branch.

Perform the one-time inspection and reference mapping.

Start with Ender Dragon Girl.

Finish its entire visual overhaul and validation cycle before moving to Vampire.

Continue sequentially until all 13 creatures have been processed.

Do not ask for confirmation between creatures unless an essential reference or legally required permission is missing.

Do not stop after planning.

MAKE THE ACTUAL CODE AND ASSET CHANGES.

The final objective is the highest-quality legally permissible reference-inspired visual result for all 13 monster girls, with complete gameplay preservation and efficient credit usage.