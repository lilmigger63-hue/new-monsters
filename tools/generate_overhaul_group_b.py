#!/usr/bin/env python3
"""Original sculptural woodland beasts; reference analysis in REFERENCE_ATLAS.md."""
from overhaul_asset_pipeline import Model, clip, keys, write_creature

MATERIALS=['bark','bark','bone','moss','glow','skin','feather','leather','iron','cloth','fur','fur','rune','bone','skin','moss']
PALETTES={
'ancient_treant':['49372b','2c2921','917752','405037','e2be65','665740','657449','5b4631','77776a','364331','544638','8d7853','a9ce72','b7a784','332d25','6a7748'],
'forest_dryad':['edd9c4','25412b','d9e4c3','397d34','b9ed82','f5e3d0','428a36','376231','9fb878','2e682a','568c40','75a855','d5eaa0','f5eedc','b18a76','709e43'],
'griffin':['8e6a41','55442e','d1c6a5','65624b','d1ad55','303439','b9ad8f','4b3429','8c805c','6b4634','92744c','62543c','c5ae71','dfc795','6e634b','84795b'],
'dire_wolf':['646d70','363e43','c1c0ac','626c62','b8ceb3','242b2d','939b96','4a3530','8b8a76','713c36','778184','a0a69f','b1baa5','c6bd9d','474b48','6d7770'],
'wild_wyvern':['4b6150','2a3d38','b9ac80','475c3f','d0de81','292d2c','6d574c','45372e','8a876b','664a3b','536b5a','849071','a8c173','d0c49d','303f38','687253']}
WIND={'ancient_treant':1.2,'forest_dryad':.8,'griffin':.6,'dire_wolf':.35,'wild_wyvern':1.0}
DIMS={'ancient_treant':(1.8,4.6),'forest_dryad':(.65,1.9),'griffin':(1.4,1.8),'dire_wolf':(1.05,1.35),'wild_wyvern':(1.6,2.1)}

def bone(m,n,p,v,r=None):
    m.bone(n,p,v,rotation=r);return n

def box(m,n,o,s,mat=0,r=None):m.box(n,o,s,material=mat,rotation=r)

def tapered(m,n,o,s,mat=0,r=None):
    box(m,n,o,s,mat,r)
    box(m,n,[o[0]+s[0]*.15,o[1]+s[1]*.8,o[2]+s[2]*.15],[s[0]*.7,s[1]*.5,s[2]*.7],mat,r)

def woodland(name):
    m=Model(name);tree=name=='ancient_treant'
    hips=23 if tree else 12;chest=49 if tree else 21
    bone(m,'body','root',[0,hips,0])
    if tree:
        box(m,'body',[-4,23,-4],[8,12,8],0,[0,12,7])
        box(m,'body',[-6,33,-4.5],[12,14,9],0,[0,-9,-6])
        box(m,'body',[-7,45,-5],[14,9,10],0,[0,7,3])
        for side in [-1,1]:
            box(m,'body',[side*5-1.5,25,-4],[3,23,3],1,[0,side*10,-side*15])
            box(m,'body',[side*6-2,44,-2],[4,10,6],0,[0,0,-side*32])
    else:
        box(m,'body',[-2,12,-1.5],[4,4,3],0)
        box(m,'body',[-1.7,16,-1.4],[3.4,3,2.8],0)
        box(m,'body',[-2.6,19,-1.8],[5.2,3.5,3.6],0)
    # Rib-like overlapping trunk facets leave a dark central hollow.
    for side in [-1,1]:
        box(m,'body',[side*(3 if tree else 1.1)-(2 if tree else .6),hips+3,-6 if tree else -2.1],[2.4 if tree else 1.2,25 if tree else 7,2 if tree else .7],2,[0,0,side*9])
    bone(m,'head','body',[0,chest+3,0]);box(m,'head',[-6 if tree else -3,chest+2,-5 if tree else -2.8],[12 if tree else 6,12 if tree else 7,9 if tree else 5],0 if tree else 5)
    for side in [-1,1]:
        box(m,'head',[side*(3 if tree else 1.6)-(1.1 if tree else .5),chest+8 if tree else 25,-5.5 if tree else -3],[2.2 if tree else 1,1.4 if tree else .7,.6],4)
        box(m,'head',[side*(3 if tree else 1.8)-2 if tree else side*1.8-.9,chest+10 if tree else 26,-5.6 if tree else -3],[4 if tree else 1.8,1 if tree else .5,1],1,[0,0,side*12])
        leg='leg_'+('left' if side>0 else 'right');bone(m,leg,'root',[side*(4.5 if tree else 1.5),hips,0])
        if tree:
            box(m,leg,[side*4.5-2.5,12,-2.7],[5,11,5.4],0,[0,side*18,side*13])
            box(m,leg,[side*5-2,2,-2.1],[4,12,4.2],1,[0,-side*20,-side*9])
            box(m,leg,[side*4.5-.8,2,-3],[1.6,15,1.7],0,[0,side*15,side*7])
        else:box(m,leg,[side*1.5-1,2,-1.3],[2,hips-2,2.6],0,[0,0,side*6])
        for j in range(3 if tree else 1):
            box(m,leg,[side*(4.5 if tree else 1.5)-3+j*2 if tree else side*1.5-1,0,-8+j if tree else -2.6],[2 if tree else 2,3 if tree else 1.5,11-j*2 if tree else 4],1,[0,side*(j-1)*20,0])
        arm='arm_'+('left' if side>0 else 'right');sx=side*(9 if tree else 3.5)
        bone(m,arm,'body',[sx,chest,0]);box(m,arm,[sx-(2.5 if tree else 1),chest-(14 if tree else 7),-2],[5 if tree else 2,15 if tree else 7,4 if tree else 2.6],0,[0,0,side*12])
        fore='fore_'+('left' if side>0 else 'right');bone(m,fore,arm,[sx,chest-(13 if tree else 6),0]);box(m,fore,[sx-2 if tree else sx-.8,chest-(26 if tree else 12),-2],[4 if tree else 1.6,13 if tree else 6,4 if tree else 2],0,[0,0,-side*10])
        for j in range(3):
            finger=f'finger_{side}_{j}';bone(m,finger,fore,[sx-1.5+j*1.5 if tree else sx-.6+j*.6,chest-(25 if tree else 11),-1])
            box(m,finger,[sx-1.5+j*1.5 if tree else sx-.6+j*.6,chest-(32 if tree else 13.5),-1.5],[1 if tree else .4,7 if tree else 2.5,1.6 if tree else .6],1,[8+j*9,0,side*8])
        crown='crown_'+('left' if side>0 else 'right');bone(m,crown,'head',[side*3,chest+(12 if tree else 8),0])
        for j in range(3):
            box(m,crown,[side*(3+j*(3 if tree else 1.1))-.7,chest+(12 if tree else 7)+j*(3 if tree else .6),0],[2 if tree else .9,9-j if tree else 2-j*.3,2 if tree else .9],1,[0,0,-side*(22+j*12)])
        if tree:
            for j in range(3):
                box(m,crown,[side*(5+j*3)-1,chest+17+j*2,0],[2,5,2],1,[0,0,-side*(40+j*9)])
                box(m,crown,[side*(6+j*3)-2,chest+18+j*2,1],[4,2,4],3)
            for j in range(4):
                box(m,'body',[side*(6+j%2*2),30+j*6,2],[4,2,5-j*.6],3)
                box(m,'body',[side*7,38+j*4,-4],[3,1,4],13)
        else:
            for j in range(4):
                panel=f'vine_{side}_{j}';bone(m,panel,'body',[side*(2.3+j*.25),19,1.5])
                box(m,panel,[side*(2.3+j*.25)-.5,4+j*.7,1.5+j*.35],[1,15-j*.7,1],3,[0,0,side*(9+j*5)])
                for k in range(3):box(m,panel,[side*(2.3+j*.25)-1,7+k*3,1.2+j*.35],[2.2,2.5,.6],6,[0,0,side*27])
    if tree:
        for j in range(5):box(m,'head',[-4+j*2,45-j%2*3,-5.5],[1.3,13-j%3*2,2],1,[0,0,(j-2)*7])
        for j in range(6):box(m,'body',[-7+j*2.4,50+j%2*2,2],[3,2,5],3)
    else:
        box(m,'head',[-3.3,23,1],[6.6,6,2],3)
        for j in range(5):box(m,'head',[-3+j*1.3,26+j%2*.5,2],[1.4,3,1],6,[10,0,(j-2)*10])
        box(m,'body',[-.8,19,-2.5],[1.6,2,.7],12)
        for side in [-1,1]:
            panel='vine_front_'+str(side);bone(m,panel,'body',[side*1.5,14,-2])
            for j in range(3):box(m,panel,[side*(1.4+j*.2)-1.2,6+j*2.2,-2.3],[2.4,4,.7],3 if j%2 else 6,[0,0,-side*18])
    return m

