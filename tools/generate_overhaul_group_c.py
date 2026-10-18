#!/usr/bin/env python3
"""Original Group C art. Inspected reference analysis lives in REFERENCE_ATLAS.md.

Scute rhythm, arthropod anatomy, ragged spectral hems, layered historical plate
and bat wing fingers inform these independently authored block silhouettes.
Coordinates are pixels, forward is negative Z; no reference pixels are reused.
"""
from math import cos, sin, radians
from overhaul_asset_pipeline import Model, clip, keys, write_creature

PALETTES = {
'cave_basilisk': '465442 253b32 728066 9b8759 c9ec7c 17271f d3cda3 737348 8b9872 354735 574733 b3db78 6e8973 555c45 7f896e b8bd8e',
'crystal_spider': '34344b 202133 675879 9c92b5 e9bcff 141725 d4c9e1 75618e 50475e 2c2c42 443848 c886ee 9874c4 4e405d 878196 ece0fa',
'shadow_wraith': '343c4b 1b2531 525366 737e8b 8de5d5 101a24 a7adb8 514361 475a65 252c3a 3a3344 9bdad9 6b8f9a 3d394b 565e70 caefdf',
'grave_knight': '505c66 29323d 78838a a18b5b 99e7d5 171f29 c6bf9d 6d3946 777161 404750 594334 7ac8bc 667b7e 432d3c 98a1a1 d0d5c7',
'flame_imp': '963d32 542a2d c06638 d2954a ffe18c 241e28 d4b58e 873440 c47b50 713329 49342e ffab4c e98c39 592933 95694a ffdfa0',
}
MATERIALS = ['scales','scales','scales','metal','glow','cloth','bone','leather','skin','scales','leather','rune','crystal','cloth','metal','bone']


def b(m,n,p,v,o,s,mat=0,r=None):
    m.bone(n,p,v,r); m.box(n,o,s,mat); return n


def oscillate(a, axis=0):
    v=[0,0,0];v[axis]=a
    w=[-x for x in v]
    return {'0.0':v,'0.5':w,'1.0':v}


def action(t, prepare, impact):
    return {'rotation':keys(t,prepare,impact)}


def basilisk():
    m=Model('cave_basilisk')
    b(m,'body','root',[0,6,2],[-5,3,-4],[10,6,15])
    m.box('body',[-4,2,-3],[8,1.4,13],2)
    b(m,'neck','body',[0,7,-3],[-3.8,5,-8],[7.6,5,6],0,[-8,0,0])
    b(m,'head','neck',[0,8,-7],[-4.6,6,-12],[9.2,4.7,6],2)
    m.box('head',[-3.6,5.8,-17],[7.2,2.5,6],0)
    m.box('head',[-3.8,8.4,-13.8],[7.6,1,3],1)
    b(m,'jaw','head',[0,6,-8],[-3.5,4.8,-16.5],[7,1.1,8],8)
    for side in (-1,1):
        m.box('head',[side*4.2-.35,8,-12],[.7,1.1,2],4)
        for z in (-15,-12):m.box('jaw',[side*2.7-.3,5.8,z],[.6,.8,.7],6)
        for i,z in enumerate((-2,7)):
            n=f'leg_{side}_{i}';x=side*4
            b(m,n,'body',[x,5,z],[min(x,x+side*4),2.7,z-1],[4,2.6,3],0,[0,side*14,side*18])
            b(m,n+'_foot',n,[side*7,3,z],[side*7-1.2,.5,z-3],[2.4,2.8,5],1)
            for j in range(3):m.box(n+'_foot',[side*7-1+j,.3,z-3.9],[.6,.6,1.6],6)
    for i,z in enumerate((-8,-4,0,4,8)):
        m.box('head' if i==0 else 'body',[-.8,10 if i==0 else 8,z],[1.6,3.5 if i<2 else 2.5,2.7],3,[-25,0,0],[0,9,z])
    for side in (-1,1):
        for z in (0,4,8):m.box('body',[side*3-1,8,z],[2,1.4,3.5],2)
    b(m,'tail','body',[0,6,10],[-3,3.7,10],[6,4,8],0,[0,12,0])
    b(m,'tail_tip','tail',[0,5.5,17],[-1.8,4,17],[3.6,2.6,9],2,[0,18,0])
    a=common(m,1.0,'head')
    for state,speed in [('walk',1),('run',1.7)]:
        bones={'tail':{'rotation':oscillate(11,1)},'tail_tip':{'rotation':oscillate(-16,1)}}
        for side in (-1,1):
            for i in range(2):bones[f'leg_{side}_{i}']={'rotation':oscillate((17 if (i+(side==1))%2 else -17)*speed)}
        a[state]=clip(1/speed,bones,True)
    a['attack']=clip(1.5,{'neck':action(1,[-18,0,0],[22,0,0]),'jaw':action(1,[30,0,0],[-5,0,0]),'tail':action(1,[0,-22,0],[0,24,0])})
    a['cast']=clip(1.5,{'head':action(1,[-15,-20,0],[4,20,0]),'body':{'scale':{'0':[1,1,1],'.8':[1,1.05,1],'1':[1,1,1]}},'jaw':action(1,[8,0,0],[22,0,0])})
    return m,a


