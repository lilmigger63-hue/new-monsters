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

def vampire():
    m=old_model('vampire',True);X=m.box
    def joint(n,p):m.by_name[n]['pivot']=p
    for n,p in [('pelvis',[0,11,0]),('body',[0,14,0]),('chest',[0,19,0]),('neck',[0,22,0]),('head',[0,23.1,-.1])]:joint(n,p)
    X('pelvis',[-2.9,10,-1.8],[5.8,3.6,3.6],2)
    X('body',[-2.3,13,-1.65],[4.6,5.1,3.3],3)
    X('chest',[-3.2,17.5,-1.95],[6.4,4.5,4],2)
    X('neck',[-1,21.5,-.9],[2,2,1.8],1)
    # Crimson waistcoat and narrow gold fastening strips under charcoal lapels.
    X('body',[-2.5,13,-1.9],[5,4.6,.6],10)
    X('chest',[-2.4,17,-2.2],[4.8,4.8,.8],3)
    for y in (14,15.8,17.6):
        X('body',[-2.45,y,-2.25],[4.9,.55,.5],4)
        X('body',[-.35,y-.1,-2.8],[.7,.8,.25],9)
    for side in (-1,1):
        X('chest',[side*1.75-.65,18,-2.7],[1.3,4,.8],15,[0,0,side*22])
        X('neck',[side*2.2-.8,21.5,.3],[1.6,3.4,1.2],15,[0,0,side*29])
        X('neck',[side*2-.55,22,.05],[1.1,2.4,.4],10,[0,0,side*29])
        for j in range(3):X('chest',[side*(.55+j*.55)-.38,20.5-j*.13,-2.7],[.76,1.5,.65],11,[0,0,side*(8+j*12)])
    X('chest',[-.6,20.2,-3.15],[1.2,1.1,.5],7,[0,0,45])
    # Adult broad pale face framed by solid blonde scalp and layered short fringe.
    X('head',[-3.5,23,-3],[7,6.1,5.7],0)
    X('head',[-2.8,22.7,-2.8],[5.6,.9,5.2],1)
    X('head',[-.35,25,-3.3],[.7,.7,.6],1)
    X('head',[-.6,23.8,-3.2],[1.2,.16,.2],12)
    for side in (-1,1):
        x=side*1.8
        X('head',[x-.8,25.3,-3.15],[1.6,1.35,.18],11)
        X('head',[x-.5,25.35,-3.34],[1,1.25,.16],13)
        X('head',[x-.17,25.4,-3.53],[.34,1.13,.12],15)
        X('head',[x-.4,26.12,-3.66],[.24,.25,.08],11)
        X('head',[x-.95,26.7,-3.3],[1.9,.23,.3],5)
        X('head',[side*3.45-.45,24.5,-.5],[.9,1.5,1.4],1)
    X('head',[-3.75,28,-3.1],[7.5,1.6,6.2],5)
    for j in range(5):
        X('head',[-3.6+j*1.4,26.2+(j%2)*.7,-3.2],[1.6,2.4-(j%2)*.7,.8],8 if j%2 else 5,[0,0,(j-2)*7])
    for side,n in [(-1,'right'),(1,'left')]:
        joint('hair_'+n,[side*3.3,28.6,0]);joint('hair_tip_'+n,[side*3.3,22,0])
        X('hair_'+n,[side*3.3-.7,21.7,-1.6],[1.4,7.1,3.6],5)
        X('hair_tip_'+n,[side*3.3-.6,19.5,-1.4],[1.2,3,3.2],8)
    joint('hair_back',[0,28.6,2.3])
    for j in range(5):X('hair_back',[-3.5+j*1.35,19.5+abs(2-j)*.7,2],[1.5,9.4-abs(2-j)*.7,1.5],5 if j%2 else 8)
    # Small asymmetric red bow, clearly separate from forehead/eyes.
    for side in (-1,1):X('head',[2.4+side*.7-.7,28.7,-1.2],[1.4,.8,1.8],7,[0,0,-side*17])
    X('head',[2,28.6,-1.3],[.8,1,1.9],10)
    for side,n in [(-1,'right'),(1,'left')]:
        x=side*1.55
        joint('thigh_'+n,[x,11,0]);joint('shin_'+n,[x,5.7,0]);joint('foot_'+n,[x,1.5,0])
        X('thigh_'+n,[x-1.3,5.5,-1.25],[2.6,5.8,2.7],2)
        X('shin_'+n,[x-1.2,1,-1.25],[2.4,4.9,2.7],15)
        X('foot_'+n,[x-1.4,.1,-2.3],[2.8,1.5,3.9],15)
        x=side*4.1;arm='arm_'+n;fore='forearm_'+n;hand='hand_'+n
        joint(arm,[x,21.2,0]);joint(fore,[x,16.8,0]);joint(hand,[x,12.6,-.6])
        X(arm,[x-1.3,16.5,-1.35],[2.6,5,2.8],2)
        X(arm,[x-1.65,19.5,-1.65],[3.3,2.4,3.4],15)
        X(fore,[x-1.3,12,-1.35],[2.6,4.9,2.8],3)
        X(fore,[x-1.6,13,-1.6],[3.2,1.4,3.4],10)
        X(hand,[x-1.4,10.7,-1.8],[2.8,2.1,3.2],10)
        if side>0:
            for j in range(3):X(hand,[x-1.2+j*.8,10,-1.9],[.7,1.2,1.7],3)
        coat='coat_'+n;joint(coat,[side*1.8,11.4,.5])
        for j,(yy,ww,dd) in enumerate([(7.2,3.8,4.6),(4,4.3,5.1),(1.8,4.8,5.6)]):
            X(coat,[side*2-ww/2,yy,-dd/2],[ww,3.5,dd],15)
            X(coat,[side*2-ww/2,yy,-dd/2-.12],[ww,1.1,.35],10)
            X(coat,[side*2-ww/2,yy,dd/2-.2],[ww,1.2,.45],3)
        X(coat,[side*3.5-.4,3.4,-2.95],[.8,6.5,.45],7)
    joint('cape',[0,21.7,2.1])
    for j in range(5):
        w=6.3+j*.6;y=17.3-j*3.2
        X('cape',[-w/2,y,2.4+j*.22],[w,3.7,.85],15,[5,0,0])
        X('cape',[-w/2,y,3.15+j*.22],[w,.65,.35],10,[5,0,0])
    joint('grip_right',[-4.1,11.8,-1.8]);joint('dagger',[-4.1,11.8,-1.8])
    for j in range(3):X('grip_right',[-5.35,10.9+j*.6,-2.55],[1.8,.5,.65],3)
    X('grip_right',[-3.7,11,-2.5],[.6,1.6,1.5],10)
    X('dagger',[-4.5,9.5,-2.2],[.8,4,.8],6)
    X('dagger',[-5.45,13,-2.5],[2.7,.55,1.4],4)
    X('dagger',[-4.65,13.5,-2],[1.1,4.6,.45],9)
    X('dagger',[-4.4,18,-1.95],[.6,.9,.35],9,[0,0,16])
    palette=['e5cfb5','f1dac1','292a2c','6f2132','a78c49','b49b56','26252b','ce3549','c7ad68','929a9c','9d2941','f1ede2','b78f80','df5260','60533e','191b20']
    roles=['skin','skin','cloth','cloth','gold','hair','leather','cloth','hair','metal','cloth','skin','skin','cloth','hair','cloth']
    # Corrective pass: swept blonde locks, a readable bow and flared black mantle.
    for side,n in [(-1,'right'),(1,'left')]:
        X('hair_'+n,[side*3.35-.8,23.5,-1.8],[1.6,5.3,3.9],8,[0,0,-side*5])
        X('hair_tip_'+n,[side*3.5-.5,19.8,.3],[1,3.4,2.4],5,[0,0,side*9])
        for j in range(3):
            X('cape',[side*(3+j*.3)-.8,15.2-j*3.6,2.8+j*.4],[1.6,4.2,1.1],15,[0,0,-side*(8+j*4)])
            X('cape',[side*(3.3+j*.35)-.5,13.7-j*3.6,3+j*.4],[1,2.2,1.1],10,[0,0,-side*16])
        X('arm_'+n,[side*4.1-1.8,20.9,-1.7],[3.6,1.1,3.6],15,[0,0,-side*13])
        X('head',[2.4+side*.95-.85,28.75,-1.3],[1.7,.85,2.1],7,[0,0,-side*18])
    X('head',[-2.4,26.6,-3.45],[2.7,1.3,.8],8,[0,0,-13])
    X('head',[.25,27.1,-3.4],[2.2,1.1,.7],5,[0,0,12])
    return m,palette,roles,(.7,1.85)