def beasts(name):
    m=Model(name);wolf=name=='dire_wolf';wyv=name=='wild_wyvern'
    y=13 if wolf else 17 if wyv else 16
    bone(m,'body','root',[0,y,0]);box(m,'body',[-4.5 if wolf else -6,y-4,-7],[9 if wolf else 12,6 if wolf else 9 if wyv else 6.5,18 if wolf else 22],10 if wolf else 0)
    box(m,'body',[-3.5 if wolf else -5,y-4,-8],[7 if wolf else 10,7 if wolf else 10,8],11 if wolf else 2)
    if wyv:
        bone(m,'neck','body',[0,22,-7]);box(m,'neck',[-3,21,-13],[6,9,7],0,[28,0,0]);box(m,'neck',[-2.5,26,-18],[5,5,8],0,[10,0,0]);hp=[0,29,-17]
    else:hp=[0,y+4,-8]
    bone(m,'head','neck' if wyv else 'body',hp);hy=hp[1]
    box(m,'head',[-3.5,hy-2,-15 if not wyv else -23],[7,6,8],10 if wolf else 0 if wyv else 6)
    snout=-20 if wolf else -28 if wyv else -20
    box(m,'head',[-2.6,hy-3,snout],[5.2,3.4,7],11 if wolf else 1 if wyv else 13)
    box(m,'head',[-2,hy-2.5,snout-.4],[4,1.8,.7],5 if wolf else 13)
    bone(m,'jaw','head',[0,hy-2,-12 if not wyv else -21]);box(m,'jaw',[-2.5,hy-4,snout+.6],[5,1.3,7],1 if wyv else 11 if wolf else 13)
    for s in [-1,1]:
        box(m,'head',[s*2.8-.7,hy+1,-15.3 if not wyv else -23.3],[1.4,1,.6],4)
        box(m,'head',[s*2.7-1,hy+2,-15.3 if not wyv else -23.3],[2,.7,2],1,[0,0,s*12])
        if wolf:
            bone(m,'ear_'+str(s),'head',[s*2.6,hy+3,-10]);box(m,'ear_'+str(s),[s*2.6-1,hy+3,-11],[2,4,2],1,[0,0,-s*14]);box(m,'ear_'+str(s),[s*2.6-.5,hy+4,-11.2],[1,2,.5],9)
        elif wyv:box(m,'head',[s*3-.7,hy+2,-20],[1.4,6,2],13,[30,0,-s*22])
        else:
            for j in range(3):box(m,'head',[s*(2+j*.5)-1,hy-4-j,-10+j],[2,5,2],6,[15,0,s*(20+j*9)])
        for j in range(3):box(m,'jaw',[s*1.9-.3,hy-3.5,snout+1+j*1.5],[.6,1.4,.7],13)
    for front in ([False] if wyv else [True,False]):
        for s in [-1,1]:
            n=('arm_' if front else 'leg_')+('left' if s>0 else 'right');x=s*(3.2 if wolf else 4.5);z=-5 if front else 9
            bone(m,n,'body',[x,y-1,z]);box(m,n,[x-1.5,y-7,z-1.5],[3,7,4],10 if wolf else 6 if front else 0,[18 if front else -25,0,0])
            lower=n+'_lower';bone(m,lower,n,[x,y-7,z+(-1 if front else 2)]);box(m,lower,[x-1,2,z+(0 if front else 1)],[2,y-9,2.5],1 if wolf or wyv else 13,[-12 if front else 25,0,0])
            paw=n+'_paw';bone(m,paw,lower,[x,2,z]);box(m,paw,[x-1.7,0,z-3],[3.4,2.5,5],11 if wolf else 13 if front or wyv else 0)
            for j in range(3):box(m,paw,[x-1.2+j,0,z-4],[.65,1,2],13 if wolf or wyv else 5)
    # Rotate connected segments about their joints, rather than cube centers.
    bone(m,'tail','body',[0,y,13],[12,0,0]);box(m,'tail',[-1.5,y-1.5,12],[3,3,10],10 if wolf else 0)
    bone(m,'tail_tip','tail',[0,y,21],[12,0,0]);box(m,'tail_tip',[-1,y-1,20],[2,2,11],11 if wolf else 0);box(m,'tail_tip',[-2,y-1.5,28],[4,3,4],11 if wolf else 13 if wyv else 1)
    # Continuous mane shingles, not a rectangular neck collar.
    if not wyv:
        for j in range(4):
            for s in [-1,1]:box(m,'body',[s*(3.5+j*.25)-1,y-1+j%2,-9+j*2],[2.8,5-j*.4,3],11 if wolf else 6,[18,0,s*(20+j*4)])
    else:
        for j in range(5):box(m,'body',[-.65,y+4,-3+j*4],[1.3,3.5,2],13,[20,0,0])
        for j in range(3):box(m,'neck',[-2,22+j*2,-12-j*2],[4,1,2.5],2,[20,0,0])
    # Harness, saddle and low pommel preserve the existing rider attachment height.
    top=15 if wolf else 22 if wyv else 19
    box(m,'body',[-4.7 if wolf else -6.2,y-3,-1],[9.4 if wolf else 12.4,6,1.4],7)
    box(m,'body',[-3.5,top-1,-1],[7,1.2,7],9);box(m,'body',[-3.7,top,4],[7.4,1.2,1],7)
    for s in [-1,1]:box(m,'body',[s*(4.8 if wolf else 6.3)-.6,y-1,-1.2],[1.2,2,.7],8)
    if not wolf:
        for s in [-1,1]:
            wing='wing_'+('left' if s>0 else 'right');bone(m,wing,'body',[s*5,y+5,-2],[0,s*70,-s*20])
            box(m,wing,[5 if s>0 else -16,y+4,-4],[11,2.3,5],0 if wyv else 6)
            tip=wing+'_tip';bone(m,tip,wing,[s*15,y+5,-2],[0,-s*10,-s*145]);box(m,tip,[15 if s>0 else -28,y+4,-3],[13,1.6,3],1 if wyv else 6)
            for j in range(7):
                x=7+j*2.8;x=x if s>0 else -x-3.5
                if wyv:
                    box(m,wing if j<3 else tip,[x,y+3,-1],[3.6,.65,13-j*.8],6,[0,-s*j*4,0])
                    box(m,wing if j<3 else tip,[x,y+3.6,-1],[.6,.8,14-j*.8],1,[0,-s*j*4,0])
                else:
                    box(m,wing if j<3 else tip,[x,y+3,-1],[3.5,1,10+j*.7],6 if j%2 else 2,[0,-s*j*4,0])
                    box(m,wing if j<3 else tip,[x,y+4,-2],[3.3,1,5],0,[0,-s*j*3,0])
            if wyv:box(m,wing,[s*14-.7,y+5,-6],[1.4,3,3],13,[20,0,s*18])
    return m



