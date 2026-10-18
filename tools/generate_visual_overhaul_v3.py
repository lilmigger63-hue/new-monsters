#!/usr/bin/env python3
"""Original V3 artwork. Explicitly exports ONE selected species per invocation."""
import argparse,copy,json,subprocess,math
from pathlib import Path
from PIL import ImageDraw
import overhaul_asset_pipeline as pipeline
from overhaul_asset_pipeline import Model,write_creature
ROOT=Path(__file__).resolve().parents[1]
BASE='50dfab973a053e6c6761f45771e72c898f3963d4'
ASSET=Path('src/main/resources/assets/mythic_realms_creatures')

def baseline(path):
    cache=ROOT/'tools/visual_v3_baselines'/path.name
    if not cache.exists():
        cache.parent.mkdir(parents=True,exist_ok=True)
        cache.write_bytes(subprocess.check_output(['git','show',BASE+':'+str(path)],cwd=ROOT))
    return json.loads(cache.read_text())

def old_model(name,clear=False):
    m=Model(name)
    m.bones=copy.deepcopy(baseline(ASSET/'geckolib/models/entity'/f'{name}.geo.json')['minecraft:geometry'][0]['bones'])
    m.by_name={b['name']:b for b in m.bones}
    if clear:
        for b in m.bones:b['cubes']=[];b.pop('rotation',None)
    return m

