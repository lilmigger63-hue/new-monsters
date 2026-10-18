"""Write the inspected-reference catalog. No downloaded artwork is copied into the repo."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
# Entries describe what was actually visible in contact sheets, not inferred anatomy.
SPECIES = [
('goblin_scout','Goblin Scout','#596347 #382b22 #a8986d','Low hunch, long ears, narrow shoulders and an offset blade.',[
('goblins/spearman','Large ear, long pointed nose, sloping shoulders and rough leather create a wiry scavenger.','Use stepped ear cuboids and a forward head pivot; keep leather in broad dark patches.'),
('goblins/rouser','Cloth headband, layered shoulder mail and dangling trinkets distinguish rank without bulk.','One torn scarf tail and two large bone beads; omit tiny chain detail.'),
('orcs/assassin','Masked face, wrapped forearms and separated knives make readiness legible.','Asymmetric wrist wrap and short side blade; preserve the small goblin proportions.')]),
('goblin_shaman','Goblin Shaman','#506936 #322e27 #7fe85f','Bent caster with a tall crystal staff and hanging charms.',[
('goblins/rouser','Aged face, head ties and dangling ceremonial objects suggest a tribal elder.','Extend one head tie and enlarge three pendant silhouettes rather than copying the outfit.'),
('trolls/troll-shaman','Paint bands, rope, beads and a bright magical hand contrast a stony dark torso.','Reinterpret as sparse green paint and a luminous staff head, keeping goblin skin organic.'),
('humans/dark-adept+female','Raised open hand surrounds a small pale green magical orb beneath a dark hood.','Animate fingers as a simple grouped hand and stage a green orb before release.')]),
('orc_warrior','Orc Warrior','#4f5739 #463c32 #b98142','Broad trapezoid torso, projecting tusks and one oversized armored shoulder.',[
('orcs/warrior','Open tusked mouth, broad neck, layered reddish armor and a lifted blade emphasize aggression.','Separate jaw/tusk blocks and three large shoulder plates; retain a visible neck.'),
('orcs/warlord','Heavy helmet, cloak, mail and warm metal edges convey command and mass.','Offset helmet crest and one thick pauldron; reduce mail to grouped dark pixels.'),
('humans/iron-mauler','Rounded riveted plate, hard specular edges and dark joints separate steel from straps.','Use three metal tones and sparse rivets, with darker flexible gaps at elbows.')]),
('minotaur','Minotaur','#513c2c #997343 #d1bb87','Bull-headed giant, lateral horns, deep chest and split hooves.',[
('trolls/troll-warrior','Massive neck and shoulders carrying a large weapon demonstrate weight; this is not a bovine reference.','Use the shoulder-to-waist contrast only, with original bull muzzle and paired horns.'),
('orcs/warlord','Helmet and wrapped torso show how warm metal and leather can frame a threatening face.','Build original bronze brow guards around, rather than over, the horn silhouette.'),
('monsters/great-horse','Heavy quadruped legs and long muzzle show large ungulate mass; horse feet are not cloven hooves.','Borrow lower-leg taper only; create explicitly split original hooves and bovine head proportions.')]),
('stone_troll','Stone Troll','#555f58 #899286 #566b38','Unequal huge arms, boulder shoulders and a low stone head.',[
('trolls/troll-rocklobber','Faceted gray shoulders and enormous throwing arm are balanced by a narrow waist and rope.','Build asymmetrical shoulder boulders and a distinct throwing arm with elbow articulation.'),
('trolls/troll-warrior','Rock plates have clear light upper planes and dark fissures between chunky forms.','Use broad stone planes with sparse cracks, reserving green pixels for damp seams.'),
('trolls/troll-shaman','Warm magic against muted gray stone demonstrates a restrained emissive contrast.','Translate to a few dim mineral seams; keep most rock opaque and unlit.')]),
('ancient_treant','Ancient Treant','#382b22 #606537 #bed081','Wide branching crown, narrow trunk waist and splayed root feet.',[
('woses/wose','A dark gnarled trunk face sits beneath a broad irregular green canopy and hanging moss.','Use unequal crown branches, a recessed face and separated root toes; avoid a solid leaf cube.'),
('elves/druid','Living vines and flowers curve around the arm and shoulders with localized green magic.','Attach sparse vine strips and one fungus shelf, keeping bark the primary material.'),
('trolls/troll-rocklobber','Oversized shoulder and hand provide a useful heavy guardian proportion analog, not wood anatomy.','Turn the large hand into forked wooden fingers and make root recovery slow and deliberate.')]),
('forest_dryad','Forest Dryad','#47633d #4d382a #b5ce77','Slender trunk limbs, leaf mantle and a branching crown.',[
('elves/druid','Leaf clothing, a wooden circlet and a flowering vine link humanoid anatomy to vegetation.','Create original bark hips and forearms, with a layered leaf skirt and blossom accent.'),
('elves/shyde','A raised arm, trailing sleeve and floating motes establish a graceful outward casting pose.','Use leaf and vine movement instead of copying fairy wings; hands lead the cast arc.'),
('woses/wose','Gnarled branching and deep bark seams show the organic construction missing from a plain humanoid.','Split crown branches at unequal heights and run broad bark grooves along limb direction.')]),
('griffin','Griffin','#594839 #e4d8b6 #b99b4e','Hooked eagle head, layered wings, large chest and feline hindquarters.',[
('monsters/gryphon','Hooked yellow beak, pale ruff and layered brown wings provide the direct hybrid design anchor; hindquarters are cropped.','Build a pale stepped ruff, dark wing coverts and an original lion rear body.'),
('monsters/falcon','Full airborne bird shows spread primary feathers, tucked legs and fanned tail.','Use three articulated feather banks per wing; keep leg tucking separate from wingbeats.'),
('monsters/roc','Huge lifted wing and heavy yellow talons emphasize lift and predatory reach.','Give takeoff a strong upstroke silhouette and large visible talons; preserve saddle clearance.')]),
('dire_wolf','Dire Wolf','#494b49 #b4b5a5 #cfbd8a','Deep ruff, long muzzle, raised shoulders and low sweeping tail.',[
('goblins/direwolver','Gray wolf head, thick cheek fur and layered chest ruff frame the rider.','Use stepped mane blocks around a long jaw and keep saddle above the shoulder line.'),
('goblins/wolf-rider','Brown-gray wolf muzzle and shaggy cheek create an alert face beneath practical riding straps.','Add broad cheek fur and a thin optional harness; avoid covering the ear silhouette.'),
('monsters/great-horse','Full-body weight-bearing stance helps compare mounted quadruped mass; it does not supply canine gait anatomy.','Borrow clear leg spacing and saddle-zone mass only; preserve digitigrade wolf hindlegs.')]),
('wild_wyvern','Wild Wyvern','#49633b #9ba66a #526788','Two wing arms, two hindlegs, long counterbalancing tail and narrow head.',[
('monsters/wyvern','A long neck curls below enormous green membranes carried by jointed wing arms.','Retain two-leg anatomy, with elbow and wrist wing bones plus a segmented balancing tail.'),
('monsters/fire-dragon','Broad belly plates, teeth and horn placement separate reptile surfaces from membrane.','Use original scale blocks and a muted throat stripe; do not add dragon forelegs.'),
('drakes/glider','Folded wings rise into a narrow tall silhouette; pale scales and blue cloth separate surfaces.','Use folding wing pivots and desaturated blue rare-variant membranes, with no copied clothing.')]),
('cave_basilisk','Cave Basilisk','#3e4f3b #7b8061 #cad26a','Low reptilian body with armored back, crown crest and a clear gaze point.',[
('monsters/crocodile','Low sprawling limbs, long toothed snout and raised dorsal scutes show convincing reptile mass.','Build a low belly, elbowed legs and three broad back ridges; eyes must remain visible.'),
('saurians/skirmisher','Crested reptile head and grouped bright scales give a readable brow and neck silhouette.','Create an original stone crown above the eye line and larger scale groupings.'),
('monsters/wyvern','Narrow aggressive head and horn clusters frame a focused eye beneath angular brows.','Borrow head direction and horn rhythm only; keep basilisk wingless and ground-bound.')]),
('crystal_spider','Crystal Spider','#3d294f #865bb2 #c9a5e2','Eight clear leg spokes around a raised faceted abdomen.',[
('monsters/giant-spider','Separated cephalothorax and round abdomen, with eight jointed legs, supply the anatomical anchor.','Keep eight independent articulated legs and a clear narrow connection between body masses.'),
('monsters/jumping-spider','Large forward eyes and blue-violet limb bands demonstrate focal face contrast and segmented color.','Use two dominant bright eyes and a few amethyst joint accents rather than painting every segment.'),
('monsters/scorpion-rock','Pale mineral nodules cover a dark arthropod shell; this is not a spider or crystal growth reference.','Replace round nodules with original angular crystals on the abdomen only, leaving leg joints clear.')]),
('shadow_wraith','Shadow Wraith','#252731 #555167 #9b9dd1','Floating hood and ragged hem with separated hanging forearms.',[
('undead/wraith','Blue spectral blade and smoky shredded robe contrast with a dark skeletal face.','Use a few pale eye pixels and an opaque dark robe core with restrained edge wisps.'),
('undead/spectre','Muted green-gray armor fades into haze and thin shredded cloth beneath a raised weapon.','Separate shoulder armor from the tapering lower body; keep strong opacity in the face.'),
('undead/nightgaunt','Faceless polished helmet and torn diagonal mantle produce an ominous silhouette without facial detail.','Use a recessed hollow face and asymmetric cloth strips; avoid copying the helmet outline.')]),
('grave_knight','Grave Knight','#35373c #79624e #a0babc','Heavy helmet, unequal plate shoulders, long sword and a broken cape edge.',[
('undead/death-knight','Exposed ribs, worn shoulder plates and a tattered cloak make age and undeath legible.','Keep armor coverage heavier, revealing only a narrow cursed eye slit and broken heraldry.'),
('undead/draug','Dark spikes, a damaged shield and isolated pale highlights make a powerful ruined soldier.','Use one broken pauldron silhouette and three large chips rather than uniform noise.'),
('humans/iron-mauler','Strong plate highlights and deep joint shadows explain readable heavy armor construction.','Reserve brightest pixels for upper plate edges; darken cloth and articulation gaps.')]),
('flame_imp','Flame Imp','#512b27 #b54c29 #ffce6a','Small horned head, broad bat wings and a hooked tail.',[
('monsters/bat-red','Red fur, broad wing membranes and finger-supported silhouettes provide the airborne anatomy analog.','Use two wing folds per side and a small heavy head, leaving hands visually separate.'),
('monsters/fire_guardian','Bright branching flame edges against a dark center suggest a readable contained heat source.','Place warm emissive pixels at eyes and chest cracks; use short ember trails.'),
('monsters/fire_wraith_A','Dark armor embedded in orange flames demonstrates material separation in an infernal palette.','Keep skin charcoal and set bright seams around horn roots and wrists, avoiding full-body glow.')]),
('frost_elemental','Frost Elemental','#344e66 #79b2ce #d9f1eb','Jagged broad shoulders around a narrow bright core and separated shard limbs.',[
('monsters/big-icemonax','Lavender-white shell nodules and bright edge facets provide cold mineral contrast, not an ice golem.','Replace rounded nodules with angular original shoulder shards and reserve white for upper edges.'),
('monsters/yeti','Broad pale shoulders, dark face and raised heavy arms demonstrate cold-creature mass and focal contrast.','Borrow upper-body weight distribution only, replacing fur with chunky ice planes.'),
('undead/wraith','Cyan glow concentrated on a weapon and surrounding haze shows cold emissive staging.','Concentrate cyan in a chest core and sparse fissures; add a low-budget cold mist effect.')]),
('moon_stag','Moon Stag','#abbac1 #d8e4dd #8caacc','Slim quadruped, long neck and a huge open branching antler crown.',[
('monsters/white-horse','Pale blue-white coat and darker cool mane show restrained moonlit quadruped shading; not deer anatomy.','Use cool light coat bands with dark lower-leg accents; keep original slender deer proportions.'),
('monsters/great-horse','Clearly separated four-leg standing pose and rounded chest help check mounted quadruped balance.','Borrow grounded hoof spacing only; narrow the muzzle and make the legs more gracile.'),
('woses/wose','Open asymmetrical branching against the dark canopy provides a natural crown rhythm.','Create paired but nonidentical luminous antlers with empty space between tines; omit foliage.')]),
('slime_maiden','Slime Maiden','#2b7d79 #69c4b1 #c4f1d7','Soft pear-shaped body, looping liquid hair and rounded arm ends.',[
('monsters/mudcrawler','Rounded sagging lobes and smooth drips show deformable substance; its brown rocky surface is not translucent gel.','Translate lobe overlap and dripping edge rhythm into aqua rounded cuboids with coherent highlight bands.'),
('monsters/cuttlefish','Cool teal mantle, smooth wet highlight and curling tentacles show liquid-like contour flow.','Create two broad hair curls and curved arm poses, using sparse pale highlights instead of copied anatomy.'),
('humans/dark-adept+female','Readable feminine face and open-hand orb pose supply a humanoid casting gesture, not slime anatomy.','Use an original friendly face with larger expressive eyes and a grouped liquid casting hand.')]),
('harpy','Harpy','#4b414f #907e81 #c4b6a2','Humanoid head and torso merging into large feather wings and taloned legs.',[
('monsters/falcon','Full spread wings, extended talons and fanned tail establish predatory avian movement.','Build stepped primary feather banks and downward-facing talons; articulate wing wrists.'),
('monsters/roc','Raised layered wing presents a powerful dark feather silhouette and striking yellow claws.','Use overlapping dark feather bands and a clear light claw tip at gameplay distance.'),
('elves/shyde','Humanoid raised arm integrated with wide wings provides a pose composition analog; these are insect wings.','Borrow torso balance only; use original feathered arm-wings and no transparent insect membranes.')]),
('demon_sorceress','Demon Sorceress','#322a3d #79517b #cf7168','Tall horned crown, flowing robe tiers and open floating casting hands.',[
('humans/necromancer+female','Dark fitted robe, pale face, curved skull-staff horns and violet smoke establish a strong caster focal hierarchy.','Create original swept head horns and a hovering rune focus, keeping face and hands distinct.'),
('elves/sorceress','An extended palm and loose hair lead the eye toward fine rising magic beside a wooden staff.','Animate an open-palm anticipation and layered robe panels with dark infernal materials.'),
('undead/nightgaunt','High dark collar, pointed shoulder shapes and shredded trailing cloth offer threatening negative space.','Use two unequal robe tails and a sharp shoulder silhouette without copying the armored face.')]),
]
BASE='https://raw.githubusercontent.com/wesnoth/wesnoth/master/data/core/images/portraits/'
LICENSE='Repository README: most art GPL-2.0-or-later; newer contributions CC-BY-SA-4.0. Exact per-image license not established. Study only; no redistribution or tracing authorized by this catalog.'
rows=[]
for sid,name,pal,sil,refs in SPECIES:
 r=[]
 for img,analysis,translation in refs:
  r.append(dict(image_url=BASE+img+'.webp',source_url='https://github.com/wesnoth/wesnoth/blob/master/data/core/images/portraits/'+img+'.webp',source='The Battle for Wesnoth',artist='Individual attribution not established; see project artwork credits',license=LICENSE,inspected=True,inspection='Downloaded successfully and viewed in labeled contact sheets sheet0–sheet3, 2026-10-18',local_study_file='/workspace/validation/overhaul/references/'+img.replace('/','_')+'.webp',analysis=analysis,original_minecraft_translation=translation))
 rows.append(dict(id=sid,name=name,palette=pal.split(),silhouette=sil,references=r))
data=dict(researched_at='2026-10-18',scope='20 species, three individually inspected image references each; several are partial anatomy/material analogs, not exact species matches.',provenance=dict(repository_readme='https://github.com/wesnoth/wesnoth/blob/master/README.md',project_credits='https://github.com/wesnoth/wesnoth/blob/master/data/core/about.cfg',license_file='https://github.com/wesnoth/wesnoth/blob/master/COPYING'),creatures=rows)
(ROOT/'references.json').write_text(json.dumps(data,indent=2)+'\n')
lines=['# Creature overhaul reference atlas','','Research date: 2026-10-18. All 60 entries below refer to real, successfully downloaded images that were visually inspected in four labeled contact sheets. Repeated images are deliberately analyzed for different design purposes. Artwork downloads remain outside the repository in `/workspace/validation/overhaul/references`; no reference pixels are shipped as game assets.','','## Scope and limits','','GitHub and raw GitHub were accessible. Wikimedia Commons, Met Museum and Art Institute endpoints returned proxy 403 responses; those restrictions were not bypassed. Consequently the research uses one accessible professional game-art collection. This satisfies three inspected relevant image studies per creature, but does **not** provide three direct species depictions per creature or a complete anatomical study. Minotaur, moon stag, frost elemental and slime maiden particularly rely on explicitly identified partial analogs. Additional bovine/deer anatomy and true crystal/gel material studies remain desirable. Do not interpret horse hooves as cloven hooves, fairy membranes as bird feathers, or a mineral-covered arthropod as actual crystals. Most portrait references are cropped, so full-body proportions are original design decisions.','','## Credits and usage','','Source: [The Battle for Wesnoth portrait collection](https://github.com/wesnoth/wesnoth/tree/master/data/core/images/portraits). Its [README licensing section](https://github.com/wesnoth/wesnoth/blob/master/README.md) states that most art is GPL v2+ and newer art contributions use CC BY-SA 4.0; the repository [COPYING](https://github.com/wesnoth/wesnoth/blob/master/COPYING) is GPL v2. The exact license of each selected image was not established. Treat these as study references only: no copying, tracing, asset extraction or redistribution. Original Minecraft assets use written observations, not reference pixels.','','[Project artwork credits](https://github.com/wesnoth/wesnoth/blob/master/data/core/about.cfg) credit Emilien Rotival (LordBob) as portrait director focusing on loyalists, trolls and monsters; James Woo (Pickslide) for portraits with a major orc focus; and Kathrin Polikeit (Kitty) as portrait director focusing on mage/necromancer, elvish, naga, merfolk and troll trees. These are **collection credits**, not verified individual authorship for every selected file. Per-image artist attribution remains unestablished and is recorded that way.','','## Visual translation rules','','Retain the silhouette features below at gameplay distance. Use large material patches and three-value ramps, minimal noise, articulated appendages and selective emissive accents. Interpret anatomy and material principles; invent shapes, markings, outfits and palettes for this project.']
for row in rows:
 lines += ['', '## '+row['name']+' — `'+row['id']+'`','', '**Palette:** '+' · '.join('`'+c+'`' for c in row['palette'])+'. These are proposed original colors, not measured samples.','', '**Distance silhouette:** '+row['silhouette'],'']
 for i,r in enumerate(row['references'],1):
  lines += [str(i)+'. ['+r['image_url'].split('/')[-1]+']('+r['image_url']+') · [source page]('+r['source_url']+'). **Inspected.** Source: The Battle for Wesnoth; individual artist unestablished. License: mixed project art licenses, per-image status unverified; study only.','   - **Observed:** '+r['analysis'],'   - **Original translation:** '+r['original_minecraft_translation']]
(ROOT/'REFERENCE_ATLAS.md').write_text('\n'.join(lines)+'\n')
print('Wrote',len(rows),'species and',sum(len(r['references']) for r in rows),'inspected reference entries.')
