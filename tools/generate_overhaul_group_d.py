#!/usr/bin/env python3
"""Original Group D sculpted sources. All coordinates are pixels; no gameplay edits.

Research translation: icy golem facets and floating core; deer long metatarsals /
branching antlers; gel layered lobes; avian primary/secondary feathers; horned
caster's layered robes. See docs/creature-overhaul/REFERENCE_ATLAS.md.
"""
import math
from PIL import ImageDraw
import overhaul_asset_pipeline as asset_pipeline
from overhaul_asset_pipeline import Model, clip, keys, write_creature

PALETTES = {
'frost_elemental': ['659db9','294358','b8dce5','eef8f5','c5ffff','152d41','e6f3ef','4f7786','789fab','375569','506576','68e4fa','9acbd7','617987','90b3bd','ffffff'],
'moon_stag':['899ba9','445565','cbd4d2','baa77c','b9efff','233441','e8e7db','687b8d','aabdc4','4e6375','59494b','a6deed','92b0c6','3e586c','9ea9ae','f1f9ef'],
'slime_maiden':['49aaa2','236575','8bcbb9','cee9d1','bcffe7','183d51','e0fff0','5b87a3','8ccfc4','327b88','37767a','9beed6','67bebd','56a899','8ebfba','f3fff5'],
'harpy':['665970','332c41','a999a5','c5b18a','e7c57d','211f2b','e5d9c5','796778','c9a18f','483c50','5b4640','d5b375','8d8998','534357','8e858b','efe3d2'],
'demon_sorceress':['46354c','211f2e','70506d','b79a61','f4a4e5','171822','d1bbaa','8f3e5a','bd9294','292739','503640','dc77d3','a761c7','352936','91838e','ffdfef']}
SIZES={'frost_elemental':(1.1,2.4,1.2),'moon_stag':(1.1,1.8,.4),'slime_maiden':(.85,1.65,.7),'harpy':(.9,1.8,.6),'demon_sorceress':(.7,1.95,1.1)}

def bone(m,n,p,pivot,origin=None,size=None,mat=0,rot=None):
    m.bone(n,p,pivot,rot)
    if size:m.box(n,origin,size,mat)
    return n

def eyes(m,parent,x,y,z,wide=1):
    for s in (-1,1):
        m.box(parent,[s*x-wide*.6,y-.1,z],[wide*1.2,1.1,.2],5)
        m.box(parent,[s*x-wide*.45,y,z-.12],[wide*.9,.7,.18],4)
        m.box(parent,[s*x-.1,y+.4,z-.23],[.22,.22,.1],15)

def frost():
    m=Model('frost_elemental');bone(m,'body','root',[0,22,0])
    # Interlocking irregular chunks leave readable negative space around the core.
    for i,(o,s,r) in enumerate([([-5,17,-3],[5,13,6],[0,0,-13]),([1,18,-3],[5,12,6],[0,0,17]),([-4,27,-2],[8,5,5],[0,10,0])]):
        bone(m,'torso_shard_'+str(i),'body',[0,24,0],o,s,i%3, r)
    bone(m,'core','body',[0,23,0],[-2.2,20.8,-3.6],[4.4,4.4,4.4],11,[0,0,45])
    bone(m,'head','body',[0,31,0],[-3.2,30,-2.7],[6.4,6.5,5.4],2,[0,0,-6]);eyes(m,'head',1.45,33,-2.95)
    for s,n in [(-1,'right'),(1,'left')]:
        bone(m,'arm_'+n,'body',[s*7,28,0],[s*7-2.7,21,-2.5],[5.4,8,5],0,[0,0,s*14])
        bone(m,'hand_'+n,'arm_'+n,[s*8,21,0],[s*8-2.3,13,-2.6],[4.6,7,5.2],2,[0,0,-s*9])
        for j in range(3):m.box('arm_'+n,[s*(6+j*1.8)-.8,28,-1],[1.6,7-j,2],2,[0,0,-s*(20+j*14)])
        bone(m,'leg_'+n,'body',[s*3,17,0],[s*3-2,4,-2],[4,11,4],1,[0,0,s*7])
        m.box('leg_'+n,[s*3-2.7,1,-4],[5.4,4,6],0)
    for i in range(5):
        a=i*math.tau/5; x,z=math.cos(a)*8,math.sin(a)*5
        bone(m,'orbit_'+str(i),'body',[x,22+i%2*5,z],[x-.8,20+i%2*5,z-.8],[1.6,4,1.6],12,[15,i*37,25])
    # Original radial ground eruption; parent root keeps shards grounded during casting.
    bone(m,'nova','root',[0,0,0])
    for i in range(8):
        a=i*math.tau/8; x,z=math.cos(a)*13,math.sin(a)*13
        bone(m,'nova_spike_'+str(i),'nova',[x,0,z],[x-.8,0,z-.8],[1.6,5+i%3,1.6],12,[math.sin(a)*18,0,-math.cos(a)*18])
        m.box('nova_spike_'+str(i),[x-.5,4+i%3,z-.5],[1,2.5,1],2,[math.sin(a)*26,0,-math.cos(a)*26])
    return m

