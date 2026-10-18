#!/usr/bin/env python3
"""Original material painting and validated GeckoLib/Blockbench export.

Offline only. Reuses the proven native-project serializer; never touches gameplay data.
"""
from __future__ import annotations
import math
from pathlib import Path
from PIL import Image, ImageDraw
from generate_groups_cd_assets import Model as BaseModel, blockbench, validate, save

ROOT=Path(__file__).resolve().parents[1]
ASSET=ROOT/'src/main/resources/assets/mythic_realms_creatures'

class Model(BaseModel):
    def bone(self,name,parent,pivot,rotation=None):
        if name in self.by_name:raise ValueError('Duplicate bone: '+name)
        if parent not in self.by_name:raise ValueError('Unknown parent: '+str(parent))
        if len(pivot)!=3 or not all(math.isfinite(v) for v in pivot):raise ValueError('Invalid pivot')
        return super().bone(name,parent,list(pivot),rotation)

    def box(self,bone,origin,size,material=0,rotation=None,pivot=None):
        if bone not in self.by_name:raise ValueError('Unknown bone: '+bone)
        if len(origin)!=3 or len(size)!=3 or not all(math.isfinite(v) for v in (*origin,*size)) or any(v<=0 for v in size):raise ValueError('Invalid cube dimensions')
        if not 0<=material<16:raise ValueError('Material must address one of sixteen atlas tiles')
        return super().box(bone,list(origin),list(size),material,rotation,pivot)


def clip(length,bones,loop=False):
    return {'loop':loop,'animation_length':length,'bones':bones}


def keys(t,prepare,impact,final=(0,0,0),start=(0,0,0),recovery=.3):
    return {'0.0':list(start),str(round(max(.01,t-.12),4)):list(prepare),str(round(t,4)):list(impact),str(round(t+recovery,4)):list(final)}


