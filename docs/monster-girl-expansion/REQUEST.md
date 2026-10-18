# CODEX TASK — MYTHIC REALMS: CREATURES — MONSTER GIRL EXPANSION V1

## 1. Project and primary objective

Repository: https://github.com/lilmigger63-hue/new-monsters

Target: Minecraft Java Edition 1.21.10, Fabric, Java 21.

Extend the existing Mythic Realms: Creatures mod. Do not create an unrelated replacement mod.

Implement:
- Exactly 13 new fantasy monster-girl entities.
- Visual-only overhauls of 4 existing creatures.
- Strict natural spawning changes.
- 13 new custom fantasy-style spawn eggs.
- Reusable AI profiles based on 4 existing entities.
- Appropriate GeckoLib animations, original textures, models, and attack effects.
- Future-proof architecture for additional creatures and advanced AI.

Do not stop at planning. Make the actual source, asset, registry, and data changes, build the project, fix errors, and run relevant tests.

Preserve existing working functionality unless explicitly changed in this specification.

## 2. Reference material

Use the attached reference images and the supplied Grimoire of Gaia JAR as visual, technical, and gameplay research material.

Reference JAR:
`GrimoireOfGaia4-1.20.1-4.0.0-alpha.12.jar`

This is a Forge 1.20.1 mod and is NOT a Fabric 1.21.10 dependency.

Inspect it only as necessary to understand creature concepts, general model proportions, animations, behaviors, and asset organization.

IMPORTANT COPYRIGHT RULES:
- Do not extract and redistribute proprietary Grimoire of Gaia models, textures, audio, or other copyrighted assets without appropriate permission.
- Create original, independently implemented Minecraft-compatible models and textures inspired by the supplied screenshots.
- Do not reproduce third-party copyrighted character designs exactly.
- Record the source and license of any third-party asset included.
- The final mod must work independently of the reference JAR.

## 3. New creatures — exactly 13

Add these entities:

1. Ender Dragon Girl
   - Dark dragon-themed girl.
   - Black wings, horns, purple eyes and dark clothing.
   - End-related magical effects.
   - Initial AI profile: Demon Sorceress.

2. Vampire
   - Gothic vampire girl with a dark-red and black color palette.
   - Humanoid appearance and vampire-inspired visual effects.
   - Initial AI profile: Goblin Scout.

3. Holstaurus
   - Cow-themed humanoid fantasy girl.
   - Horns, ears, cow-pattern elements and matching clothing.
   - Initial AI profile: Slime Maiden.

4. Centaur
   - Female humanoid upper body with a four-legged horse body.
   - Detailed legs, tail, armor, and weapon-holding animations.
   - Initial AI profile: Goblin Scout.

5. Sahuagin
   - Aquatic fantasy girl with fins and ocean-inspired clothing.
   - Suitable underwater and surface movement animations.
   - Initial AI profile: Goblin Scout.

6. Valkyrie
   - Armored winged warrior.
   - Metal armor, helmet, sword, and large feathered wings.
   - Initial AI profile: Goblin Scout.

7. Fox Spirit Girl
   - Temporary name until the reference image is identified.
   - Fox ears and multiple fluffy tails.
   - Fantasy clothing inspired by the supplied reference.
   - Initial AI profile: Goblin Shaman.

8. Anubis
   - Egyptian fantasy-inspired jackal girl.
   - Black ears, Egyptian-style armor and golden accessories.
   - Initial AI profile: Goblin Scout.

9. Kobold
   - Small reptilian monster girl.
   - Armor, tail, reptilian details, and a small melee weapon.
   - Initial AI profile: Goblin Scout.

10. Cyclops
    - Female humanoid with one central eye.
    - Blue and gold armor with a large weapon.
    - Initial AI profile: Goblin Scout.

11. Dhampir
    - Dark fantasy vampire-hunter girl.
    - Black/red clothing, hat, and a handheld weapon.
    - Initial AI profile: Goblin Scout.

12. Succubus
    - Adult-looking demon girl.
    - Horns, demon wings, black/red fantasy clothing.
    - Initial AI profile: Demon Sorceress.

13. Ashen Wing Girl
    - Temporary name until the reference image is identified.
    - Silver-gray hair, red eyes, pale fantasy clothing, and dark wing-like features.
    - Initial AI profile: Goblin Shaman.

Use the supplied reference images to refine the appearance and correctly identify the two temporarily named creatures if possible.