def refine(m):
    """Small original anatomical/material refinements, retaining the authored rig."""
    n=m.name
    if n=='forest_dryad':
        # Frame the existing adult face with leaf hair rather than a bare square.
        face=m.by_name['head']['cubes'][0]
        face['origin']=[-2.8,23,-2.8];face['size']=[5.6,5.8,4.8]
        box(m,'head',[-2.35,22.7,-2.5],[4.7,1.4,3.9],5)
        box(m,'head',[-.32,24,-3.16],[.64,1,.48],5)
        box(m,'head',[-.65,23.6,-2.91],[1.3,.18,.18],7)
        for side in [-1,1]:
            # Ivory sclera, dark pupils, upper lashes and pin highlights.
            x=side*1.6
            box(m,'head',[x-.58,24.85,-3.16],[1.16,.9,.2],13)
            box(m,'head',[x-.3,24.95,-3.3],[.6,.65,.17],3)
            box(m,'head',[x-.12,25,-3.43],[.24,.5,.15],1)
            box(m,'head',[x-.23,25.3,-3.51],[.18,.2,.1],4)
            box(m,'head',[x-.65,25.65,-3.28],[1.3,.16,.22],1,[0,0,side*5])
            hair='hair_'+('left' if side>0 else 'right')
            bone(m,hair,'head',[side*2.5,28,0])
            for j in range(3):
                box(m,hair,[side*(2.5+j*.18)-.5,21.4+j*.6,-1+j*1.3],[1.05,6.5-j*.5,1.3],6,[0,0,side*(5+j*3)])
            box(m,'head',[side*1.45-1.25,27,-3],[2.5,1.45,1.1],6,[0,0,side*11])
            # Overlapping leaf bodice and waist sash retain woodland costume.
            box(m,'body',[side*1.1-1.1,19,-2.05],[2.2,2.9,.65],3,[0,0,-side*10])
            box(m,'body',[side*1.2-.8,16.4,-1.8],[1.6,2.5,.5],6,[0,0,side*12])
        box(m,'body',[-2.2,14.6,-1.85],[4.4,.65,3.8],7)
    elif n=='ancient_treant':
        for side in [-1,1]:
            sx=side*9
            box(m,'arm_'+('left' if side>0 else 'right'),[sx-2.9,46,-2.5],[5.8,5,5],0,[0,0,side*8])
            box(m,'fore_'+('left' if side>0 else 'right'),[sx-2.3,34,-2.3],[4.6,4.2,4.6],1)
            box(m,'leg_'+('left' if side>0 else 'right'),[side*4.5-2.4,10,-2.7],[4.8,4.6,5.4],0)
            # Root knuckles and knot lips visually bridge bark facets.
            box(m,'body',[side*3-1.5,39,-5.25],[3,4,.9],0,[0,0,side*14])
            box(m,'head',[side*3-1.4,58,-5.8],[2.8,.7,.8],0,[0,0,side*9])
    else:
        wolf=n=='dire_wolf';wyv=n=='wild_wyvern';y=13 if wolf else 17 if wyv else 16
        for front in ([False] if wyv else [True,False]):
            for side in [-1,1]:
                limb=('arm_' if front else 'leg_')+('left' if side>0 else 'right')
                x=side*(3.2 if wolf else 4.5);z=-5 if front else 9
                # Rounded shoulder/haunch overlap, hock and metacarpal bridge.
                box(m,limb,[x-1.8,y-4,z-1.4],[3.6,3.8,4.2],10 if wolf else 6 if front else 0,[0,0,side*8])
                box(m,limb+'_lower',[x-1.25,y-8,z+(-1.2 if front else .8)],[2.5,2.6,2.8],1 if wolf or wyv else 13)
                box(m,limb+'_paw',[x-1.05,1.5,z-1.5],[2.1,1.6,2.8],11 if wolf else 13 if front or wyv else 0)
                for j in range(3):
                    box(m,limb+'_paw',[x-1.35+j,0.6,z-3.15],[.82,1.4,1.8],11 if wolf else 13 if front or wyv else 0)
        if wolf:
            for side in [-1,1]:
                box(m,'head',[side*2.4-1.05,15,-14],[2.1,2.5,3.8],10,[0,side*8,side*10])
                box(m,'head',[side*2.8-.3,18.15,-15.65],[.6,.5,.35],5)
            box(m,'head',[-2,14,-20.7],[4,1.5,1.3],5)
        elif wyv:
            for side in [-1,1]:
                wing='wing_'+('left' if side>0 else 'right')
                box(m,wing,[side*14-1.4,y+3.8,-4],[2.8,2.6,4],0)
                # Narrow trailing ribs emphasize stretched membrane panels.
                for j in range(5):
                    x=side*(8+j*3)-(0 if side>0 else .35)
                    box(m,wing if j<2 else wing+'_tip',[x,y+3.15,4],[.35,.45,5.5-j*.45],0,[0,-side*j*4,0])
        else:
            # Eagle hooked beak and layered lesser coverts over flight feathers.
            box(m,'head',[-1.8,15.4,-20.5],[3.6,2,2],13,[12,0,0])
            for side in [-1,1]:
                wing='wing_'+('left' if side>0 else 'right')
                for j in range(5):
                    x=side*(7+j*2.2)-(0 if side>0 else 2.4)
                    box(m,wing if j<4 else wing+'_tip',[x,y+4.2,-2.4],[2.4,.65,5.5+j*.4],6,[0,-side*j*4,0])
    return m