def harpy():
    m=old_model('harpy',True);X=m.box
    def joint(n,p):m.by_name[n]['pivot']=p
    joint('body',[0,14,0]);joint('head',[0,21,0])
    # Compact feathered hips, shaped waist and pale shoulder/chest opening.
    for o,s,k in [([-2.9,11.5,-2],[5.8,3.8,4.2],0),([-2.25,15,-1.7],[4.5,3.3,3.4],8),([-3,17.4,-1.8],[6,2.9,3.6],8),([-1.1,19.8,-1],[2.2,1.4,2],8)]:X('body',o,s,k)
    for side in (-1,1):
        X('body',[side*1.4-1.5,17.3,-2.4],[3,2.1,1.4],0,[0,0,-side*8])
        X('body',[side*2.5-.7,18.3,-1.9],[1.4,2.6,3.7],1,[0,0,-side*15])
        for j in range(3):X('body',[side*(1+j*.8)-.65,10.7+j*.3,-2.25],[1.3,3.3,.9],2 if j%2 else 0,[0,0,-side*(8+j*8)])
    for side in (-1,1):
        X('body',[side*.9-.4,15.8,-2.27],[.8,4.4,.5],1,[0,0,-side*22])
    # Broad face framed by swept triangular bangs; avoid an elongated mask.
    X('head',[-3.65,20.8,-3.15],[7.3,6.6,6.1],8)
    X('head',[-3.1,20.45,-2.9],[6.2,.85,5.5],8)
    X('head',[-.35,23,-3.55],[.7,.6,.6],8)
    X('head',[-.65,21.8,-3.4],[1.3,.16,.18],7)
    for side in (-1,1):
        x=side*1.85
        X('head',[x-.9,23,-3.32],[1.8,1.4,.17],8)
        X('head',[x-.76,23.1,-3.49],[1.52,1.27,.16],15)
        X('head',[x-.37,23.1,-3.66],[.74,1.25,.13],4)
        X('head',[x-.13,23.14,-3.78],[.26,1.15,.1],5)
        X('head',[x-.25,23.88,-3.89],[.22,.25,.08],15)
        X('head',[x-1,24.45,-3.5],[2,.24,.25],9)
    X('head',[-3.9,26.2,-3.35],[7.8,1.7,6.65],9)
    X('head',[-3.8,23.8,2.05],[7.6,3.7,1.65],9)
    for side,n in [(-1,'right'),(1,'left')]:
        joint('temple_'+n,[side*3.4,26.8,0])
        X('temple_'+n,[side*3.4-.8,21.3,-1.6],[1.6,5.8,3.5],9)
        X('temple_'+n,[side*3.7-.8,22.1,1],[1.6,3.7,3.4],1,[0,0,-side*16])
        for j in range(3):X('head',[side*(.9+j*1.1)-.8,25.1+j*.33,-3.45],[1.6,2.4-j*.25,.7],9,[0,0,-side*(12+j*8)])
    for i in range(5):
        name='crest_'+str(i);x=(i-2)*1.15;joint(name,[x,27,1.5])
        X(name,[x-.75,25.5,1.1],[1.5,2.7,3.7],9)
        if i==2:
            for j,(w,h) in enumerate([(2.2,1.8),(1.5,1.5),(.7,1.1)]):
                X(name,[-w/2,27.5+j*1.1,1.5+j*.35],[w,h,1.8-j*.35],9,[-18,0,0])
    # Short, fully filled rear locks; keep existing secondary-motion bones.
    for i in range(7):
        name='v2_hair_'+str(i);x=(i-3)*1.02;joint(name,[x,27,2.7])
        X(name,[x-.65,20.1+abs(i-3)*.35,2.5],[1.3,6.9-abs(i-3)*.35,1.5],9)
    for side in (-1,1):
        name='v2_hair_temple_'+str(side);joint(name,[side*3.5,26.6,-.8])
        X(name,[side*3.5-.7,22.1,-1.3],[1.4,4.5,1.2],9)
    for side,n in [(-1,'right'),(1,'left')]:
        wing='wing_'+n;tip='wingtip_'+n
        joint(wing,[side*3,19.7,0]);joint(tip,[side*6,16.1,0])
        m.by_name[wing]['rotation']=[0,0,side*20]
        X(wing,[side*3.7-1,15.8,-1],[2,5.1,2],8)
        X(tip,[side*6-1.15,12.5,-.9],[2.3,4.2,1.9],0)
        for j in range(5):
            x=side*(3.3+j*.65)
            X(wing,[x-.9,14.2-j*.3,-1.35],[1.8,3.7,1.1],0 if j%2 else 2,[0,0,side*(10+j*6)])
        for j in range(7):
            x=side*(5.5+j*.85);y=14.9-j*.2;length=8.1+(3-abs(3-j))*.9
            # Gecko mirrors cube Z rotations; negative signs fan the tips outward.
            p=[x,y,0];angle=-side*(12+j*7)
            for fraction,width,start,depth in [(.63,2.5,0,1.15),(.29,1.9,.58,1),(.2,1.15,.83,.8)]:
                X(tip,[x-width/2,y-length*(start+fraction),.1],[width,length*fraction,depth],0 if j%2 else 2,[0,0,angle],p)
            X(tip,[x-.7,y-1.8,-.55],[1.4,2.5,.7],1,[0,0,angle],p)
        joint('leg_'+n,[side*1.85,12.5,0]);joint('talon_'+n,[side*1.85,6.4,.5])
        X('leg_'+n,[side*1.85-1.2,6.2,-.7],[2.4,6.5,2.5],0)
        for j in range(3):X('leg_'+n,[side*1.85-1.4+j*.85,7.5+j%2*.6,-1.05],[.95,3,1.3],2)
        X('talon_'+n,[side*1.85-.75,1.2,.15],[1.5,5.5,1.5],3)
        X('talon_'+n,[side*1.85-1.05,.65,-.5],[2.1,1.2,2],3)
        for j in range(3):
            x=side*1.85+(j-1)*.9
            X('talon_'+n,[x-.31,.12,-3.2],[.62,.85,3.9],5)
            X('talon_'+n,[x-.23,.12,-3.65],[.46,.45,.8],6)
        X('talon_'+n,[side*1.85-.35,.2,.6],[.7,.75,2.7],5)
    # Bird hocks bend behind the feathered thighs; an ankle joint keeps toes flat.
    for side,n in [(-1,'right'),(1,'left')]:
        leg=m.by_name['leg_'+n];shin=m.by_name['talon_'+n]
        leg['rotation']=[-16,0,0];shin['rotation']=[30,0,0]
        foot='foot_'+n;m.bone(foot,'talon_'+n,[side*1.85,1.2,.5],[-14,0,0])
        m.by_name[foot]['cubes']=shin['cubes'][1:];shin['cubes']=shin['cubes'][:1]
    feet=[]
    for n in ('right','left'):
        for c in m.by_name['foot_'+n]['cubes']:
            for bits in range(8):
                p=[c['origin'][i]+(c['size'][i] if bits&(1<<i) else 0) for i in range(3)]
                b=m.by_name['foot_'+n]
                while b['name']!='root':
                    angle=math.radians(-b.get('rotation',[0,0,0])[0]);v=b['pivot'];dy=p[1]-v[1];dz=p[2]-v[2]
                    p[1]=v[1]+dy*math.cos(angle)-dz*math.sin(angle);p[2]=v[2]+dy*math.sin(angle)+dz*math.cos(angle)
                    b=m.by_name[b['parent']]
                feet.append(p[1])
    shift=.12-min(feet)
    for b in m.bones:
        b['pivot'][1]+=shift
        for c in b.get('cubes',[]):
            c['origin'][1]+=shift
            if 'pivot' in c:c['pivot'][1]+=shift
    joint('tail',[0,12.5+shift,2])
    for j in range(5):X('tail',[-2.9+j*1.2,8.7+abs(2-j)*.35+shift,1.8],[1.5,4.5,1.6],0 if j%2 else 2,[-18,0,(j-2)*10])
    palette=['68402c','38251e','986144','7e8443','9b312b','241f19','dfd5af','805039','ead5be','69432f','56301f','9b673d','b57d54','68462e','a3a05c','fff0d8']
    roles=['feather','feather','feather','scales','eyes','cloth','bone','feather','skin','hair','leather','feather','feather','feather','scales','skin']
    return m,palette,roles,(.9,1.8)