def stag():
    m=Model('moon_stag');bone(m,'body','root',[0,17,0],[-4,13,-7],[8,6,15],0)
    m.box('body',[-3.6,12,-5],[7.2,5,11],2)
    bone(m,'neck','body',[0,17,-5],[-2.5,17,-7],[5,8,4.5],2,[-17,0,0])
    for j in range(4):m.box('neck',[-2+j*.25,16+j*1.6,-8-j*.1],[4-j*.5,2.6,2],0,[-20,0,0])
    bone(m,'head','neck',[0,24,-6],[-2.5,23,-8],[5,4,5],2)
    m.box('head',[-1.6,23,-11.4],[3.2,2.3,4],0);m.box('head',[-1.5,23.2,-11.8],[3,1.3,.5],5)
    eyes(m,'head',1.65,25,-8.2,.7)
    for s,n in [(-1,'right'),(1,'left')]:
        bone(m,'ear_'+n,'head',[s*2.1,25.5,-5],[s*2.1-1,25,-5.8],[2,4,1.4],0,[0,0,-s*48])
        # A rising main beam with independent brow, fork and terminal tines.
        bone(m,'antler_'+n,'head',[s*1.6,26.5,-5.5])
        for j in range(4):
            x=s*(1.6+j*1.55); y=27+j*3.0
            m.box('antler_'+n,[x-.65,y,-5+j*.4],[1.3,4.7,1.3],3,[0,0,-s*(24+j*4)])
            m.box('antler_'+n,[x-.4,y+1,-5+j*.4],[.8,3.8+j*.25,.8],11,[s*20,0,s*(22+j*9)])
            if j>0:m.box('antler_'+n,[x-.35,y+.6,-5+j*.4],[.7,3,.7],6,[-35,0,-s*61])
        for front in (True,False):
            z=-5 if front else 5;leg=('front_' if front else 'rear_')+n
            bone(m,leg,'body',[s*2.7,15,z],[s*2.7-1,8,z-1],[2,7,2],0,[(-5 if front else -23),0,0])
            bone(m,leg+'_hock',leg,[s*2.7,8,z],[s*2.7-.65,1.6,z-.65],[1.3,6.8,1.3],2,[(5 if front else 28),0,0])
            for toe in (-1,1):m.box(leg+'_hock',[s*2.7+toe*.5-.42,0,z-1.8],[.84,2,2.7],5)
    bone(m,'tail','body',[0,17,7],[-1,14,7],[2,4,2],2,[22,0,0])
    # Saddle is centered at the immutable y19.008 passenger attachment.
    m.box('body',[-3.9,18,-1.8],[7.8,.65,5],10)
    m.box('body',[-3,18.65,-1],[6,.35,3.8],13)
    for s in (-1,1):
        for j in range(5):m.box('body',[s*4,15+(j%2)*.8,-4+j*2],[.18,.5,.5],11)
        m.box('body',[s*4,12.5,0],[.25,5,1],10)
    return m

def slime():
    m=Model('slime_maiden');bone(m,'body','root',[0,11,0])
    # Offset intersecting rounded lobes form an organic pear shape, no straight legs.
    for i,(o,s) in enumerate([([-5,1,-3],[10,4,6]),([-6,3,-2],[11,5,5]),([-4.8,5,-3.7],[9,6,7]),([-3.5,9,-3],[7,6,6]),([-3,13,-2.3],[6,5,4.6])]):
        bone(m,'gel_'+str(i),'body',[0,o[1]+s[1]/2,0],o,s,[0,2,0,2,0][i],[0,0,(i%3-1)*8])
    bone(m,'head','body',[0,18,0],[-3,17.5,-2.7],[6,6,5.4],2,[0,0,-7]);eyes(m,'head',1.25,20,-2.94,1.05)
    m.box('head',[-.7,18.9,-3],[1.3,.25,.2],5)
    for i in range(6):
        x=-3.4+i*1.2;y=23.5-abs(i-2)*.25
        bone(m,'hair_'+str(i),'head',[x,y,0],[x-.9,14+(i%3),-.5 if i<2 else 1],[1.9,10-(i%3),3.2],9,[8+i*3,0,(-1 if i<3 else 1)*14])
        if i<4:m.box('hair_'+str(i),[x-.8,22,-3],[1.8,2.7,2],0,[0,0,12-i*7])
    for s,n in [(-1,'right'),(1,'left')]:
        bone(m,'arm_'+n,'body',[s*3,16,0],[s*4-1.3,10,-1.3],[2.6,6,2.6],0,[0,0,s*22])
        bone(m,'hand_'+n,'arm_'+n,[s*4,10,0],[s*4-1.7,7.5,-1.5],[3.4,3.2,3],2,[0,0,s*12])
    for i in range(7):
        a=i*2.4;x=math.cos(a)*(3+i%2*3);z=math.sin(a)*3;y=5+i*2.8
        bone(m,'bubble_'+str(i),'body',[x,y,z],[x-.55,y-.55,z-.55],[1.1,1.1,1.1],11,[20,i*23,25])
    return m

def harpy():
    m=Model('harpy');bone(m,'body','root',[0,16,0],[-3.2,13,-2],[6.4,9,4],0,[-9,0,0])
    m.box('body',[-2.7,17,-2.3],[5.4,4,1],8)
    bone(m,'head','body',[0,23,0],[-2.8,22,-2.6],[5.6,5.5,5.2],8);eyes(m,'head',1.25,24.7,-2.84,.85)
    m.box('head',[-.5,23.1,-3.1],[1,.55,.9],3)
    for i in range(5):bone(m,'crest_'+str(i),'head',[-2+i,26,1],[-2.5+i,25,1],[1.1,4+i%2,2.8],9,[-25-i*7,0,(i-2)*9])
    for s,n in [(-1,'right'),(1,'left')]:
        # The wing is the arm; no extra humanoid arms alongside it.
        bone(m,'wing_'+n,'body',[s*3,21,0],[s*3-1,17,-1],[2,5,2],8,[0,0,-s*50])
        bone(m,'wingtip_'+n,'wing_'+n,[s*6,17,0],[s*6-1,13,-.8],[2,5,1.6],0,[0,0,-s*34])
        for j in range(7):
            x=s*(4+j*.9)
            m.box('wingtip_'+n,[x-.6,9-j*.65,.2],[1.2,7+j*.45,1],1 if j%2 else 2,[0,0,-s*(14+j*5)])
        for j in range(5):m.box('wing_'+n,[s*(3.2+j*.8)-.8,15-j*.4,-1.2],[1.6,5,1],0,[0,0,-s*(12+j*5)])
        bone(m,'leg_'+n,'body',[s*1.7,14,0],[s*1.7-1,7,0],[2,7,2],0,[-18,0,0])
        bone(m,'talon_'+n,'leg_'+n,[s*1.7,7,1],[s*1.7-.65,2,1],[1.3,5,1.3],3,[24,0,0])
        for j in range(3):m.box('talon_'+n,[s*1.7-1+j*.7,.5,-2.5],[.45,1,4],5,[0,(j-1)*16,0])
    bone(m,'tail','body',[0,14,2])
    for j in range(5):m.box('tail',[-2.5+j,8,2],[1.2,8,1],2,[-30,0,(j-2)*13])
    m.box('body',[-3.3,14,-2.2],[6.6,1.1,4.4],10)
    return m

