#!/usr/bin/env python3
"""Original V5.3 art: one explicit active species; never rewrites another creature."""
import argparse,copy,json,math
from pathlib import Path
from PIL import ImageDraw
import generate_visual_overhaul_v3 as v3
import overhaul_asset_pipeline as pipeline
from visual_v3_geometry import support_death
ROOT=Path(__file__).resolve().parents[1];DOC=ROOT/'docs/monster-girl-v5-3';ASSET=v3.ASSET

def load(species):
    m=pipeline.Model(species)
    m.bones=json.loads((DOC/'baselines'/ASSET/'geckolib/models/entity'/f'{species}.geo.json').read_text())['minecraft:geometry'][0]['bones'];m.by_name={b['name']:b for b in m.bones}
    _,palette,roles,size=v3.BUILDERS[species]()
    animations=json.loads((DOC/'baselines'/ASSET/'geckolib/animations/entity'/f'{species}.animation.json').read_text())['animations']
    return m,palette,roles,size,animations

def ender_dragon_girl():
    m,palette,roles,size,animations=load('ender_dragon_girl');X=m.box
    # Clear the old silver/black rectangular eye stacks and high flat brow strips.
    head=m.by_name['head'];head['cubes']=[c for c in head['cubes'] if not(c['origin'][2]<-2.8 and c['size'][2]<.3)]
    for side in (-1,1):
        x=side*1.52
        X('head',[x-.95,28.32,-3.11],[1.9,1.06,.16],15)
        X('head',[x-.62,28.35,-3.3],[1.24,1.01,.12],4)
        X('head',[x-.14,28.38,-3.44],[.28,.96,.1],5)
        X('head',[x-.5,29.05,-3.55],[.18,.22,.08],15)
        X('head',[x-.99,29.35,-3.29],[1.98,.19,.22],9,[0,0,-side*6])
    # Sweep the original fringe into short uneven locks; no detached goggle/brow silhouette.
    for c in head['cubes']:
        if v3.material_of(c)==9 and c['size'][0]<3 and c['origin'][2]<-3:
            c['origin'][1]-=.45;c['rotation']=[0,0,9 if c['origin'][0]<0 else -11]
            c['pivot']=[c['origin'][0]+c['size'][0]/2,c['origin'][1]+c['size'][1],c['origin'][2]+c['size'][2]/2]
    # Broad overlapping membrane panels on the existing two-joint wing rig.
    for side,n in [(-1,'right'),(1,'left')]:
        name='wingtip_'+n;m.by_name[name]['cubes']=[]
        for x,top,bottom,w in [(5.2,24.3,17.8,3.2),(7.5,23.6,17.5,3.5),(9.7,21.9,18.3,2.3)]:
            X(name,[side*x-w/2,bottom,2.15],[w,top-bottom,.44],7)
        for x,y,w in [(5.4,16.9,1.7),(7.6,16.65,1.8),(9.7,17.5,1.3)]:
            X(name,[side*x-w/2,y,2.16],[w,1.25,.42],7)
        X(name,[side*6.5-2.2,23.25,2.09],[4.4,.3,.52],5,[0,0,side*12])
        # Broad stepped horns avoid the long thin antenna-like silhouette.
        horn='horn_'+n;m.by_name[horn]['cubes']=[]
        X(horn,[side*2.45-1.12,31,.05],[2.24,3.2,2.2],6,[-24,0,-side*5])
        X(horn,[side*2.6-.95,33.2,1.2],[1.9,1.8,1.7],6,[-24,0,-side*5])
        # Shorter split overskirt lets the already animated lower legs read clearly.
        for c in m.by_name['skirt_'+n]['cubes']:
            top=c['origin'][1]+c['size'][1]
            c['origin'][1]=max(c['origin'][1],8.3)
            c['size'][1]=max(.4,top-c['origin'][1])
            if 'pivot' in c:c['pivot'][1]=c['origin'][1]+c['size'][1]/2
        # Upper arms remain scale covered rather than showing a pale elbow band.
        for c in m.by_name['arm_'+n]['cubes']:
            if v3.material_of(c)==8:v3.repaint_cube(c,1)
        for c in m.by_name['forearm_'+n]['cubes']:
            if v3.material_of(c) in (0,8):v3.repaint_cube(c,1)
            if v3.material_of(c)==1:c['size'][0]*=1.06
    # Expose a coherent pale chest opening, framed by a dark shoulder yoke.
    chest=m.by_name['chest'];chest['cubes']=[c for c in chest['cubes'] if not(v3.material_of(c)==2 and c['origin'][2]<-2.5)]
    X('chest',[-2.1,20.65,-3.05],[4.2,3.15,.62],8)
    for side in (-1,1):X('chest',[side*2.05-.55,20.35,-3.25],[1.1,3.55,.55],2,[0,0,-side*12])
    X('chest',[-2.5,23.45,-2.9],[5,.7,1.2],2)
    palette[4]='b96fe3';palette[7]='1c1c23';palette[6]='929590';palette[9]='15161c'
    # Subtle phase-offset secondary motion; all gameplay/attack clips stay byte-identical.
    idle=animations['idle'];length=idle['animation_length']
    for i in range(5):
        idle['bones']['hair_back_'+str(i)]['rotation']={str(round(length*j/12,5)):[-1.8+1.7*math.sin(2*math.pi*j/12+i*.22),1.1*math.sin(2*math.pi*j/12+i*.3),.5*math.cos(2*math.pi*j/12+i*.2)] for j in range(13)}
    for name in ('fly','hover'):
        for bone,channels in animations[name]['bones'].items():
            if bone.startswith('wingtip_'):
                for key,value in channels.get('rotation',{}).items():
                    if isinstance(value,list):channels['rotation'][key]=[v*.86 for v in value]
    support_death(m,animations)
    return m,palette,roles,size,animations

BUILDERS={'ender_dragon_girl':ender_dragon_girl}

def atlas(palette,roles,translucent,species):
    image=v3.reference_atlas(palette,roles,translucent,species)
    # Broad membrane planes stay dark; seams and veins must not look like pale rib bars.
    if species=='ender_dragon_girl':
        d=ImageDraw.Draw(image);x,y=96,32
        d.rectangle((x,y,x+31,y+31),fill=(26,27,34,255))
        for points,color in [([(2,3),(12,13),(28,28)],(35,36,44,255)), ([(4,25),(13,18),(28,22)],(20,21,28,255))]:d.line([(x+a,y+b) for a,b in points],fill=color,width=1)
    return image

def main():
    p=argparse.ArgumentParser();p.add_argument('species',choices=BUILDERS);a=p.parse_args()
    state=json.loads((DOC/'state.json').read_text());assert state['active']==a.species,'Export only the single active creature'
    m,palette,roles,size,animations=BUILDERS[a.species]()
    pipeline.material_atlas=lambda p,r,t=False:atlas(p,r,t,a.species)
    pipeline.write_creature(m,palette,roles,animations,*size,glow=(4,))
if __name__=='__main__':main()