def material_atlas(palette,materials,translucent=False):
    """Deliberately drawn grain, panel edges, clusters and facets; no RNG noise."""
    if len(palette)!=16 or len(materials)!=16:raise ValueError('Expected sixteen colors and material roles')
    image=Image.new('RGBA',(128,128))
    for index,(value,role) in enumerate(zip(palette,materials)):
        if isinstance(value,str):
            value=value.lstrip('#');rgb=tuple(int(value[i:i+2],16) for i in (0,2,4))
        else:rgb=tuple(value)
        if len(rgb)!=3:raise ValueError('RGB palette expected')
        role=role.lower();alpha=202 if translucent else 255
        if role in ('glow','rune','eyes'):alpha=255
        def tint(amount):return tuple(max(0,min(255,c+amount)) for c in rgb)+(alpha,)
        tile=Image.new('RGBA',(32,32),tint(0));d=ImageDraw.Draw(tile)
        # Broad directional lighting and edge bevels remain readable at distance.
        d.rectangle((0,0,31,2),fill=tint(12));d.rectangle((0,3,2,29),fill=tint(5))
        d.rectangle((29,3,31,31),fill=tint(-15));d.rectangle((2,29,28,31),fill=tint(-20))
        if role in ('bark','wood','root'):
            for x in (5,12,21,27):
                d.line([(x,3),(x-2,10),(x+1,17),(x-1,28)],fill=tint(-19),width=2)
                d.line([(x+2,4),(x,12),(x+3,20),(x+1,28)],fill=tint(12),width=1)
            d.ellipse((14,10,20,18),outline=tint(-22),width=1);d.line((16,12,18,15),fill=tint(18))
        elif role in ('stone','rock','moss','mineral'):
            for points in ([(3,9),(13,8),(17,4)],[(13,8),(15,19),(26,22)],[(15,19),(7,26)],[(25,4),(22,12),(28,16)]):d.line(points,fill=tint(-20),width=1)
            for box in ((5,5,9,7),(18,13,23,15),(7,19,11,21)):d.rectangle(box,fill=tint(11))
            if role=='moss':
                for x,y in ((5,11),(16,22),(23,8)):d.polygon([(x,y),(x+4,y-2),(x+6,y+2),(x+2,y+3)],fill=tint(20))
        elif role in ('metal','iron','bronze','gold','armor'):
            for y in range(4,28):d.line((3,y,28,y),fill=tint(round(15*(1-abs(y-9)/23))))
            d.line((4,5,26,5),fill=tint(32),width=1);d.line((5,6,5,26),fill=tint(21))
            d.line((7,24,24,24),fill=tint(-17));d.line((19,10,24,15),fill=tint(-13))
            for x,y in ((5,8),(25,8),(5,26),(25,26)):d.rectangle((x,y,x+1,y+1),fill=tint(34))
        elif role in ('fur','hair','mane'):
            for y in (5,12,19,25):
                for x in (5,13,22):
                    k=2 if y in (12,25) else 0
                    d.line([(x+k,y),(x+k-1,y+4),(x+k+2,y+6)],fill=tint(-12),width=1)
                    d.line((x+k+2,y,x+k+3,y+3),fill=tint(14))
        elif role in ('feather','feathers'):
            for x in (7,16,25):
                d.line((x,4,x-1,28),fill=tint(-18))
                for y in (7,12,17,22):
                    d.line((x,y,x-5,y-3),fill=tint(15));d.line((x,y+1,x+4,y-2),fill=tint(-11))
        elif role=='chitin':
            d.polygon([(4,5),(16,3),(27,8),(26,25),(16,29),(4,24)],fill=tint(8))
            d.line([(4,13),(15,15),(27,12)],fill=tint(-23),width=2)
            d.line([(5,22),(16,24),(26,21)],fill=tint(-17),width=1)
            d.line([(6,6),(15,5),(24,9)],fill=tint(25),width=1)
            d.line((15,6,16,13),fill=tint(-10))
        elif role in ('scale','scales'):
            for row,y in enumerate((4,10,16,22)):
                for x in (3,11,19,27):
                    x+=3 if row%2 else 0
                    d.line([(x-3,y),(x,y+4),(x+4,y)],fill=tint(-18))
                    d.line((x-2,y,x+2,y),fill=tint(12))
        elif role in ('cloth','robe','fabric','leather','membrane'):
            for x in (7,17,26):
                d.rectangle((x,4,x+1,27),fill=tint(-12));d.line((x+2,4,x+2,27),fill=tint(7))
            if role=='leather':
                d.line((4,7,27,7),fill=tint(-24))
                for x in range(5,28,4):d.line((x,6,x+1,8),fill=tint(25))
            elif role=='membrane':d.line([(3,5),(14,14),(26,28)],fill=tint(-20),width=2)
            else:
                for x in (9,21):d.line((x,22,x+3,25),fill=tint(5))
        elif role in ('ice','crystal','gem'):
            d.polygon([(5,8),(14,3),(23,7),(27,20),(18,28),(5,23)],fill=tint(11))
            d.polygon([(14,3),(23,7),(18,28),(13,18)],fill=tint(-12))
            d.line([(5,8),(13,18),(18,28)],fill=tint(28),width=1)
            d.line((13,18,27,20),fill=tint(35));d.line((8,10,11,8),fill=tint(50))
        elif role in ('glow','rune','eyes'):
            d.rectangle((3,3,28,28),fill=tint(-28))
            if role=='rune':
                for x in (8,21):
                    d.line([(x,6),(x-3,12),(x+2,17),(x-2,24)],fill=tint(25),width=1)
                    d.line((x-3,13,x+4,13),fill=tint(40));d.line((x,18,x+4,22),fill=tint(35))
            else:
                d.polygon([(16,5),(27,16),(16,27),(5,16)],fill=tint(5))
                d.polygon([(16,9),(23,16),(16,23),(9,16)],fill=tint(25))
                d.rectangle((14,13,17,17),fill=tint(48))
        elif role in ('slime','gel','liquid'):
            d.ellipse((4,4,16,19),fill=tint(14));d.line([(5,9),(6,6),(10,5)],fill=tint(34),width=1)
            d.arc((15,16,26,27),10,260,fill=tint(20),width=1)
            d.line((4,26,13,27),fill=tint(-13))
        elif role in ('bone','horn','ivory'):
            d.line((7,4,8,27),fill=tint(18),width=2);d.line((22,4,24,27),fill=tint(-15))
            for y in (9,18,25):d.line((9,y,22,y+1),fill=tint(-8))
        else:
            # Skin: broad warm planes and sparse deliberate marks, never RGB noise.
            d.rectangle((5,5,24,11),fill=tint(5));d.rectangle((5,23,24,27),fill=tint(-6))
            d.line((7,17,11,18),fill=tint(-9));d.line((21,12,24,14),fill=tint(9))
        image.paste(tile,(index%4*32,index//4*32))
    return image


def write_creature(model,palette,materials,animations,width,height,glow=(),variants=None,translucent=False):
    if width<=0 or height<=0:raise ValueError('Positive world dimensions required')
    # Vanilla removes dead mobs after20ticks; allow5blend ticks and finish every authored collapse first.
    death=animations.get('death')
    if death and death['animation_length']>.65:
        factor=.65/death['animation_length']
        death['animation_length']=.65
        for transforms in death.get('bones',{}).values():
            for channel,frames in transforms.items():
                if isinstance(frames,dict):
                    transforms[channel]={str(round(float(time)*factor,6)):value for time,value in frames.items()}
    names=set(model.by_name)
    for bone in model.bones:
        cursor=bone['name'];seen=set()
        while cursor in model.by_name:
            if cursor in seen:raise ValueError('Bone hierarchy cycle')
            seen.add(cursor);cursor=model.by_name[cursor].get('parent')
    for animation in animations.values():
        if not set(animation.get('bones',{}))<=names:raise ValueError('Animation uses unknown bone')
    images={'':palette,**(variants or {})}
    normal=material_atlas(palette,materials,translucent)
    native=blockbench(model,normal,animations)
    validate(model,animations,normal,native)
    texture_dir=ASSET/'textures/entity';texture_dir.mkdir(parents=True,exist_ok=True)
    for suffix,colors in images.items():
        image=normal if not suffix else material_atlas(colors,materials,translucent)
        image.save(texture_dir/f'{model.name}{suffix}.png')
        if glow:
            mask=Image.new('RGBA',(128,128))
            for index in glow:
                if not 0<=index<16:raise ValueError('Invalid glow material')
                x,y=index%4*32,index//4*32;mask.paste(image.crop((x,y,x+32,y+32)),(x,y))
            mask.save(texture_dir/f'{model.name}{suffix}_glowmask.png')
    # Generous bounds include wing tips, branch crowns and attack rotations.
    cubes=[cube for b in model.bones for cube in b.get('cubes',[])]
    extent=max(abs(c['origin'][axis])+c['size'][axis] for c in cubes for axis in (0,2))/16
    description={'identifier':'geometry.'+model.name,'texture_width':128,'texture_height':128,
        'visible_bounds_width':max(4,extent*2+2),'visible_bounds_height':max(4,height*2+1),'visible_bounds_offset':[0,height/2,0]}
    save(ASSET/f'geckolib/models/entity/{model.name}.geo.json',{'format_version':'1.12.0','minecraft:geometry':[{'description':description,'bones':model.bones}]})
    save(ASSET/f'geckolib/animations/entity/{model.name}.animation.json',{'format_version':'1.8.0','animations':animations})
    native['visible_box']=[description['visible_bounds_width'],description['visible_bounds_height'],height/2]
    save(ROOT/f'tools/blockbench/{model.name}.bbmodel',native)
    print(f'{model.name}: {len(model.bones)} bones, {len(cubes)} cubes, {len(animations)} clips; native/UV/PNG verified')