def reference_wyvern_head(m):
    """Original blunt theropod-inspired head from the user's supplied screenshot.

    Existing neck/head/jaw pivots and attack clips remain authoritative.
    Only cranial geometry changes; no reference pixels or model data are copied.
    """
    m.by_name['head']['cubes']=[]
    m.by_name['jaw']['cubes']=[]
    # Broad braincase steps down into a short, squared, pale muzzle.
    box(m,'head',[-3.5,28.8,-24],[7,4.8,8],0)
    box(m,'head',[-3,33.2,-23.3],[6,.8,6.2],10)
    box(m,'head',[-3.3,28.3,-30.5],[6.6,3.5,7.5],13)
    box(m,'head',[-2.8,31.4,-29.8],[5.6,.8,6],2)
    box(m,'head',[-3.45,28.2,-24.5],[6.9,2.7,2],1)
    # Mouth stays visibly open in rest pose; teeth belong to their own jaw.
    box(m,'jaw',[-3,25.8,-30],[6,1.5,9.8],13)
    box(m,'jaw',[-2.5,25.3,-28.7],[5,.7,7.7],2)
    box(m,'jaw',[-2.6,27.25,-29.5],[5.2,.18,8.2],7)
    for side in (-1,1):
        # Side-set eyes, heavy brow and small nasal openings read in profile.
        x=3.46 if side>0 else -3.78
        box(m,'head',[x,30.3,-23.1],[.32,1.25,1.7],13)
        box(m,'head',[3.73 if side>0 else -3.91,30.5,-22.7],[.18,.85,.65],5)
        box(m,'head',[side*3.35-.4,31.55,-23.5],[.8,.65,2.6],1)
        box(m,'head',[side*2.2-.4,30,-30.65],[.8,.5,.25],5)
        for j in range(5):
            z=-29+j*1.45
            box(m,'head',[side*2.45-.25,27.55,z],[.5,.9,.55],13)
            box(m,'jaw',[side*2.35-.22,27.35,z+.6],[.44,.65,.5],13)
    # Low crest replaces the previous tall paired horns.
    for j in range(3):
        box(m,'head',[-.65,33.65,-23+j*2],[1.3,1+j%2*.5,1.6],10,[8,0,0])
    return m


