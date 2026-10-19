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

def holstaurus():
    m,palette,roles,size,animations=load('holstaurus');X=m.box
    head=m.by_name['head'];head['cubes']=[c for c in head['cubes'] if not((v3.material_of(c)==6 and c['origin'][1]>25.8 and c['size'][2]>1) or (v3.material_of(c)==9 and c['origin'][2]<-2.5 and c['size'][2]<1.7))]
    for side,n in [(-1,'right'),(1,'left')]:
        # Short ivory horns and broad cow ears, rather than a tall helmet crest.
        X('head',[side*3.05-.85,25.8,-.45],[1.7,1.65,1.65],6,[0,0,-side*18])
        X('head',[side*3.4-.6,27.05,-.25],[1.2,.85,1.25],6,[0,0,-side*10])
        X('head',[side*4.6-1.05,23.8,-.3],[2.1,.55,1.2],7,[0,0,-side*9])
        # Rebuild bare arms as connected tapered volumes, removing the old plate/cuff geometry.
        arm='arm_'+n;fore='fore_'+n;m.by_name[arm]['cubes']=[];m.by_name[fore]['cubes']=[]
        x=side*3.2
        X(arm,[x-1,14.8,-1],[2,4.5,2.3],8)
        X(arm,[x-.82,18.8,-.85],[1.64,.85,1.95],8)
        X(fore,[x-.85,11.4,-1],[1.7,3.7,2.1],8)
        X(fore,[x-.7,14.6,-.82],[1.4,.65,1.8],8)
        X('chest',[side*1.4-.75,19.8,-2.4],[1.5,1.6,.65],11,[0,0,side*22])
        X('chest',[side*2-.2,18.1,-2.6],[.4,2.1,.5],11,[0,0,-side*9])
    for i,(x,y,w,h,ang) in enumerate([(-3.4,24.4,1.8,2,-12),(-2,24.7,1.7,1.8,-5),(-.55,24.25,1.8,2.3,5),(1,24.6,1.7,1.9,11),(2.4,24.9,1.3,1.5,17)]):
        X('head',[x,y,-3.18],[w,h,.85],9,[0,0,ang])
    for c in head['cubes']:
        if v3.material_of(c)==4:v3.repaint_cube(c,10)
    # A shoulder-length layered bob keeps the cow ears visible.
    for b in m.bones:
        if b['name'].startswith('hair_'):
            for c in b.get('cubes',[]):
                top=c['origin'][1]+c['size'][1];c['origin'][1]=max(20.7,c['origin'][1]);c['size'][1]=max(.35,top-c['origin'][1])
                if 'pivot' in c:c['pivot'][1]=c['origin'][1]+c['size'][1]/2
        if b['name'].startswith('leg_') and not b['name'].endswith('_foot'):
            for c in b.get('cubes',[]):
                if v3.material_of(c)==0:
                    # More texels are allocated to irregular cow markings, without enlarging the atlas.
                    for face,data in c['uv'].items():
                        dims=(c['size'][0],c['size'][1]) if face in ('north','south') else (c['size'][2],c['size'][1]) if face in ('west','east') else (c['size'][0],c['size'][2])
                        data['uv_size']=[min(27,max(1,round(x*4.4))) for x in dims]
        if b['name'].startswith('leg_') and b['name'].endswith('_foot'):
            for c in b.get('cubes',[]):
                if v3.material_of(c)==14 and c['size'][1]>.7:v3.repaint_cube(c,0)
    # The existing cow tail gains a small articulated tuft; hopping physics and its clip remain untouched.
    tail=m.by_name['tail'];m.bone('tail_tuft','tail',[0,5.3,3.5]);m.by_name['tail_tuft']['cubes']=tail['cubes'][1:];tail['cubes']=tail['cubes'][:1]
    for name,amplitude in [('idle',2),('walk',3.2),('run',4.5)]:
        clip=animations[name];length=clip['animation_length']
        clip['bones']['tail_tuft']={'rotation':{str(min(length,round(length*i/12,5))):[amplitude*math.sin(2*math.pi*i/12),0,amplitude*.4*math.cos(2*math.pi*i/12)] for i in range(13)}}
    palette[9]='b6b9c9';palette[3]='657995';palette[7]='b7a7ad';palette[0]='e7e7e2'
    support_death(m,animations)
    return m,palette,roles,size,animations