def reference_harpy_wings(m):
    """Original wing-only bird reference: overlapping tapered flight feathers.

    Broad shoulder coverts blend into layered secondaries and long, individually
    fanned three-stage primaries. The arm is the wing, with no extra human arms.
    """
    for side,n in ((-1,'right'),(1,'left')):
        wing='wing_'+n;tip='wingtip_'+n
        m.by_name[wing]['cubes']=m.by_name[wing]['cubes'][:1]
        m.by_name[tip]['cubes']=m.by_name[tip]['cubes'][:1]
        m.by_name[wing]['rotation']=[0,0,0]
        m.by_name[tip]['rotation']=[0,0,0]
        # Broad overlapping shoulder coverts avoid a skeletal arm attachment.
        for j in range(5):
            x=side*(3.3+j*.75)
            m.box(wing,[x-1.15,15.3-j*.38,-.3],[2.3,5.8-j*.3,1.2],2 if j%2 else 0,[0,0,side*(12+j*6)])
            m.box(wing,[x-.95,17.7-j*.36,-1],[1.9,3,.75],12 if j%2 else 2,[0,0,side*(10+j*5)])
        for j in range(4):
            x=side*(5.5+j*.8);y=15-j*.35;length=6.6+j*.65
            pivot=[x,y,0]
            m.box(tip,[x-1,y-length,.2],[2,length,1],2,[0,0,side*(18+j*8)],pivot)
            m.box(tip,[x-.65,y-length-1.2,.3],[1.3,1.8,.8],6,[0,0,side*(18+j*8)],pivot)
        # Long primaries fan outward, ending in stepped tapered tips rather than
        # a rectangular plate edge; each remains a substantial visible feather.
        for j in range(7):
            x=side*(7.1+j*.75);y=14.5-j*.26;length=9.2+(3-abs(3-j))*.8
            pivot=[x,y,0];angle=side*(30+j*6)
            mat=6 if j%3==0 else 2
            m.box(tip,[x-1,y-length*.64,.3],[2,length*.64,1],mat,[0,0,angle],pivot)
            m.box(tip,[x-.73,y-length*.9,.38],[1.46,length*.32,.84],mat,[0,0,angle],pivot)
            m.box(tip,[x-.4,y-length-1,.45],[.8,length*.17+.5,.7],2 if j%3==0 else 6,[0,0,angle],pivot)
            m.box(tip,[x-.9,y-3.1,-.5],[1.8,3.6,.65],12 if j%2 else 2,[0,0,angle],pivot)
    return m


def demon():
    m=Model('demon_sorceress');bone(m,'body','root',[0,17,0],[-2.6,13,-1.8],[5.2,10,3.6],13)
    m.box('body',[-3,18,-2],[6,4,4],0)
    bone(m,'head','body',[0,24,0],[-2.5,23,-2.4],[5,5.5,4.8],8);eyes(m,'head',1.15,25.4,-2.65,.8)
    m.box('head',[-.5,24,-2.6],[1,.23,.15],7)
    for i in range(5):bone(m,'hair_'+str(i),'head',[-2+i,27,1],[-2.6+i,17+i%2,1],[1.5,11-i%2,2.1],9,[7+i*3,0,(i-2)*6])
    for s,n in [(-1,'right'),(1,'left')]:
        bone(m,'horn_'+n,'head',[s*1.9,27,0])
        for j,(dx,y,ang) in enumerate([(0,27,-35),(1.3,29,-8),(1.4,31,32),(.5,32,65)]):
            m.box('horn_'+n,[s*(1.9+dx)-.55,y,-.2],[1.1 if j<2 else .7,2.8,1.1],1,[0,0,s*ang])
        bone(m,'earring_'+n,'head',[s*2.8,24.7,0],[s*2.8-.4,22.6,-.5],[.8,2.1,.3],3)
        m.box('earring_'+n,[s*2.8-.25,22.7,-.7],[.5,.8,.3],11)
        bone(m,'arm_'+n,'body',[s*3,22,0],[s*3-1,17,-1],[2,5,2],0,[0,0,s*15])
        bone(m,'hand_'+n,'arm_'+n,[s*3.7,17,0],[s*3.7-.8,13,-1],[1.6,4,2],8)
        for j in range(3):
            bone(m,'finger_'+n+'_'+str(j),'hand_'+n,[s*3.7-.5+j*.5,13,-.5],[s*3.7-.65+j*.5,11.6,-.65],[.3,1.5,.45],8,[j*14,0,0])
        bone(m,'sleeve_'+n,'arm_'+n,[s*3,20,0],[s*3-1.3,13,0],[2.6,7,2],13,[0,0,s*12])
        bone(m,'leg_'+n,'body',[s*1.3,13,0],[s*1.3-.8,1,-1],[1.6,12,2],1)
        # Split hem and offset inner lining prevent a solid rectangular robe.
        bone(m,'robe_'+n,'body',[s*2,14,0],[s*2-1.6,1,-1.8],[3.2,13,3.6],0,[0,0,-s*9])
        m.box('robe_'+n,[s*2-1.7,1,-2],[.45,13,.35],3)
        bone(m,'circle_'+n,'hand_'+n,[s*3.7,13,-3])
        for j in range(12):
            a=j*math.tau/12;x=s*3.7+math.cos(a)*3.5;y=13+math.sin(a)*3.5
            m.box('circle_'+n,[x-.8,y-.12,-3.1],[1.6,.24,.24],11,[0,0,j*30+90])
            if j%3==0:m.box('circle_'+n,[x-.22,y-.65,-3.15],[.44,1.3,.24],12,[0,0,j*30])
    m.box('body',[-2.9,13,-2.1],[5.8,1,4.2],3)
    m.box('body',[-.7,13,-2.6],[1.4,2,.5],12,[0,0,45])
    bone(m,'cape','body',[0,22,2],[-3.2,3,1.8],[6.4,19,1],13,[9,0,0])
    return m