def dryad():
    m=old_model('forest_dryad',True);X=m.box
    def joint(n,p):m.by_name[n]['pivot']=p
    joint('body',[0,12,0]);joint('head',[0,23,0])
    for o,s,k in [([-3,11.3,-1.9],[6,3.8,3.8],3),([-2.2,15,-1.65],[4.4,3.4,3.3],0),([-2.85,18,-1.8],[5.7,3.7,3.6],0),([-1,21.1,-.95],[2,1.7,1.9],0)]:X('body',o,s,k)
    for side in (-1,1):
        X('body',[side*1.35-1.5,18.1,-2.5],[3,3.1,1.4],3,[0,0,-side*10])
        X('body',[side*.85-.55,16.7,-2],[1.1,3.5,.8],6,[0,0,-side*20])
    X('body',[-2.55,14.5,-2],[5.1,.8,4.1],10)
    # Full adult face, leaf-green scalp, pointed ears and layered long hair.
    X('head',[-3.7,22.1,-3.15],[7.4,7.2,6.15],0)
    X('head',[-3.1,21.7,-2.9],[6.2,.8,5.6],0)
    X('head',[-.32,24.1,-3.5],[.64,.7,.55],0)
    X('head',[-.7,23,-3.35],[1.4,.15,.16],8)
    for side,n in [(-1,'right'),(1,'left')]:
        x=side*1.8
        X('head',[x-.87,24.7,-3.31],[1.74,1.05,.18],15)
        X('head',[x-.4,24.7,-3.51],[.8,1.02,.14],4)
        X('head',[x-.15,24.74,-3.66],[.3,.95,.1],5)
        X('head',[x-.95,25.67,-3.49],[1.9,.25,.22],5)
        X('head',[x-.27,25.34,-3.78],[.21,.23,.08],15)
        for j in range(3):
            w=1.45-j*.3
            X('head',[side*(3.9+j*.8)-w/2,24.7+j*.34,-.75],[w,1.5-j*.32,1.3-j*.25],0)
        X('head',[side*6-.2,25.65,-.65],[.4,.4,.65],0)
        hair='hair_'+n;joint(hair,[side*3,29,1])
        X(hair,[side*3.4-.9,20.4,-1.6],[1.8,8.8,3.1],9)
        for j in range(4):
            x=side*(.55+j*.9);bottom=13.8+j*.45
            X(hair,[x-.65,bottom+.5,2.4],[1.3,15-j*.45,1.9],9 if j%2 else 3)
            X(hair,[x-.6,bottom+.3,3.8],[1.2,8-j*.5,.7],2 if j%2 else 9)
            X(hair,[x-.45,bottom-.4,2.6],[.9,1.7,1.7],9 if j%2 else 3)
        for j in range(3):X('head',[side*(.7+j*1.15)-.9,26.5+j*.4,-3.5],[1.8,2.5-j*.15,.8],9,[0,0,-side*(9+j*4)])
        arm='arm_'+n;fore='fore_'+n;joint(arm,[side*3.65,21,0]);joint(fore,[side*3.65,15.3,0])
        m.by_name[arm]['rotation']=[0,0,-side*6]
        X(arm,[side*3.65-1,15.1,-1.1],[2,6.1,2.2],0)
        X(arm,[side*3.65-1.35,20,-1.4],[2.7,2,2.8],3)
        X(arm,[side*3.65-1.45,19.6,-1.5],[2.9,.8,3],6)
        X(arm,[side*3.65-1.3,19.3,-1.4],[2.6,.55,2.8],13)
        X(fore,[side*3.65-.9,10.9,-1.05],[1.8,4.6,2.1],0)
        X(fore,[side*3.65-1,9.6,-1.1],[2,1.7,2.2],0)
        for j in range(3):
            finger='finger_'+str(side)+'_'+str(j);x=side*3.65+(j-1)*.57;joint(finger,[x,9.9,-.6])
            X(finger,[x-.24,8.9,-.75],[.48,1.25,1.3],0)
        joint('leg_'+n,[side*1.65,12,0])
        X('leg_'+n,[side*1.65-1.35,7.6,-1.3],[2.7,4.8,2.6],0)
        X('leg_'+n,[side*1.65-1.45,1,-1.4],[2.9,7.3,2.8],13)
        X('leg_'+n,[side*1.65-1.55,7.9,-1.5],[3.1,.8,3],14)
        X('leg_'+n,[side*1.65-1.5,.12,-2.3],[3,1.5,4],13)
        X('leg_'+n,[side*1.65-1.5,.12,-2.4],[3,.45,4.1],14)
        X('leg_'+n,[side*1.65-1.48,2,-1.43],[2.96,.45,2.86],14)
        X('leg_'+n,[side*1.65-.12,2.4,-1.48],[.24,5,.16],14)
        for j in range(4):
            vine='vine_'+str(side)+'_'+str(j);z=-1.45+j*1.05;joint(vine,[side*2.65,14.5,z])
            X(vine,[side*2.75-1.15,8.4+j%2*.7,z-.65],[2.3,6.4,.95],3 if j%2 else 6,[0,0,-side*(7+j*3)])
            X(vine,[side*2.75-.8,7.8+j%2*.7,z-.55],[1.6,1.6,.75],7)
        front='vine_front_'+str(side);joint(front,[side*1.4,14,-2])
        for j in range(3):
            X(front,[side*(.6+j*.85)-.9,8.3+abs(j-1)*.65,-2.45-j*.07],[1.8,6.2-abs(j-1)*.4,1.05],3 if j%2 else 6,[0,0,-side*(4+j*5)])
        crown='crown_'+n;joint(crown,[side*2.6,29.5,0])
        X(crown,[side*2.6-1,29.5,-.3],[2,1,2.7],6,[0,0,side*12])
        if side==1:
            X(crown,[1.5,30,-.2],[1,1.6,1],11,[0,0,-20])
            X(crown,[2.2,30.9,-.35],[2.4,.8,1.3],12,[0,0,-25])
            X(crown,[3.8,31.3,-.25],[1.3,.55,1],6,[0,0,-25])
    X('head',[-3.9,28.4,-3.2],[7.8,1.8,6.6],9)
    X('head',[-3.8,25.4,2.2],[7.6,3.8,1.5],9)
    palette=['eedbc7','263d24','7e9b3a','4d7c2c','68813a','292c21','729c3b','365823','cbb8a4','4b752d','507529','89a347','c5c14a','eee9db','c4cabc','fff2df']
    roles=['skin','leaf','hair','leaf','eyes','cloth','leaf','leaf','skin','hair','leaf','leaf','cloth','cloth','cloth','skin']
    return m,palette,roles,(.65,1.9)