def spider():
    m=Model('crystal_spider')
    b(m,'body','root',[0,8,0],[-4,5,-6],[8,6,9],0)
    b(m,'abdomen','body',[0,8,2],[-5.5,6,2],[11,7,11],1,[-10,0,0])
    m.box('abdomen',[-4,5,4],[8,2,7],2)
    for side in (-1,1):
        for i in range(4):
            z=-4+i*2.3; n=f'leg_{side}_{i}'; spread=11+(1 if i in (1,2) else 0)
            # Rooted leg girdle isolates planted feet from carapace lunges.
            # Yaw changes footprint only; stacked Z bends previously raised all feet.
            b(m,n,'root',[side*3.5,8,z],[min(side*3.5,side*spread),7.3,z-.65],[spread-3.5,1.5,1.5],8,[0,side*(25-i*16),0])
            # Exact lower outer corner: 8 - length*cos(14) - .7*sin(14) = 0.
            shin_length=(8-.7*sin(radians(14)))/cos(radians(14))
            b(m,n+'_knee',n,[side*spread,8,z],[side*spread-.7,8-shin_length,z-.65],[1.4,shin_length,1.4],0,[0,0,side*14])
            m.box(n+'_knee',[side*spread-.9,6.2,z-.9],[1.8,2,1.8],3)
        for i in range(3):
            m.box('body',[side*(1.3+i)-.5,8.1+(i%2),-6.5],[1,1.2,1],4)
        n=f'fang_{side}';b(m,n,'body',[side*2.5,6,-5],[side*2.5-.65,3.5,-7.5],[1.3,3.5,1.3],6,[25,0,side*15])
        b(m,f'palp_{side}','body',[side*3,6,-4.5],[side*3-.6,5,-9],[1.2,1.2,4],2,[0,side*18,0])
    for i,(x,z,h) in enumerate([(-3,5,5),(2,7,7),(0,3,4),(3,10,4),(-2,10,3)]):
        n=f'crystal_{i}';b(m,n,'abdomen',[x,11,z],[x-1,10,z-1],[2,h,2],12,[10,i*23-35,(i%2*2-1)*20])
        m.box(n,[x-.6,10+h,z-.6],[1.2,1.2,1.2],15)
    b(m,'spinneret','abdomen',[0,8,12],[-1.4,6.5,12],[2.8,2.8,2],11)
    a=common(m,.7,'body')
    for state,speed in [('walk',1),('run',1.65)]:
        bones={'abdomen':{'rotation':oscillate(3,1)}}
        for side in (-1,1):
            for i in range(4):
                phase=1 if (i+(side==1))%2 else -1
                bones[f'leg_{side}_{i}']={'rotation':oscillate(phase*13,1)}
                # Alternating tetrapod support: four feet remain planted while
                # the other four swing; yaw never changes sole height.
                lift={'0':[0,0,0],'.25':[0,1.1,0],'.5':[0,0,0],'1':[0,0,0]} if phase==1 else {'0':[0,0,0],'.5':[0,0,0],'.75':[0,1.1,0],'1':[0,0,0]}
                bones[f'leg_{side}_{i}_knee']={'position':lift}
        a[state]=clip(1/speed,bones,True)
    a['attack']=clip(1.2,{'body':action(.7,[-14,0,0],[17,0,0]),'fang_-1':action(.7,[25,0,0],[-22,0,0]),'fang_1':action(.7,[25,0,0],[-22,0,0])})
    a['cast']=clip(1.3,{'abdomen':action(.7,[-24,0,0],[12,0,0]),'spinneret':{'scale':{'0':[1,1,1],'.5':[1.3,1.3,1.3],'.7':[.8,.8,.8],'1.3':[1,1,1]}},'body':action(.7,[0,-20,0],[0,22,0])})
    return m,a


