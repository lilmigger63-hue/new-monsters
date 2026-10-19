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

def vampire():
    m,palette,roles,size,animations=load('vampire');X=m.box
    # Short layered blonde bob instead of shoulder-length solid side slabs.
    for n,side in [('right',-1),('left',1)]:
        m.by_name['hair_'+n]['cubes']=[];m.by_name['hair_tip_'+n]['cubes']=[]
        X('hair_'+n,[side*3.25-.8,23.1,-1.7],[1.6,5.6,3.7],5,[0,0,-side*5])
        X('hair_'+n,[side*3.5-.55,23.2,-2.35],[1.1,4.6,1.5],8,[0,0,-side*8])
        X('hair_tip_'+n,[side*3.35-.65,22.2,-1.2],[1.3,2.1,3],8,[0,0,side*12])
    for c in m.by_name['hair_back']['cubes']:
        top=c['origin'][1]+c['size'][1];c['origin'][1]=22.1;c['size'][1]=top-22.1
    # Remove repeated metallic waistcoat bars; one small clasp remains.
    m.by_name['body']['cubes']=[c for c in m.by_name['body']['cubes'] if v3.material_of(c) not in (4,9)]
    X('body',[-.45,15.5,-2.65],[.9,.8,.35],9)
    for side in (-1,1):
        X('body',[side*1.7-.25,13.4,-2.35],[.5,4.1,.35],15)
        X('chest',[side*1.1-.5,19.7,-2.95],[1,1.1,.5],11,[0,0,side*24])
    # A voluminous dark mantle with visible burgundy lining, on the existing cape rig.
    m.by_name['cape']['cubes']=[]
    X('cape',[-4.2,10.8,3.05],[8.4,11.8,1],15)
    X('cape',[-4.45,21,2.75],[8.9,2.2,1.8],15)
    for n,side in [('right',-1),('left',1)]:
        for x,y,w,h,angle in [(4.1,15.7,2.5,6.8,9),(5,10.3,2.8,7.1,15),(5.4,6.6,3,5.2,20)]:
            X('cape',[side*x-w/2,y,2.75],[w,h,1.65],15,[0,0,-side*angle])
            X('cape',[side*x-w/2+.2,y+.15,2.54],[w-.4,h-.45,.32],3,[0,0,-side*angle])
        bone='cape_lower_'+n;m.bone(bone,'cape',[side*3.2,12.5,3.5])
        X(bone,[side*3.15-2.4,1.15,3.4],[4.8,12.3,1.1],15,[0,0,-side*6])
        X(bone,[side*4.4-1.1,1.2,3.12],[2.2,7.6,.4],10,[0,0,-side*8])
        X(bone,[side*3.2-2.45,1.1,3.15],[4.9,1,.7],10,[0,0,-side*6])
        # Pleated skirt panels replace ladder-like horizontal rectangular borders.
        coat='coat_'+n;m.by_name[coat]['cubes']=[]
        X(coat,[side*1.65-1.7,1.7,-2.15],[3.4,9.5,4.3],15,[0,0,-side*4])
        for j in range(3):
            X(coat,[side*1.65-1.4+j*.94,2.7,-2.45],[.82,7.9,.5],3 if j%2 else 10,[0,0,-side*4])
        X(coat,[side*1.65-1.75,1.55,-2.22],[3.5,1.15,4.45],15,[0,0,-side*4])
        X(coat,[side*1.65-1.65,10.3,-2.3],[3.3,.7,.45],11)
        for name,amplitude in [('idle',1.2),('walk',2.4),('run',3.6)]:
            clip=animations[name];length=clip['animation_length']
            clip['bones'][bone]={'rotation':{str(min(length,round(length*i/12,5))):[amplitude*math.sin(2*math.pi*i/12),side*.7*math.cos(2*math.pi*i/12),side*amplitude*.35*math.sin(2*math.pi*i/12)] for i in range(13)}}
    # Corrective pass: swept overlapping locks, a dimensional rosette and layered jabot.
    head=m.by_name['head'];head['cubes']=[c for c in head['cubes'] if not(v3.material_of(c) in (5,8) and c['origin'][2]<-2.5 and .6<c['size'][1]<3 and c['size'][2]<2.6)]
    for i,(x,y,w,h,ang) in enumerate([(-3,26.5,1.6,2.1,-12),(-1.8,26.8,1.6,2,-8),(-.5,26.4,1.7,2.2,8),(.9,26.8,1.5,1.9,14),(2.1,27.1,1.2,1.6,19)]):
        X('head',[x,y,-3.3],[w,h,.9],8 if i%2 else 5,[0,0,ang])
    for x,y,w,h,ang in [(2.1,28.5,1.1,.7,-24),(2.7,28.2,.9,.8,18),(2.8,28.9,.8,.65,35)]:
        X('head',[x,y,-2.2],[w,h,.65],7,[0,0,ang])
    X('head',[2.75,28.55,-2.45],[.65,.65,.4],10)
    for side in (-1,1):
        X('chest',[side*.8-.55,19.3,-3.1],[1.1,1.1,.45],11,[0,0,side*18])
        X('chest',[side*.45-.4,18.8,-3.15],[.8,.8,.4],11,[0,0,side*9])
    # Turn the dagger forward/down from its grip instead of back into the forearm.
    m.by_name['dagger']['rotation']=[112,0,0]
    palette[5]='c9ad68';palette[8]='b49a59';palette[3]='632333';palette[10]='922b42'
    support_death(m,animations)
    return m,palette,roles,size,animations

BUILDERS={'ender_dragon_girl':ender_dragon_girl,'vampire':vampire}

def atlas(palette,roles,translucent,species):
    image=v3.reference_atlas(palette,roles,translucent,species)
    # Broad membrane planes stay dark; seams and veins must not look like pale rib bars.
    if species=='ender_dragon_girl':
        d=ImageDraw.Draw(image);x,y=96,32
        d.rectangle((x,y,x+31,y+31),fill=(26,27,34,255))
        for points,color in [([(2,3),(12,13),(28,28)],(35,36,44,255)), ([(4,25),(13,18),(28,22)],(20,21,28,255))]:d.line([(x+a,y+b) for a,b in points],fill=color,width=1)
    if species=='vampire':
        d=ImageDraw.Draw(image)
        for rect,color in [((99,101,110,109),(31,32,39,255)),((114,107,123,120),(21,23,29,255)),((101,116,112,125),(28,30,36,255))]:d.rectangle(rect,fill=color)
    return image

def main():
    p=argparse.ArgumentParser();p.add_argument('species',choices=BUILDERS);a=p.parse_args()
    state=json.loads((DOC/'state.json').read_text());assert state['active']==a.species,'Export only the single active creature'
    m,palette,roles,size,animations=BUILDERS[a.species]()
    pipeline.material_atlas=lambda p,r,t=False:atlas(p,r,t,a.species)
    pipeline.write_creature(m,palette,roles,animations,*size,glow={'vampire':(13,),'holstaurus':(),'centaur':(),'sahuagin':(),'anubis':(7,),'kobold':(13,),'cyclops':(7,),'dhampir':(7,),'werecat':()}.get(a.species,(4,)))
if __name__=='__main__':main()