def refine(m):
    """Original finishing pass; keep authored proportions, costume and joint names."""
    name=m.name
    if name=='frost_elemental':
        # Facet bevels bridge the shoulder/wrist intersections without filling the core.
        for side,n in ((-1,'right'),(1,'left')):
            m.box('arm_'+n,[side*7-2.2,25,-2.75],[4.4,2.2,5.5],2,[0,0,side*18])
            m.box('hand_'+n,[side*8-1.9,19,-2.8],[3.8,1.7,5.6],12,[0,0,-side*10])
            m.box('leg_'+n,[side*3-1.9,8,-2.3],[3.8,2.3,4.6],2,[0,0,side*9])
            m.box('head',[side*2.7- .4,30.7,-2.9],[.8,4.2,.65],0,[0,0,side*11])
        m.box('head',[-2.1,30,-2.85],[4.2,.8,.7],0)
    elif name=='moon_stag':
        # Keep the corrected vertical metatarsals and flat cloven soles.
        for side,n in ((-1,'right'),(1,'left')):
            for front in (True,False):
                leg=('front_' if front else 'rear_')+n; z=-5 if front else 5
                upper=m.by_name[leg];lower=m.by_name[leg+'_hock']
                upper.pop('rotation',None);lower.pop('rotation',None)
                # Organic bend is sculpted into the upper surface, never the sole.
                upper['cubes'][0]['size']=[2,7.4,2]
                # Isolate cloven hoof orientation from the bending hock.
                hoof=bone(m,leg+'_hoof',leg+'_hock',[side*2.7,2,z])
                m.by_name[hoof]['cubes']=lower['cubes'][1:]
                lower['cubes']=lower['cubes'][:1]
                m.box(leg,[side*2.7-1.15,7.3,z-1],[2.3,1.8,2.3],0)
            m.box('ear_'+n,[side*2.1-.6,25.6,-5.92],[1.2,2.6,.18],7)
            m.box('head',[side*1.8-.35,23.2,-8.2],[.7,1.5,.45],0,[0,0,side*18])
        # Under-jaw and throat taper; no changes above the y19.008 saddle seat.
        m.box('head',[-1.7,22.7,-9.8],[3.4,.7,3.2],2)
        m.box('neck',[-1.8,17,-7.3],[3.6,5,1.4],6,[-17,0,0])
    else:
        # Replace square luminous eyes with sclera, a narrower iris and tapered lash.
        head=m.by_name['head'];head['cubes']=head['cubes'][:1]+head['cubes'][7:]
        x,y,z,w={'slime_maiden':(1.25,20,-2.94,1.05),'harpy':(1.25,24.7,-2.84,.85),'demon_sorceress':(1.15,25.4,-2.65,.8)}[name]
        for side in (-1,1):
            center=side*x
            m.box('head',[center-w*.62,y-.08,z],[w*1.24,1.04,.18],5)
            m.box('head',[center-w*.5,y+.07,z-.12],[w,.78,.16],6)
            m.box('head',[center-w*.25,y+.08,z-.24],[w*.5,.76,.13],4)
            m.box('head',[center-.08,y+.56,z-.36],[.18,.2,.09],15)
            m.box('head',[center-w*.65,y+.92,z-.08],[w*1.3,.16,.2],5,[0,0,-side*7])
            m.box('head',[center-w*.45,y+1.45,z+.01],[w*.9,.14,.16],9,[0,0,-side*5])
        # A shallow tapered jaw reduces the hard square transition, same head envelope.
        skin=2 if name=='slime_maiden' else 8
        bottom={'slime_maiden':17.5,'harpy':22,'demon_sorceress':23}[name]
        cube=head['cubes'][0];cube['origin'][1]+=.45;cube['size'][1]-=.45
        m.box('head',[-1.95,bottom,-2.32],[3.9,.8,4.35],skin)
        if name=='slime_maiden':
            for side,n in ((-1,'right'),(1,'left')):
                m.box('hand_'+n,[side*4-1.2,7,-1.65],[2.4,1.8,3.3],0,[0,0,side*14])
                m.box('hair_'+('0' if side<0 else '5'),[side*2.55-.45,18,-2],[.9,4.8,1],9,[0,0,-side*9])
            # Reshape existing gel lobes rather than stacking dozens of extra cubes.
            for i in range(3):
                cube=m.by_name['gel_'+str(i)]['cubes'][0]
                cube['rotation']=[0,(i-1)*9,(i%3-1)*5]
        elif name=='harpy':
            for side,n in ((-1,'right'),(1,'left')):
                bone(m,'temple_'+n,'head',[side*2.1,26,0],[side*2.1-.55,22.4,-.7],[1.1,4.2,1.8],9,[0,0,-side*12])
                # Small coverts articulate the wing root; retain all long primaries.
                m.box('wing_'+n,[side*3-.9,18.5,-1.4],[1.8,3,.7],2,[0,0,-side*25])
                m.box('talon_'+n,[side*1.7-.3,1.1,2.1],[.6,1.1,2.2],5,[-22,0,0])
            m.box('body',[-2.7,20.6,-2.4],[5.4,.6,.6],10)
        else:
            for side,n in ((-1,'right'),(1,'left')):
                bone(m,'fringe_'+n,'head',[side*1.7,27.5,-1.5],[side*1.7-.65,25.7,-2.65],[1.3,2.3,.65],9,[0,0,-side*19])
                m.box('hand_'+n,[side*3.7-.9,13.8,-1.13],[1.8,.7,.25],3)
                m.box('sleeve_'+n,[side*3-1.4,13,-.1],[2.8,.65,2.2],3)
            m.box('body',[-1.4,20.8,-2.15],[2.8,.6,.4],3)
    return m