def animations(m):
    n=m.name;t=WIND[n];tree=n=='ancient_treant';wolf=n=='dire_wolf';wyv=n=='wild_wyvern';bird=n=='griffin';quadr=wolf or bird
    names=set(m.by_name);rate=210 if tree else 360;runrate=650 if wolf else 450
    idle={'body':{'position':[0,'math.sin(query.anim_time * 100) * .18',0]},'head':{'rotation':['math.sin(query.anim_time * 70) * 1.8','math.sin(query.anim_time * 45) * 3',0]}}
    if 'tail' in names:idle['tail']={'rotation':[0,'math.sin(query.anim_time * 85) * 7',0]};idle['tail_tip']={'rotation':[0,'math.sin(query.anim_time * 85 - 30) * 10',0]}
    walk={};run={'body':{'rotation':[f'math.sin(query.anim_time * {runrate}) * 5',0,0]},'root':{'position':[0,f'math.abs(math.sin(query.anim_time * {runrate})) * .65',0]}}
    for bn in sorted(names):
        if bn.startswith(('leg_','arm_')) and not bn.endswith(('_lower','_paw')):
            sign=1 if bn.endswith('left') else -1
            if bn.startswith('arm'):sign*=-1
            walk[bn]={'rotation':[f'math.sin(query.anim_time * {rate}) * {sign*(15 if tree else 25)}',0,0]}
            gallop=1 if bn.startswith('arm') else -1
            run[bn]={'rotation':[f'math.sin(query.anim_time * {runrate} + {20 if bn.endswith("left") else -20}) * {(gallop if quadr else sign)*42}',0,0]}
        if bn.endswith('_lower'):run[bn]={'rotation':[f'12 + math.sin(query.anim_time * {runrate} - 45) * 18',0,0]}
        if bn.startswith(('vine_','crown_','hair_')):idle[bn]={'rotation':[f'math.sin(query.anim_time * 85) * {2 if tree else 4}',0,0]}
    for bn in sorted(names):
        if bn.startswith(('hair_','vine_','crown_')):
            walk[bn]={'rotation':[f'math.sin(query.anim_time * {rate} - 35) * {3 if tree else 6}',0,0]}
            run[bn]={'rotation':[f'math.sin(query.anim_time * {runrate} - 45) * {5 if tree else 9}',0,0]}
        if bn.startswith('ear_'):
            idle[bn]={'rotation':[f'math.sin(query.anim_time * 63 - 20) * 3',0,0]}
        if bn.endswith('_paw'):
            walk[bn]={'rotation':[f'math.sin(query.anim_time * {rate} - 30) * 6',0,0]}
        if bn.startswith('wing_') and bn.endswith('_tip'):
            idle[bn]={'rotation':[f'math.sin(query.anim_time * 65 - 35) * 2',0,0]}
    attack={'head':{'rotation':keys(t,[-20,0,0],[30,0,0])},'body':{'rotation':keys(t,[-8,0,0],[12,0,0])}}
    if 'jaw' in names:attack['jaw']={'rotation':keys(t,[28,0,0],[0,0,0])}
    for bn in ('arm_right','fore_right'):
        if bn in names and not quadr:attack[bn]={'rotation':keys(t,[-85,0,-15],[-25,0,15])}
    heavy={'body':{'rotation':keys(t,[-16,0,-8],[22,0,8])},'head':{'rotation':keys(t,[-30,0,0],[35,0,0])}}
    if 'tail' in names:heavy['tail']={'rotation':keys(t,[0,-35,0],[0,40,0])}
    if bird:
        for side,s in [('left',1),('right',-1)]:
            attack['arm_'+side]={'rotation':keys(t,[-65,0,s*12],[30,0,0])}
            heavy['arm_'+side]={'rotation':keys(t,[-90,0,s*18],[42,0,0])}
    if tree:
        for side,s in [('left',1),('right',-1)]:
            heavy['arm_'+side]={'rotation':keys(t,[-105,0,s*15],[-15,0,0])}
            heavy['fore_'+side]={'rotation':keys(t,[-20,0,0],[22,0,0])}
    if wolf:heavy['head']={'rotation':keys(t,[-18,-24,0],[20,28,0])}
    cast={'head':{'rotation':keys(t,[-25,0,0],[10,0,0])},'body':{'position':keys(t,[0,.5,0],[0,0,0])}}
    for bn in ('arm_left','arm_right'):
        if bn in names and not quadr:cast[bn]={'rotation':keys(t,[-80,0,20 if bn.endswith('left') else -20],[-45,0,0])}
    if 'jaw' in names:cast['jaw']={'rotation':keys(t,[8,0,0],[28,0,0])}
    if wyv:cast['neck']={'rotation':keys(t,[-12,0,0],[8,0,0])}
    if tree:
        for bn in sorted(names):
            if bn.startswith('finger_'):heavy[bn]={'rotation':keys(t,[25,0,0],[-12,0,0])}
    hurt={'body':{'rotation':{'0.0':[0,0,0],'.08':[-12,0,5],'.45':[0,0,0]}},'head':{'rotation':{'0.0':[0,0,0],'.08':[15,-8,0],'.45':[0,0,0]}}}
    death={'root':{'rotation':{'0.0':[0,0,0],'.5':[8,0,20],'1.2':[0,0,85]},'position':{'0.0':[0,0,0],'1.2':[0,-2,0]}}}
    out={k:clip(l,b,loop=loop) for k,l,b,loop in [('idle',3.6,idle,True),('walk',360/rate,walk,True),('run',360/runrate,run,True),('attack',round(t+.3,4),attack,False),('heavy',round(t+.3,4),heavy,False),('cast',round(t+.3,4),cast,False),('hurt',.45,hurt,False),('death',1.2,death,False)]}
    if quadr or wyv:
        sit={'body':{'position':[0,-4,0]},'leg_left':{'rotation':[-65,0,0]},'leg_right':{'rotation':[-65,0,0]},'head':{'rotation':[8,0,0]}}
        out['sit']=clip(2,sit,loop=True);out['rest']=clip(3,{**sit,'head':{'rotation':[18,0,0]}},loop=True)
        out['ride']=clip(360/runrate,{k:v for k,v in run.items() if k!='root'},loop=True)
        out['tame']=clip(1.4,{'head':{'rotation':{'0.0':[0,0,0],'.4':[16,-12,0],'.8':[8,12,0],'1.4':[0,0,0]}}})
    if wolf:
        out['jump']=clip(.7,{'body':{'rotation':[-8,0,0]},'arm_left':{'rotation':[-35,0,0]},'arm_right':{'rotation':[-35,0,0]},'leg_left':{'rotation':[25,0,0]},'leg_right':{'rotation':[25,0,0]}},loop=True)
    if bird or wyv:
        for state,rate,amp in [('fly',400,35),('hover',520,44)]:
            b={'body':{'rotation':[-5,0,0]},'leg_left':{'rotation':[-45,0,0]},'leg_right':{'rotation':[-45,0,0]},'tail':{'rotation':[8,'math.sin(query.anim_time * 120) * 5',0]}}
            for side,s in [('left',1),('right',-1)]:
                b['wing_'+side]={'rotation':[0,-s*70,f'{s*20} + math.sin(query.anim_time * {rate}) * {s*amp}']}
                b['wing_'+side+'_tip']={'rotation':[0,s*10,f'{s*145} + math.sin(query.anim_time * {rate} - 35) * {s*18}']}
            out[state]=clip(360/rate,b,loop=True)
        for state,unfold in [('takeoff',True),('landing',False)]:
            b={'body':{'rotation':{'0.0':[0,0,0],'.4':[-12,0,0],'.9':[0,0,0]}}}
            for side,s in [('left',1),('right',-1)]:
                b['wing_'+side]={'rotation':{'0.0':[0,0 if unfold else -s*70,0 if unfold else s*20],'.9':[0,-s*70 if unfold else 0,s*20 if unfold else 0]}}
                b['wing_'+side+'_tip']={'rotation':{'0.0':[0,0 if unfold else s*10,0 if unfold else s*145],'.9':[0,s*10 if unfold else 0,s*145 if unfold else 0]}}
            out[state]=clip(.9,b)
    return out

