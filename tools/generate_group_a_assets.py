#!/usr/bin/env python3
"""Editable block geometry and pixel-art atlases for the first creature group.
Requires Pillow only when regenerating assets, never at game runtime.
"""
from pathlib import Path
import json
import random
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1] / 'src/main/resources'
NS = 'mythic_realms_creatures'
ASSET = ROOT / 'assets' / NS

def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + '\n')

PALETTES = {
    'goblin_scout': [(83,119,52),(57,44,29),(161,133,79),(160,171,177),(232,184,60),(28,29,23),(212,211,159),(87,62,41)],
    'goblin_shaman': [(67,112,55),(48,37,69),(110,77,138),(86,57,36),(93,224,71),(26,21,36),(214,210,164),(70,96,47)],
    'orc_warrior': [(97,123,70),(63,74,79),(112,119,124),(79,47,27),(184,137,55),(28,32,29),(220,209,158),(117,57,38)],
    'minotaur': [(112,69,42),(70,42,29),(165,112,58),(75,79,82),(207,186,126),(28,23,20),(227,212,170),(119,42,29)],
    'stone_troll': [(111,118,114),(72,81,78),(144,148,140),(81,95,54),(151,182,77),(31,38,35),(175,176,151),(68,99,49)],
}
SCALE = {'goblin_scout':.625,'goblin_shaman':.74,'orc_warrior':1,'minotaur':1.25,'stone_troll':1.5}
WINDUP = {'goblin_scout':7,'goblin_shaman':16,'orc_warrior':18,'minotaur':24,'stone_troll':22}