def slime():
    m=old_model('slime_maiden',True);X=m.box
    m.bones=[b for b in m.bones if not b['name'].startswith('bubble_')];m.by_name={b['name']:b for b in m.bones}
    def joint(n,p):m.by_name[n]['pivot']=p
    joint('body',[0,10.5,0]);joint('head',[0,19.4,0])
    for name,p,o,s,k in [
        ('gel_0',[0,9.6,0],[-3.1,8.4,-1.9],[6.2,3.5,3.8],0),
        ('gel_1',[0,12.2,0],[-2.3,10.8,-1.6],[4.6,3.8,3.2],8),
        ('gel_2',[0,15.3,0],[-3,13.7,-1.8],[6,4.1,3.6],0),
        ('gel_3',[0,18,0],[-1,17.4,-.9],[2,1.6,1.8],8)]:
        joint(name,p);X(name,o,s,k)
    joint('gel_4',[0,15.5,0])
    for side in (-1,1):
        X('gel_4',[side*1.4-1.5,14.3,-2.6],[3,2.9,1.8],8,[0,0,-side*6])
        X('gel_0',[side*2.5-.75,8.1,-1.7],[1.5,2.7,3.4],12)
    X('head',[-3.45,18.4,-2.9],[6.9,6.2,5.8],8)
    X('head',[-2.9,18.1,-2.6],[5.8,.9,5.2],8)
    X('head',[-.3,20,-3.15],[.6,.55,.4],8)
    X('head',[-.45,19.25,-3.1],[.9,.14,.14],5)
    for side in (-1,1):
        x=side*1.65
        X('head',[x-.62,20.5,-3.07],[1.24,.68,.17],4)
        X('head',[x-.3,20.96,-3.28],[.24,.22,.1],15)
        X('head',[side*2.25-.3,19.9,-3.12],[.6,.4,.12],7)
    X('head',[-3.6,23.6,-3],[7.2,1.7,6.1],9)
    X('head',[-3.5,21.1,2.1],[7,3.4,1.4],9)
    # Two hollow-topped gel loops with heavy, tapering side lobes.
    for side,name in [(-1,'hair_0'),(1,'hair_5')]:
        joint(name,[side*3.1,23.4,0])
        m.by_name[name]['rotation']=[0,0,side*12]
        X(name,[side*3.65-1.1,22.9,-.6],[2.2,2,2.7],9)
        X(name,[side*4.8-2,25.9,-.4],[4,2,3.4],9)
        X(name,[side*6.1-1.45,23.1,-.3],[2.9,3.8,3.6],9)
        X(name,[side*5.8-1.65,20.2,-.3],[3.3,3.6,3.4],0)
        X(name,[side*5.35-1.15,18.3,.1],[2.3,2.5,2.8],9)
        X(name,[side*5.1-.65,17.2,.5],[1.3,1.7,1.9],12)
        X(name,[side*5.8-1.05,23.6,-.48],[2.1,.5,.15],2)
    for i,name in enumerate(['hair_1','hair_2','hair_3','hair_4']):
        x=-2.7+i*1.8;joint(name,[x,24,-1.8])
        X(name,[x-.95,22.2+(i%2)*.5,-3.18],[1.9,2.8-(i%2)*.5,1],9)
        X(name,[x-.65,21.9+(i%2)*.5,-3.1],[1.3,.9,.8],0)
    for i in range(7):
        name='v2_hair_'+str(i);x=(i-3)*.95;joint(name,[x,24.2,2.1])
        X(name,[x-.58,17.5+abs(i-3)*.3,2.1],[1.16,7-abs(i-3)*.3,1.5],9)
        X(name,[x-.36,17.1+abs(i-3)*.3,2.25],[.72,1.3,1.1],0)
    for side in (-1,1):
        name='v2_hair_temple_'+str(side);joint(name,[side*3.2,23.5,-.8])
        X(name,[side*3.2-.65,19,-1.4],[1.3,5.3,2.2],9)
    for side,n in [(-1,'right'),(1,'left')]:
        arm='arm_'+n;hand='hand_'+n;joint(arm,[side*3.35,16.3,0]);joint(hand,[side*3.65,11.9,0])
        m.by_name[arm]['rotation']=[0,0,-side*8]
        X(arm,[side*3.35-1.1,11.9,-1],[2.2,4.9,2.1],0)
        X(arm,[side*3.35-1.3,15,-1.2],[2.6,1.8,2.5],12)
        X(hand,[side*3.65-.95,8.2,-.95],[1.9,4.1,2],0)
        X(hand,[side*3.65-1.05,7.4,-1.1],[2.1,1.4,2.3],8)
        for j in range(3):X(hand,[side*3.65-.9+j*.6,6.8,-1],[.55,1.1,1.8],0)
        leg='leg_'+n;lower=leg+'_lower';foot=leg+'_foot'
        m.bone(leg,'root',[side*1.6,9.8,0]);X(leg,[side*1.6-1.4,5.9,-1.2],[2.8,4.3,2.6],0)
        m.bone(lower,leg,[side*1.6,6.1,0]);X(lower,[side*1.6-1.25,.8,-1.25],[2.5,5.6,2.7],0)
        m.bone(foot,lower,[side*1.6,1,-.2]);X(foot,[side*1.6-1.4,.12,-2.3],[2.8,1.35,3.8],0)
        X(foot,[side*1.6-1.1,.12,-2.65],[2.2,.8,1.1],8)
    palette=['79c953','44983d','a5e17b','95d368','273b25','1e3b24','d0f7ac','c7a489','84cf60','68b952','4b9c43','bbf191','91d96b','75c452','5aaa43','aef397']
    roles=['slime']*16;roles[4]='eyes';roles[7]='skin'
    return m,palette,roles,(.85,1.65)