def overhaul_v2(m):
    """Large silhouette edits on the compatible original rig; seat remains fixed."""
    n=m.name
    if n=='ancient_treant':
        # Widen the whole branched upper trunk, including attached joint pivots.
        for b in m.bones:
            if b['name'] not in ('root','leg_left','leg_right'):
                b['pivot'][0]*=1.32
                for c in b.get('cubes',[]):
                    c['origin'][0]*=1.32;c['size'][0]*=1.32
        m.by_name['head']['cubes']=[]
        # A dark irregular knot cavity framed by split bark; no human nose/lips.
        box(m,'head',[-6.4,51,-5.3],[12.8,12,8.8],1)
        box(m,'head',[-4.8,52,-5.65],[9.6,8,.7],14)
        for side in (-1,1):
            box(m,'head',[side*4.8-1.8,51,-6.2],[3.6,13,3],0,[0,side*12,side*16])
            box(m,'head',[side*2.5-1.5,58,-6],[3,1.1,.7],4,[0,0,-side*23])
            box(m,'head',[side*3.3-.7,52,-6.1],[1.4,5,1.5],2,[0,0,side*29])
            box(m,'body',[side*8-3,43,-4],[6,11,8],0,[0,0,-side*28])
            box(m,'body',[side*10-2,48,0],[4,8,5],1,[0,0,-side*40])
        for j in range(4):
            box(m,'head',[-4.5+j*3,51-j%2,-6],[1.5,3+j%2,1.5],0,[0,0,(j-1.5)*13])
    elif n=='forest_dryad':
        # Expansion reference: pale adult woodland woman, leaf costume and green hair.
        # All legacy rig bones and every animation are preserved verbatim.
        m.by_name['head']['cubes']=[]
        box(m,'head',[-2.65,23.4,-2.5],[5.3,5.1,4.5],5)
        box(m,'head',[-2.1,23,-2.3],[4.2,1,4.1],5)
        box(m,'head',[-.25,24.35,-2.93],[.5,.65,.5],5)
        box(m,'head',[-.56,23.9,-2.85],[1.12,.16,.15],14)
        for side in (-1,1):
            x=side*1.25
            box(m,'head',[x-.72,25.1,-2.72],[1.44,.93,.16],13)
            box(m,'head',[x-.35,25.15,-2.88],[.7,.77,.14],3)
            box(m,'head',[x-.12,25.2,-3.02],[.24,.64,.1],1)
            box(m,'head',[x-.25,25.62,-3.13],[.18,.18,.08],13)
            box(m,'head',[x-.78,25.97,-2.86],[1.56,.15,.19],1,[0,0,-side*6])
            box(m,'head',[x-.5,26.5,-2.68],[1.05,.13,.16],9,[0,0,-side*6])
            # Long pointed ears start inside the cheek planes, behind the hair.
            box(m,'head',[side*3.15-.8,25.1,-.7],[1.6,2.5,.8],5,[0,0,-side*38])
            box(m,'head',[side*3.8-.35,26.6,-.6],[.7,1.6,.65],5,[0,0,-side*38])
        # Continuous cap covers the full upper skull, followed by broad green locks.
        box(m,'head',[-3,27.6,-2.8],[6,1.25,5.3],6)
        box(m,'head',[-2.5,28.7,-2.3],[5,.55,4.4],6)
        for side,label in ((-1,'right'),(1,'left')):
            hair='hair_'+label;m.by_name[hair]['cubes']=[]
            box(m,hair,[side*2.65-.7,18.2,-1.5],[1.4,10,1.8],6,[0,0,-side*4])
            box(m,hair,[side*2.7-.5,17.2,-1.1],[1,3.2,1.3],9,[0,0,-side*7])
            for j in range(3):
                x=side*(.65+j*.85)
                box(m,hair,[x-.65,16.5+j*.7,1.5],[1.4,11.5-j*.7,1.6],6,[5,0,side*(j+2)])
            box(m,'head',[side*1.3-1.2,26.9,-2.95],[2.4,1.4,.8],6,[0,0,-side*12])
            m.by_name['crown_'+label]['cubes']=[]
            # Small leaf circlet integrated with the scalp rather than wooden horns.
            box(m,'crown_'+label,[side*1.8-.7,28,-1.1],[1.4,1.3,.65],3,[0,0,-side*28])
            for j in range(3):
                n=f'finger_{side}_{j}';m.by_name[n]['cubes']=[]
                box(m,n,[side*3.5-.6+j*.6,7.5,-1.5],[.4,2.5,.6],5,[8+j*9,0,side*8])
            # Tall light boots with grounded soles; no collision/leg pivot change.
            leg='leg_'+label;m.by_name[leg]['cubes']=[]
            box(m,leg,[side*1.5-.9,1,-1.15],[1.8,10.5,2.3],2)
            box(m,leg,[side*1.5-1,0,-2.5],[2,1.6,3.8],2)
            box(m,leg,[side*1.5-1.02,9.3,-1.25],[2.04,1.2,2.5],13)
        m.by_name['body']['cubes']=[]
        for o,sz,mat in [([-2.3,12,-1.6],[4.6,4.3,3.2],0),([-1.8,16,-1.5],[3.6,3.7,3],3),([-2.7,19,-1.8],[5.4,3.2,3.6],0)]:box(m,'body',o,sz,mat)
        for side in (-1,1):
            box(m,'body',[side*1.15-1.25,19,-2.7],[2.5,2.8,1.7],3,[0,0,-side*9])
            box(m,'body',[side*1.5-.75,16.5,-1.95],[1.5,3.1,.7],6,[0,0,-side*13])
            front='vine_front_'+str(side);m.by_name[front]['cubes']=[]
            for j in range(3):box(m,front,[side*(.6+j*.6)-1,9.3+j*.9,-2.25],[2,4.5,.7],3 if j%2 else 6,[0,0,-side*15])
            for j in range(4):
                n=f'vine_{side}_{j}';m.by_name[n]['cubes']=[]
                box(m,n,[side*(1.6+j*.25)-.7,10+j*.3,1.3+j*.25],[1.5,5-j*.2,.9],3,[0,0,side*(8+j*4)])
                box(m,n,[side*(1.6+j*.25)-.65,9.4+j*.3,1.4+j*.25],[1.3,1.6,.65],6,[0,0,side*22])
        box(m,'body',[-2.2,14.5,-1.9],[4.4,.65,3.8],7)
    else:
        wolf=n=='dire_wolf';wyv=n=='wild_wyvern';y=13 if wolf else 17 if wyv else 16
        # Overlapping pectoral/scapular masses replace rectangular slab reads.
        for side in (-1,1):
            box(m,'body',[side*(3.1 if wolf else 4)-1.8,y-2,-8],[3.6,6 if wolf else 8,8],10 if wolf else 0,[0,side*9,side*13])
        if wolf:
            # Replace the horizontal eyebrow blocks with integrated rising sockets.
            for c in m.by_name['head']['cubes']:
                if c['size']==[2,.7,2]:c['rotation']=[0,0,-(1 if c['origin'][0]>0 else -1)*24]
            box(m,'head',[-2.2,15,-19.5],[4.4,2.8,4.8],11,[5,0,0])
            for side in (-1,1):
                box(m,'body',[side*3.7-1,13,-7],[2,5,6],10,[12,0,side*19])
                box(m,'tail_tip',[-1.5,11.5,24],[3,3,7],10,[12,0,0]) if side==1 else None
        elif wyv:
            # Long airborne trunk from the supplied body silhouette; seat untouched.
            m.by_name['body']['cubes'][0]['size'][2]=26
            box(m,'body',[-5.3,14,-9],[10.6,8.5,10],0,[9,0,0])
            box(m,'body',[-4.3,13,-8.8],[8.6,6,8],2,[8,0,0])
            box(m,'neck',[-3.6,20,-13],[7.2,8,7],0,[24,0,0])
            # Strengthen tail without moving saddle top (22 model units).
            for bn in ('tail','tail_tip'):
                for c in m.by_name[bn].get('cubes',[]):
                    c['size'][0]*=1.35;c['origin'][0]=-c['size'][0]/2
                    c['size'][2]*=1.35
            bone(m,'tail_end','tail_tip',[0,17,31],[8,0,0])
            box(m,'tail_end',[-1,16,30],[2,2,14],0,[5,0,0])
            box(m,'tail_end',[-.65,16.3,43],[1.3,1.3,11],0,[4,0,0])
            for j in range(3):
                box(m,'tail_tip' if j<2 else 'tail_end',[-.45,18.2-j*.3,23+j*8],[.9,2-j*.35,2.1],13,[18,0,0])
        else:
            # Hooked keratin beak with descending tip, scowling orbital shields.
            box(m,'head',[-2,17,-21.4],[4,3.2,3.6],13,[12,0,0])
            box(m,'head',[-1.25,14.8,-22],[2.5,3,1.5],13,[18,0,0])
            for side in (-1,1):
                box(m,'head',[side*2.8-1.1,22.6,-15.7],[2.2,1.1,2.4],1,[0,0,-side*22])
                box(m,'body',[side*4-1.5,18,-8],[3,6,7],6,[15,0,side*17])
        if not wolf:
            for side in (-1,1):
                wing='wing_'+('left' if side>0 else 'right');tip=wing+'_tip'
                # Rebuild as a connected humerus, wrist, finger fan / primary fan.
                m.by_name[wing]['cubes']=[];m.by_name[tip]['cubes']=[]
                m.by_name[wing]['rotation']=[0,side*70,-side*20]
                m.by_name[tip]['rotation']=[0,-side*10,-side*145]
                def span(b,x,length,z,width,depth,mat,rot=0):
                    box(m,b,[x if side>0 else -x-length,y+3,z],[length,width,depth],mat,[0,side*rot,0])
                span(wing,4.5,11.5,-4,3,5,0 if wyv else 6)
                span(tip,15,26 if wyv else 16,-3,1.8,3,0 if wyv else 6)
                for j in range(7):
                    x=6+j*(5 if wyv else 3.5)
                    b=wing if j<3 else tip
                    span(b,x,5.4 if wyv else 3.8,-1,.55 if wyv else .9,24-j*1.3 if wyv else 13+j*.45,6 if wyv else (2 if j%2 else 6),-j*3)
                    span(b,x,.6 if wyv else 3.5,-1,.8 if wyv else .7,25-j*1.3 if wyv else 6,1 if wyv else 0,-j*3)
                span(wing,13,2,-5,2.8,3,13)
                if not wyv:
                    # Fold backwards along the flanks rather than forwards above
                    # the skull. Wrist stays aligned with the shoulder segment.
                    m.by_name[wing]['rotation']=[0,-side*78,-side*12]
                    m.by_name[tip]['rotation']=[0,side*20,side*10]
                    for b in (wing,tip):
                        for c in m.by_name[b]['cubes']:
                            if c['size'][1]<1.1:
                                c['origin'][2]-=3
                                c['size'][2]*=.72
    return m


