# CODEX ADD-ON: Asset Integration and Visual Refinement

## Project
Repository: https://github.com/lilmigger63-hue/new-monsters

Minecraft: Fabric 1.21.10
Animation system: GeckoLib 5
Compatibility: Better Combat (optional)

## Main objective

Expand the existing creature visual overhaul by finding, downloading, and integrating useful, legally reusable assets from the sources below.

**IMPORTANT: This is a visual refinement, NOT a creature redesign.**

Follow all instructions from the existing visual overhaul prompt. This new prompt adds asset integration requirements without replacing the previous instructions.

Every creature must remain recognizable and maintain its established:
- Appearance and overall silhouette
- Fantasy theme and personality
- Species identity and original description
- Main colors, signature equipment, and abilities
- Relative size and gameplay behavior

The goal is to make the creatures look like professionally finished versions of their current designs.

## 1. Asset sources

Examine these sources and download useful assets where redistribution and modification are permitted:

- Quaternius Ultimate Monsters: https://quaternius.com/packs/ultimatemonsters.html
- Quaternius Ultimate Animated Animals: https://quaternius.com/packs/ultimateanimatedanimals.html
- Quaternius Ultimate RPG: https://quaternius.com/packs/ultimaterpg.html
- Quaternius Cute Animated Monsters: https://quaternius.com/packs/cutemonsters
- OpenGameArt Low Poly Goblin: https://opengameart.org/content/low-poly-goblin-rigged
- Blockbench Workshop GeckoLib models: https://blockbenchworkshop.com/models/geckolib

Use these assets as starting points for geometry, animation, accessories, and textures.

Check the exact license of each downloaded file before integrating it. Use CC0 assets preferentially. Do not include third-party assets whose permissions are unclear.

Never replace an existing creature with an unrelated downloaded model.

## 2. Preserve the three existing creature styles

### Group A — Polished fantasy humanoids

Goblin Scout, Goblin Shaman, Orc Warrior, Minotaur, Stone Troll.

Use available assets to improve model geometry, proportions, rounded edges, material transitions, armor, hands, and weapon grips.

Ensure that weapons follow the correct hand bones and remain naturally aligned throughout idle, walking, attacking, and casting animations.

Keep their existing identities and equipment.

### Group B — Fossils and Archeology-inspired creatures

Ancient Treant, Wild Wyvern, Dire Wolf, Griffin, Cave Basilisk, Frost Elemental, Moon Stag.

Use downloaded animal and monster assets as references for believable anatomical proportions, motion, joints, and secondary movement.

Preserve the organic, detailed, creature-like feeling described in the previous prompt.

Use the supplied Fossils and Archeology JAR for structural and stylistic reference only. Do not transfer copyrighted models, textures, or animations without permission.

Keep each creature's original magical and fantasy characteristics.

### Group C — Anime-inspired female fantasy characters

Forest Dryad, Shadow Wraith, Grave Knight, Slime Maiden, Harpy, Demon Sorceress.

Preserve and improve the feminine anime aesthetic requested in the original prompt.

Refine facial shapes, eyes, hair, clothing, body proportions, expressions, and animation.

Make the designs attractive, expressive, recognizable adult anime-style fantasy characters while keeping their original species identities and combat roles.

Do not turn them into generic humans or copy existing anime characters.

## 3. Asset integration workflow

1. Inspect the existing creature models, textures, animations, and entity renderers.
2. Identify which downloaded assets offer meaningful improvements.
3. Download and inspect suitable files.
4. Record the source and license for every selected asset.
5. Extract only the useful geometry, animation ideas, materials, or accessories.
6. Adapt the selected assets to each creature's established design.
7. Convert or recreate them in Minecraft-compatible GeckoLib model, animation, and texture formats.
8. Preserve the existing bone names where practical; otherwise safely update animation references.
9. Ensure every creature's held weapons, equipment, and effects remain positioned correctly.
10. Keep original entity IDs, spawning, AI, attributes, animations, attacks, taming, riding, and gameplay functionality intact.

Do not replace finished or better-quality existing parts simply because an external asset is available.

## 4. Quality requirements

Every modified creature must have:

- Better model detailing and consistent geometry
- Improved texture definition without losing its original palette
- Natural idle, walking, running, attack, hurt, and death animations where applicable
- Smooth transitions without broken bone movement
- Correct weapon and equipment alignment
- No clipping, detached parts, floating accessories, or severe animation jitter
- Stable rendering and reasonable performance

Keep the original descriptions, sounds, behavior, attacks, and special effects unless a small technical adjustment is essential.

## 5. Required implementation

This is an actual implementation task, not a research or planning exercise.

Make real changes to the repository.

Prioritize reusing suitable legal assets, but custom-build missing parts where necessary.

Do not introduce unnecessary dependencies or replace the existing GeckoLib rendering architecture.

After implementing changes, run the relevant Gradle build, asset validation, and available tests. Test the creatures in-game when a client environment is available.

## 6. Required deliverables

Provide:

- Updated creature model files
- Updated texture files
- Updated GeckoLib animations
- Necessary renderer and attachment fixes
- An asset attribution and license document
- A creature-by-creature before/after change summary
- Build and test results
- A list of any remaining issues

If an external asset cannot be downloaded, converted, or legally reused, document the limitation and continue with an original replacement.

**Final rule: Improve the execution of the existing creature designs, not their fundamental design concepts. The original visual overhaul prompt remains authoritative.**