for index, (name, palette) in enumerate(PALETTES.items()):
    rng = random.Random(20261017 + index)
    texture = Image.new('RGBA', (128,128))
    d = ImageDraw.Draw(texture)
    for i, color in enumerate(palette):
        x, y = (i % 4) * 32, (i // 4) * 32
        for py in range(32):
            for px in range(32):
                noise = rng.choice((-9,-4,0,0,0,4,8))
                # Material edge shading, scattered chips and woven stripes.
                shade = -10 if px % 16 == 0 or py % 16 == 15 else 0
                texture.putpixel((x+px,y+py), tuple(max(0,min(255,c+noise+shade)) for c in color)+(255,))
    (ASSET/'textures/entity').mkdir(parents=True,exist_ok=True)
    texture.save(ASSET/f'textures/entity/{name}.png')
    if name == 'goblin_shaman':
        # GeckoLib AutoGlowingGeoLayer reads this suffix. Only the magic
        # material (eyes, staff crystal and pendant) emits light.
        glowmask = Image.new('RGBA', texture.size)
        glowmask.paste(texture.crop((0,32,32,64)), (0,32))
        glowmask.save(ASSET/f'textures/entity/{name}_glowmask.png')
    bones = [{'name':'root','pivot':[0,0,0]}]
    scale = SCALE[name]
    def bone(key, parent, pivot):
        bones.append({'name':key,'parent':parent,'pivot':[v*scale for v in pivot],'cubes':[]})
    def box(key, origin, size, material=0, rotation=None):
        uv=[(material%4)*32+2,(material//4)*32+2]
        cube={'origin':[v*scale for v in origin], 'size':[v*scale for v in size],
              'uv':{face:{'uv':uv,'uv_size':[16,16]} for face in ['north','south','east','west','up','down']}}
        if rotation:
            cube['rotation']=rotation;cube['pivot']=[(origin[i]+size[i]/2)*scale for i in range(3)]
        next(b for b in bones if b['name']==key)['cubes'].append(cube)
    bone('body','root',[0,12,0]);box('body',[-4,12,-2.5],[8,10,5],1)
    bone('head','body',[0,22,0]);box('head',[-4,22,-3],[8,8,6],0)
    bone('arm_left','body',[5,21,0]);box('arm_left',[4,12,-2],[3,10,4],0)
    bone('arm_right','body',[-5,21,0]);box('arm_right',[-7,12,-2],[3,10,4],0)
    bone('leg_left','root',[2,12,0]);box('leg_left',[.5,1,-2],[3,11,4],1)
    bone('leg_right','root',[-2,12,0]);box('leg_right',[-3.5,1,-2],[3,11,4],1)
    for key,x in [('leg_left',.5),('leg_right',-3.5)]:box(key,[x,0,-3],[3,3,5],3)
    # Face details live on separate geometry instead of a single-color head.
    box('head',[-3,26,-3.25],[2,1.2,.5],5);box('head',[1,26,-3.25],[2,1.2,.5],5)
    box('head',[-2.5,26,-3.6],[1,.8,.5],4);box('head',[1.5,26,-3.6],[1,.8,.5],4)
    box('body',[-4.3,12,-2.8],[8.6,2,5.6],3)
    if name.startswith('goblin'):
        box('head',[-7,25,-1],[3,3,1],0,[0,0,-18]);box('head',[4,25,-1],[3,3,1],0,[0,0,18])
        box('head',[-1,23.5,-5],[2,2,3],0)
        box('head',[-2,22,-3.6],[1,1.5,.6],6);box('head',[1,22,-3.6],[1,1.5,.6],6)
    if name=='goblin_scout':
        box('head',[-4.2,28,-3.2],[8.4,2,6.4],3)
        box('body',[-1,14,-3],[2,8,1],3,[0,0,-25])
        box('arm_right',[-7,8,-3],[1.3,7,1.3],3)
        box('arm_right',[-8,8,-3.3],[3,1,2],4);box('arm_right',[-7,2,-3],[1.5,6,1],2)
    elif name=='goblin_shaman':
        box('body',[-5,7,-3],[10,10,6],2)
        box('head',[-5,29,-4],[10,1.5,8],1);box('head',[-3.5,30,-2.5],[7,3,5],2)
        box('arm_right',[-7,0,-3],[1.5,22,1.5],3)
        box('arm_right',[-8,21,-4],[4,4,4],4)
        box('body',[-1,18,-3.5],[2,2,1],4)
    elif name=='orc_warrior':
        box('body',[-5,14,-3.4],[10,8,6.8],2)
        box('arm_left',[3,19,-3],[6,4,6],2);box('arm_right',[-9,19,-3],[6,4,6],2)
        box('head',[-4.5,28,-3.5],[9,3,7],1)
        box('head',[-3,22,-4],[1.5,3,1.5],6,[15,0,0]);box('head',[1.5,22,-4],[1.5,3,1.5],6,[15,0,0])
        bone('shield','arm_left',[6,15,-3]);box('shield',[4,8,-4],[6,12,2],3)
        box('shield',[4,8,-4.5],[6,1,1],2);box('shield',[4,19,-4.5],[6,1,1],2)
        box('shield',[6.5,10,-4.6],[1,8,1],4)
        box('arm_right',[-7,2,-2],[1.5,15,1.5],3);box('arm_right',[-12,13,-2.5],[7,5,2.5],2)
    elif name=='minotaur':
        box('body',[-5,15,-3.5],[10,9,7],0)
        box('head',[-3.5,22,-6],[7,4,4],2)
        box('head',[-2,23,-6.5],[1,1,1],5);box('head',[1,23,-6.5],[1,1,1],5)
        bone('horn_left','head',[4,28,0]);box('horn_left',[4,27,-1],[5,2,2],6,[0,0,25]);box('horn_left',[7,29,-1],[2,4,2],6,[0,0,-15])
        bone('horn_right','head',[-4,28,0]);box('horn_right',[-9,27,-1],[5,2,2],6,[0,0,-25]);box('horn_right',[-9,29,-1],[2,4,2],6,[0,0,15])
        box('body',[-3,8,-3],[6,6,1],7)
        bone('tail','body',[0,13,3]);box('tail',[-.5,6,3],[1,8,1],0,[25,0,0])
        box('arm_right',[-7,2,-2],[1.5,15,1.5],3);box('arm_right',[-12,13,-2.5],[11,4,2.5],2)
    else:
        box('body',[-6,13,-4],[12,11,10],0)
        box('body',[-5,20,2],[10,8,5],1)
        box('head',[-4,22,-5],[8,7,8],0)
        box('head',[-4,27,-5.5],[8,1.5,1],1)
        for key,x in [('arm_left',4),('arm_right',-9)]:
            box(key,[x,8,-3],[5,14,6],0);box(key,[x-.5,6,-3.5],[6,4,7],1)
            box(key,[x,20,-3],[5,4,6],3,[0,0,15 if x>0 else -15])
        for x,y,z in [(-4,24,4),(2,25,3),(-2,16,6),(5,19,2)]:box('body',[x,y,z],[3,4,3],7,[10,0,15])
        box('head',[-2,23,-5.5],[1,2,1],6);box('head',[1,23,-5.5],[1,2,1],6)
    save(ASSET/f'geckolib/models/entity/{name}.geo.json', {
        'format_version':'1.12.0','minecraft:geometry':[{'description':{
            'identifier':f'geometry.{name}','texture_width':128,'texture_height':128,
            'visible_bounds_width':6,'visible_bounds_height':6,'visible_bounds_offset':[0,2,0]},'bones':bones}]})
    speed = [420,270,300,260,180][index]
    windup = WINDUP[name]/20
    attack_bones={'arm_right':{'rotation':{'0.0':[0,0,0], str(round(windup-.05,2)):[-135,0,-12],str(windup):[45,0,8], str(round(windup+.3,2)):[0,0,0]}}}
    if name=='goblin_shaman':attack_bones['arm_left']={'rotation':[-90,0,20]}
    if name=='minotaur':attack_bones['body']={'rotation':{'0.0':[0,0,0],str(windup):[28,0,0],str(windup+.3):[0,0,0]}}
    # A run is a faster, longer stride with a forward lean and full-body lift.
    # The shaman braces its staff; the two giants keep their heavier cadence.
    run_rate = [720,540,540,450,300][index]
    stride = [45,34,40,42,33][index]
    lean = [12,8,14,22,12][index]
    bounce = [.55,.35,.45,.6,.45][index] * scale
    run_bones = {
        'root': {'position':[0,f'math.abs(math.sin(query.anim_time * {run_rate})) * {bounce}',0]},
        'body': {'rotation':[lean,0,f'math.sin(query.anim_time * {run_rate}) * 2']},
        'head': {'rotation':[-lean*.6,0,0]},
        'leg_left': {'rotation':[f'math.sin(query.anim_time * {run_rate}) * {stride}',0,0]},
        'leg_right': {'rotation':[f'-math.sin(query.anim_time * {run_rate}) * {stride}',0,0]},
        'arm_left': {'rotation':[f'-math.sin(query.anim_time * {run_rate}) * {stride*.65}',0,-6]},
        'arm_right': {'rotation':[f'math.sin(query.anim_time * {run_rate}) * {stride*.65}',0,6]},
    }
    if name == 'goblin_shaman':
        run_bones['arm_right'] = {'rotation':[f'-22 + math.sin(query.anim_time * {run_rate}) * 6',0,-10]}
    if name == 'minotaur':
        run_bones['tail'] = {'rotation':[12,f'math.sin(query.anim_time * {run_rate}) * 14',0]}
    hurt_length = [.3,.4,.4,.5,.55][index]
    def recoil_channel(impact, recovery=None):
        return {'0.0':[0,0,0],'.08':impact,str(hurt_length):recovery or [0,0,0]}
    hurt_bones = {
        'root': {'position':recoil_channel([0,0,round(.7*scale,3)])},
        'body': {'rotation':recoil_channel([-14 if index<3 else -8,0,6])},
        'head': {'rotation':recoil_channel([12 if index<3 else 7,-5,-4])},
        'arm_left': {'rotation':recoil_channel([-12,0,-10])},
        'arm_right': {'rotation':recoil_channel([-18,0,10])},
    }
    animations={
        'idle':{'loop':True,'animation_length':2,'bones':{'body':{'position':[0,f'math.sin(query.anim_time * 180) * {0.25+index*.04}',0]},'head':{'rotation':[0,'math.sin(query.anim_time * 90) * 3',0]}}},
        'walk':{'loop':True,'animation_length':1,'bones':{
            'leg_left':{'rotation':[f'math.sin(query.anim_time * {speed}) * 28',0,0]},
            'leg_right':{'rotation':[f'-math.sin(query.anim_time * {speed}) * 28',0,0]},
            'arm_left':{'rotation':[f'-math.sin(query.anim_time * {speed}) * 20',0,0]},
            'arm_right':{'rotation':[f'math.sin(query.anim_time * {speed}) * 20',0,0]}}},
        'run':{'loop':True,'animation_length':360/run_rate,'bones':run_bones},
        'hurt':{'animation_length':hurt_length,'bones':hurt_bones},
        'attack':{'animation_length':round(windup+.3,2),'bones':attack_bones},
        'cast':{'animation_length':.8,'bones':{'arm_left':{'rotation':{'0.0':[0,0,0],'.3':[-120,0,20],'.8':[0,0,0]}},'arm_right':{'rotation':{'0.0':[0,0,0],'.3':[-120,0,-20],'.8':[0,0,0]}}}},
        'death':{'animation_length':.8,'bones':{'root':{'rotation':{'0.0':[0,0,0],'.8':[0,0,85]},'position':{'0.0':[0,0,0],'.8':[0,1,0]}}}}
    }
    save(ASSET/f'geckolib/animations/entity/{name}.animation.json',{'format_version':'1.8.0','animations':animations})
    # Custom pixel-art spawn egg avoids depending on obsolete vanilla egg tint formats.
    egg=Image.new('RGBA',(16,16));ed=ImageDraw.Draw(egg)
    ed.polygon([(6,1),(9,1),(12,5),(13,9),(12,13),(10,15),(5,15),(2,12),(2,8),(4,4)],fill=palette[0]+(255,),outline=palette[5]+(255,))
    for x,y in [(6,4),(9,7),(4,10),(8,12)]:ed.rectangle([x,y,x+1,y+1],fill=palette[4]+(255,))
    (ASSET/'textures/item').mkdir(parents=True,exist_ok=True);egg.save(ASSET/f'textures/item/{name}_spawn_egg.png')
    save(ASSET/f'models/item/{name}_spawn_egg.json',{'parent':'minecraft:item/generated','textures':{'layer0':f'{NS}:item/{name}_spawn_egg'}})
    save(ASSET/f'items/{name}_spawn_egg.json',{'model':{'type':'minecraft:model','model':f'{NS}:item/{name}_spawn_egg'}})
    loot=[('iron_nugget',1,3),('slime_ball',1,2),('iron_ingot',1,2),('leather',2,4),('cobblestone',4,8)][index]
    save(ROOT/f'data/{NS}/loot_table/entities/{name}.json',{'type':'minecraft:entity','pools':[{'rolls':1,'entries':[{'type':'minecraft:item','name':'minecraft:'+loot[0],'functions':[{'function':'minecraft:set_count','count':{'type':'minecraft:uniform','min':loot[1],'max':loot[2]}}]}]}]})
    biomes=[['minecraft:plains','minecraft:sunflower_plains','#minecraft:is_forest'],['minecraft:swamp','minecraft:mangrove_swamp'],['#minecraft:is_forest','#minecraft:is_hill'],['#minecraft:is_mountain'],['#minecraft:is_overworld']][index]
    save(ROOT/f'data/{NS}/tags/worldgen/biome/spawns/{name}.json',{'replace':False,'values':[{'id':b,'required':False} for b in biomes]})

langpath=ASSET/'lang/en_us.json'
language=json.loads(langpath.read_text()) if langpath.exists() else {}
for name in PALETTES:
    title=name.replace('_',' ').title()
    language[f'entity.{NS}.{name}']=title
    language[f'item.{NS}.{name}_spawn_egg']=title+' Spawn Egg'
save(ASSET/'lang/en_us.json',language)
print('Generated five distinct models, atlases, animation sets, eggs, biome tags and loot tables')

if __name__=='__main__':
    from generate_overhaul_group_a import main as export_overhaul
    export_overhaul()
    import integrate_content