def animate_v2(m,out):
    n=m.name;tree=n=='ancient_treant';wolf=n=='dire_wolf';winged=n in ('griffin','wild_wyvern')
    for state in ('walk','run','ride'):
        if state not in out:continue
        b=out[state]['bones'];rate=210 if tree else 360 if state=='walk' else 650 if wolf else 450
        # Root never floats above the collision floor during grounded cycles.
        b.pop('root',None)
        b['body']={'position':[0,f'-math.abs(math.sin(query.anim_time * {rate})) * {.25 if tree else .18}',0],
                   'rotation':[f'math.sin(query.anim_time * {rate}) * {1.5 if tree else 2}',0,f'math.sin(query.anim_time * {rate}) * {2 if tree else 1}']}
        b['head']={'rotation':[f'math.sin(query.anim_time * {rate} - 35) * 2',f'math.sin(query.anim_time * {rate}) * 2',0]}
        for bn in m.by_name:
            if bn.endswith('_lower'):
                sign=1 if 'left' in bn else -1
                b[bn]={'rotation':[f'8 + math.sin(query.anim_time * {rate} - {35 if sign>0 else 215}) * 12',0,0]}
            if bn in ('tail','tail_tip','tail_end'):
                lag={'tail':0,'tail_tip':35,'tail_end':65}[bn]
                b[bn]={'rotation':[f'math.sin(query.anim_time * {rate} - {lag}) * 3',f'math.sin(query.anim_time * {rate} - {lag}) * 8',0]}
    # Match authoritative impact times while adding torso twist and recoil lag.
    for state in ('attack','heavy'):
        b=out[state]['bones'];t=WIND[n]
        b['body']={'rotation':keys(t,[-10,-9,-3],[14,10,3])}
        if 'tail_tip' in m.by_name:
            b['tail_tip']={'rotation':keys(t,[5,-18,0],[-8,23,0])}
        if 'neck' in m.by_name:
            b['neck']={'rotation':keys(t,[-12,-6,0],[16,7,0])}
        if wolf:
            for side in (-1,1):
                b['ear_'+str(side)]={'rotation':keys(t,[-18,0,side*8],[8,0,0])}
            b['jaw']={'rotation':keys(t,[24,0,0],[4,0,0])}
    if tree:
        for state in ('idle','walk','run'):
            for side,s in [('left',1),('right',-1)]:
                out[state]['bones']['fore_'+side]={'rotation':[f'5 + math.sin(query.anim_time * 105 - {s*25}) * 4',0,0]}
    if n=='forest_dryad':
        for state in ('attack','cast','heavy'):
            for bn in m.by_name:
                if bn.startswith(('hair_','vine_')):out[state]['bones'][bn]={'rotation':keys(WIND[n],[7,0,4],[-9,0,-3])}
    if winged:
        for state in ('fly','hover'):
            b=out[state]['bones'];rate=400 if state=='fly' else 520
            b['body']={'rotation':[f'{-2 if n=="wild_wyvern" else -5} + math.sin(query.anim_time * {rate} - 35) * 2',0,0]}
            if n=='wild_wyvern':
                # Broad high recovery stroke, bent elbow and lagging membrane tips.
                for side,sign in [('left',1),('right',-1)]:
                    b['wing_'+side]['rotation'][2]=f'{sign*28} + math.sin(query.anim_time * {rate}) * {sign*43}'
                    b['wing_'+side+'_tip']['rotation'][2]=f'{sign*145} + math.sin(query.anim_time * {rate} - 40) * {sign*23}'
                b['leg_left']={'rotation':[-58,0,5]}
                b['leg_right']={'rotation':[-58,0,-5]}
                b['leg_left_lower']={'rotation':[38,0,0]}
                b['leg_right_lower']={'rotation':[38,0,0]}
            b['tail_tip']={'rotation':[f'math.sin(query.anim_time * {rate} - 65) * 7','math.sin(query.anim_time * 120 - 35) * 7',0]}
            if 'tail_end' in m.by_name:b['tail_end']={'rotation':[f'math.sin(query.anim_time * {rate} - 95) * 10',0,0]}
        for state in ('takeoff','landing'):
            b=out[state]['bones']
            b['leg_left']={'rotation':{'0.0':[0,0,0],'.25':[22,0,0],'.6':[-35,0,0],'.9':[-40,0,0]} if state=='takeoff' else {'0.0':[-40,0,0],'.4':[12,0,0],'.65':[22,0,0],'.9':[0,0,0]}}
            b['leg_right']=b['leg_left'].copy()
            b['tail_tip']={'rotation':{'0.0':[0,0,0],'.3':[-14,0,0],'.65':[12,0,0],'.9':[0,0,0]}}
    if n=='griffin':
        for state,a in out.items():
            b=a['bones']
            for side,sign in [('left',1),('right',-1)]:
                wing='wing_'+side;tip=wing+'_tip'
                if state in ('fly','hover'):
                    rate=400 if state=='fly' else 520
                    b[wing]={'rotation':[0,sign*78,f'{sign*12} + math.sin(query.anim_time * {rate}) * {sign*35}'],'scale':[1,1,1]}
                    b[tip]={'rotation':[0,-sign*20,f'{-sign*10} + math.sin(query.anim_time * {rate} - 35) * {sign*18}'],'scale':[1,1,1]}
                elif state in ('takeoff','landing'):
                    opening=state=='takeoff'
                    b[wing]={'rotation':{'0.0':[0,0 if opening else sign*78,0 if opening else sign*12],'.9':[0,sign*78 if opening else 0,sign*12 if opening else 0]},
                             'scale':{'0.0':[.55,1,.55] if opening else [1,1,1],'.9':[1,1,1] if opening else [.55,1,.55]}}
                    b[tip]={'rotation':{'0.0':[0,0 if opening else -sign*20,0 if opening else -sign*10],'.9':[0,-sign*20 if opening else 0,-sign*10 if opening else 0]}}
                else:
                    b[wing]={'rotation':[0,0,0],'scale':[.55,1,.55]}
                    b[tip]={'rotation':[0,0,0],'scale':[1,1,1]}
    return out