No boss system is required for this phase.

## 4. Four existing creatures — visual changes only

The following entities already exist and MUST NOT be duplicated:

- Harpy
- Minotaur
- Slime Maiden / Slime Girl
- Forest Dryad / Dryad

Update them according to the four supplied screenshots.

Harpy:
- Change appearance to the supplied brown-feathered Harpy reference.
- Retain existing attack AI, movement, attributes, and mechanics.

Minotaur:
- Change appearance to the supplied horned Minotaur reference with the large hammer.
- Retain existing combat behavior and gameplay balance.

Slime Maiden:
- Change appearance to the supplied green Slime Girl reference.
- Preserve existing AI, behavior, attributes, interactions, and natural spawning.

Forest Dryad:
- Change appearance to the supplied green Dryad reference.
- Preserve existing AI, behavior, attributes, interactions, and natural spawning.

For all four:
- Preserve original entity registry IDs.
- Preserve save compatibility.
- Preserve existing animations and animation timing unless minor visual adjustments are necessary to fit the new models.
- Do not create duplicate entities.
- Do not change AI, attack logic, health, damage, loot, or other gameplay mechanics.
- Prefer texture-only edits where sufficient.
- Where texture edits cannot reproduce the silhouette, modify only the client-side geometry/rig required for the appearance.
- Preserve existing hitbox dimensions.

## 5. CRITICAL — Natural spawning rules

All 20 original entities must remain registered and usable.

Only TWO original creatures may continue spawning naturally:

- Forest Dryad (`forest_dryad`)
- Slime Maiden (`slime_maiden` or its existing registry ID)

ALL OTHER ORIGINAL ENTITIES MUST HAVE NATURAL SPAWNING DISABLED.

This explicitly includes:
- Harpy
- Minotaur
- Goblin Scout
- Goblin Shaman
- Demon Sorceress
- Every other original entity, including mounts and rare variants.

Do not disable these creatures entirely.

They must still be accessible through:
- Their existing spawn eggs.
- Summon commands.
- Existing persistent world entities.
- Other intentional manual/admin spawning mechanisms.

Remove original natural spawn registrations, biome spawn entries, and any equivalent registrations that would otherwise make these creatures appear naturally.

Check special spawn registrations and alternative variants to avoid accidental natural spawning.

All 13 NEW monster girls must receive appropriate natural biome spawning.

Assign different biome tags, spawn weights, spawn group sizes, light conditions, and rarity based on their species.

Avoid excessive spawning and unnecessary server load.

Do not accidentally remove vanilla mobs or spawning from other mods.

Add automated tests where feasible to verify that:
- Exactly the 2 specified original species retain natural spawning.
- No other original species are added to natural spawn tables.
- All 13 new species have intended spawning support.
- Disabled natural spawning does not break spawn eggs or manual summon commands.

## 6. Reusable AI architecture

Reuse and generalize the existing AI implementations of:

1. Goblin Scout
2. Goblin Shaman
3. Slime Maiden
4. Demon Sorceress

Do not duplicate large amounts of AI source code for every new entity.

Build reusable AI profiles or shared goal components.

Allow species-specific configuration for:
- Movement speed.
- Attack range.
- Attack damage.
- Cooldowns.
- Detection range.
- Target selection.
- Aggression.
- Magical projectile type.
- Combat particles.
- Animation triggers.

Initial AI profiles only need existing functional behaviors.

Do not build a complex new AI system yet.

IMPORTANT:
- Preserve the original four AI implementations' gameplay.
- Keep the new architecture extensible so unique species-specific behavior can be added in future updates.
- Use server-authoritative combat and keep animation/network state synchronized.

## 7. 3D models and animations

Create original, visually polished 3D models inspired by the attached screenshots.

Requirements:
- Detailed block-based Minecraft fantasy style.
- Smooth-looking silhouettes achieved with suitable geometry.
- Anime-inspired faces and proportions.
- Correct anatomy for wings, tails, horns, ears, legs, and arms.
- No missing or floating model parts.
- Appropriate attachment points for weapons.
- Natural weapon grips.
- Correct entity scaling.
- Correct visual-ground alignment.

Where appropriate, supply GeckoLib animations for:
- Idle.
- Walking.
- Running.
- Melee attack.
- Ranged/magic attack.
- Hurt.
- Death.
- Flying.
- Swimming.

Flying and swimming animation requirements only apply to species with those capabilities.