def centaur():
    m,palette,roles,size,animations=load('centaur');X=m.box
    # Faceted shoulder, barrel, tucked belly and rounded croup replace the bench-like trunk.
    m.by_name['horse_body']['cubes']=[]
    for origin,scale,mat in [([-4.4,11.3,1],[8.8,5.7,13.5],0),([-3.8,10.8,-1.1],[7.6,6.2,5.3],0),([-4.2,12,13],[8.4,5.2,5.7],2),([-3.4,10.25,3.3],[6.8,2.1,10.2],0),([-3.5,15.4,-.9],[7,3,6.4],0)]:X('horse_body',origin,scale,mat)
    for side,n in [(-1,'right'),(1,'left')]:
        X('horse_body',[side*3.75-1.1,11.4,12.4],[2.2,4.6,5.7],2,[0,side*8,-side*4])
        X('horse_body',[side*3.3-1,11.4,-.6],[2,4.8,5.2],0,[0,side*7,side*4])
        X('horse_body',[side*4.35-.25,12.3,3.5],[.5,4.7,1],10)
        X('horse_body',[side*4.45-.35,13.5,3.3],[.7,1,1.3],4)
        # Broad haunch, distinct hock and sloping cannon on each original three-joint chain.
        upper='hind_'+n;lower=upper+'_lower';foot=upper+'_foot'
        m.by_name[upper]['cubes']=[];m.by_name[lower]['cubes']=[]
        m.by_name[lower]['pivot']=[side*3.3,8,16.2]
        X(upper,[side*3.3-1.45,8.1,13.25],[2.9,6.1,3.9],2,[-7,0,0],[side*3.3,13,15])
        X(upper,[side*3.3-1.15,7.4,14.5],[2.3,2.7,2.8],0)
        X(lower,[side*3.3-.8,1.5,15.35],[1.6,6.5,1.7],0,[-10,0,0],[side*3.3,8,16.2])
        X(lower,[side*3.3-1.05,6.7,15.2],[2.1,2.1,2.4],2)
        # Retain forelegs/cuffs and all four individual hooves.
        arm='arm_'+n;m.by_name[arm]['cubes']=[c for c in m.by_name[arm]['cubes'] if v3.material_of(c) not in (3,12,14)]
        X(arm,[side*3.2-1.5,22.7,-1.55],[3,1.65,3.2],3,[0,0,-side*8])
        X(arm,[side*3.2-1.3,23.65,-1.45],[2.6,.55,3],14,[0,0,-side*8])
    # Allocate a previously unused corner of the gold tile to muted green irises.
    for c in m.by_name['head']['cubes']:
        if v3.material_of(c)==4:
            for face in c['uv'].values():face['uv']=[26,56];face['uv_size']=[4,5]
    # Four-beat walk: hind-left, front-left, hind-right, front-right; no server velocity changes.
    phases={'hind_left':0,'front_left':90,'hind_right':180,'front_right':270}
    walk=animations['walk']
    for name,phase in phases.items():
        swing=f'math.sin(query.anim_time * 300 + {phase}) * 17'
        knee=f'math.max(0, math.sin(query.anim_time * 300 + {phase} - 30)) * 20'
        walk['bones'][name]={'rotation':[swing,0,0],'position':[0,f'math.max(0, math.sin(query.anim_time * 300 + {phase})) * 0.5',0]}
        walk['bones'][name+'_lower']={'rotation':[knee,0,0]}
        walk['bones'][name+'_foot']={'rotation':[f'-({swing}) - ({knee})',0,0]}
    # Corrective comparison: compact the horse silhouette coherently, including hock pivots and tail.
    for bone in m.bones:
        if bone['name']=='horse_body' or bone['name'].startswith(('hind_','tail')):
            bone['pivot'][2]*=.78
            for c in bone.get('cubes',[]):
                c['origin'][2]*=.78;c['size'][2]*=.78
                if 'pivot' in c:c['pivot'][2]*=.78
    head=m.by_name['head'];head['cubes']=[c for c in head['cubes'] if not(v3.material_of(c)==9 and c['origin'][2]<-2.5 and c['size'][2]<1.5 and c['size'][1]>.5)]
    for x,y,w,h,ang in [(-3,28.65,1.7,1.9,-11),(-1.6,28.9,1.8,1.7,-5),(-.05,28.5,1.8,2,9),(1.5,28.95,1.6,1.6,17)]:
        X('head',[x,y,-3.2],[w,h,.8],9,[0,0,ang])
    for side in (-1,1):X('head',[side*3.5-.22,29.15,-.8],[.44,.65,3.2],10)
    palette[3]='858b89'
    # Keep the existing fast diagonal trot and all combat clips, soften idle tail tip lag.
    idle=animations['idle'];length=idle['animation_length']
    idle['bones']['tail_tip']={'rotation':{str(min(length,round(length*i/12,5))):[2.2*math.sin(2*math.pi*i/12-.35),3*math.sin(2*math.pi*i/12-.5),0] for i in range(13)}}
    for j in range(2):X('tail_tip',[-.95+j*.9,4.1+j*.2,15.015],[1,3.2,1.56],9,[-10,0,(j-.5)*10])
    support_death(m,animations)
    return m,palette,roles,size,animations