def main():
    for name,p in PALETTES.items():
        p=list(p)
        # Refine local material separation within the established muted palette.
        slot,color={'ancient_treant':(2,'9b8059'),'forest_dryad':(5,'f5e3d0'),'griffin':(6,'c1b69b'),'dire_wolf':(11,'a8afa8'),'wild_wyvern':(6,'796455')}[name]
        p[slot]=color
        m=refine(woodland(name) if name in ('ancient_treant','forest_dryad') else beasts(name))
        if name=='wild_wyvern': m=reference_wyvern_head(m)
        m=overhaul_v2(m)
        variants={}
        if name in ('griffin','dire_wolf','wild_wyvern'):
            tame=list(p);tame[7]='603b2e';tame[9]='914d43' if name=='dire_wolf' else 'b19453';tame[8]='c6b47a';variants['_tamed']=tame
        if name=='wild_wyvern':
            rare=list(p);rare[0]='467a88';rare[1]='294955';rare[4]='b7e5e4';rare[6]='436078';rare[10]='5b8e9a';variants['_rare']=rare
            variants['_tamed'][0]='467a88';variants['_tamed'][1]='294955';variants['_tamed'][6]='436078'
        w,h=DIMS[name]
        materials=list(MATERIALS)
        if name=='ancient_treant':materials[2]='bark'
        if name=='forest_dryad':
            materials[0]=materials[5]='skin';materials[6]=materials[9]='hair';materials[13]='bone';materials[2]='cloth';materials[3]='cloth';materials[7]='leather'
        if name=='griffin':materials[13]='bone'
        if name=='griffin':
            materials[0]='fur';materials[1]=materials[2]=materials[6]='feather'
        if name=='dire_wolf':
            for i in (0,1,2,3,6,10,11):materials[i]='fur'
        if name=='wild_wyvern':
            materials[0]=materials[1]='scales';materials[6]='membrane'
        write_creature(m,p,materials,animate_v2(m,animations(m)),w,h,glow=(4,12) if name in ('ancient_treant','forest_dryad','wild_wyvern') else (),variants=variants)

if __name__=='__main__':main()