def wraith():
    m=Model('shadow_wraith')
    b(m,'body','root',[0,22,0],[-4,17,-2.5],[8,9,5],13)
    b(m,'head','body',[0,27,0],[-3.5,25,-3.4],[7,6.5,6.5],1)
    m.box('head',[-2.7,25.4,-3.8],[5.4,4.9,.6],5)
    for side in (-1,1):m.box('head',[side*1.5-.6,28,-4],[1.2,.65,.5],4)
    m.box('head',[-4,30,-3.7],[8,1.8,7],13)
    for side in (-1,1):
        n=f'arm_{side}';b(m,n,'body',[side*4,24,0],[side*5-1.5,17,-1.8],[3,7,3.6],14,[0,0,side*19])
        b(m,n+'_hand',n,[side*5,18,0],[side*5-1,13,-1],[2,5,2],12)
        for j in range(3):m.box(n+'_hand',[side*5-1+j*.7,11.5,-1.3],[.5,2.7,.7],4)
        m.box(n,[side*4-2,23,-2.5],[4,2,5],1)
    for i in range(7):
        x=-4.5+i*1.35; y=3+(i*3)%5
        n=f'shroud_{i}';b(m,n,'body',[x,18,1],[x-.8,y,-1+(i%2)*2],[1.7,18-y,2.2],13 if i%2 else 0,[0,0,(i-3)*3])
        b(m,n+'_wisp',n,[x,y,0],[x-.45,y-2.5,.2],[.9,4,1],12,[14,0,(i-3)*7])
    a=common(m,.9,'body')
    floatbones={'body':{'position':{'0':[0,0,0],'1':[0,1.2,0],'2':[0,0,0]}},'head':{'rotation':oscillate(5,1)}}
    for i in range(7):floatbones[f'shroud_{i}']={'rotation':oscillate((i-3)*2+5)}
    a['idle']=clip(2,floatbones,True)
    for s in ['walk','run','fly','hover']:a[s]=clip(2,floatbones,True)
    for s in ['attack','cast','heavy']:
        a[s]=clip(1.5,{'body':action(.9,[0,-25,0],[0,28,0]),'arm_-1':action(.9,[-65,0,-25],[25,0,15]),'arm_1':action(.9,[-65,0,25],[25,0,-15]),'head':action(.9,[-12,0,0],[14,0,0])})
    a['death']=clip(2,{'body':{'position':{'0':[0,0,0],'1.5':[0,-12,0]},'scale':{'0':[1,1,1],'1.8':[.1,.05,.1]}},'shroud_3':{'rotation':{'0':[0,0,0],'1.5':[0,180,0]}}})
    return m,a