Avoid stiff, stationary limbs during movement.

Use efficient rigs and sensible polygon/part counts.

No unnecessary animation controllers, per-frame allocations, or excessively expensive particle effects.

Verify that gameplay and animations are synchronized.

## 8. Textures and artwork

Create new original fantasy-style texture artwork for every new entity.

Design priorities:
- Recognizable anime-inspired monster-girl appearance.
- Species-specific features.
- Clear facial details.
- Cohesive fantasy color palette.
- Readable armor and clothing details.
- Visually consistent texture quality.
- No missing UV mapping.

For the four existing entities, prioritize the supplied reference looks while retaining their existing gameplay.

## 9. Spawn eggs

Every one of the 13 new species needs a separately registered spawn egg.

Create new custom egg textures instead of giving all new creatures identical vanilla-looking eggs.

Differentiate eggs using:
- Species-specific colors.
- Fantasy symbols.
- Small identifying patterns.
- Readable pixel-art silhouettes.

Keep the original spawn eggs working.

Ensure each new spawn egg summons its correct entity and has a proper display name.

## 10. Technical integration

Inspect the current project before modifying it.

Reuse its existing:
- Fabric architecture.
- Java version.
- Entity registration conventions.
- GeckoLib animation system.
- Combat utilities.
- Networking patterns.
- Attribute registration.
- Loot tables.
- Spawn egg infrastructure.
- Resource organization.

Maintain compatibility with Minecraft Fabric 1.21.10.

Keep Better Combat integration working without making Better Combat a mandatory dependency.

Do not use unsupported APIs or Forge-only code.

Avoid unnecessary new dependencies.

Ensure client-only renderer classes never load on dedicated servers.

## 11. Performance and quality

The mod must remain suitable for ordinary modded survival gameplay.

Optimize:
- AI tick behavior.
- Target searches.
- Animation controllers.
- Entity rendering.
- Particle counts.
- Natural spawn frequency.

Do not sacrifice basic functionality just to reduce code size.

Reuse shared implementations where technically reasonable.

Avoid unbounded scans, entity targeting loops, and excessive network packets.

## 12. Implementation workflow

Follow this order:

1. Inspect the complete repository.
2. Identify all 20 original entity IDs and their spawning registrations.
3. Identify the four existing AI implementations.
4. Inventory the supplied screenshots and reference JAR.
5. Establish an exact per-creature reference mapping.
6. Implement and verify natural spawning restrictions.
7. Implement four existing visual updates without gameplay changes.
8. Create reusable AI profiles.
9. Implement the 13 new entity types.
10. Implement their models, textures, and GeckoLib animations.
11. Implement fantasy-style spawn eggs.
12. Add spawning, attributes, and loot data.
13. Build the mod.
14. Run tests and fix errors.
15. Verify behavior in a client and dedicated server where practical.
16. Produce a final report describing completed features and remaining limitations.

Do not claim that something was tested unless it actually was.

Do not silently omit entities or assets.

## 13. Acceptance criteria

The task is complete only when:

- All 13 new creatures are registered and implemented.
- Each new creature has a working model and texture.
- Each new creature has appropriate functional animations.
- All 13 new spawn eggs work.
- All 13 new creatures have natural spawning registrations.
- Only Dryad and Slime Maiden of the original 20 spawn naturally.
- The other 18 original creatures no longer spawn naturally.
- All original entities still work through manual spawning.
- The original Harpy, Minotaur, Dryad, and Slime Maiden have updated visuals.
- The four existing creatures retain their original gameplay behavior.
- Existing registry IDs and save compatibility are preserved.
- The project builds successfully on Fabric 1.21.10.
- Required dependencies are documented.
- Any unimplemented or untested requirements are explicitly reported.

## 14. Final deliverables

Provide:
1. Complete updated source code in the existing repository.
2. All original new models, textures, and animation files.
3. Updated spawn registrations and spawn egg artwork.
4. Automated tests where appropriate.
5. A buildable Fabric 1.21.10 mod JAR.
6. Updated README and changelog.
7. An asset licensing/attribution report.
8. A concise verification report including tests run and results.

Use small, verifiable commits or development milestones.

Work systematically and prioritize a fully functional result over placeholder content.

START BY INSPECTING THE EXISTING REPOSITORY AND IMPLEMENTING THE CHANGES. DO NOT STOP AFTER WRITING A PLAN.