def sahuagin():
    m,palette,roles,size,animations=load('sahuagin');X=m.box
    # Short teal locks and overlapping gill-fan membranes keep the marine silhouette distinct.
    for b in m.bones:
        if b['name'].startswith('hair_'):
            for c in b.get('cubes',[]):
                top=c['origin'][1]+c['size'][1];c['origin'][1]=max(19.55,c['origin'][1]);c['size'][1]=max(.3,top-c['origin'][1])
                if 'pivot' in c:c['pivot'][1]=c['origin'][1]+c['size'][1]/2
    for side,n in [(-1,'right'),(1,'left')]:
        fin='fin_head_'+str(side);m.by_name[fin]['cubes']=[]
        for x,y,z,w,h,depth in [(4.2,21.6,.2,.6,4,2.9),(4.65,22.2,2,.5,3,1.9),(4.9,22.6,3.1,.44,1.9,1.4)]:
            X(fin,[side*x-w/2,y,z],[w,h,depth],12)
        X(fin,[side*4.3-.13,22,.15],[.26,3.2,2.9],2)
        fore='fore_'+n;m.by_name[fore]['cubes']=[];x=side*3.2
        X(fore,[x-1.1,10.8,-1.25],[2.2,4.15,2.65],3)
        X(fore,[x-1.25,14,-1.38],[2.5,1,2.9],2)
        X(fore,[side*4.5-.3,11.8,.3],[.6,3,2.2],12)
        X(fore,[side*4.85-.28,12.5,1.8],[.56,2.1,1.7],12)
        X(fore,[side*4.55-.12,12,.25],[.24,2.7,.35],2)
        X('hand_'+n,[x-.9,10.2,-1.42],[1.8,.8,.3],12)
        lower='leg_'+n+'_lower';m.by_name[lower]['cubes']=m.by_name[lower]['cubes'][:2]
        X(lower,[side*2.4-.25,2.4,.2],[.5,3,2.6],12)
        X(lower,[side*2.65-.22,3,1.7],[.44,1.8,1.7],12)
        foot='leg_'+n+'_foot';m.by_name[foot]['cubes']=[];x=side*1.45
        X(foot,[x-1,.1,-.7],[2,1.5,1.8],3)
        X(foot,[x-1.4,.1,-3.1],[2.8,.75,2.7],12)
        for j in range(3):X(foot,[x-1.1+j*.75,.12,-3.45],[.7,.85,1.5],2)
    head=m.by_name['head'];head['cubes']=[c for c in head['cubes'] if not(v3.material_of(c)==9 and c['origin'][2]<-2.5 and c['size'][2]<1.6 and c['size'][1]>.5)]
    for x,y,w,h,ang in [(-3,24.2,1.7,2,-12),(-1.55,24.55,1.7,1.7,-4),(0,24.1,1.8,2.2,9),(1.6,24.65,1.4,1.5,17)]:
        X('head',[x,y,-3.05],[w,h,.8],9,[0,0,ang])
    X('chest',[-.55,18.45,-2.75],[1.1,1.1,.4],6,[0,0,45])
    for j in range(3):X('body',[-2.25+j*1.55,10.8+(j%2)*.2,-2.1],[1.4,1.8,.4],13,[0,0,(j-1)*7])
    for side,n in [(-1,'right'),(1,'left')]:
        X('fore_'+n,[side*5.05-.25,13,1],[.5,1.5,1.4],12,[0,0,-side*15])
    for c in m.by_name['weapon']['cubes']:
        if v3.material_of(c)==12:v3.repaint_cube(c,14)
    # A delayed caudal wave replaces rigid in-phase tail motion; root swim/body pose is retained.
    for name,speed,amp in [('swim',300,11),('idle_swim',160,3)]:
        animations[name]['bones']['tail']={'rotation':[f'math.sin(query.anim_time * {speed}) * {amp*.4}',f'math.sin(query.anim_time * {speed}) * {amp}',0]}
        animations[name]['bones']['tail_tip']={'rotation':[f'math.sin(query.anim_time * {speed} - 50) * {amp*.65}',f'math.sin(query.anim_time * {speed} - 55) * {amp*1.25}',0]}
    palette[9]='30584f';palette[8]='dacbb8';roles[3]='scale'
    support_death(m,animations)
    return m,palette,roles,size,animations