def knight():
    m=Model('grave_knight')
    b(m,'body','root',[0,19,0],[-4.6,16,-2.6],[9.2,10,5.2],0)
    m.box('body',[-3.5,17,-3.2],[7,7,.8],14)
    m.box('body',[-.6,18,-3.7],[1.2,6,.5],3)
    b(m,'head','body',[0,27,0],[-3,26,-3],[6,6.1,6],0)
    m.box('head',[-3.3,28,-3.6],[6.6,1.2,.7],1)
    m.box('head',[-2.5,28.4,-3.9],[5,.4,.4],4)
    m.box('head',[-.5,26,-4],[1,5,.7],14)
    for side in (-1,1):
        for j in range(2):m.box('head',[side*(2-j*.4)-.4,31,-1+j*2],[.8,2.4+j*.5,.8],3,[0,0,side*-13],[side*2,31,0])
        n=f'leg_{side}';b(m,n,'body',[side*2.4,16,0],[side*2.4-1.9,8,-2],[3.8,8,4],1)
        b(m,n+'_shin',n,[side*2.4,9,0],[side*2.4-1.7,1,-2],[3.4,8,4],0)
        m.box(n+'_shin',[side*2.4-1.9,0,-4],[3.8,2.5,6],14)
        m.box(n, [side*2.4-2.1,8,-2.7],[4.2,2.5,1.1],3)
        arm=f'arm_{side}';b(m,arm,'body',[side*5,24,0],[side*5-1.7,17,-1.8],[3.4,7,3.6],0,[0,0,side*6])
        for j in range(3):m.box(arm,[side*5-2.5,23-j*.75,-2.5],[5,1.1,5],0 if j%2 else 14)
        b(m,arm+'_forearm',arm,[side*5,18,0],[side*5-1.8,12,-2],[3.6,6,4],14)
        m.box(arm+'_forearm',[side*5-1.7,11,-2],[3.4,2.2,3.8],10)
    b(m,'sword','arm_1_forearm',[5,12,-1],[4.35,8,-1.7],[1.3,6,1.3],10,[10,0,-55])
    m.box('sword',[1.5,8,-1.9],[7,1.1,1.8],3)
    m.box('sword',[3.7,-7,-1.6],[2.6,15,1.1],14)
    m.box('sword',[4.5,-9,-1.6],[1,2,1.1],2)
    m.box('sword',[4.8,-5,-1.85],[.5,11,.3],11)
    b(m,'guard','arm_-1_forearm',[-5,16,-2],[-7.2,12,-3],[4.4,7,1],1)
    m.box('guard',[-5.5,13,-3.4],[1,5,.5],3)
    for side in (-1,1):
        n=f'cape_{side}';b(m,n,'body',[side*2.2,25,3],[side*2.2-2,8+(side==1)*2,3],[4,17-(side==1)*2,.8],13,[8,0,side*5])
        for j in range(2):m.box(n,[side*2.2-1.8+j*2,5+j*2,3.4],[1.5,5,.6],7)
    a=common(m,.6,'body')
    for state,speed in [('walk',1),('run',1.5)]:
        a[state]=clip(1/speed,{'leg_-1':{'rotation':oscillate(22)},'leg_1':{'rotation':oscillate(-22)},'arm_-1':{'rotation':oscillate(-12)},'arm_1':{'rotation':oscillate(9)},'cape_-1':{'rotation':oscillate(7)},'cape_1':{'rotation':oscillate(-6)}} ,True)
    a['attack']=clip(1.25,{'body':action(.6,[0,-30,0],[0,42,0]),'arm_1':action(.6,[-45,0,-60],[30,0,40]),'sword':action(.6,[-25,0,0],[22,0,0]),'cape_1':action(.6,[0,-12,0],[0,25,0])})
    a['attack_two']=clip(1.25,{'body':action(.6,[0,35,0],[0,-40,0]),'arm_1':action(.6,[25,0,60],[-60,0,-35]),'sword':action(.6,[15,0,0],[-28,0,0])})
    a['heavy']=clip(1.6,{'body':action(.6,[-16,0,0],[25,0,0]),'arm_1':action(.6,[-145,0,-15],[40,0,8]),'arm_-1':action(.6,[-90,0,30],[20,0,0]),'sword':action(.6,[-30,0,0],[35,0,0])})
    a['guard']=clip(1,{'arm_-1':{'rotation':[ -55,0,-20]},'arm_1':{'rotation':[-25,0,-30]},'body':{'rotation':[0,15,0]}},True)
    a['cast']=a['heavy']
    a['death']=clip(2.2,{'body':{'rotation':{'0':[0,0,0],'.7':[18,0,0],'1.3':[18,0,0],'2.2':[80,0,-8]},'position':{'0':[0,0,0],'1.3':[0,-8,0],'2.2':[0,-15,0]}},'arm_1':{'rotation':{'0':[0,0,0],'1.2':[30,0,25]}},'sword':{'rotation':{'0':[0,0,0],'1.2':[35,0,0]}}})
    return m,a