def slime_motion(model,animations):
    for clip in animations.values():
        for name in list(clip['bones']):
            if name.startswith('bubble_'):del clip['bones'][name]
    for state,amplitude in [('walk',18),('run',28)]:
        clip=animations[state];length=clip['animation_length'];bones=clip['bones']
        for side,n in [(-1,'right'),(1,'left')]:
            upper={};lower={};feet={}
            for i in range(9):
                t=length*i/8;phase=math.tau*i/8+(math.pi if side<0 else 0)
                angle=math.sin(phase)*amplitude;knee=max(0,math.cos(phase))*16
                key=str(round(t,6));upper[key]=[angle,0,0];lower[key]=[knee,0,0];feet[key]=[-angle-knee,0,0]
            bones['leg_'+n]={'rotation':upper};bones['leg_'+n+'_lower']={'rotation':lower};bones['leg_'+n+'_foot']={'rotation':feet}
    from visual_v3_geometry import support_death
    support_death(model,animations)
    return animations

def minotaur():
    m=old_model('minotaur',True);X=m.box
    def joint(n,p):m.by_name[n]['pivot']=p
    joint('body',[0,16.5,0]);joint('chest',[0,26,0]);joint('head',[0,33,-1]);joint('jaw',[0,33,-4])
    # Bull barrel and shoulder hump: broad pectorals, pinched flank and fur seams.
    X('body',[-4.8,15,-3],[9.6,5.5,6],0)
    X('body',[-4.2,20,-2.7],[8.4,7.4,5.6],0)
    X('chest',[-6.6,25,-3.1],[13.2,7.7,7],0)
    X('chest',[-5.4,29,1.4],[10.8,7,4.3],1,[8,0,0])
    for side,n in [(-1,'right'),(1,'left')]:
        for j in range(3):
            X('chest',[side*(2.8+j*.6)-2,27+j*1.6,-3.7],[4,2.4,1.3],8,[0,0,-side*8])
            X('body',[side*2.4-1.5,20+j*1.7,-3],[3,1.5,.8],8)
        X('chest',[side*6.8-2.4,28.2,-2.6],[4.8,5,5.3],0,[0,0,-side*10])
        for j in range(3):X('chest',[side*(6+j*.5)-.8,26.5+j*.9,1.3],[1.6,3,2],1,[0,0,-side*19])
    # Squared bovine skull, projecting dark muzzle and heavy brow.
    X('head',[-4.1,33,-4.7],[8.2,7.6,7.3],0)
    X('head',[-3.4,38.6,-4.6],[6.8,3.1,6.4],8)
    X('head',[-3.8,32.6,-7],[7.6,3.9,4.3],8)
    X('head',[-3.25,33,-7.5],[6.5,2.7,1],5)
    X('jaw',[-3.3,31.7,-6.7],[6.6,1.7,4.4],1)
    X('jaw',[-2.4,31.9,-7],[4.8,.25,.35],5)
    for side,n in [(-1,'right'),(1,'left')]:
        x=side*2.4
        X('head',[x-.7,36.4,-4.95],[1.4,1.25,.35],11)
        X('head',[x-.25,36.5,-5.33],[.5,.85,.16],5)
        X('head',[x-1,37.55,-5.15],[2.2,1,1.1],1,[0,0,side*12])
        X('head',[side*1.9-.5,34,-7.65],[1,.8,.2],1)
        X('head',[side*4.5-1.25,36.6,-.7],[2.5,1.6,2.5],0,[0,0,-side*22])
        X('head',[side*4.7-.7,36.9,-.85],[1.4,.7,1.6],8,[0,0,-side*22])
        joint('horn_'+n,[side*3.7,39.8,-1.1])
        # Successive blocks bend laterally then upward and inward; ivory tips.
        for x,y,w,h,angle,mat in [(4,39.5,2.6,2.3,-side*28,4),(5.7,40.6,2.1,2.5,side*5,4),(6.3,42.4,1.45,2.1,side*24,11),(5.9,44,1,.95,side*35,11)]:
            X('horn_'+n,[side*x-w/2,y,-2],[w,h,2 if mat==4 else 1.4],mat,[0,0,angle])
        leg='leg_'+n;foot='foot_'+n;x=side*3.5
        joint(leg,[x,16.4,0]);joint(foot,[x,2,0])
        X(leg,[x-2.25,9.5,-2],[4.5,7.5,4.8],0,[-9,0,0])
        X(leg,[x-1.8,2,-.8],[3.6,8.5,3.7],8,[12,0,0])
        X(leg,[x-2.1,8.5,-2.25],[4.2,2.5,2.4],1)
        for j in range(2):X(foot,[x-2+j*2.15,.15,-3.1],[1.85,2.3,5.6],14)
        X(foot,[x-2.1,2,-1.5],[4.2,1.2,3.7],2)
        arm='arm_'+n;fore='forearm_'+n;hand='hand_'+n;x=side*8
        joint(arm,[x,31.3,0]);joint(fore,[x,24,0]);joint(hand,[x,18,-.2])
        X(arm,[x-2.2,23.6,-2.1],[4.4,8,4.5],0)
        X(arm,[x-2.6,27.5,-2.4],[5.2,4.6,4.9],8)
        X(fore,[x-2.15,17.4,-2],[4.3,7,4.3],0)
        X(fore,[x-2.5,17.7,-2.3],[5,2.5,4.9],2)
        X(fore,[x-2.65,17.5,-2.45],[5.3,.55,5.2],9)
        X(hand,[x-1.75,15.6,-1.9],[3.5,2.2,3.8],1)
        if side==1:
            for j in range(3):X(hand,[x-1.5+j*1.1,14.8,-2],[.95,1.6,1.6],8)
    joint('loincloth',[0,17,0]);X('loincloth',[-4.8,15.6,-3.25],[9.6,1.7,6.5],10)
    for side in (-1,1):
        X('loincloth',[side*1.85-1.9,10.7,-3.45],[3.8,5.2,.85],3,[0,0,-side*5])
        X('loincloth',[side*2-1.8,10.9,2.8],[3.6,5,.85],3,[0,0,side*5])
        X('loincloth',[side*4.2-.7,12,-2.6],[1.4,4.3,5.4],10)
    joint('tail',[0,17,2.5]);joint('tail_tip',[0,8,4]);X('tail',[-.6,7,3],[1.2,10,1.3],0,[12,0,0]);X('tail_tip',[-1.1,5.5,3.6],[2.2,3,2.4],1)
    # Closed three-finger grip around one continuous wooden hammer shaft.
    joint('grip_right',[-8,16.7,-2]);joint('axe',[-8,16.7,-2])
    for j in range(3):
        X('grip_right',[-9.6,15.55+j*.7,-2.85],[2.2,.55,.8],8)
        X('grip_right',[-7.6,15.55+j*.7,-2.7],[.65,.55,1.6],1)
    X('grip_right',[-9.9,16.8,-1.8],[.8,1.1,1.6],8,[0,0,-15])
    X('axe',[-8.65,12.5,-2.3],[1.3,16,1.3],6)
    for y in (13,14,15,18,19,20):X('axe',[-8.8,y,-2.45],[1.6,.45,1.6],1)
    X('axe',[-12.7,26,-5],[9.4,5.8,6.5],2)
    X('axe',[-12.2,25.5,-4.5],[8.4,.8,5.5],14)
    X('axe',[-12.2,31.4,-4.5],[8.4,.8,5.5],9)
    for x in (-13.1,-3.7):
        X('axe',[x,26.5,-4.65],[.8,4.8,5.8],14)
        X('axe',[x-.12,28,-2.6],[1,1.5,1.5],9)
    X('axe',[-8.9,31.9,-2.5],[1.8,.6,1.8],14)
    palette=['704232','432d28','8c9293','9b3056','e5e1cb','282423','725039','b29463','85503c','b2b7b1','70203d','f8f4df','63392f','a97850','53585b','9d6750']
    roles=['fur','fur','metal','cloth','horn','skin','wood','leather','fur','metal','cloth','ivory','fur','fur','metal','fur']
    # Corrective pass: shorten the long abdomen without reducing the feet/hips.
    def ymap(y):return y if y<17 else 17+(y-17)*.7 if y<26 else y-2.7
    for bone in m.bones:
        bone['pivot'][1]=ymap(bone['pivot'][1])
        for cube in bone.get('cubes',[]):
            low=cube['origin'][1];cube['origin'][1]=ymap(low);cube['size'][1]=ymap(low+cube['size'][1])-ymap(low)
            if 'pivot' in cube:cube['pivot'][1]=ymap(cube['pivot'][1])
    # Broader bovine head and shoulders, with a short overlapping forelock.
    for bone in m.bones:
        if bone['name'] in ('head','jaw','horn_left','horn_right'):
            bone['pivot'][0]*=1.14
            for cube in bone.get('cubes',[]):
                cube['origin'][0]*=1.14;cube['size'][0]*=1.14
                if 'pivot' in cube:cube['pivot'][0]*=1.14
    for j in range(5):
        X('head',[-4+j*1.6,36.7+(j%2)*.6,-4.9],[1.8,2.5-(j%2)*.4,1.25],8,[0,0,(j-2)*7])
    for side in (-1,1):
        X('chest',[side*5.1-2,25.4,-3.7],[4,4.3,1.4],0,[0,0,-side*8])
    for cube in m.by_name['axe']['cubes']:
        if cube['origin'][1]>22:cube['origin'][1]-=2.6
    # The shaft remains continuous into the lowered head, with excess upper wood hidden.
    return m,palette,roles,(1.35,2.85)