def valkyrie():
    m,palette,roles,size,animations=load('valkyrie');X=m.box
    head=m.by_name['head'];eyes=[c for c in head['cubes'] if v3.material_of(c)==4]
    head['cubes']=[c for c in head['cubes'] if v3.material_of(c) not in (2,3,6,12,14) and not(c['origin'][2]<-2.7 and c['size'][2]<.3)]
    # A fitted dome, single brow and swept thin crests replace the stacked helmet bands.
    X('head',[-3.65,30.2,-3.15],[7.3,1.1,6.4],2)
    X('head',[-2.85,31.4,-2.45],[5.7,.6,5.2],14)
    X('head',[-2,31.6,-1.8],[4,.5,3.8],3)
    X('head',[-3.6,29.9,-3.5],[7.2,.75,.65],12)
    X('head',[-3.2,29.65,-3.65],[6.4,.25,.35],14)
    for side,n in [(-1,'right'),(1,'left')]:
        X('head',[side*3.2-.5,26.3,-2.75],[1,3.7,2.7],2)
        X('head',[side*3.25-.26,26.1,-2.9],[.52,1.2,1.9],12)
        X('head',[side*3.3-.38,30.1,-.8],[.76,3.4,1.2],12,[0,0,-side*45])
        X('head',[side*4.1-.3,31,-.7],[.6,2.5,1.1],12,[0,0,-side*60])
        X('head',[side*4.15-.2,32.2,-.73],[.4,.9,.8],6,[0,0,-side*60])
        shin='shin_'+n;m.by_name[shin]['cubes']=[c for c in m.by_name[shin]['cubes'] if v3.material_of(c)!=12]
        for y,h in ((2.25,.7),(6.6,.8)):X(shin,[side*1.35-1.4,y,-1.65],[2.8,h,.5],12)
        X(shin,[side*1.35-1.4,7.2,-1.55],[2.8,1.1,3.2],14,[0,0,-side*5])
        # More compact overlapping faulds show the articulated underlayer at the knee.
        for c in m.by_name['fauld_'+n]['cubes']:
            top=c['origin'][1]+c['size'][1];c['origin'][1]=max(11.7,c['origin'][1]);c['size'][1]=max(.45,top-c['origin'][1])
            if 'pivot' in c:c['pivot'][1]=c['origin'][1]+c['size'][1]/2
        for c in m.by_name['leg_'+n]['cubes']:v3.repaint_cube(c,10)
        # Fold the retained detailed feathers along the back during the death pose.
        animations['death']['bones']['wing_'+n]={'rotation':{'0':[0,side*90,side*15]}}
        animations['death']['bones']['wingtip_'+n]={'rotation':{'0':[0,0,side*10]}}
    # Slim red eyes framed by the skin plane rather than dark rectangular rims.
    for c in eyes:
        x=c['origin'][0]+c['size'][0]/2;y=c['origin'][1];z=c['origin'][2]
        X('head',[x-.78,y,z+.2],[1.56,1.02,.14],8)
        X('head',[x-.4,y+.05,z+.03],[.8,.92,.12],4)
        X('head',[x-.1,y+.08,z-.1],[.2,.82,.1],5)
        X('head',[x-.3,y+.72,z-.21],[.17,.18,.08],15)
    for b in m.bones:
        if b['name'].startswith('hair_'):
            for c in b.get('cubes',[]):
                top=c['origin'][1]+c['size'][1];c['origin'][1]=max(23,c['origin'][1]);c['size'][1]=max(.3,top-c['origin'][1])
                if 'pivot' in c:c['pivot'][1]=c['origin'][1]+c['size'][1]/2
    m.by_name['sword']['rotation']=[25,0,0]
    shield=m.by_name['shield'];pivot=shield['pivot']
    for c in shield['cubes']:
        c['origin']=[pivot[i]+(c['origin'][i]-pivot[i])*.88 for i in range(3)];c['size']=[x*.88 for x in c['size']]
        if 'pivot' in c:c['pivot']=[pivot[i]+(c['pivot'][i]-pivot[i])*.88 for i in range(3)]
    # Feather tips trail the main flap by one existing sample, with the loop seam kept closed.
    for name in ('fly','hover'):
        for bone,channels in animations[name]['bones'].items():
            if bone.startswith('wingtip_') and isinstance(channels.get('rotation'),dict):
                frames=channels['rotation'];keys=sorted(frames,key=float);values=[copy.deepcopy(frames[k]) for k in keys[:-1]]
                for j,key in enumerate(keys[:-1]):frames[key]=values[(j-1)%len(values)]
                frames[keys[-1]]=copy.deepcopy(frames[keys[0]])
    palette[9]='c9b271';palette[2]='9ba2a1';palette[6]='cdd3cf'
    support_death(m,animations)
    return m,palette,roles,size,animations

