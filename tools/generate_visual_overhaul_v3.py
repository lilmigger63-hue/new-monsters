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

BUILDERS={'harpy':harpy}

BASE_ATLAS=pipeline.material_atlas

def reference_atlas(palette,roles,translucent=False):
    image=BASE_ATLAS(palette,roles,translucent);draw=ImageDraw.Draw(image)
    for k,role in enumerate(roles):
        if role!='feather':continue
        x=k%4*32;y=k//4*32;rgb=tuple(int(palette[k][i:i+2],16) for i in (0,2,4))
        def ink(d):return tuple(max(0,min(255,c+d)) for c in rgb)+(255,)
        draw.rectangle((x,y,x+31,y+31),fill=ink(0))
        for box,d in [((0,0,31,5),10),((0,6,8,18),5),((9,6,23,13),-7),((16,14,31,24),6),((3,19,14,28),-10),((15,25,31,31),-15)]:
            draw.rectangle(tuple(v+(x if i%2==0 else y) for i,v in enumerate(box)),fill=ink(d))
    return image

def main():
    parser=argparse.ArgumentParser();parser.add_argument('species',choices=BUILDERS);args=parser.parse_args()
    model,palette,roles,size=BUILDERS[args.species]()
    pipeline.material_atlas=reference_atlas
    animations=baseline(ASSET/'geckolib/animations/entity'/f'{args.species}.animation.json')['animations']
    write_creature(model,palette,roles,animations,*size,glow=(4,))

if __name__=='__main__':main()
