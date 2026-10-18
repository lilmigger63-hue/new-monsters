# Original winged / nine-tail expansion artwork

Generator: `tools/generate_expansion_winged.py` (Python 3 + Pillow). Run `python tools/generate_expansion_winged.py`. This creates only Ender Dragon Girl, Succubus, Valkyrie and Fox Spirit Girl resource/native/egg artwork. It changes no existing generator, entity or gameplay source.

| ID | Bones | Cubes | Clips | Design |
|---|---:|---:|---:|---|
| `ender_dragon_girl` | 35 | 122 | 13 | Slender black-haired adult dragon mage; large pale forward-swept horns; violet eyes and inset rune; black-violet scalloped three-bay membrane wings with articulated wrist/ribs; covered long split coat, claw gloves, three-joint pointed tail. |
| `succubus` | 37 | 124 | 13 | Golden blonde adult demon mage; curved dark horns; layered black gown with red lining and gold hems; dark gauntlets, animated gemstone earrings; red bat membranes with separate upper/wrist joints; slender dark pointed tail. |
| `valkyrie` | 32 | 155 | 13 | Silver-haired armored adult warrior; fitted silver breastplate, pauldrons, greaves and faulds; winged helmet, red waist sash; broad black layered seven-primary feather fans; baked sword gripped inside right palm and shield strapped to left forearm. |
| `fox_spirit_girl` | 46 | 130 | 8 | Golden-haired green-eyed adult fox spirit, identified by coordinator as the supplied Nine Tails reference; pointed fox ears, red crossover tunic, pale stockings; **nine** separately anchored two-joint golden fluffy tails in a three-level fan, each with ivory tapered tips and phase-delayed motion. |

All four have a continuous adult clothed bust/waist/hip silhouette, complete scalp caps and seven articulated long hair sections. They share joint conventions rather than costume geometry: species-specific shoulders/hips/face proportions, costume additions, appendages, palettes and painted emblem patterns produce distinct silhouettes. No extra gameplay abilities are implied by animation capability.

## Animation and material details

All models include idle, walk, run, attack, heavy, cast, hurt and death. Impact keyframes preserve the delegated AI windups: Ender/Succubus 22 ticks (1.1s), Valkyrie 14 ticks (.7s), Fox 16 ticks (.8s). Torso anticipation/recovery, shoulders, elbows, wrists, bent knees, hair and costume follow-through are authored. Nine Tails retains its baked radial tail fan under additive animation, with independent base and delayed tip phases.

Each winged species additionally has fly, hover, fold, levitate and teleport visual clips, with wing roots connected to the chest and wrist follow-through. Their default ground states fold the wings alongside the body. Ender/Succubus initially use the existing Demon profile, Valkyrie Scout, Fox Shaman; this artwork does not implement flight AI or new spells.

Every death finishes at .65s. A 129-key support envelope transforms all eight corners of every cube through cube rotations, every rest bone, the folded wing pose and root collapse. Root lift supports the whole silhouette throughout the roll. An independent dense 4,097-time interpolation check measured minimum Y of +.099774px (Ender), +.099790px (Succubus), +.099766px (Valkyrie), +.099893px (Fox). This geometric check does not replace actual-game rendering review.

Original 128px atlases use directional skin planes, hair strands, woven cloth grain, brocade/emblems, stitchwork, engraved brushed metals, membrane veins and feather barbs. All share the established original project material-atlas foundation; additional painting is local to this generator. Runtime base texture bytes exactly match the embedded PNG in each native Blockbench file. Glow masks isolate iris/rune tiles rather than illuminating the whole model.

Each species has original transparent-background 32px spawn egg pixel art: Ender angular violet eye/wing emblem, Succubus red bat/crescent, Valkyrie silver feather/sword insignia, Fox gold fox-mask/tail motif.

## Paths and validation

For each ID the generator writes:

- `src/main/resources/assets/mythic_realms_creatures/geckolib/models/entity/<id>.geo.json`
- `src/main/resources/assets/mythic_realms_creatures/geckolib/animations/entity/<id>.animation.json`
- `src/main/resources/assets/mythic_realms_creatures/textures/entity/<id>.png` and `<id>_glowmask.png`
- `src/main/resources/assets/mythic_realms_creatures/textures/item/<id>_spawn_egg.png`
- `tools/blockbench/<id>.bbmodel`

Verified exporter native/UV/PNG checks for all four; separate checks covered model/bone references, <=180 cubes and <=55 bones, native cube/clip/embedded-PNG parity, all channel vectors finite with keyframe times inside clip lengths, full hair joints, exact nine base-tail joints, actual palm/forearm weapon hierarchy, windup landmarks, death support, glow/egg alpha and 128px/32px image dimensions. Session validation script: `/tmp/check_expansion_winged.py`. Session static front/back silhouette montage: `/tmp/expansion-winged-preview.png` (untextured geometric sanity check, not Minecraft). Python compilation passed.

## Attribution and limits

Geometry, animation, atlas additions and egg pixels were authored independently for this task. No extracted third-party art is included. The coordinator inspected the supplied character screenshots and relayed visual guidance; their exact proprietary costumes/pixels were not copied. Grimoire of Gaia assets are treated as all-rights-reserved reference material. All seven proposed external pack URLs returned 403 to the coordinator, so no pack archive or unverified-license asset is used. The existing original project material painting/export utilities are reused under the project's stated CC0 foundation.

Registration, spawning, AI, item JSON integration, build, dedicated server and actual-game screenshot review belong to the coordinator. This art batch does not claim those checks have already passed.