def valkyrie():
    m=old_model('valkyrie');X=m.box
    # Remove superseded original plates before adding the larger fitted replacements.
    m.by_name['head']['cubes']=[c for c in m.by_name['head']['cubes'] if int(c['uv']['north']['uv'][0]//32+4*(c['uv']['north']['uv'][1]//32)) not in (2,3,6,12)]
    for n in ('right','left'):
        m.by_name['shin_'+n]['cubes']=[];m.by_name['foot_'+n]['cubes']=[]
    # Compact feather span keeps the reference's body-sized resting wings.
    for b in m.bones:
        if b['name'].startswith(('wing_','wingtip_')):
            center=[-2.6 if b['name'].endswith('right') else 2.6,22.3,1.9]
            def wingpoint(v):return [center[i]+(v[i]-center[i])*.67 for i in range(3)]
            b['pivot']=wingpoint(b['pivot'])
            for c in b.get('cubes',[]):
                c['origin']=wingpoint(c['origin']);c['size']=[v*.67 for v in c['size']]
                if 'pivot' in c:c['pivot']=wingpoint(c['pivot'])
    # Keep the detailed species rig, attachments and armor seams; rebuild helmet/head proportions.
    headnames={'head',*(f'hair_back_{j}' for j in range(5)),'hair_side_right','hair_side_left'}
    def point(p,head=False):
        x,y,z=p
        if head:return [x*1.23,25.4+(y-25.4)*1.08,z*1.18]
        return [x,y,z]
    for b in m.bones:
        if b['name'] in headnames:
            b['pivot']=point(b['pivot'],True)
            for c in b.get('cubes',[]):
                c['origin']=point(c['origin'],True);c['size']=[c['size'][0]*1.23,c['size'][1]*1.08,c['size'][2]*1.18]
                if 'pivot' in c:c['pivot']=point(c['pivot'],True)
    # Add broad cheek plates, helmet brow and an unmistakable swept metal wing crest.
    X('head',[-3.8,31.3,-3.4],[7.6,.85,6.8],2)
    X('head',[-3.5,29.3,-3.35],[7,1.05,6.8],2)
    X('head',[-3.3,29.4,-3.65],[6.6,.55,.7],12)
    X('head',[-2.6,30.2,-2.9],[5.2,.9,5.8],14)
    X('head',[-2,31,-2.3],[4,.65,4.7],3)
    for side,n in [(-1,'right'),(1,'left')]:
        X('head',[side*3.2-.65,26.2,-2.8],[1.3,3.5,3.2],2)
        X('head',[side*3.4-.4,25.8,-2.95],[.8,1.3,2.4],12)
        for j in range(3):
            X('head',[side*(3.2+j*.65)-.55,30.1+j*.6,-.8],[1.1,3.4-j*.35,1.6],12,[0,0,-side*(31+j*12)])
            X('head',[side*(3.3+j*.65)-.3,32.7+j*.25,-.7],[.6,1.2,1.3],6,[0,0,-side*(31+j*12)])
        # More substantial segmented greaves, dark joints and bright toe plates.
        x=side*1.35
        X('shin_'+n,[x-1.3,2.1,-1.4],[2.6,5.7,3],2)
        for y in (2.3,4.2,6.1):X('shin_'+n,[x-1.4,y,-1.65],[2.8,.65,.5],12)
        X('foot_'+n,[x-1.4,.2,-2.7],[2.8,1.3,4.1],14)
        X('foot_'+n,[x-1.25,.9,-2.85],[2.5,.55,1.7],12)
        # Reference-style pale upper arm and substantial silver shoulder stack.
        X('arm_'+n,[side*3.7-1.55,21,-1.75],[3.1,1.3,3.7],12,[0,0,-side*12])
        X('arm_'+n,[side*3.9-1.5,20.4,-1.85],[3,1,3.9],14,[0,0,-side*14])
        m.by_name['wing_'+n]['rotation']=[0,0,-side*15]
        m.by_name['wingtip_'+n]['rotation']=[0,0,-side*10]
        for c in m.by_name['wingtip_'+n]['cubes']:
            if 'rotation' in c:c['rotation'][2]=-c['rotation'][2]
    # Short red central tabard, overlapping silver faulds and dark waist joints.
    X('body',[-1.45,11.1,-2.7],[2.9,4.5,.7],7)
    X('body',[-1.05,11,-2.85],[2.1,.6,.45],13)
    for side in (-1,1):X('body',[side*2.1-.8,15,-2.2],[1.6,1.3,.5],14)
    palette=['e0cdb9','282326','929797','b8a158','ce5452','19171c','e3e4da','963744','ead7c1','c1a360','353136','c2c9c7','c4cac7','572b37','656d6e','f3ead8']
    roles=['skin','feather','metal','gold','eyes','feather','metal','cloth','skin','hair','leather','metal','metal','cloth','metal','skin']
    X('head',[-3.55,30.2,-3.65],[7.1,1.25,.7],2)
    # The released blade projected behind the palm. Mirror its Z geometry forward.
    for c in m.by_name['sword']['cubes']:
        c['origin'][2]=-.2-c['origin'][2]-c['size'][2]
        if 'pivot' in c:c['pivot'][2]=-.2-c['pivot'][2]
        if 'rotation' in c:c['rotation'][0]*=-1;c['rotation'][1]*=-1
    return m,palette,roles,(.8,2)

def succubus():
    m=old_model('succubus');X=m.box
    for b in m.bones:
        n=b['name']
        if n=='head' or n.startswith(('hair_','horn_','earring_')):
            def p(v):return [v[0]*1.27,24.13+(v[1]-24.13)*1.08,v[2]*1.2]
            b['pivot']=p(b['pivot'])
            for c in b.get('cubes',[]):
                c['origin']=p(c['origin']);c['size']=[c['size'][0]*1.27,c['size'][1]*1.08,c['size'][2]*1.2]
                if 'pivot' in c:c['pivot']=p(c['pivot'])
                if n.startswith('hair_'):
                    low=c['origin'][1];top=low+c['size'][1];c['origin'][1]=max(low,21.2);c['size'][1]=max(.3,top-c['origin'][1])
        if n.startswith(('wing_','wingtip_')):
            center=[-2.185 if n.endswith('right') else 2.185,20.9,1.425]
            def p(v):return [center[i]+(v[i]-center[i])*.66 for i in range(3)]
            b['pivot']=p(b['pivot'])
            for c in b.get('cubes',[]):
                c['origin']=p(c['origin']);c['size']=[v*.66 for v in c['size']]
                if 'pivot' in c:c['pivot']=p(c['pivot'])
    # Fitted two-piece bodice: pale adult waist separated by dark belts.
    m.by_name['body']['cubes']=[]
    X('body',[-2.7,11.6,-1.8],[5.4,3.2,3.7],2)
    X('body',[-1.95,14.6,-1.6],[3.9,4.2,3.2],8)
    X('body',[-2.4,14.1,-2],[4.8,.8,4],10)
    X('body',[-2.35,17.4,-1.8],[4.7,.8,3.6],2)
    for side,n in [(-1,'right'),(1,'left')]:
        m.by_name['gown_'+n]['cubes']=[];m.by_name['horn_'+n]['cubes']=[]
        for x,y,w,h,ang in [(2.3,29.2,1.8,2.4,-side*28),(3.4,30,1.8,2.3,side*22),(3.6,28.8,1.8,1.9,side*60),(2.9,28.3,1.3,1.5,side*85)]:
            X('horn_'+n,[side*x-w/2,y,-1.5],[w,h,1.8],1,[0,0,ang])
        X('gown_'+n,[side*2.1-.75,10.5,-2.1],[1.5,3.7,4.2],2,[0,0,-side*8])
        x=side*1.4
        X('leg_'+n,[x-1.25,7,-1.25],[2.5,4.7,2.6],2)
        X('leg_'+n,[x-1.4,9.6,-1.45],[2.8,.9,3],10)
        X('shin_'+n,[x-1.2,1.3,-1.25],[2.4,5.7,2.7],2)
        X('foot_'+n,[x-1.4,.1,-2.5],[2.8,1.8,4],2)
        X('foot_'+n,[x-1.45,.1,-2.6],[2.9,.7,4.2],14)
        x=side*3.7
        X('forearm_'+n,[x-1.6,12.4,-1.6],[3.2,5.2,3.4],10)
        X('forearm_'+n,[x-1.8,15.8,-1.8],[3.6,1.5,3.8],2)
        X('hand_'+n,[x-1.35,11.3,-1.6],[2.7,2.1,3.1],10)
        for j in range(3):X('hand_'+n,[x-1.15+j*.8,10.8,-1.65],[.7,1.2,1.7],2)
    X('head',[-2.4,27.5,-3],[2.9,1.5,.8],9,[0,0,-12])
    X('head',[.1,27.7,-3.05],[2.7,1.3,.85],12,[0,0,14])
    palette=['e2cbb4','563728','242528','767a78','bd6260','252322','eee2cb','a44438','ead8bf','b59d57','343539','c95752','ccb36c','393738','969995','f5ecdc']
    roles=['skin','horn','cloth','metal','eyes','skin','skin','membrane','skin','hair','leather','eyes','hair','cloth','metal','skin']
    # Continuous overlapping membrane bays replace the old disconnected rib-like strips.
    for side,n in [(-1,'right'),(1,'left')]:
        wing='wingtip_'+n;m.by_name[wing]['cubes']=[]
        for j,(x,top,h) in enumerate([(4.8,22.1,4.9),(6.6,21.2,5),(8.3,19.9,4.2)]):
            X(wing,[side*x-1.15,top-h,2.05],[2.3,h,.5],7)
            X(wing,[side*x-.7,top-h-.65,2.07],[1.4,1,.46],7)
            X(wing,[side*x-.18,top-h,1.8],[.36,h+.25,.8],1)
        X(wing,[side*8.9-.35,15.2,2],[.7,1.9,.75],1,[0,0,-side*18])
    return m,palette,roles,(.7,1.9)

def ender_dragon_girl():
    m=old_model('ender_dragon_girl');X=m.box
    for b in m.bones:
        if b['name']=='head' or b['name'].startswith(('hair_','horn_')):
            def p(v):return [v[0]*1.26,26.035+(v[1]-26.035)*1.05,v[2]*1.2]
            b['pivot']=p(b['pivot'])
            for c in b.get('cubes',[]):
                c['origin']=p(c['origin']);c['size']=[c['size'][0]*1.26,c['size'][1]*1.05,c['size'][2]*1.2]
                if 'pivot' in c:c['pivot']=p(c['pivot'])
        if b['name'].startswith(('wing_','wingtip_')):
            center=[-2.3575 if b['name'].endswith('right') else 2.3575,22.55,1.5375]
            def p(v):return [center[i]+(v[i]-center[i])*.73 for i in range(3)]
            b['pivot']=p(b['pivot'])
            for c in b.get('cubes',[]):
                c['origin']=p(c['origin']);c['size']=[v*.73 for v in c['size']]
                if 'pivot' in c:c['pivot']=p(c['pivot'])
    m.by_name['body']['cubes']=[]
    X('body',[-2.8,12.2,-1.9],[5.6,3.4,3.8],2)
    X('body',[-2,15.6,-1.6],[4,4.5,3.2],8)
    X('body',[-2.7,15,-2],[5.4,.9,4],10)
    X('body',[-2.3,18.9,-1.8],[4.6,.8,3.6],2)
    # Pale chest opening is framed by the existing dark dragon bodice.
    X('chest',[-1.85,21,-3.05],[3.7,2.8,.6],8)
    for side,n in [(-1,'right'),(1,'left')]:
        m.by_name['horn_'+n]['cubes']=[]
        for j,(y,z,w,h) in enumerate([(31,.1,1.9,2.8),(33.1,1.2,1.6,2.5),(34.8,2.3,1.1,1.4)]):
            X('horn_'+n,[side*(2.4+j*.1)-w/2,y,z],[w,h,1.9-j*.25],6,[-22,0,-side*5])
        # Scale-covered arm/hand volumes and black connected finger claws.
        x=side*3.85
        X('forearm_'+n,[x-1.15,14.1,-1.25],[2.3,4.6,2.6],1)
        m.by_name['hand_'+n]['cubes']=[]
        X('hand_'+n,[x-1.1,12.9,-1.3],[2.2,2.1,2.6],10)
        for j in range(3):
            X('hand_'+n,[x-.9+j*.65,12.1,-1.4],[.55,1.3,1.5],1)
            X('hand_'+n,[x-.85+j*.65,11.7,-1.7],[.4,.9,.65],5,[-20,0,0])
        x=side*1.4
        X('shin_'+n,[x-1.2,1.5,-1.15],[2.4,5.8,2.6],2)
        X('foot_'+n,[x-1.45,.15,-2.6],[2.9,1.8,4.1],10)
        for j in range(3):X('foot_'+n,[x-1.1+j*.8,.15,-3.25],[.65,.8,1.5],5)
        # Dark ribs enclose broad overlapping black membrane surfaces.
        wing='wingtip_'+n;m.by_name[wing]['cubes']=[]
        for j,(x,top,h) in enumerate([(5,23.6,5.3),(7,22.8,6),(9,21.2,5.2)]):
            X(wing,[side*x-1.25,top-h,2.2],[2.5,h,.5],7)
            X(wing,[side*x-.8,top-h-.8,2.21],[1.6,1.2,.45],7)
            X(wing,[side*x-.22,top-h,1.9],[.44,h+.3,.9],1)
        X('chest',[side*2.1-.4,21.8,-3.1],[.8,2.1,.65],2,[0,0,-side*20])
    palette=['dec9b8','27262b','1c1e23','36383c','ac70d2','111217','929795','222329','e8d8c6','191b21','24262c','9c5bbc','34363c','272930','5a5e63','f3e8df']
    roles=['skin','scale','cloth','metal','eyes','scale','horn','membrane','skin','hair','leather','eyes','scale','cloth','metal','skin']
    m.by_name['chest']['cubes']=[c for c in m.by_name['chest']['cubes'] if int(c['uv']['north']['uv'][0]//32+4*(c['uv']['north']['uv'][1]//32))!=11]
    for b in m.bones:
        if b['name'].startswith('hair_'):
            for c in b.get('cubes',[]):
                low=c['origin'][1];top=low+c['size'][1];c['origin'][1]=max(low,21.7);c['size'][1]=max(.35,top-c['origin'][1])
    for side in (-1,1):
        X('chest',[side*1.1-.35,21.2,-3.75],[.7,2.3,.4],2,[0,0,-side*24])
        X('head',[side*2.8-.55,26.6,-2.5],[1.1,3.5,.85],9,[0,0,-side*8])
    return m,palette,roles,(.8,2.05)

def centaur():
    m=old_model('centaur');X=m.box
    m.by_name['horse_body']['cubes']=[]
    for b in m.bones:
        if b['name']=='head' or b['name'].startswith('hair_'):
            def p(v):return [v[0]*1.28,27+(v[1]-27)*1.08,v[2]*1.18]
            b['pivot']=p(b['pivot'])
            for c in b.get('cubes',[]):
                c['origin']=p(c['origin']);c['size']=[c['size'][0]*1.28,c['size'][1]*1.08,c['size'][2]*1.18]
                if 'pivot' in c:c['pivot']=p(c['pivot'])
    # Full horse barrel, rounded croup and an overlapping withers-to-torso transition.
    X('horse_body',[-4.8,11,-.7],[9.6,6.3,17.8],0)
    X('horse_body',[-3.9,10.2,3],[7.8,2.4,10.8],0)
    X('horse_body',[-4.6,12.2,13],[9.2,5.4,6],2)
    X('horse_body',[-3.8,15.4,-.9],[7.6,3.3,7.5],0)
    X('body',[-3,17,-2],[6,2.1,4.1],10)
    X('body',[-2,19,-1.6],[4,2.5,3.2],8)
    X('chest',[-2.9,23.7,-2.2],[5.8,.8,.7],14)
    for side,n in [(-1,'right'),(1,'left')]:
        X('arm_'+n,[side*3.2-1.6,22.6,-1.65],[3.2,1.4,3.4],14,[0,0,-side*10])
        X('arm_'+n,[side*3.3-1.5,22,-1.7],[3,1,3.5],3,[0,0,-side*13])
        X('body',[side*1.8-1.2,15,-2.35],[2.4,3.1,.65],7,[0,0,-side*10])
        # Fetlocks/hooves remain individual four-chain anatomy, front silver cuffs only.
        X('front_'+n+'_lower',[side*3.3-1.3,1.8,-1.4],[2.6,1.3,2.9],14)
        for fore in ('front_','hind_'):
            z=0 if fore=='front_' else 15
            X(fore+n+'_foot',[side*3.3-1.4,.1,z-1.95],[2.8,1.2,3.7],1)
        X('horse_body',[side*4.5-.3,12.6,3.5],[.6,4.2,1],10)
        X('horse_body',[side*4.6-.35,13.4,3.4],[.7,1.2,1.2],4)
    # Reference sword points forward/down; retain original weapon attachment name.
    m.by_name['weapon']['cubes']=[];m.by_name['weapon']['rotation']=[25,0,0]
    X('weapon',[-3.6,15.9,-1.8],[.8,.8,3.1],10)
    X('weapon',[-3.85,15.7,1.1],[1.3,1.2,.65],4)
    X('weapon',[-5.2,15.8,-2.5],[4,.9,.7],4)
    X('weapon',[-3.85,16,-11.9],[1.3,.55,9.5],14)
    X('weapon',[-3.55,15.9,-11.9],[.7,.75,9.5],12)
    X('weapon',[-3.6,16.05,-13],[.8,.45,1.3],14)
    for j in range(3):X('hand_right',[-4.1+j*.65,15.3,-1.2],[.55,1,1.8],8)
    palette=['79513c','302c2a','91654c','777c7b','a48d54','202725','eee6d7','782e36','e0c8ae','252a27','4e3930','9a7751','b5bcb7','343b3a','9fa7a3','f4ebdc']
    roles=['fur','leather','fur','metal','gold','skin','skin','cloth','skin','hair','leather','cloth','metal','cloth','metal','skin']
    for side,n in [(-1,'right'),(1,'left')]:
        for prefix in ('front_','hind_'):
            name=prefix+n+'_lower'
            for c in m.by_name[name]['cubes']:
                if c['size'][1]>3:
                    center=c['origin'][0]+c['size'][0]/2;c['size'][0]*=1.25;c['origin'][0]=center-c['size'][0]/2
        X('hair_'+str(side),[side*3-.6,24.6,-1.4],[1.2,6.7,1.8],9,[0,0,-side*6])
    for j in range(3):X('head',[-2.8+j*1.9,29+(j%2)*.5,-3],[2.1,2-(j%2)*.4,.8],9,[0,0,(j-1)*10])
    for j in range(3):X('tail_tip',[-.9+j*.6,4+j*.4,19],[.6,3-j*.3,2.1],9,[-8,0,(j-1)*9])
    return m,palette,roles,(1.25,2.15)

def material_of(cube):
    uv=cube['uv']['north']['uv'];return int(uv[0]//32+4*(uv[1]//32))

def repaint_cube(cube,index):
    old=material_of(cube);dx=(index%4-old%4)*32;dy=(index//4-old//4)*32
    for face in cube['uv'].values():face['uv']=[face['uv'][0]+dx,face['uv'][1]+dy]

def fox_spirit_girl():
    m=old_model('fox_spirit_girl');X=m.box
    for b in m.bones:
        n=b['name']
        if n=='head' or n.startswith(('hair_','ear_')):
            def p(v):return [v[0]*1.29,23.495+(v[1]-23.495)*1.08,v[2]*1.2]
            b['pivot']=p(b['pivot'])
            for c in b.get('cubes',[]):
                c['origin']=p(c['origin']);c['size']=[c['size'][0]*1.29,c['size'][1]*1.08,c['size'][2]*1.2]
                if 'pivot' in c:c['pivot']=p(c['pivot'])
                if n.startswith('ear_') and material_of(c)==6:repaint_cube(c,12)
        if n.startswith(('tail_','tailtip_')):
            if 'rotation' in b:b['rotation'][0]*=-1
            for c in b.get('cubes',[]):
                if 'rotation' in c:c['rotation'][0]*=-1
                if material_of(c)==6:repaint_cube(c,12)
                center=c['origin'][0]+c['size'][0]/2;c['size'][0]*=1.1;c['origin'][0]=center-c['size'][0]/2
        if n.startswith('leg_'):
            for c in b.get('cubes',[]):repaint_cube(c,6)
        if n.startswith('hand_'):
            for c in b.get('cubes',[]):repaint_cube(c,10)
    for side,n in [(-1,'right'),(1,'left')]:
        x=side*3.4
        X('arm_'+n,[x-1.4,16.7,-1.4],[2.8,4.4,2.9],6,[0,0,-side*6])
        X('forearm_'+n,[x-1.25,12.9,-1.3],[2.5,4.1,2.7],6)
        X('forearm_'+n,[x-1.35,12.8,-1.4],[2.7,1.2,2.9],7)
        X('hand_'+n,[x-1.1,11.6,-1.3],[2.2,1.7,2.5],10)
        # Red charm patches on white stockings, black shoes remain distinct.
        x=side*1.25
        X('shin_'+n,[x-.5,5.3,-1.1],[1,1.2,.3],7)
        X('foot_'+n,[x-1.2,.1,-2.4],[2.4,1.6,3.8],10)
        X('head',[side*2.7-.7,25.6,-2.5],[1.4,3.2,1],9,[0,0,-side*10])
    X('body',[-2.2,13.2,-2.1],[4.4,1.1,4.2],10)
    X('chest',[-2.1,19,-2.85],[4.2,.7,.6],6,[0,0,-13])
    X('chest',[-2.1,18.3,-2.9],[4.2,.7,.6],6,[0,0,13])
    palette=['e0c4a8','967740','a43237','c0a14d','57a657','2d3026','e6e5da','ba353c','ead7bf','bca14f','26272b','9bc781','d3bb67','5b3032','999b96','f5efda']
    roles=['skin','fur','cloth','gold','eyes','skin','cloth','cloth','skin','hair','leather','eyes','fur','cloth','metal','skin']
    for side,n in [(-1,'right'),(1,'left')]:
        ear='ear_'+n;m.by_name[ear]['cubes']=[]
        for x,y,w,h,mat in [(2.4,28.4,2.6,2,9),(2.8,30.1,1.9,2,9),(3.15,31.6,.9,1.2,12)]:
            X(ear,[side*x-w/2,y,-.6],[w,h,1.6],mat,[0,0,-side*12])
        X(ear,[side*2.4-.7,28.9,-.85],[1.4,1.5,.4],1,[0,0,-side*12])
        tunic='tunic_'+n;m.by_name[tunic]['cubes']=[]
        X(tunic,[side*1.45-1.6,9.4,-2.1],[3.2,3.3,4.2],10,[0,0,-side*6])
        X(tunic,[side*1.45-1.65,12.3,-2.15],[3.3,1.1,4.3],2)
    for c in m.by_name['body']['cubes']:
        if material_of(c)==3:repaint_cube(c,10)
    m.by_name['body']['cubes']=[c for c in m.by_name['body']['cubes'] if not(material_of(c)==7 and c.get('rotation')==[0,0,45])]
    X('chest',[-3.2,20.9,-2.1],[6.4,.7,4.2],10)
    X('head',[-3,28.6,-2.7],[1.8,.55,1.2],7)
    return m,palette,roles,(.7,1.85)

def anubis():
    m=old_model('anubis');X=m.box
    m.by_name['head']['cubes']=[c for c in m.by_name['head']['cubes'] if material_of(c)!=4]
    for b in m.bones:
        n=b['name']
        if n=='head' or n.startswith(('hair_','ear_')):
            def p(v):return [v[0]*1.47,21.458+(v[1]-21.458)*1.04,v[2]*1.28]
            b['pivot']=p(b['pivot'])
            for c in b.get('cubes',[]):
                c['origin']=p(c['origin']);c['size']=[c['size'][0]*1.47,c['size'][1]*1.04,c['size'][2]*1.28]
                if 'pivot' in c:c['pivot']=p(c['pivot'])
        if n in ('body','chest'):
            for c in b.get('cubes',[]):
                if material_of(c)==3:repaint_cube(c,0)
        if n.startswith('forearm_'):
            for c in b.get('cubes',[]):
                if material_of(c)==3:repaint_cube(c,2)
                if material_of(c)==12:repaint_cube(c,4)
        if n.startswith(('hand_','grip_')):
            for c in b.get('cubes',[]):
                if material_of(c) in (0,1):repaint_cube(c,2)
    for side,n in [(-1,'right'),(1,'left')]:
        linen='linen_'+n;m.by_name[linen]['cubes']=[]
        X(linen,[side*1.55-1.65,1.7,-1.9],[3.3,8.4,3.9],3)
        X(linen,[side*1.55-1.6,1.7,-2],[3.2,.8,4.1],6)
        X(linen,[side*1.55-1.5,8.9,-2.1],[3,1.2,.55],4)
        X('arm_'+n,[side*3.6-1.45,18.8,-1.5],[2.9,1.1,3.1],4)
        X('forearm_'+n,[side*3.6-1.25,12.7,-1.3],[2.5,.8,2.7],4)
        X('head',[side*3-.35,23.5,-2.15],[.7,3.1,.5],4)
    X('head',[-3.25,25.6,-2.9],[6.5,.65,.6],4)
    m.by_name['head']['cubes']=[c for c in m.by_name['head']['cubes'] if not(material_of(c)==7 and c.get('rotation')==[0,0,45])]
    # Closed grip and hooked blade rotate together forward/down from the palm.
    m.by_name['grip_right']['rotation']=[115,0,0]
    for c in m.by_name['khopesh']['cubes']:
        if material_of(c)==9 or c['origin'][1]>17:repaint_cube(c,14)
    palette=['dfcbb0','eedcc0','22252b','dedbc7','bea04a','15191f','efeddd','559cbb','24292d','9aa3a1','2b3034','f4ead3','a4853e','80b0b4','41474b','171c20']
    roles=['skin','skin','cloth','cloth','gold','hair','cloth','eyes','hair','metal','cloth','skin','gold','eyes','metal','cloth']
    for b in m.bones:
        if b['name'].startswith('ear_'):
            def y(v):return 25.55+(v-25.55)*.74
            b['pivot'][1]=y(b['pivot'][1])
            for c in b.get('cubes',[]):
                c['origin'][1]=y(c['origin'][1]);c['size'][1]*=.74
                if 'pivot' in c:c['pivot'][1]=y(c['pivot'][1])
        if b['name'].startswith('foot_'):
            for c in b.get('cubes',[]):repaint_cube(c,2)
        if b['name']=='chest':
            for c in b.get('cubes',[]):
                if material_of(c)==7:repaint_cube(c,4)
    return m,palette,roles,(.7,1.95)

def kobold():
    m=old_model('kobold');X=m.box
    for b in m.bones:
        if b['name']=='head' or b['name'].startswith(('hair_','ear_')):
            def p(v):return [v[0]*1.4,16.288+(v[1]-16.288)*1.12,v[2]*1.2]
            b['pivot']=p(b['pivot'])
            for c in b.get('cubes',[]):
                c['origin']=p(c['origin']);c['size']=[c['size'][0]*1.4,c['size'][1]*1.12,c['size'][2]*1.2]
                if 'pivot' in c:c['pivot']=p(c['pivot'])
                if b['name'].startswith('ear_'):
                    x=b['pivot'][0];c['origin'][0]=x+(c['origin'][0]-x)*.65;c['size'][0]*=.65
    # Small swept crest and overlapping armor plates retain the reptilian muzzle/tail.
    X('head',[-.7,20.8,.3],[1.4,1.6,1.5],8,[-22,0,0])
    X('head',[-.45,21.9,.7],[.9,1.1,1.1],5,[-24,0,0])
    for side,n in [(-1,'right'),(1,'left')]:
        X('arm_'+n,[side*3.1-1.4,13.9,-1.45],[2.8,1.3,3],2,[0,0,-side*12])
        X('arm_'+n,[side*3.2-1.3,13.5,-1.5],[2.6,.7,3.1],9,[0,0,-side*13])
        X('shin_'+n,[side*1.25-.95,2.2,-1.3],[1.9,2.1,.6],2)
        X('foot_'+n,[side*1.25-1.1,.3,-2],[2.2,.7,1.5],9)
    X('body',[-2.15,9.3,-1.8],[4.3,.9,3.8],6)
    X('body',[-.4,9.2,-2.05],[.8,1.1,.4],12)
    X('neck',[-1.3,14.8,-1.3],[2.6,1.25,2.7],6)
    X('chest',[-.6,13.8,-2.55],[1.2,1.5,.6],12,[0,0,12])
    m.by_name['grip_right']['rotation']=[115,0,0]
    palette=['c1c2bb','d7d5c8','737582','62646e','b0afb0','656775','73503d','272c31','8c8e9b','9da2a7','84838f','e0dfd1','88624c','454954','7c7e89','35383e']
    roles=['skin','skin','metal','cloth','metal','hair','leather','eyes','hair','metal','metal','skin','leather','cloth','scale','cloth']
    for b in m.bones:
        if b['name'].startswith('hip_plate_'):
            for c in b.get('cubes',[]):
                top=c['origin'][1]+c['size'][1];c['origin'][1]-=1.05;c['size'][1]=top-c['origin'][1]
                mid=c['origin'][0]+c['size'][0]/2;c['size'][0]*=1.15;c['origin'][0]=mid-c['size'][0]/2
        if b['name'].startswith('foot_'):
            for c in b.get('cubes',[]):
                if material_of(c)==6:repaint_cube(c,2)
    X('pelvis',[-.8,7.2,-2.3],[1.6,1.5,.75],6)
    X('pelvis',[-.3,7.5,-3.1],[.6,.65,.2],12)
    palette[9]='636a71'
    return m,palette,roles,(.6,1.3)

def cyclops():
    m=old_model('cyclops');X=m.box
    for b in m.bones:
        if b['name']=='head' or b['name'].startswith('hair_') or b['name']=='plume':
            def p(v):return [v[0]*1.45,24.917+(v[1]-24.917)*1.1,v[2]*1.28]
            b['pivot']=p(b['pivot'])
            for c in b.get('cubes',[]):
                c['origin']=p(c['origin']);c['size']=[c['size'][0]*1.45,c['size'][1]*1.1,c['size'][2]*1.28]
                if 'pivot' in c:c['pivot']=p(c['pivot'])
        if b['name'].startswith(('hand_','grip_')):
            for c in b.get('cubes',[]):
                if material_of(c) in (0,1):repaint_cube(c,2)
        if b['name'].startswith(('shin_','foot_')):
            for c in b.get('cubes',[]):
                if material_of(c) in (6,9):repaint_cube(c,2)
    # Keep both original arm/grip joint chains and their solved cross-body action poses.
    for c in m.by_name['poleaxe']['cubes']:
        if material_of(c)==9:repaint_cube(c,13)
        if material_of(c)==7:repaint_cube(c,4)
    for side,n in [(-1,'right'),(1,'left')]:
        X('forearm_'+n,[side*5.08-1.5,15.8,-1.55],[3,1.2,3.2],4)
        X('shin_'+n,[side*1.7-1.2,2,-1.5],[2.4,4.4,.65],2)
        X('shin_'+n,[side*1.7-1.3,5.5,-1.55],[2.6,.8,.7],4)
        X('foot_'+n,[side*1.7-1.4,.2,-2.65],[2.8,1.2,4],2)
        X('foot_'+n,[side*1.7-1.35,.4,-2.75],[2.7,.55,1.1],4)
        X('head',[side*3.4-.5,25.7,-2.6],[1,3.2,.7],2)
    palette=['d8c3ad','e5d2b8','394d8a','283867','b5a15a','23262d','534329','7f91a1','33373e','9fa6a9','657eb3','efeadb','77613e','71603c','4c6190','19243d']
    roles=['skin','skin','metal','cloth','gold','hair','wood','eyes','hair','metal','metal','skin','leather','bronze','metal','cloth']
    # A narrower fitted armor silhouette; rigid shared chest carry preserves both grips.
    for b in m.bones:
        if b['name']=='head' or b['name'].startswith('hair_') or b['name']=='plume':continue
        b['pivot'][0]*=.78
        for c in b.get('cubes',[]):
            c['origin'][0]*=.78;c['size'][0]*=.78
            if 'pivot' in c:c['pivot'][0]*=.78
    for c in m.by_name['head']['cubes']:
        if material_of(c)==4:repaint_cube(c,5)
    X('head',[-3.25,29,-3.1],[6.5,.4,.5],4)
    return m,palette,roles,(.85,2.05)

def dhampir():
    m=old_model('dhampir');X=m.box
    for b in m.bones:
        if b['name']=='head' or b['name'].startswith('hair_') or b['name']=='hat_feather':
            def p(v):return [v[0]*1.4,21.212+(v[1]-21.212)*1.1,v[2]*1.25]
            b['pivot']=p(b['pivot'])
            for c in b.get('cubes',[]):
                c['origin']=p(c['origin']);c['size']=[c['size'][0]*1.4,c['size'][1]*1.1,c['size'][2]*1.25]
                if 'pivot' in c:c['pivot']=p(c['pivot'])
                if b['name']=='head' and material_of(c)==7 and c.get('rotation')==[0,0,23]:repaint_cube(c,13)
        if b['name']=='body':
            for c in b.get('cubes',[]):
                if material_of(c)==3:repaint_cube(c,0)
        if b['name'].startswith('forearm_'):
            for c in b.get('cubes',[]):
                if material_of(c)==3:repaint_cube(c,2)
        if b['name'].startswith(('hand_','grip_')):
            for c in b.get('cubes',[]):
                if material_of(c) in (0,1):repaint_cube(c,2)
    m.by_name['hat_feather']['cubes']=[]
    X('hat_feather',[-1,28.8,0],[2,1.3,2],15,[-12,0,0])
    X('hat_feather',[-.65,29.8,.3],[1.3,.8,1.4],15,[-15,0,0])
    for side in (-1,1):X('head',[side*.8-.9,27.7,-3.55],[1.8,1.5,.6],13,[0,0,-side*18])
    X('head',[-.65,27.5,-3.8],[1.3,1.8,.55],12)
    for side,n in [(-1,'right'),(1,'left')]:
        X('chest',[side*1.8-.35,17.2,-2.7],[.7,2.5,.5],12,[0,0,side*12])
        X('thigh_'+n,[side*1.35-.8,6.8,-1.5],[1.6,2.3,.45],3,[0,0,-side*12])
        X('shin_'+n,[side*1.35-.75,3,-1.45],[1.5,2.4,.45],3,[0,0,side*14])
        X('shin_'+n,[side*1.35-1.1,1.8,-1.6],[2.2,.75,.5],12)
    # Preserve the original poleblade and finger hierarchy; present it forward/down.
    pivot=m.by_name['grip_right']['pivot'];m.by_name['grip_right']['rotation']=[115,0,0]
    for c in m.by_name['poleblade']['cubes']:
        c['origin'][1]=pivot[1]+(c['origin'][1]-pivot[1])*.8;c['size'][1]*=.8
        if 'pivot' in c:c['pivot'][1]=pivot[1]+(c['pivot'][1]-pivot[1])*.8
    palette=['e1cbb2','eed9be','24262b','c0bbaa','9b8348','b5a05b','58432d','b5464c','c9b46b','596167','652b3a','eee5d6','ac2944','d13b50','5d3947','171b20']
    roles=['skin','skin','cloth','cloth','gold','hair','wood','eyes','hair','metal','cloth','skin','cloth','cloth','cloth','cloth']
    for b in m.bones:
        if b['name'].startswith('foot_'):
            for c in b.get('cubes',[]):repaint_cube(c,2)
        if b['name'].startswith('hair_'):
            for c in b.get('cubes',[]):
                low=c['origin'][1];top=low+c['size'][1];c['origin'][1]=max(low,18.4);c['size'][1]=max(.3,top-c['origin'][1])
    for side,n in [(-1,'right'),(1,'left')]:
        X('head',[side*4.9-.7,25.9,-3.5],[1.4,.65,6],15,[0,0,-side*15])
        X('coat_'+n,[side*1.7-1.65,4.4,2],[3.3,7.2,.9],15,[8,0,-side*5])
        X('coat_'+n,[side*1.7-1.5,4.4,2.8],[3,.65,.35],12,[8,0,-side*5])
    X('head',[-4.5,25.6,-4.1],[9,.55,.7],15)
    return m,palette,roles,(.7,1.85)

def sahuagin():
    m=old_model('sahuagin');X=m.box
    for b in m.bones:
        if b['name']=='head' or b['name'].startswith(('hair_','fin_head_')):
            def p(v):return [v[0]*1.28,22+(v[1]-22)*1.08,v[2]*1.18]
            b['pivot']=p(b['pivot'])
            for c in b.get('cubes',[]):
                c['origin']=p(c['origin']);c['size']=[c['size'][0]*1.28,c['size'][1]*1.08,c['size'][2]*1.18]
                if 'pivot' in c:c['pivot']=p(c['pivot'])
        if b['name'].startswith('leg_') and not b['name'].endswith(('_lower','_foot')):
            for c in b.get('cubes',[]):
                if material_of(c)==13:repaint_cube(c,8)
        if b['name'].startswith('hand_'):
            for c in b.get('cubes',[]):
                if material_of(c)==8:repaint_cube(c,3)
        if b['name'].endswith('_foot'):
            for c in b.get('cubes',[]):
                if material_of(c)==6:repaint_cube(c,1)
    m.by_name['body']['cubes']=[]
    X('body',[-2.65,11.5,-1.8],[5.3,2.5,3.6],13)
    X('body',[-1.95,14,-1.6],[3.9,4.1,3.2],8)
    X('body',[-2.7,13,-1.95],[5.4,.75,4],9)
    m.by_name['chest']['cubes']=[c for c in m.by_name['chest']['cubes'] if material_of(c)!=3]
    for c in m.by_name['chest']['cubes']:
        if material_of(c)==13:repaint_cube(c,8)
    X('chest',[-2.8,17,-1.7],[5.6,3.1,3.4],8)
    for side,n in [(-1,'right'),(1,'left')]:
        X('chest',[side*1.4-1.15,18.3,-2.5],[2.3,1.7,1.2],3,[0,0,-side*9])
        X('fore_'+n,[side*3.2-1.35,10.8,-1.4],[2.7,4.3,2.9],3)
        X('fore_'+n,[side*3.2-1.5,13.9,-1.55],[3,1.2,3.2],2)
        X('fore_'+n,[side*4.6-.3,11.8,-.2],[.6,3.2,2.6],12,[0,0,-side*23])
        X('leg_'+n,[side*1.45-1.25,8,-1.35],[2.5,1,2.8],3)
        X('leg_'+n,[side*1.45-1.3,10.4,-1.4],[2.6,.7,2.9],9)
    X('chest',[-2.3,18.15,-2.65],[4.6,.45,.55],6)
    X('chest',[-.4,20.15,-1.9],[.8,.7,.45],4)
    palette=['507f78','203e57','41678c','365c85','a6a064','253b3a','d9dfd5','876f70','d8c4ac','294b45','324959','608f98','35567c','2c4e48','647b90','eef0de']
    roles=['scale','scale','scale','metal','gold','skin','cloth','cloth','skin','hair','leather','cloth','membrane','cloth','metal','skin']
    m.by_name['weapon']['rotation']=[115,0,0]
    m.by_name['tail']['cubes']=[];m.by_name['tail_tip']['cubes']=[]
    m.by_name['tail_tip']['pivot']=[0,7.8,3.3]
    X('tail',[-.7,7.3,1.8],[1.4,6.3,2.4],0)
    X('tail_tip',[-.55,5.1,2.7],[1.1,3.4,2.1],0)
    for side,n in [(-1,'right'),(1,'left')]:
        X('tail_tip',[side*1.15-1.15,3.3,4.5],[2.3,2.9,.65],12,[0,0,side*25],[0,5.5,4.7])
        lower='leg_'+n+'_lower'
        X(lower,[side*2.2-.4,2.5,.1],[.8,3,2.2],3)
        X(lower,[side*2.5-.35,2.7,.5],[.7,2.5,1.7],12,[0,0,-side*22],[side*2.25,3.9,.4])
    for j in range(3):X('head',[-2.8+j*1.8,24.3+j%2*.5,-2.95],[2,2.1-j%2*.5,.8],9,[0,0,(j-1)*9])
    return m,palette,roles,(.7,1.85)

def holstaurus():
    m=old_model('holstaurus');X=m.box
    for b in m.bones:
        n=b['name']
        if n=='head' or n.startswith('hair_'):
            def p(v):return [v[0]*1.3,22+(v[1]-22)*1.08,v[2]*1.18]
            b['pivot']=p(b['pivot'])
            for c in b.get('cubes',[]):
                c['origin']=p(c['origin']);c['size']=[c['size'][0]*1.3,c['size'][1]*1.08,c['size'][2]*1.18]
                if 'pivot' in c:c['pivot']=p(c['pivot'])
                if n=='head' and material_of(c)==6 and c['origin'][1]>26 and c['size'][2]>1:
                    c['origin'][1]=26.3+(c['origin'][1]-26.3)*.75;c['size'][1]*=.75
                    if 'pivot' in c:c['pivot'][1]=26.3+(c['pivot'][1]-26.3)*.75
        if n.startswith(('arm_','fore_')):
            for c in b.get('cubes',[]):
                if material_of(c)==0 or n.startswith('fore_') and material_of(c)==13:repaint_cube(c,8)
        if n.startswith('leg_'):
            for c in b.get('cubes',[]):
                if n.endswith('_foot'):repaint_cube(c,14)
                elif material_of(c) in (13,3):repaint_cube(c,0)
        if n=='chest':
            for c in b.get('cubes',[]):
                if material_of(c)==13:repaint_cube(c,8)
    m.by_name['body']['cubes']=[]
    X('body',[-2.7,11.5,-1.8],[5.4,3,3.8],13)
    X('body',[-1.9,14.5,-1.6],[3.8,3.8,3.2],8)
    X('body',[-2.5,13.8,-2],[5,1,4],3)
    X('body',[-.7,11.8,-2.8],[1.4,1.6,1.2],4)
    X('body',[-.3,11.5,-2.95],[.6,.55,.4],1)
    X('chest',[-2.4,19.1,-2.3],[4.8,.6,.6],11)
    for side,n in [(-1,'right'),(1,'left')]:
        X('chest',[side*2.1-.35,18,-2.2],[.7,2,.6],11,[0,0,-side*9])
        X('fore_'+n,[side*3.2-1.1,11.5,-1.2],[2.2,1.1,2.5],3)
        X('leg_'+n+'_lower',[side*1.45-1.05,1.8,-1.35],[2.1,3.8,.7],0)
        X('leg_'+n+'_lower',[side*2.15-.4,1.8,-1],[.8,4,2.5],3)
        X('leg_'+n+'_foot',[side*1.45-1.2,.1,-2.6],[2.4,.65,3.9],1)
    palette=['e1e2df','32373d','b0afb4','69758e','c3a24b','292e39','eeeade','b39ca2','dfc9b3','969bab','485368','e0e3e2','bec4c9','45536c','7d8798','f0ece4']
    roles=['fur','fur','fur','cloth','gold','skin','horn','cloth','skin','hair','leather','cloth','metal','cloth','metal','skin']
    for side,n in [(-1,'right'),(1,'left')]:
        x=side*1.55
        X('leg_'+n+'_lower',[x-1.45,1,-1.5],[2.9,5.2,3.4],0)
        X('leg_'+n+'_lower',[x-1.5,5.7,-1.55],[3,.65,3.5],3)
        X('leg_'+n+'_foot',[x-1.5,.2,-2.7],[3,1.6,4.2],14)
    for j in range(3):X('head',[-3.1+j*2,24.6+j%2*.4,-2.9],[2.2,2.2-j%2*.4,.9],9,[0,0,(j-1)*11])
    return m,palette,roles,(.8,1.9)

def werecat():
    m=old_model('werecat');X=m.box
    for b in m.bones:
        n=b['name']
        if n=='head' or n.startswith(('hair_','ear_')):
            def p(v):return [v[0]*1.3,22+(v[1]-22)*1.08,v[2]*1.2]
            b['pivot']=p(b['pivot'])
            for c in b.get('cubes',[]):
                c['origin']=p(c['origin']);c['size']=[c['size'][0]*1.3,c['size'][1]*1.08,c['size'][2]*1.2]
                if 'pivot' in c:c['pivot']=p(c['pivot'])
        if n.startswith('fore_'):
            for c in b.get('cubes',[]):
                if material_of(c)==14:repaint_cube(c,13)
    # No wings: retain triangular cat ears, connected two-joint tail and clawed hands.
    m.by_name['body']['cubes']=[]
    X('body',[-2.7,11.5,-1.8],[5.4,3.2,3.7],13)
    X('body',[-1.9,14.6,-1.6],[3.8,3.7,3.2],8)
    X('body',[-2.5,14,-2],[5,.8,4],13)
    X('chest',[-1.2,17.1,-2.65],[2.4,3,.65],14)
    for side,n in [(-1,'right'),(1,'left')]:
        X('body',[side*2.1-.75,10.2,-2.1],[1.5,3.6,4.2],3,[0,0,-side*10])
        X('arm_'+n,[side*3.2-1.45,17.9,-1.55],[2.9,1.2,3.2],14,[0,0,-side*13])
        X('fore_'+n,[side*3.2-1.4,10.8,-1.45],[2.8,4.5,3.1],13)
        X('fore_'+n,[side*3.2-1.55,13.9,-1.6],[3.1,1.1,3.4],3)
        X('hand_'+n,[side*3.2-1.05,9.9,-1.2],[2.1,1.8,2.5],13)
        X('leg_'+n+'_lower',[side*1.45-1.2,1.5,-1.3],[2.4,4.8,2.8],13)
        X('leg_'+n+'_lower',[side*1.45-.85,5,-1.65],[1.7,1.6,.7],14,[0,0,side*8])
        X('leg_'+n+'_foot',[side*1.45-1.4,.1,-2.6],[2.8,1.6,4],14)
        X('leg_'+n+'_foot',[side*1.45-1.45,.1,-2.7],[2.9,.55,4.2],1)
    palette=['7c8590','303746','a5acb6','6a788e','c14e58','2c313a','deded7','9c818a','d7c9bc','a1a7b2','3e4655','a6b3c5','c7cdd1','303c54','8793a6','ece8df']
    roles=['fur','cloth','fur','metal','eyes','skin','bone','cloth','skin','hair','leather','cloth','metal','cloth','metal','skin']
    for b in m.bones:
        if b['name'].startswith('hair_'):
            for c in b.get('cubes',[]):
                low=c['origin'][1];top=low+c['size'][1];c['origin'][1]=max(low,19.8);c['size'][1]=max(.3,top-c['origin'][1])
    X('head',[-1.2,26.7,1],[2.4,1.4,2.1],9,[-12,0,-15])
    X('head',[-.5,27.7,1.5],[1.3,1,1.3],9,[-22,0,-15])
    for j in range(3):X('head',[-3.1+j*2,24.5+j%2*.5,-3],[2.2,2.1-j%2*.4,.8],9,[0,0,(j-1)*10])
    for side,n in [(-1,'right'),(1,'left')]:
        X('fore_'+n,[side*2.8-.4,11.2,-1.65],[.8,2.4,.3],4)
        for y in (2.4,4):X('leg_'+n+'_lower',[side*1.45-1.25,y,-1.4],[2.5,.55,.45],14)
    return m,palette,roles,(.7,1.8)

BUILDERS={'harpy':harpy,'forest_dryad':dryad,'slime_maiden':slime,'minotaur':minotaur,'vampire':vampire,'valkyrie':valkyrie,'succubus':succubus,'ender_dragon_girl':ender_dragon_girl,'centaur':centaur,'fox_spirit_girl':fox_spirit_girl,'anubis':anubis,'kobold':kobold,'cyclops':cyclops,'dhampir':dhampir,'sahuagin':sahuagin,'holstaurus':holstaurus,'werecat':werecat}

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
    if species=='werecat':
        k=9;x=k%4*32;y=k//4*32;rgb=tuple(int(palette[k][i:i+2],16) for i in (0,2,4))
        for box,delta in [((3,4,12,12),-18),((16,6,27,16),12),((5,20,15,28),-10)]:
            draw.rectangle(tuple(v+(x if i%2==0 else y) for i,v in enumerate(box)),fill=tuple(max(0,min(255,c+delta)) for c in rgb)+(255,))
    if species=='holstaurus':
        rgb=tuple(int(palette[0][i:i+2],16) for i in (0,2,4));draw.rectangle((0,0,31,31),fill=rgb+(255,))
        draw.polygon([(4,5),(10,5),(10,9),(13,9),(13,15),(6,15),(6,12),(3,12)],fill=(126,133,145,255))
        draw.polygon([(20,18),(28,18),(28,23),(25,23),(25,28),(18,28),(18,22)],fill=(156,163,173,255))
        draw.rectangle((0,29,12,31),fill=(201,205,207,255))
        k=9;x=k%4*32;y=k//4*32;rgb=tuple(int(palette[k][i:i+2],16) for i in (0,2,4))
        for box,delta in [((3,4,12,12),-14),((16,6,27,16),9),((5,20,15,28),-9)]:
            draw.rectangle(tuple(v+(x if i%2==0 else y) for i,v in enumerate(box)),fill=tuple(max(0,min(255,c+delta)) for c in rgb)+(255,))
    if species=='dhampir':
        for k in (5,8):
            x=k%4*32;y=k//4*32;rgb=tuple(int(palette[k][i:i+2],16) for i in (0,2,4))
            for box,delta in [((3,5,12,12),10),((15,8,26,19),-12),((4,22,14,28),6)]:
                draw.rectangle(tuple(v+(x if i%2==0 else y) for i,v in enumerate(box)),fill=tuple(max(0,min(255,c+delta)) for c in rgb)+(255,))
    if species=='kobold':
        for k in (5,8):
            x=k%4*32;y=k//4*32;rgb=tuple(int(palette[k][i:i+2],16) for i in (0,2,4))
            for box,delta in [((4,5,12,13),-13),((15,8,26,19),10),((4,22,14,28),-8)]:
                draw.rectangle(tuple(v+(x if i%2==0 else y) for i,v in enumerate(box)),fill=tuple(max(0,min(255,c+delta)) for c in rgb)+(255,))
    if species=='anubis':
        k=3;x=k%4*32;y=k//4*32;rgb=tuple(int(palette[k][i:i+2],16) for i in (0,2,4))
        draw.rectangle((x,y,x+31,y+31),fill=rgb+(255,))
        for box,delta in [((0,0,31,4),9),((3,7,12,14),-11),((15,4,23,11),5),((20,17,30,26),-9),((5,23,17,29),-14)]:
            draw.rectangle(tuple(v+(x if i%2==0 else y) for i,v in enumerate(box)),fill=tuple(max(0,min(255,c+delta)) for c in rgb)+(255,))
    if species=='fox_spirit_girl':
        for k in (9,12):
            x=k%4*32;y=k//4*32;rgb=tuple(int(palette[k][i:i+2],16) for i in (0,2,4))
            draw.rectangle((x,y,x+31,y+31),fill=rgb+(255,))
            for box,delta in [((0,0,31,4),9),((4,7,14,14),-9),((17,8,28,20),7),((4,23,20,30),-12)]:
                draw.rectangle(tuple(v+(x if i%2==0 else y) for i,v in enumerate(box)),fill=tuple(max(0,min(255,c+delta)) for c in rgb)+(255,))
    if species=='centaur':
        for k in (0,2):
            x=k%4*32;y=k//4*32;rgb=tuple(int(palette[k][i:i+2],16) for i in (0,2,4))
            draw.rectangle((x,y,x+31,y+31),fill=rgb+(255,))
            for box,delta in [((0,0,31,4),9),((4,7,13,15),6),((16,10,28,20),-8),((4,22,18,30),-10)]:
                draw.rectangle(tuple(v+(x if i%2==0 else y) for i,v in enumerate(box)),fill=tuple(max(0,min(255,c+delta)) for c in rgb)+(255,))
    if species=='ender_dragon_girl':
        for k in (7,9):
            x=k%4*32;y=k//4*32;rgb=tuple(int(palette[k][i:i+2],16) for i in (0,2,4))
            draw.rectangle((x,y,x+31,y+31),fill=rgb+(255,))
            for box,delta in [((0,0,31,3),4),((3,6,13,15),-3),((16,5,28,18),3),((6,22,21,29),-4)]:
                draw.rectangle(tuple(v+(x if i%2==0 else y) for i,v in enumerate(box)),fill=tuple(max(0,min(255,c+delta)) for c in rgb)+(255,))
    if species=='vampire':
        for k in (5,8):
            x=k%4*32;y=k//4*32;rgb=tuple(int(palette[k][i:i+2],16) for i in (0,2,4))
            for box,delta in [((3,5,12,11),12),((15,8,24,18),-10),((5,19,14,26),7),((23,23,30,30),-15)]:
                draw.rectangle(tuple(v+(x if i%2==0 else y) for i,v in enumerate(box)),fill=tuple(max(0,min(255,c+delta)) for c in rgb)+(255,))
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
    if args.species in ('succubus','ender_dragon_girl'):
        for side,n in [(-1,'right'),(1,'left')]:
            animations['death']['bones']['wing_'+n]={'rotation':{'0':[0,side*90,0]}}
            animations['death']['bones']['wingtip_'+n]={'rotation':{'0':[0,0,0]}}
    if args.species=='cyclops':
        animations['death']['bones']['grip_right']={'rotation':{'0':[0,0,0],'.3':[0,0,-45],'.65':[0,0,-90]}}
    if args.species=='fox_spirit_girl':
        for i in range(9):
            name='tail_'+str(i);delta=(i-4)*1.5-model.by_name[name]['rotation'][1]
            animations['death']['bones'][name]={'rotation':{'0':[0,0,0],'.3':[0,delta*.45,0],'.65':[0,delta,0]}}
    if args.species in ('forest_dryad','succubus','ender_dragon_girl','fox_spirit_girl','cyclops'):
        from visual_v3_geometry import support_death
        support_death(model,animations)
    write_creature(model,palette,roles,animations,*size,glow=() if args.species in ('minotaur','centaur','sahuagin','holstaurus','werecat') else (7,) if args.species in ('cyclops','dhampir') else (13,) if args.species=='kobold' else (7,) if args.species=='anubis' else (13,) if args.species=='vampire' else (11,) if args.species=='slime_maiden' else (4,),translucent=args.species=='slime_maiden')

if __name__=='__main__':main()