def imp():
    m=Model('flame_imp')
    b(m,'body','root',[0,7,0],[-2.2,4,-1.7],[4.4,5,3.4],0,[0,0,-6])
    m.box('body',[-1.4,4.5,-2],[2.8,3,.4],12)
    b(m,'head','body',[0,9,0],[-2.8,8.5,-2],[5.6,3.7,4],0,[0,0,8])
    m.box('head',[-1.8,8.1,-2.8],[3.6,1.4,1],1)
    for side in (-1,1):
        m.box('head',[side*1.3-.6,10,-2.3],[1.2,.7,.5],4)
        m.box('head',[side*2.1-.5,11.5,-.7],[1,2.2,1],6,[0,0,side*-25],[side*2,11.5,0])
        m.box('head',[side*2.8-.7,9.5,-.7],[1.4,1,2],7,[0,0,side*20],[side*2,10,0])
        n=f'arm_{side}';b(m,n,'body',[side*2.2,8,0],[side*2.8-.65,4,-1],[1.3,4,1.5],0,[0,0,side*28])
        b(m,n+'_hand',n,[side*3,4,0],[side*3-1,3,-1.5],[2,1.5,2],1)
        for j in range(3):m.box(n+'_hand',[side*3-1+j*.7,2.5,-1.9],[.5,1,.9],6)
        b(m,f'leg_{side}','body',[side*1.2,5,0],[side*1.2-.7,1.5,-.5],[1.4,3.5,1.8],1,[15,0,side*10])
        m.box(f'leg_{side}',[side*1.2-.9,1,-1.8],[1.8,1,2.8],6)
        n=f'wing_{side}';b(m,n,'body',[side*1.8,8,1],[min(side*2,side*6),7.8,1],[4,.65,.65],14,[0,side*-12,side*15])
        for j in range(3):
            x=side*(4+j*1.2)
            m.box(n,[x-.35,4.5-j*.4,1],[.7,4+j*.5,.7],14,[0,0,side*(-22+j*16)],[x,8,1])
        m.box(n,[min(side*3,side*7),5,1.2],[4,3,.35],7)
        b(m,n+'_tip',n,[side*7,8,1],[min(side*7,side*10),5.8,1],[3,2.3,.4],13,[0,0,side*20])
    b(m,'tail','body',[0,4,1],[-.5,3,1],[1,1,4],0,[28,20,0])
    b(m,'tail_tip','tail',[0,3,4.5],[-.4,3,4.5],[.8,1,3],1,[-30,25,0])
    m.box('tail_tip',[-.8,3,7],[1.6,1.4,1.4],12,[0,0,45],[0,3.7,7.7])
    a=common(m,.7,'body')
    for state,speed in [('idle',1),('hover',1.5),('fly',2),('walk',1),('run',2)]:
        a[state]=clip(1/speed,{'wing_-1':{'rotation':oscillate(32,2)},'wing_1':{'rotation':oscillate(-32,2)},'wing_-1_tip':{'rotation':oscillate(-20,2)},'wing_1_tip':{'rotation':oscillate(20,2)},'body':{'position':{'0':[0,0,0],'.5':[0,.7,0],'1':[0,0,0]}},'tail':{'rotation':oscillate(20,1)},'head':{'rotation':oscillate(7,2)}},True)
    for s in ['attack','cast','heavy']:
        a[s]=clip(1.2,{'arm_1':action(.7,[-110,0,-35],[35,0,0]),'arm_-1':action(.7,[-50,0,25],[-70,0,-20]),'head':action(.7,[-12,-18,0],[14,15,0]),'tail':action(.7,[0,-35,0],[0,40,0])})
    return m,a


def common(m,t,focus):
    a={'idle':clip(1,{focus:{'rotation':oscillate(2)}},True)}
    a['walk']=a['idle'];a['run']=a['idle']
    for s in ('attack','heavy','cast'):a[s]=clip(t+.5,{focus:action(t,[-15,0,0],[20,0,0])})
    a['hurt']=clip(.45,{focus:{'rotation':{'0':[0,0,0],'.1':[-12,0,8],'.45':[0,0,0]}}})
    a['death']=clip(1.5,{'root':{'rotation':{'0':[0,0,0],'1.5':[0,0,85]},'position':{'0':[0,0,0],'1.5':[0,-2,0]}}})
    return a


def main():
    for build,w,h in [(basilisk,1.2,.85),(spider,1.4,1.1),(wraith,.7,2),(knight,.8,2.1),(imp,.5,.8)]:
        m,a=build(); mats=list(MATERIALS)
        if m.name=='grave_knight':mats[:3]=['metal']*3
        if m.name=='shadow_wraith':mats[:3]=['cloth']*3
        if m.name=='crystal_spider':mats[:3]=['chitin']*3
        if m.name=='flame_imp':mats[:3]=['skin']*3
        # Normalize gait cycles to their speed-dependent clip duration.
        for anim in a.values():
            if anim.get('loop'):
                length=anim['animation_length']
                for transforms in anim['bones'].values():
                    for channel,frames in list(transforms.items()):
                        if isinstance(frames,dict):
                            end=max(float(t) for t in frames)
                            if end>length:
                                transforms[channel]={str(min(length,round(float(t)*length/end,8))):v for t,v in frames.items()}
        write_creature(m,PALETTES[m.name].split(),mats,a,w,h,glow=(4,11,12) if m.name!='cave_basilisk' else (4,),translucent=m.name=='shadow_wraith')

if __name__=='__main__':main()