def refined_atlas(palette,materials,translucent=False):
    """Small original material finishing marks, authored without external pixels."""
    image=BASE_ATLAS(palette,materials,translucent);draw=ImageDraw.Draw(image)
    def color(index,delta=0,alpha=255):
        rgb=tuple(int(palette[index][i:i+2],16) for i in (0,2,4))
        return tuple(max(0,min(255,c+delta)) for c in rgb)+(alpha,)
    # Eye tile keeps the established hue and adds a dark pupil/high catch light.
    draw.ellipse((6,34,25,61),fill=color(4,-12))
    draw.ellipse((11,36,20,60),fill=color(4,12))
    draw.ellipse((14,39,18,57),fill=color(5))
    draw.rectangle((10,36,13,40),fill=color(15))
    # Hair strands and cloth seams remain subtle at the original 128px resolution.
    for index,role in enumerate(materials):
        if role not in ('hair','cloth','feather','slime','fur'):continue
        x,y=index%4*32,index//4*32
        alpha=202 if translucent else 255
        for dx in (10,23):
            draw.line([(x+dx,y+6),(x+dx-1,y+14),(x+dx+1,y+23)],fill=color(index,9,alpha),width=1)
    return image

BASE_ATLAS=asset_pipeline.material_atlas

def motion(m):
    name=m.name;t=SIZES[name][2];B=m.by_name
    def c(length,b,loop=False):return clip(length,b,loop=loop)
    def wave(v=(0,0,0),half=(0,0,0),length=2):
        return {str(round(length*i/8,6)):[a+(b-a)*(1-math.cos(math.tau*i/8))/2 for a,b in zip(v,half)] for i in range(9)}
    idle={'body':{'rotation':wave((0,0,-1),(0,0,1))},'head':{'rotation':wave((0,-4,0),(2,4,0))}}
    for n in B:
        if n.startswith(('hair_','robe_','sleeve_','tail','crest_','earring_','temple_','fringe_')):idle[n]={'rotation':wave((-3,0,-2),(4,0,2))}
        if n=='nova':idle[n]={'scale':{'0':[.01,.01,.01]}}
        if n.startswith('circle_'):idle[n]={'scale':{'0':[.015,.015,.015]}}
        if n.startswith(('orbit_','bubble_')):idle[n]={'position':wave((0,-.45,0),(0,.45,0)),'rotation':wave((0,0,-8),(0,18,8))}
    if name=='moon_stag':idle['body']={'rotation':{'0':[0,0,0]}}
    if name=='slime_maiden':
        idle['body']['scale']=wave((1.035,.96,1.035),(.97,1.035,.97))
        for i in range(5):
            idle['gel_'+str(i)]={'scale':{str(round(j/4,6)):[1+.02*math.cos(math.tau*j/8-i*.4),1-.035*math.cos(math.tau*j/8-i*.4),1+.02*math.cos(math.tau*j/8-i*.4)] for j in range(9)}}
    a={'idle':c(2,idle,True)}
    for run in (False,True):
        length=.65 if run else 1.1; b={'body':{'position':wave((0,0,0),(0,1.1 if run else .4,0),length)}}
        for n in B:
            if n.startswith(('leg_','front_','rear_')) and not n.endswith('_hock'):
                sign=-1 if 'left' in n else 1
                if n.startswith('rear_'):sign=-sign
                b[n]={'rotation':wave((sign*(32 if run else 20),0,0),(-sign*(32 if run else 20),0,0),length)}
        if name=='slime_maiden':b['body']['scale']=wave((1.1,.9,1.1),(.91,1.12,.91),length)
        for n in B:
            if n.startswith(('hair_','robe_','tail','sleeve_','crest_','temple_','fringe_')):b[n]={'rotation':wave((-8,0,-4),(10,0,4),length)}
        for n in B:
            if n=='nova':b[n]={'scale':{'0':[.01,.01,.01]}}
            if n.startswith('circle_'):b[n]={'scale':{'0':[.015,.015,.015]}}
        a['run' if run else 'walk']=c(length,b,True)
    attack={'body':{'rotation':keys(t,(-10,0,-5),(18,0,5))},'head':{'rotation':keys(t,(-12,0,0),(15,0,0))}}
    if name=='moon_stag':attack['neck']={'rotation':keys(t,(-23,0,0),(40,0,0))}
    for n in ('arm_left','arm_right','wing_left','wing_right'):
        if n in B:attack[n]={'rotation':keys(t,(-60,0,(-25 if 'left' in n else 25)),(55,0,0))}
    if 'nova' in B:attack['nova']={'scale':{'0':[.01,.01,.01]}}
    a['attack']=c(t+.5,attack);a['heavy']=c(t+.65,{**attack,'body':{'rotation':keys(t,(-17,0,0),(26,0,0),recovery=.55)}})
    cast={'body':{'rotation':keys(t,(-5,0,0),(5,0,0))}}
    for n in ('arm_left','arm_right','hand_left','hand_right','wing_left','wing_right'):
        if n in B:cast[n]={'rotation':keys(t,(-50,0,20 if 'left' in n else -20),(-80,0,15 if 'left' in n else -15))}
    for n in B:
        if n.startswith('circle_'):cast[n]={'rotation':{'0':[0,0,0],str(t):[0,0,180],str(t+.5):[0,0,360]},'scale':{'0':[.03,.03,.03],str(t*.55):[1,1,1],str(t):[1.15,1.15,1.15],str(t+.5):[.03,.03,.03]}}
        if n.startswith('finger_'):cast[n]={'rotation':keys(t,(30,0,0),(-18,0,0))}
    if 'nova' in B:
        cast['nova']={'scale':{'0':[.01,.01,.01],str(round(t-.12,4)):[.01,.01,.01],str(t):[1,1,1],str(round(t+.3,4)):[.01,.01,.01]},'position':{'0':[0,-5,0],str(round(t-.12,4)):[0,-5,0],str(t):[0,0,0],str(round(t+.3,4)):[0,-5,0]}}
    a['cast']=c(t+.5,cast)
    a['hurt']=c(.45,{'body':{'rotation':{'0':[0,0,0],'.12':[-12,0,8],'.45':[0,0,0]}}})
    a['death']=c(1.4,{'root':{'rotation':{'0':[0,0,0],'.7':[0,0,68],'1.4':[0,0,88]},'position':{'0':[0,0,0],'1.4':[0,-3,0]}}})
    if name=='moon_stag':
        sit={'body':{'position':{'0':[0,-7,0]}},'neck':{'rotation':{'0':[-12,0,0]}}}
        for n in B:
            if n.startswith(('front_','rear_')):sit[n]={'rotation':{'0':[5 if n.endswith('_hoof') else 70 if n.endswith('_hock') else -75,0,0]}}
        a['sit']=c(2,sit,True);a['tame']=c(1.2,{'head':{'rotation':wave((0,0,-8),(0,0,8),1.2)}});a['ride']=a['run']
        # Stance/swing inverse kinematics: two planted diagonal hooves at all times.
        for state in ('walk','run'):
            animation=a[state];L=animation['animation_length'];b=animation['bones']
            b['body']={'position':{'0':[0,-.8,0]}}
            for side in ('right','left'):
                for front in (True,False):
                    leg=('front_' if front else 'rear_')+side
                    phase=0 if (front==(side=='right')) else .5
                    hip={};knee={};hoof={}
                    for frame in range(65):
                        u=frame/64;f=(u+phase)%1;stride=2.4 if state=='run' else 1.8
                        dz=stride*(1-4*f) if f<.5 else stride*(-1+4*(f-.5))
                        lift=0 if f<=.5 else (1.1 if state=='run' else .6)*math.sin(math.tau*(f-.5))**2
                        dy=12.2-lift;d=math.hypot(dy,dz)
                        h=math.atan2(-dz,dy)-math.acos(max(-1,min(1,(49+d*d-36)/(14*d))))
                        k=math.acos(max(-1,min(1,(d*d-49-36)/84)))
                        time=str(round(L*u,6));hip[time]=[math.degrees(h),0,0];knee[time]=[math.degrees(k),0,0];hoof[time]=[-math.degrees(h+k),0,0]
                    b[leg]={'rotation':hip};b[leg+'_hock']={'rotation':knee};b[leg+'_hoof']={'rotation':hoof}
        a['ride']=a['run']
        a['jump']=c(.8,{'body':{'rotation':wave((-12,0,0),(15,0,0),.8),'position':wave((0,0,0),(0,2,0),.8)}})
    if name=='harpy':
        for state,L,amp in [('fly',.55,62),('hover',.9,42)]:
            b={'body':{'rotation':wave((12,0,0),(18,0,0),L)}}
            for n in ('left','right'):
                s=1 if n=='left' else -1
                b['wing_'+n]={'rotation':wave((0,0,s*amp),(0,0,-s*amp),L)}
                b['wingtip_'+n]={'rotation':wave((0,0,s*25),(0,0,-s*40),L)}
                b['talon_'+n]={'rotation':wave((35,0,0),(40,0,0),L)}
            a[state]=c(L,b,True)
        a['swoop']=c(t+.5,{**attack,'body':{'rotation':keys(t,(-25,0,0),(65,0,0))}})
    if name=='demon_sorceress':
        a['levitate']=c(2,{**idle,'root':{'position':wave((0,1,0),(0,2.3,0))}},True)
        a['teleport']=c(1.1,{'root':{'scale':{'0':[1,1,1],'.4':[.15,1.3,.15],'.55':[.05,.05,.05],'1.1':[1,1,1]}}})
    return a


