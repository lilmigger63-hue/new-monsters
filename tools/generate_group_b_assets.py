#!/usr/bin/env python3
"""Editable Group B block models and pixel atlases. Regeneration requires Pillow."""
from pathlib import Path
import json, random
from PIL import Image, ImageDraw
ROOT=Path(__file__).resolve().parents[1]/'src/main/resources'
NS='mythic_realms_creatures'; A=ROOT/'assets'/NS

def save(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(obj,indent=2)+'\n')

PALETTES={
 'ancient_treant':[(97,68,42),(60,44,31),(136,103,60),(61,100,43),(163,230,74),(25,34,21),(174,142,85),(78,125,46)],
 'forest_dryad':[(182,157,110),(54,111,63),(91,148,67),(121,79,48),(128,224,135),(32,50,40),(205,185,136),(146,88,127)],
 'griffin':[(184,137,76),(224,218,194),(118,83,47),(220,170,53),(240,201,76),(31,35,37),(148,116,71),(100,72,43)],
 'dire_wolf':[(115,124,133),(65,77,89),(179,185,188),(59,66,72),(168,210,222),(23,29,35),(201,205,203),(102,110,120)],
 'wild_wyvern':[(66,97,80),(39,62,56),(100,56,73),(118,146,100),(183,226,77),(24,31,32),(210,197,146),(59,73,64)],
}
WINDUP={'ancient_treant':24,'forest_dryad':16,'griffin':12,'dire_wolf':7,'wild_wyvern':20}
for index,(name,palette) in enumerate(PALETTES.items()):
    def atlas(colors):
        image=Image.new('RGBA',(128,128)); rng=random.Random(701+index)
        for material,color in enumerate(colors):
            x,y=material%4*32,material//4*32
            for py in range(32):
                for px in range(32):
                    grain=rng.choice([-9,-4,0,0,0,3,7])
                    if name=='ancient_treant' and material<3:grain+=-12 if px%5==0 else 0
                    if name in ('griffin','dire_wolf') and material<3:grain+=6 if (px+py)%9==0 else 0
                    image.putpixel((x+px,y+py),tuple(max(0,min(255,c+grain)) for c in color)+(255,))
        return image
    (A/'textures/entity').mkdir(parents=True,exist_ok=True)
    atlas(palette).save(A/f'textures/entity/{name}.png')
    if name in ('griffin','dire_wolf','wild_wyvern'):
        tame=list(palette);tame[7]=(160,45,47) if name=='dire_wolf' else (204,157,64)
        if name=='wild_wyvern':tame[0]=(67,128,135);tame[1]=(34,76,89)
        atlas(tame).save(A/f'textures/entity/{name}_tamed.png')
    if name=='wild_wyvern':
        rare=list(palette);rare[0]=(67,128,135);rare[1]=(34,76,89);rare[4]=(141,218,231)
        atlas(rare).save(A/f'textures/entity/{name}_rare.png')
    if name in ('ancient_treant','forest_dryad','wild_wyvern'):
        # Preserve the atlas's UV placement and emit just the magical material.
        # Tamed/rare variants need masks matching their actual texture paths.
        suffixes = ('','_tamed','_rare') if name=='wild_wyvern' else ('',)
        for suffix in suffixes:
            source=Image.open(A/f'textures/entity/{name}{suffix}.png').convert('RGBA')
            mask=Image.new('RGBA',source.size)
            mask.paste(source.crop((0,32,32,64)),(0,32))
            mask.save(A/f'textures/entity/{name}{suffix}_glowmask.png')
    scale={'ancient_treant':1,'forest_dryad':1,'griffin':1,'dire_wolf':.86,'wild_wyvern':.94}[name]
    bones=[{'name':'root','pivot':[0,0,0]}]
    def bone(key,parent,pivot):bones.append({'name':key,'parent':parent,'pivot':[v*scale for v in pivot],'cubes':[]})
    def box(key,origin,size,material=0,rotation=None):
        uv=[material%4*32+2,material//4*32+2]
        cube={'origin':[v*scale for v in origin],'size':[v*scale for v in size],
              'uv':{f:{'uv':uv,'uv_size':[16,16]} for f in ('north','south','east','west','up','down')}}
        if rotation:cube.update(rotation=rotation,pivot=[(origin[i]+size[i]/2)*scale for i in range(3)])
        next(b for b in bones if b['name']==key)['cubes'].append(cube)
    if name=='ancient_treant':
        bone('body','root',[0,23,0]);box('body',[-8,18,-7],[16,39,14],0)
        box('body',[-6,25,-8],[12,23,1],2)
        bone('head','body',[0,55,0]);box('head',[-9,53,-8],[18,17,16],0)
        for x in [-5,3]:
            box('head',[x,61,-8.5],[3,2,1],4);box('head',[x-1,64,-9],[5,2,2],1,[0,0,12 if x<0 else -12])
        box('head',[-5,56,-8.5],[10,2,1],5)
        for side in [-1,1]:
            key='arm_left' if side>0 else 'arm_right';x=8 if side>0 else -16
            bone(key,'body',[side*9,51,0]);box(key,[x,25,-4],[8,29,8],0,[0,0,-side*12])
            for finger in range(3):box(key,[x+finger*2,18,-3],[1.7,10,2],1,[0,0,side*(finger-1)*10])
            leg='leg_left' if side>0 else 'leg_right';lx=1 if side>0 else -8
            bone(leg,'root',[side*4,23,0]);box(leg,[lx,1,-4],[7,23,8],1)
            box(leg,[lx-2,0,-9],[11,4,17],0)
        for x,y,z,s in [(-14,66,-7,12),(3,68,-5,13),(-7,70,2,15),(-18,52,0,9),(11,49,-1,10)]:
            box('head' if y>60 else 'body',[x,y,z],[s,5,s],3)
        box('head',[-2,66,-2],[4,10,4],1,[0,0,15])
        for x,z in [(-9,5),(6,5),(-8,-6),(5,-7)]:box('body',[x,33,z],[4,12,3],7,[0,0,10])
    elif name=='forest_dryad':
        bone('body','root',[0,12,0]);box('body',[-3,12,-2],[6,10,4],1)
        bone('head','body',[0,22,0]);box('head',[-3.5,22,-3],[7,7,6],0)
        for side in [-1,1]:
            key='arm_left' if side>0 else 'arm_right';x=3 if side>0 else -5.5
            bone(key,'body',[side*4,21,0]);box(key,[x,12,-1.5],[2.5,10,3],0)
            box(key,[x-.5,19,-2],[3.5,4,4],2)
            leg='leg_left' if side>0 else 'leg_right';x=.5 if side>0 else -3
            bone(leg,'root',[side*1.8,12,0]);box(leg,[x,0,-1.5],[2.5,12,3],0)
            box('head',[side*4-1,28,0],[2,5,1.5],3,[0,0,-side*25])
        for x,z in [(-4,-3),(0,-3),(-4,0),(0,0)]:box('body',[x,7,z],[4,8,3],2,[0,0,12 if x<0 else -12])
        box('head',[-4,23,2],[8,7,2],1);box('head',[-4,25,-3.3],[8,4,1],1)
        box('head',[-2.5,25,-3.7],[1.5,1,1],4);box('head',[1,25,-3.7],[1.5,1,1],4)
        box('head',[-1,29,-1],[2,2,2],7)
        bone('staff','arm_right',[-5,16,-2]);box('staff',[-5.5,0,-2],[1,24,1],3);box('staff',[-7,22,-3.5],[4,4,4],4)
    else:
        if name=='dire_wolf':
            bone('body','root',[0,11,0]);box('body',[-5,10,-9],[10,8,19],0)
            box('body',[-6,13,-10],[12,7,8],2)
            bone('head','body',[0,17,-9]);box('head',[-4,16,-15],[8,7,8],0)
            box('head',[-3,15,-20],[6,4,7],2);box('head',[-2,17,-20.5],[4,2,1],5)
            for side in [-1,1]:
                box('head',[side*3-1,22,-12],[2.5,4,2.5],1,[0,0,-side*15])
                box('head',[side*2.5-1,20,-15.6],[1.5,1.2,1],4)
            for key,x,z in [('arm_left',3,-6),('arm_right',-5,-6),('leg_left',3,6),('leg_right',-5,6)]:
                bone(key,'root',[x+1,12,z]);box(key,[x,0,z-1],[2.5,12,3.5],1);box(key,[x-.3,0,z-2],[3.1,2,5],2)
            bone('tail','body',[0,15,9]);box('tail',[-2,12,8],[4,4,11],0,[20,0,0]);box('tail',[-1.5,12,18],[3,3,4],2)
            box('body',[-5.7,13,-9],[11.4,3,2],7)
            box('body',[-4.7,17,-1],[9.4,1.5,8],7)
        elif name=='griffin':
            bone('body','root',[0,13,0]);box('body',[-7,12,-10],[14,10,24],0)
            box('body',[-7.5,15,-11],[15,10,10],1)
            bone('head','body',[0,23,-8]);box('head',[-4.5,22,-14],[9,8,8],1)
            box('head',[-2.5,22,-20],[5,4,7],3);box('head',[-2,20,-20],[4,3,2],3)
            for side in [-1,1]:box('head',[side*3-1,26,-14.5],[2,1.5,1],5)
            for key,x,z in [('arm_left',4,-7),('arm_right',-6,-7),('leg_left',4,9),('leg_right',-6,9)]:
                bone(key,'root',[x+1,14,z]);box(key,[x,1,z-2],[3,13,4],1 if 'arm' in key else 0)
                box(key,[x-.5,0,z-5],[4,2,7],3 if 'arm' in key else 2)
            bone('tail','body',[0,17,13]);box('tail',[-1,14,12],[2,3,14],0,[15,0,0]);box('tail',[-2,12,24],[4,5,5],2)
            for side in [-1,1]:
                key='wing_left' if side>0 else 'wing_right';bone(key,'body',[side*6,22,0])
                for step in range(4):
                    x=side*(7+step*6);x=x if side>0 else x-8
                    box(key,[x,21-step*.5,-4+step],[9,2,16-step*2],1 if step%2==0 else 6)
                    for feather in range(2):box(key,[x+feather*3,20-step*.5,9-step],[3,1,6],1)
            box('body',[-7.5,13,0],[15,9,2],7);box('body',[-5,22,-1],[10,1.5,9],7)
        else:
            bone('body','root',[0,16,0]);box('body',[-6,14,-10],[12,11,24],0)
            bone('head','body',[0,26,-9]);box('head',[-4,25,-17],[8,9,10],0)
            box('head',[-3,25,-24],[6,4,9],1);box('head',[-2,25,-24.5],[4,1,1],5)
            for side in [-1,1]:
                box('head',[side*3-1,30,-17.5],[2,1.5,1],4)
                box('head',[side*4-1,32,-12],[2,6,2],6,[20,0,-side*20])
                key='leg_left' if side>0 else 'leg_right';x=3 if side>0 else -7
                bone(key,'root',[side*5,17,8]);box(key,[x,2,5],[4,15,6],0,[10,0,side*12]);box(key,[x-.5,0,1],[5,3,9],1)
            for key,x in [('arm_left',5),('arm_right',-7)]:
                bone(key,'body',[x,22,-7]);box(key,[x,13,-8],[2,10,3],1);box(key,[x,12,-11],[2,2,6],6)
            bone('tail','body',[0,18,13]);box('tail',[-2,15,12],[4,4,15],0,[8,0,0]);box('tail',[-1.3,13,25],[2.6,3,14],1,[10,0,0]);box('tail',[-2,12,36],[4,4,5],4)
            for side in [-1,1]:
                key='wing_left' if side>0 else 'wing_right';bone(key,'body',[side*5,24,-4])
                for step in range(4):
                    x=6+step*8;x=x if side>0 else -x-9
                    box(key,[x,24-step*.5,-6+step*2],[10,1.3,20-step*3],2)
                    box(key,[x,24-step*.5,-7+step*2],[10,2,1.5],1)
                    box(key,[x+4,24-step*.5,-6+step*2],[1.5,2,20-step*3],1)
            for z in [-4,2,8,14]:box('body',[-1,25,z],[2,5,3],6,[15,0,0])
            box('body',[-6.5,15,0],[13,10,2],7);box('body',[-4,25,1],[8,1.5,8],7)
    save(A/f'geckolib/models/entity/{name}.geo.json',{'format_version':'1.12.0','minecraft:geometry':[{'description':{
        'identifier':'geometry.'+name,'texture_width':128,'texture_height':128,'visible_bounds_width':8,'visible_bounds_height':8,'visible_bounds_offset':[0,2,0]},'bones':bones}]})
    bnames={b['name'] for b in bones};windup=WINDUP[name]/20
    walk={}
    for key,sign in [('arm_left',-1),('arm_right',1),('leg_left',1),('leg_right',-1)]:
        if key in bnames:walk[key]={'rotation':[f'math.sin(query.anim_time * {220 if name=="ancient_treant" else 360}) * {sign*24}',0,0]}
    idle={'body':{'position':[0,'math.sin(query.anim_time * 160) * .2',0]}}
    if 'tail' in bnames:idle['tail']={'rotation':[0,'math.sin(query.anim_time * 120) * 8',0]}
    attack={'head':{'rotation':{'0.0':[0,0,0],str(round(windup-.05,2)):[-25,0,0],str(windup):[25,0,0],str(round(windup+.3,2)):[0,0,0]}}}
    if name in ('ancient_treant','forest_dryad'):
        attack['arm_right']={'rotation':{'0.0':[0,0,0],str(round(windup-.05,2)):[-120,0,-20],str(windup):[-60,0,0],str(round(windup+.3,2)):[0,0,0]}}
    # Quadrupeds bound with paired front/hind legs; humanoids alternate strides.
    run_rate={'ancient_treant':270,'forest_dryad':600,'griffin':540,'dire_wolf':720,'wild_wyvern':450}[name]
    stride={'ancient_treant':32,'forest_dryad':38,'griffin':42,'dire_wolf':50,'wild_wyvern':38}[name]
    quadruped=name in ('griffin','dire_wolf')
    run={
        'root':{'position':[0,f'math.abs(math.sin(query.anim_time * {run_rate})) * {.75 if quadruped else .35}',0]},
        'body':{'rotation':[f'{8 if quadruped else 10} + math.sin(query.anim_time * {run_rate}) * {5 if quadruped else 2}',0,0]},
        'head':{'rotation':[f'-6 - math.sin(query.anim_time * {run_rate}) * 3',0,0]},
    }
    for key,sign in [('arm_left',-1),('arm_right',1),('leg_left',1),('leg_right',-1)]:
        if key in bnames:
            if quadruped:sign=1 if key.startswith('arm') else -1
            amplitude=stride if key.startswith('leg') or quadruped else stride*.65
            run[key]={'rotation':[f'math.sin(query.anim_time * {run_rate}) * {sign*amplitude}',0,0]}
    if name=='forest_dryad':run['arm_right']={'rotation':[f'-20 + math.sin(query.anim_time * {run_rate}) * 6',0,-8]}
    if 'tail' in bnames:run['tail']={'rotation':[-10,f'math.sin(query.anim_time * {run_rate}) * 12',0]}
    for side,sign in [('left',1),('right',-1)]:
        if 'wing_'+side in bnames:
            run['wing_'+side]={'rotation':[0,0,f'{sign*16} + math.sin(query.anim_time * {run_rate}) * {sign*5}']}
    hurt_length=.6 if name=='ancient_treant' else .35 if name=='dire_wolf' else .45
    def recoil(impact):return {'0.0':[0,0,0],'.08':impact,str(hurt_length):[0,0,0]}
    hurt={
        'root':{'position':recoil([0,0,.4 if name=='ancient_treant' else .7])},
        'body':{'rotation':recoil([-7 if name=='ancient_treant' else -12,0,5])},
        'head':{'rotation':recoil([14,-6,-4])},
    }
    if 'tail' in bnames:hurt['tail']={'rotation':recoil([18,0,-8])}
    for side,sign in [('left',1),('right',-1)]:
        if 'arm_'+side in bnames:hurt['arm_'+side]={'rotation':recoil([-12,0,sign*8])}
        if 'wing_'+side in bnames:hurt['wing_'+side]={'rotation':recoil([0,0,sign*24])}
    animations={
        'idle':{'loop':True,'animation_length':2,'bones':idle},
        'walk':{'loop':True,'animation_length':1,'bones':walk},
        'run':{'loop':True,'animation_length':360/run_rate,'bones':run},
        'hurt':{'animation_length':hurt_length,'bones':hurt},
        'attack':{'animation_length':round(windup+.3,2),'bones':attack},
        'cast':{'animation_length':.75,'bones':{'head':{'rotation':{'0.0':[0,0,0],'.4':[-20,0,0],'.75':[0,0,0]}}}},
        'death':{'animation_length':.8,'bones':{'root':{'rotation':{'0.0':[0,0,0],'.8':[0,0,80]}}}},
    }
    if name in ('griffin','dire_wolf','wild_wyvern'):
        animations.update({
            'sit':{'loop':True,'animation_length':1,'bones':{'body':{'position':[0,-4,0]},'leg_left':{'rotation':[-65,0,0]},'leg_right':{'rotation':[-65,0,0]}}},
            'tame':{'animation_length':1,'bones':{'head':{'rotation':{'0.0':[0,0,0],'.3':[20,0,0],'.6':[-10,0,0],'1.0':[0,0,0]}}}},
            'ride':{'loop':True,'animation_length':1,'bones':walk},
        })
    if 'wing_left' in bnames:
        for state,rate in [('fly',420),('hover',540)]:
            animations[state]={'loop':True,'animation_length':1,'bones':{
                'wing_left':{'rotation':[0,0,f'math.sin(query.anim_time * {rate}) * 38 + 12']},
                'wing_right':{'rotation':[0,0,f'-math.sin(query.anim_time * {rate}) * 38 - 12']},
                'leg_left':{'rotation':[-35,0,0]},'leg_right':{'rotation':[-35,0,0]}}}
    save(A/f'geckolib/animations/entity/{name}.animation.json',{'format_version':'1.8.0','animations':animations})
    egg=Image.new('RGBA',(16,16));draw=ImageDraw.Draw(egg)
    draw.polygon([(6,1),(9,1),(12,5),(13,9),(12,13),(10,15),(5,15),(2,12),(2,8),(4,4)],fill=palette[0]+(255,),outline=palette[5]+(255,))
    for x,y in [(6,4),(9,7),(4,10),(8,12)]:draw.rectangle([x,y,x+1,y+1],fill=palette[4]+(255,))
    (A/'textures/item').mkdir(parents=True,exist_ok=True);egg.save(A/f'textures/item/{name}_spawn_egg.png')
    save(A/f'items/{name}_spawn_egg.json',{'model':{'type':'minecraft:model','model':f'{NS}:item/{name}_spawn_egg'}})
    save(A/f'models/item/{name}_spawn_egg.json',{'parent':'minecraft:item/generated','textures':{'layer0':f'{NS}:item/{name}_spawn_egg'}})
    drop,count={'ancient_treant':('oak_log',3),'forest_dryad':('glow_berries',3),'griffin':('feather',3),'dire_wolf':('leather',2),'wild_wyvern':('amethyst_shard',3)}[name]
    save(ROOT/f'data/{NS}/loot_table/entities/{name}.json',{'type':'minecraft:entity','pools':[{'rolls':1,'entries':[{'type':'minecraft:item','name':'minecraft:'+drop,'functions':[{'function':'minecraft:set_count','count':{'type':'minecraft:uniform','min':1,'max':count}}]}]}]})
    tag='#minecraft:is_mountain' if name in ('griffin','wild_wyvern') else '#minecraft:is_forest'
    save(ROOT/f'data/{NS}/tags/worldgen/biome/spawns/{name}.json',{'replace':False,'values':[{'id':tag,'required':False}]})
langpath=A/'lang/en_us.json';language=json.loads(langpath.read_text())
for name in PALETTES:
    title=name.replace('_',' ').title();language[f'entity.{NS}.{name}']=title;language[f'item.{NS}.{name}_spawn_egg']=title+' Spawn Egg'
language.update({
 'message.mythic_realms_creatures.wyvern_wild':'Only rare blue wyverns can be tamed.',
 'message.mythic_realms_creatures.land_first':'Land before asking your mount to stay.',
 'message.mythic_realms_creatures.stay':'Your companion will stay here.',
 'message.mythic_realms_creatures.follow':'Your companion will follow you.',
 'message.mythic_realms_creatures.saddle_required':'Equip a saddle before riding.'})
save(langpath,language)
print('Generated five distinct Group B models, textures, animations, eggs, loot and biome tags')