BUILDERS={'harpy':harpy,'forest_dryad':dryad,'slime_maiden':slime,'minotaur':minotaur}

BASE_ATLAS=pipeline.material_atlas

def reference_atlas(palette,roles,translucent=False,species=None):
    image=BASE_ATLAS(palette,roles,translucent);draw=ImageDraw.Draw(image)
    for k,role in enumerate(roles):
        if role not in ('feather','leaf'):continue
        x=k%4*32;y=k//4*32;rgb=tuple(int(palette[k][i:i+2],16) for i in (0,2,4))
        def ink(d):return tuple(max(0,min(255,c+d)) for c in rgb)+(255,)
        draw.rectangle((x,y,x+31,y+31),fill=ink(0))
        for box,d in [((0,0,31,5),10),((0,6,8,18),5),((9,6,23,13),-7),((16,14,31,24),6),((3,19,14,28),-10),((15,25,31,31),-15)]:
            draw.rectangle(tuple(v+(x if i%2==0 else y) for i,v in enumerate(box)),fill=ink(d))
    if species=='slime_maiden':
        for k,role in enumerate(roles):
            if role!='slime':continue
            x=k%4*32;y=k//4*32;rgb=tuple(int(palette[k][i:i+2],16) for i in (0,2,4))
            def gel(delta):return tuple(max(0,min(255,c+delta)) for c in rgb)+(228,)
            draw.rectangle((x,y,x+31,y+31),fill=gel(0))
            for box,delta in [((0,0,31,2),12),((4,4,10,8),21),((11,5,15,10),13),((3,15,9,23),-9),((14,18,25,25),7),((22,27,31,31),-13)]:
                draw.rectangle(tuple(v+(x if i%2==0 else y) for i,v in enumerate(box)),fill=gel(delta))
    if species=='minotaur':
        for k,role in enumerate(roles):
            if role!='fur':continue
            x=k%4*32;y=k//4*32;rgb=tuple(int(palette[k][i:i+2],16) for i in (0,2,4))
            def fur(delta):return tuple(max(0,min(255,c+delta)) for c in rgb)+(255,)
            draw.rectangle((x,y,x+31,y+31),fill=fur(0))
            for box,delta in [((0,0,31,4),8),((3,6,12,12),-9),((14,4,23,10),7),((7,15,18,23),10),((20,14,28,25),-12),((0,27,31,31),-15)]:
                draw.rectangle(tuple(v+(x if i%2==0 else y) for i,v in enumerate(box)),fill=fur(delta))
    if species=='forest_dryad':
        for tile in (9,13):
            x=tile%4*32;y=tile//4*32;rgb=tuple(int(palette[tile][i:i+2],16) for i in (0,2,4))
            for box,delta in [((3,4,8,9),-16),((10,6,17,13),8),((4,15,11,21),-9),((15,18,24,25),-13),((5,25,13,28),10)]:
                color=tuple(max(0,min(255,c+delta)) for c in rgb)+(255,)
                draw.rectangle(tuple(v+(x if i%2==0 else y) for i,v in enumerate(box)),fill=color)
    return image

def main():
    parser=argparse.ArgumentParser();parser.add_argument('species',choices=BUILDERS);args=parser.parse_args()
    model,palette,roles,size=BUILDERS[args.species]()
    pipeline.material_atlas=lambda p,r,t=False:reference_atlas(p,r,t,args.species)
    animations=baseline(ASSET/'geckolib/animations/entity'/f'{args.species}.animation.json')['animations']
    if args.species=='slime_maiden':animations=slime_motion(model,animations)
    if args.species=='forest_dryad':
        from visual_v3_geometry import support_death
        support_death(model,animations)
    write_creature(model,palette,roles,animations,*size,glow=() if args.species=='minotaur' else (11,) if args.species=='slime_maiden' else (4,),translucent=args.species=='slime_maiden')

if __name__=='__main__':main()