def full_hair(m, top, width, depth, bottom, material):
    """A continuous scalp cap with overlapping rear and temple locks."""
    m.box('head',[-width/2,top-1.25,-depth/2],[width,1.65,depth],material)
    m.box('head',[-width/2+.45,top+.35,-depth/2+.35],[width-.9,.55,depth-.7],material)
    for i in range(7):
        x=(i-3)*width/7; y=bottom+(abs(i-3)%3)*.65
        n='v2_hair_'+str(i)
        bone(m,n,'head',[x,top-.35,depth/2-1],[x-width/12,y,depth/2-1.35],[width/6+.3,top-y,1.8],material,[5,0,(i-3)*2])
    for side in (-1,1):
        n='v2_hair_temple_'+str(side)
        bone(m,n,'head',[side*(width/2-.5),top-.5,-.8],[side*(width/2-.5)-.65,bottom+1,-1.9],[1.3,top-bottom-1,1.7],material,[0,0,-side*5])
        m.box('head',[side*.4-.95,top-2.5,-depth/2-.15],[1.9,2,1],material,[0,0,-side*16])


def v2_sculpt(m):
    """V2 adult silhouettes, continuous materials and species-specific anatomy."""
    if m.name=='frost_elemental':
        # Preserve the rig but replace the separated golem blocks with a continuous
        # faceted feminine ice body; the rune core is embedded in the sternum.
        for n in ('body','torso_shard_0','torso_shard_1','torso_shard_2','head'):
            m.by_name[n]['cubes']=[]
        for o,s,mat in [([-3.5,15,-2.3],[7,5,4.6],0),([-2.6,19,-2],[5.2,5.5,4],2),([-4.2,24,-2.3],[8.4,5,4.6],0),([-2.4,28,-1.8],[4.8,3,3.6],2)]:
            m.box('body',o,s,mat)
        for side,n in ((-1,'right'),(1,'left')):
            m.box('body',[side*1.8-1.9,24,-3.3],[3.8,3.5,2.7],2,[0,side*8,-side*8])
            m.box('body',[side*2.5-1.5,15,-2.6],[3,4,5.2],2,[0,0,-side*10])
            # Connected shoulders and slender crystalline forearms.
            m.by_name['arm_'+n]['pivot']=[side*4,27.5,0]
            m.by_name['arm_'+n]['cubes']=[]
            m.box('arm_'+n,[side*4.6-1.6,21.5,-1.7],[3.2,7,3.4],0)
            m.box('arm_'+n,[side*4.6-1.9,25.5,-2],[3.8,3.5,4],2,[0,0,side*12])
            m.by_name['hand_'+n]['pivot']=[side*4.8,21.5,0]
            m.by_name['hand_'+n]['cubes']=[]
            m.box('hand_'+n,[side*4.8-1.3,16,-1.6],[2.6,5.8,3.2],2)
            for j in range(2):m.box('hand_'+n,[side*4.8-1+j*1.05,14.4,-1.5],[.9,2.4,2],12,[0,0,side*8])
        m.by_name['core']['cubes']=[]
        m.box('core',[-.85,25.8,-3.6],[1.7,1.7,.7],11,[0,0,45])
        m.box('head',[-2.6,30,-2.3],[5.2,5.4,4.6],0)
        m.box('head',[-1.9,29.6,-2],[3.8,1.2,3.8],2)
        # An inset single angular aurora slit and split ice mask, no human eyes/nose/mouth.
        m.box('head',[-2.3,32,-2.5],[4.6,1.2,.5],5)
        for side in (-1,1):
            m.box('head',[side*1.05-.9,32.25,-2.8],[1.8,.35,.4],11,[0,0,-side*18])
            m.box('head',[side*1.8-.55,30.3,-2.65],[1.1,2.4,.6],2,[0,0,-side*20])
        full_hair(m,35.8,6.1,5.4,23,12)
    elif m.name=='moon_stag':
        # Do not change the seat, hips, hocks, hooves or numerical gait solver.
        m.box('body',[-4.25,12.8,-6.4],[8.5,5.2,6.3],0)
        m.box('body',[-3.8,12.4,2.3],[7.6,5.2,5.6],2)
        m.box('neck',[-2.9,16.3,-7.3],[5.8,7,4.5],0,[-12,0,0])
        m.box('neck',[-2.1,15.7,-8.2],[4.2,5.3,2.2],6,[-18,0,0])
        for side,n in ((-1,'right'),(1,'left')):
            ant='antler_'+n;m.by_name[ant]['cubes']=[]
            # User-supplied Megaloceros image: low sweeping lateral beams and
            # broad flattened paddles, with long tines around the distal edge.
            for j in range(5):
                x=side*(3+j*3.4);y=27.2+j*.42
                m.box(ant,[x-2.5,y,-5.7-j*.15],[5,1.9,1.9],3,[0,0,-side*6])
            for j in range(4):
                x=side*(14+j*4.8);y=28.3+j*.35
                m.box(ant,[x-3.6,y,-6.3-j*.3],[7.2,4.5-j*.35,1.6],3,[0,0,-side*5])
                # Outer-edge tines curve up from the continuous palmate web.
                m.box(ant,[x-.7,y+3.2,-6.25-j*.3],[1.4,4.4-j*.3,1.3],6,[0,0,-side*(14+j*8)])
                m.box(ant,[x+side*1.15-.45,y+6.2-j*.3,-6.2-j*.3],[.9,2.4,1],6,[0,0,side*14])
                if j%2==0:
                    m.box(ant,[x-.85,y+.9,-6.7-j*.3],[1.7,2.6,2],11,[0,0,-side*14])
                    m.box(ant,[x-.5,y+3.1,-6.5-j*.3],[1,1.5,1.5],4,[0,0,-side*14])
            m.box(ant,[side*5-.6,28,-7.6],[1.2,3.8,1.3],6,[-35,0,-side*45])
    else:
        if m.name=='slime_maiden':
            # Waist is narrow, upper gel lobes form an opaque-looking modest bodice
            # in the same translucent material as the rest of the continuous body.
            m.by_name['gel_3']['cubes'][0].update(origin=[-2.7,9,-2.6],size=[5.4,5,5.2])
            m.by_name['gel_4']['cubes'][0].update(origin=[-3.4,13,-2.6],size=[6.8,4.7,5.2])
            for side in (-1,1):m.box('gel_4',[side*1.6-1.65,13.7,-3.4],[3.3,2.9,2.5],2,[0,side*7,-side*7])
            full_hair(m,23.7,6.7,5.9,12.2,9)
        elif m.name=='harpy':
            # Adult, fully clothed torso with defined waist and feather bodice.
            m.by_name['body']['cubes']=[]
            for o,s,mat in [([-2.6,13,-2],[5.2,3.5,4],13),([-2.1,16,-1.8],[4.2,3.2,3.6],10),([-3,19,-2],[6,3,4],13)]:m.box('body',o,s,mat)
            for side in (-1,1):m.box('body',[side*1.4-1.5,18.8,-2.8],[3,2.8,2.1],0,[0,side*8,-side*7])
            m.box('body',[-2.5,20.7,-2.5],[5,1,.7],6)
            # Retain crest bones as embedded rear locks rather than erect spikes.
            for i in range(5):
                m.by_name['crest_'+str(i)]['rotation']=[6,0,(i-2)*3]
                m.by_name['crest_'+str(i)]['cubes']=[]
                m.box('crest_'+str(i),[-2.5+i,18.5,1.8],[1.2,8.4,1.2],9)
            full_hair(m,27.8,6.1,5.7,17,9)
        else:
            m.by_name['body']['cubes']=[]
            for o,s,mat in [([-2.8,12.8,-1.9],[5.6,3.6,3.8],13),([-2,16,-1.65],[4,3.6,3.3],0),([-3,19.2,-1.9],[6,3.8,3.8],13)]:m.box('body',o,s,mat)
            for side in (-1,1):
                m.box('body',[side*1.35-1.45,19,-2.8],[2.9,3,2],0,[0,side*9,-side*8])
                m.box('body',[side*1.8-.4,16,-2],[.8,5.2,.45],3,[0,0,-side*8])
            m.box('body',[-2.4,14.6,-2.05],[4.8,.8,4.1],3)
            m.box('body',[-.6,14.7,-2.6],[1.2,1.4,.65],12,[0,0,45])
            full_hair(m,28.6,5.9,5.3,16,9)
    return m