BUILDERS={'ender_dragon_girl':ender_dragon_girl,'vampire':vampire,'holstaurus':holstaurus,'centaur':centaur,'sahuagin':sahuagin,'valkyrie':valkyrie}

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
    if species=='holstaurus':
        d=ImageDraw.Draw(image);d.rectangle((0,0,31,31),fill=(232,232,226,255))
        d.rectangle((0,64,31,95),fill=(223,201,179,255))
        d.rectangle((3,67,8,72),fill=(226,204,182,255));d.rectangle((7,80,11,85),fill=(220,198,176,255))
        for points,color in [([(3,3),(7,2),(10,5),(8,10),(4,9)],(143,149,164,255)), ([(13,12),(19,10),(23,14),(21,20),(15,22),(12,18)],(126,137,154,255)), ([(2,18),(6,17),(9,22),(7,27),(2,28)],(175,179,188,255))]:d.polygon(points,fill=color)
    if species=='centaur':
        d=ImageDraw.Draw(image);d.rectangle((26,56,30,61),fill=(75,105,80,255));d.rectangle((26,56,30,57),fill=(108,133,98,255))
        d.rectangle((0,0,31,31),fill=(121,81,60,255))
        d.polygon([(2,3),(15,2),(28,7),(26,12),(12,10),(3,13)],fill=(135,92,67,255))
        d.polygon([(3,17),(14,14),(27,19),(29,28),(9,29),(2,25)],fill=(108,71,54,255))
    if species=='sahuagin':
        d=ImageDraw.Draw(image);d.rectangle((0,96,31,127),fill=(53,86,124,255))
        d.rectangle((32,64,63,95),fill=(44,81,72,255))
        for points,color in [([(34,66),(38,66),(41,70),(39,75),(35,73)],(56,96,83,255)), ([(44,69),(53,67),(60,73),(56,80),(46,78)],(36,70,63,255)), ([(34,82),(43,80),(47,88),(39,93),(34,91)],(49,88,77,255))]:d.polygon(points,fill=color)
        for points,color in [([(2,99),(12,106),(28,123)],(66,103,142,255)), ([(3,120),(14,112),(28,115)],(40,71,108,255))]:d.line(points,fill=color,width=1)
    return image

def main():
    p=argparse.ArgumentParser();p.add_argument('species',choices=BUILDERS);a=p.parse_args()
    state=json.loads((DOC/'state.json').read_text());assert state['active']==a.species,'Export only the single active creature'
    m,palette,roles,size,animations=BUILDERS[a.species]()
    pipeline.material_atlas=lambda p,r,t=False:atlas(p,r,t,a.species)
    pipeline.write_creature(m,palette,roles,animations,*size,glow={'vampire':(13,),'holstaurus':(),'centaur':(),'sahuagin':(),'anubis':(7,),'kobold':(13,),'cyclops':(7,),'dhampir':(7,),'werecat':()}.get(a.species,(4,)))
if __name__=='__main__':main()