def grounded_harpy_death(m):
    """Support the rolling corpse on its complete rotated silhouette.

    Model coordinates use Y up. Apply cube-local rotation, then every rest
    bone from child to root; the body has an authored -9 degree X tilt.
    Sample tightly so linear channel interpolation keeps the floor envelope.
    """
    def rotate(point, pivot, angles):
        x,y,z=[point[i]-pivot[i] for i in range(3)]
        for axis,angle in enumerate(angles):
            c=math.cos(math.radians(angle));s=math.sin(math.radians(angle))
            if axis==0:y,z=y*c-z*s,y*s+z*c
            elif axis==1:x,z=x*c+z*s,-x*s+z*c
            else:x,y=x*c-y*s,x*s+y*c
        return [x+pivot[0],y+pivot[1],z+pivot[2]]
    folded={}
    for side,n in ((-1,'right'),(1,'left')):
        folded['wing_'+n]=[4,side*8,-side*54]
        folded['wingtip_'+n]=[0,-side*8,side*12]
    points=[]
    for b in m.bones:
        for cube in b.get('cubes',[]):
            for bits in range(8):
                point=[cube['origin'][a]+(cube['size'][a] if bits&(1<<a) else 0) for a in range(3)]
                point=rotate(point,cube.get('pivot',b['pivot']),cube.get('rotation',[0,0,0]))
                cursor=b
                while cursor['name']!='root':
                    point=rotate(point,cursor['pivot'],folded.get(cursor['name'],cursor.get('rotation',[0,0,0])))
                    cursor=m.by_name[cursor['parent']]
                points.append(point)
    frames={};L=.65
    for i in range(129):
        u=i/128
        # Same two-stage angular collapse as the original normalized clip.
        angle=136*u if u<=.5 else 68+40*(u-.5)
        minimum=min(rotate(point,[0,0,0],[0,0,angle])[1] for point in points)
        # 0.08px tolerance covers the chord between the densely sampled supports.
        frames[str(round(L*u,6))]=[0,max(0,.08-minimum),0]
    bones={n:{'rotation':{'0':angles}} for n,angles in folded.items()}
    bones['root']={'rotation':{'0':[0,0,0],'.325':[0,0,68],'.65':[0,0,88]},'position':frames}
    return clip(L,bones)


def v2_motion(m, animations):
    """Keep combat landmarks and clip lengths; add overlapping secondary action."""
    t=SIZES[m.name][2]
    for state,a in animations.items():
        L=a['animation_length'];b=a['bones']
        looping=a.get('loop',False)
        for i,n in enumerate(n for n in m.by_name if n.startswith('v2_hair_')):
            if looping:
                b[n]={'rotation':{str(round(L*j/8,6)):[3*math.sin(math.tau*j/8-i*.3),2*math.sin(math.tau*j/8-i*.3),1.5*math.sin(math.tau*j/8-i*.3)] for j in range(9)}}
            elif state in ('attack','heavy','cast','swoop'):
                b[n]={'rotation':keys(t,(8,0,2),(-7,0,-2),recovery=min(.3,L-t))}
        if m.name=='moon_stag':
            # Stable antlers remain wholly rigid to head; no oscillating crystals.
            if state in ('walk','run','ride'):
                b['neck']={'rotation':{'0':[-1.2,0,0],str(L/2):[1.2,0,0],str(L):[-1.2,0,0]}}
                b['head']={'rotation':{'0':[1.2,0,0],str(L/2):[-1.2,0,0],str(L):[1.2,0,0]}}
            elif state=='idle':b['neck']={'rotation':{'0':[-1,0,-.5],'1':[1,0,.5],'2':[-1,0,-.5]}}
        if m.name=='harpy':
            for side,n in ((-1,'right'),(1,'left')):
                if state in ('idle','walk','run'):
                    b['wing_'+n]={'rotation':{'0':[4,side*8,-side*54],str(L/2):[6,side*10,-side*51],str(L):[4,side*8,-side*54]}}
                    b['wingtip_'+n]={'rotation':{'0':[0,-side*8,side*12],str(L/2):[3,-side*10,side*15],str(L):[0,-side*8,side*12]}}
                elif state in ('fly','hover'):
                    b['wingtip_'+n]={'rotation':{str(round(L*j/8,6)):[8*math.sin(math.tau*j/8-.6),side*8,side*32*math.cos(math.tau*j/8-.6)] for j in range(9)}}
                elif state in ('attack','heavy','swoop'):
                    b['wingtip_'+n]={'rotation':keys(t,(0,side*15,side*45),(12,-side*12,-side*32))}
        if m.name in ('frost_elemental','demon_sorceress') and state in ('cast','attack','heavy'):
            for side,n in ((-1,'right'),(1,'left')):
                b['hand_'+n]={'rotation':keys(t,(-15,side*18,side*8),(-35,-side*22,-side*12))}
            b['body']['rotation']=keys(t,(-7,-8,-3),(5,9,3))
        if m.name=='slime_maiden' and state in ('walk','run','cast','attack','heavy'):
            for i in range(5):
                n='gel_'+str(i)
                if looping:b[n]={'scale':{str(round(L*j/8,6)):[1+.035*math.sin(math.tau*j/8-i*.5),1-.05*math.sin(math.tau*j/8-i*.5),1+.035*math.sin(math.tau*j/8-i*.5)] for j in range(9)}}
                else:b[n]={'scale':keys(t,(1.04,.94,1.04),(.96,1.06,.96),final=(1,1,1),start=(1,1,1))}
    if m.name=='harpy':animations['death']=grounded_harpy_death(m)
    return animations


def main():
    asset_pipeline.material_atlas=refined_atlas
    for maker in (frost,stag,slime,harpy,demon):
        m=refine(maker())
        if m.name=='harpy': m=reference_harpy_wings(m)
        m=v2_sculpt(m)
        p=PALETTES[m.name];w,h,_=SIZES[m.name]
        material=['ice','stone','ice','bone','glow','stone','bone','ice','ice','stone','stone','rune','ice','stone','stone','ice'] if m.name=='frost_elemental' else (['slime']*16 if m.name=='slime_maiden' else ['fur','fur','fur','bone','glow','stone','bone','fur','fur','fur','leather','rune','rune','cloth','stone','bone'] if m.name=='moon_stag' else ['feather','feather','feather','bone','glow','bone','bone','feather','skin','feather','leather','rune','feather','cloth','stone','bone'] if m.name=='harpy' else ['cloth','bone','cloth','metal','glow','stone','bone','cloth','skin','fur','leather','rune','rune','cloth','metal','bone'])
        if m.name=='demon_sorceress':material[9]='hair'
        if m.name=='slime_maiden':
            material[4]='glow';material[11]='rune';material[15]='glow'
        variants=None
        if m.name=='moon_stag':
            v=list(p);v[10]='806444';v[13]='3d6579';variants={'_tamed':v}
        write_creature(m,p,material,v2_motion(m,motion(m)),w,h,glow=(4,11,12) if m.name=='demon_sorceress' else (4,11),variants=variants,translucent=m.name=='slime_maiden')

if __name__=='__main__':main()
