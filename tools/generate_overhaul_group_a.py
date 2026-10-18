#!/usr/bin/env python3
"""Original Group A sculpts, informed by the inspected Wesnoth portrait atlas.
All coordinates are model pixels; collision dimensions remain CreatureKind's.
"""
from overhaul_asset_pipeline import Model, clip, keys, write_creature
import overhaul_asset_pipeline as pipeline
from PIL import ImageDraw

BASE_ATLAS = pipeline.material_atlas

def refined_atlas(palette,materials,translucent=False):
    """Paint narrow seams and shaped highlights in the existing sixteen colors."""
    atlas=BASE_ATLAS(palette,materials,translucent)
    draw=ImageDraw.Draw(atlas)
    for index,role in enumerate(materials):
        x=index%4*32;y=index//4*32
        base=tuple(int(palette[index][i:i+2],16) for i in (0,2,4))
        def shade(delta):return tuple(max(0,min(255,v+delta)) for v in base)+(255,)
        if role in ("skin","fur"):
            draw.line([(x+6,y+12),(x+11,y+10),(x+18,y+10)],fill=shade(11),width=1)
            draw.line([(x+8,y+24),(x+18,y+25),(x+25,y+22)],fill=shade(-13),width=1)
        elif role=="leather":
            for k in (6,11,16,21,26):draw.line((x+k,y+26,x+k+1,y+27),fill=shade(19))
        elif role=="iron":
            draw.line([(x+4,y+22),(x+4,y+4),(x+26,y+4)],fill=shade(27),width=1)
            draw.line((x+6,y+27,x+26,y+27),fill=shade(-23),width=1)
        elif role=="stone":
            draw.line([(x+4,y+9),(x+12,y+7),(x+16,y+4)],fill=shade(14),width=1)
    return atlas

MATERIALS = ['skin','leather','iron','cloth','bone','fur','bark','glow','skin','iron','cloth','bone','leather','rune','stone','moss']
PALETTES = {
'goblin_scout':['58683c','3c3026','79776a','63543b','d1c69d','32352a','63503a','dab65d','778553','a2a08b','3e4931','ede1b2','795938','c2a267','686d5c','687449'],
'goblin_shaman':['536a42','423327','6b7565','45364f','d1c8a1','303c2d','65513a','8de16a','74875b','92967e','65516c','eee2ba','856643','b8e891','586658','607544'],
'orc_warrior':['64704d','483426','5a6261','613b34','d5c8a0','3a352d','5d4936','deae63','859069','8a928b','3c2928','eee0b5','846247','a78754','646a61','65704d'],
'minotaur':['77503a','49332b','a17b42','663d32','d5c69c','46352b','624733','d4a55b','986d4b','c5a264','382d2a','eee0ba','836343','b89b56','62675e','69704c'],
'stone_troll':['747d75','46514b','899389','4a554a','b0b8a4','39443c','535e4e','b0d18a','929d8b','aeb5a5','334237','ced4b8','6d7664','a6bb75','667267','526c40']}
SPECS={'goblin_scout':(.65,1.25,7),'goblin_shaman':(.65,1.55,16),'orc_warrior':(.95,2.15,18),'minotaur':(1.35,2.85,24),'stone_troll':(1.6,3.2,22)}

class Sculpt:
    def __init__(self,name,scale): self.m=Model(name); self.s=scale
    def bone(self,n,p,piv,rot=None): self.m.bone(n,p,[v*self.s for v in piv],rot)
    def box(self,n,o,s,mat=0,rot=None): self.m.box(n,[v*self.s for v in o],[v*self.s for v in s],mat,rot)

def frame(name):
    # Separate anatomical proportions rather than scaling one Steve-shaped mesh.
    gob=name.startswith('goblin'); bull=name=='minotaur'; troll=name=='stone_troll'
    h=20 if gob else 39 if bull else 39 if troll else 32
    a=Sculpt(name,SPECS[name][1]*16/h); B=a.bone; X=a.box
    hip=7 if gob else 15 if bull else 13 if troll else 12
    shoulder=13 if gob else 29 if bull else 31 if troll else 24
    breadth=3 if gob else 6 if bull else 8 if troll else 5.5
    B('body','root',(0,hip,0)); B('chest','body',(0,shoulder-4,0))
    X('body',(-breadth*.7,hip,-2),(breadth*1.4,shoulder-hip-3,4),0 if bull or troll else 1)
    X('chest',(-breadth,shoulder-5,-3),(breadth*2,6,6),0)
    # Scapula hump establishes a forward-facing head on goblins/giant.
    if gob or troll: X('chest',(-breadth,shoulder-2,0),(breadth*2,4,4),8)
    headY=shoulder+1
    B('head','chest',(0,headY,-1)); X('head',(-3,headY,-5),(6,5 if gob else 6,5),0)
    B('jaw','head',(0,headY+1,-3)); X('jaw',(-2.7,headY-.5,-5.6),(5.4,2,3),8)
    for side,sgn in [('left',1),('right',-1)]:
        lx=sgn*(2 if gob else 3.5 if not troll else 4)
        legw=2.6 if gob else 4.5 if bull else 5 if troll else 3.6
        armw=2.6 if gob else 4.5 if troll else 4
        B('leg_'+side,'root',(lx,hip,0)); X('leg_'+side,(lx-legw/2,2,-legw/2),(legw,hip-2,legw),5 if bull else 1 if gob else 0)
        B('foot_'+side,'leg_'+side,(lx,2,0)); X('foot_'+side,(lx-legw/2-.3,0,-3),(legw+.6,2.5,4.5),1 if bull else 12)
        if bull: X('foot_'+side,(lx-.2,0,-3.15),(.4,2.2,.25),5)
        ax=sgn*(breadth+1)
        B('arm_'+side,'chest',(ax,shoulder,0)); X('arm_'+side,(ax-armw/2,shoulder-6,-armw/2),(armw,6,armw),0)
        B('forearm_'+side,'arm_'+side,(ax,shoulder-5,0)); X('forearm_'+side,(ax-armw/2,shoulder-11,-armw/2),(armw,6,armw),8)
        B('hand_'+side,'forearm_'+side,(ax,shoulder-10,-1)); X('hand_'+side,(ax-1.6,shoulder-12,-2),(3.2,2,3.6),0)
        for digit in range(3): X('hand_'+side,(ax-1.3+digit*.95,shoulder-13,-2.2),(.65,1.8,1.2),8)
    for x in (-2,1):
        X('head',(x,headY+3,-5.25),(1.3,.6,.35),7 if name=='goblin_shaman' or troll else 5)
        X('head',(x-.25,headY+3.65,-5.35),(1.9,.7,.65),8,(0,0,-12 if x<0 else 12))
    return a,hip,shoulder,headY,breadth

def goblin(name):
    a,hip,sh,hy,w=frame(name); B=a.bone;X=a.box
    for side,sgn in [('left',1),('right',-1)]:
        B('ear_'+side,'head',(sgn*3,hy+3,-1)); X('ear_'+side,(3 if sgn>0 else -6,hy+2,-1.5),(3,1.7,1),0,(0,0,sgn*22))
        X('ear_'+side,(3.1 if sgn>0 else -5.8,hy+2.3,-1.65),(2.5,.8,.25),8)
    X('head',(-.75,hy+1.6,-7),(1.5,2,2.5),8,(15,0,0))
    for x in (-1.6,1.3): X('jaw',(x,hy+.6,-5.9),(.55,1,.5),4)
    X('body',(-3.1,hip,-2.3),(6.2,1.3,4.6),12)
    B('pouch','body',(-3,hip+1,0));X('pouch',(-4.5,hip-1,-1),(2,3,2.5),1);X('pouch',(-4.7,hip+1,-1.2),(2.4,.6,2.8),12)
    if name=='goblin_scout':
        X('chest',(-2.8,sh-4,-3.2),(1,6,.6),12,(0,0,-26)); X('arm_left',(3,sh-2,-2.2),(3,2.5,4.4),2,(0,0,15))
        B('dagger','hand_right',(-4,sh-12,-2));X('dagger',(-4.5,sh-11,-2),(1,5,.7),9);X('dagger',(-5.4,sh-12,-2.2),(2.8,.6,1),2)
        X('head',(-3.2,hy+4.5,-4.6),(6.4,.7,4.5),1)
    else:
        for side,x in [('left',.2),('right',-3.4)]:
            B('robe_'+side,'body',(x+1.5,hip,0));X('robe_'+side,(x,2,-2.5),(3.2,hip-1,5),3)
        B('staff','hand_right',(-4,sh-11,-2)); X('staff',(-4.6,.2,-2.5),(1.1,sh+6,1.1),6,(0,0,-4))
        X('staff',(-6,sh+3,-3.2),(4,1.1,2.4),6);X('staff',(-5.3,sh+4,-3.1),(2.6,3,2.2),7,(0,0,25))
        B('talisman','chest',(0,sh-3,-3));X('talisman',(-.8,sh-5,-3.6),(1.6,2,.8),4);X('talisman',(-.4,sh-4.6,-3.8),(.8,.5,.3),5)
        B('rune','staff',(-4,sh+4,-2));X('rune',(-7.5,sh+3.8,-2),(1,1,.4),13); X('rune',(-1.5,sh+5,-2),(1,1,.4),13)
        X('head',(-.4,hy+1,-5.35),(.8,3.8,.3),11)
        X('head',(-2.8,hy+4.7,-3),(5.6,1,3),3)
    return a

def warrior():
    a,hip,sh,hy,w=frame('orc_warrior');B=a.bone;X=a.box
    X('jaw',(-3,hy-1,-6),(6,2.5,3),8)
    for x in (-2.5,1.7): X('jaw',(x,hy,-6.5),(.8,3.3,.8),4,(-12,0,0))
    X('chest',(-5.7,sh-5,-3.5),(11.4,4.8,1),2);X('body',(-4,hip,-2.7),(8,1.5,5.4),12)
    for i in range(3):X('chest',(-5.2+i*3.5,sh-4.4,-3.8),(2.8,.4,.4),9)
    X('arm_left',(4.5,sh-1.2,-3.1),(5,3,6),2,(0,0,12));X('arm_right',(-8,sh-2,-2.7),(4,2,5.4),5)
    B('shield','forearm_left',(7,sh-8,-2));X('shield',(4,sh-14,-4),(6,12,1.6),6);X('shield',(4,sh-14,-4.3),(6,1.2,.6),2);X('shield',(4,sh-3,-4.3),(6,1.2,.6),2);X('shield',(6.2,sh-9,-4.6),(1.6,2,1),9)
    B('cleaver','hand_right',(-6,sh-11,-1));X('cleaver',(-6.8,sh-19,-1),(1.2,14,1.2),12);X('cleaver',(-11,sh-7,-1.3),(6,5,1.8),2);X('cleaver',(-11,sh-7,-1.5),(.7,5,2),9)
    B('cape','chest',(0,sh,3));X('cape',(-4,hip+1,3.3),(8,sh-hip-1,.8),3,(8,0,0));X('cape',(-4,hip-1,3.3),(3,3,.8),10)
    return a

def bull():
    a,hip,sh,hy,w=frame('minotaur');B=a.bone;X=a.box
    X('head',(-3.3,hy-1,-7.3),(6.6,3.8,4),8);X('jaw',(-2.8,hy-1.3,-7.5),(5.6,1.5,2.5),1)
    for x in (-2.2,1.3):X('head',(x,hy+.5,-7.6),(.9,.8,.4),5)
    X('head',(-2,hy+4,-4),(4,2.5,4),5)
    X('chest',(-4,sh-1,0),(8,5,5),5)
    X('jaw',(-2,hy-3,-4),(4,2,2),5)
    for sgn in (-1,1):
        X('head',((3 if sgn>0 else -6),hy+1.5,-1),(3,1.6,2),0,(0,0,sgn*18))
    for side,sgn in [('left',1),('right',-1)]:
        B('horn_'+side,'head',(sgn*3,hy+4,-1));X('horn_'+side,((3 if sgn>0 else -7),hy+3,-1.5),(4,1.8,1.8),4,(0,0,sgn*25));X('horn_'+side,((6 if sgn>0 else -7.2),hy+4,-1.5),(1.2,3.3,1.4),11,(0,0,-sgn*15))
    X('chest',(-6.3,sh-4,-3.4),(12.6,2,1),2);X('body',(-4.5,hip,-2.5),(9,2,5),2)
    B('loincloth','body',(0,hip,0));X('loincloth',(-3,7,-2.9),(6,8,.8),3);X('loincloth',(-2.7,7,-3.1),(.5,8,.3),9)
    B('tail','body',(0,hip,2));X('tail',(-.65,hip-9,2.5),(1.3,10,1.3),0,(15,0,0));B('tail_tip','tail',(0,hip-8,3));X('tail_tip',(-1.4,hip-11,3),(2.8,3.5,2.8),5)
    B('axe','hand_right',(-7,sh-10,-2));X('axe',(-7.5,3,-2.5),(1.5,27,1.5),6);X('axe',(-14,24,-3),(14,5,2.5),2);X('axe',(-14,23,-3.2),(2,7,2.8),9);X('axe',(-2,23,-3.2),(2,7,2.8),9)
    return a

def troll():
    a,hip,sh,hy,w=frame('stone_troll');B=a.bone;X=a.box
    X('chest',(-8,sh-7,-4),(16,10,8),14,(0,0,-6));X('head',(-4,hy-1,-6),(8,7,6),14,(0,0,4))
    X('head',(-4,hy+3.6,-6.4),(8,1.2,1.5),1);X('jaw',(-3,hy-2,-6),(6,2.5,3),0)
    for side,sgn in [('left',1),('right',-1)]:
        ax=sgn*9
        X('arm_'+side,(ax-2,sh-7,-2.5),(4,8,5),14,(0,0,sgn*8));X('forearm_'+side,(ax-2.5,sh-16,-3),(5,10,6),0)
        X('hand_'+side,(ax-3,sh-18,-3.5),(6,4,7),14)
        for k in range(3):X('hand_'+side,(ax-2.6+k*1.8,sh-20,-3.8),(1.4,3,2),1)
    for i,(x,y,z) in enumerate([(-8,sh,1),(5,sh+1,0),(-5,sh+4,2),(2,sh-2,4),(-4,sh-8,4)]):
        X('chest',(x,y,z),(3+(i%2),4,3),14,(10,0,(-1)**i*18));X('chest',(x,y+3,z),(3,.6,3),15)
    # Mineral seams are deliberate stepped inlays, never random texture noise.
    for x,y in [(-5,sh-3),(-3,sh-4),(-1,sh-5),(1,sh-6)]:X('chest',(x,y,-4.3),(2,.45,.35),13)
    B('moss','chest',(-6,sh,2));X('moss',(-7,sh-6,3.8),(2,8,.6),15);X('moss',(-4,sh-4,4),(1.3,6,.6),15)
    B('boulder','hand_right',(-9,sh-16,0));X('boulder',(-12,sh-18,-2),(6,5,5),14,(15,8,12))
    return a

def polish(a,name):
    """Original finishing geometry, preserving all existing rig/attachment names.

    Fine layers are separated in depth to avoid coplanar flicker. Fingers curl
    around the existing handle center rather than introducing detached grips.
    """
    X=a.box; gob=name.startswith('goblin'); bull=name=='minotaur'; troll=name=='stone_troll'
    sh=13 if gob else 29 if bull else 31 if troll else 24
    hy=sh+1; width=3 if gob else 6 if bull else 8 if troll else 5.5
    # Cheek planes and inset eye whites/pupils, with heavy brows retained.
    face=-6.62 if troll else -5.64 if bull else -5.48
    for side,sgn in [('left',1),('right',-1)]:
        x=.9 if sgn>0 else -2.1
        X('head',(x,hy+2.82,face),(1.15,.66,.22),7 if troll or name=='goblin_shaman' else 4)
        X('head',(x+.39,hy+2.85,face-.13),(.36,.55,.16),5)
        X('head',(x+.14,hy+3.54,face+.05),(1.35,.35,.4),14 if troll else 8,(0,0,sgn*8))
        X('head',(sgn*2.25-.5,hy+.9,face+.12),(1,1.1,.45),14 if troll else 8,(0,sgn*16,sgn*9))
        ax=sgn*(width+1)
        # Thumb opposes the existing three fingers. Right hand wraps a handle.
        hand_y=sh-11.5
        X('hand_'+side,(ax+(.9 if sgn<0 else -1.7),hand_y,-2.45),(.8,1.35,1.25),8,(18,0,sgn*18))
        if not troll:
            for k in range(3):
                X('hand_'+side,(ax-1.3+k*.95,sh-12.5,-2.5),(.67,.65,1.5),0,(18,0,0))
            # Narrow cuffs mediate skin to leather, using existing colors.
            X('forearm_'+side,(ax-1.5,sh-9.3,-1.7),(3,.65,3.5),12 if gob or bull else 2)
        if gob:
            X('foot_'+side,(sgn*2-1.55,1.6,-3.12),(3.1,.55,.32),1)
    if name=='goblin_scout':
        # Rolled pauldron rim and grounded dagger hilt / pommel.
        X('arm_left',(3.05,sh-2.12,-2.5),(2.9,.48,.42),9,(0,0,15))
        X('dagger',(-4.44,sh-13.4,-2.04),(.88,1.65,.82),1)
        X('dagger',(-4.65,sh-13.65,-2.2),(1.3,.45,1.1),2)
        X('pouch',(-4.8,hip_for(name)+.75,-1.35),(2.6,.35,.3),12)
    elif name=='goblin_shaman':
        # Staff's grip is continuous with its wooden shaft; robe has sewn hems.
        for y in (sh-12,sh-11.3,sh-10.6):X('staff',(-4.73,y,-2.63),(1.36,.24,1.36),12)
        for side,x in [('left',.2),('right',-3.4)]:
            X('robe_'+side,(x,2,-2.65),(3.2,.55,.3),10)
            X('robe_'+side,(x+.15,3,-2.66),(.3,3,.25),10)
        X('talisman',(-.62,sh-4.85,-3.92),(1.24,.28,.24),11)
    elif name=='orc_warrior':
        # Stepped steel rim, corner rivets and shield side bindings.
        X('chest',(-5.4,sh-.55,-3.65),(10.8,.45,.45),9)
        for x in (-5.5,5.05):X('chest',(x,sh-4.8,-3.66),(.45,4.25,.4),9)
        for x in (4.05,9.45):X('shield',(x,sh-13.3,-4.43),(.5,10,.38),2)
        for x in (4.4,8.9):
            for y in (sh-12.7,sh-4.5):X('shield',(x,y,-4.6),(.55,.55,.3),9)
        X('cleaver',(-7,sh-12,-1.2),(1.6,2.6,1.6),1)
        X('cleaver',(-7.15,sh-12.3,-1.35),(1.9,.5,1.9),2)
    elif bull:
        # Horn root rings, muzzle lip and nostril planes keep bull anatomy.
        for side,sgn in [('left',1),('right',-1)]:
            X('horn_'+side,(2.9 if sgn>0 else -4,hy+2.9,-1.6),(1.1,1.95,2),4,(0,0,sgn*25))
        X('jaw',(-2.55,hy-.55,-7.7),(5.1,.4,.35),8)
        X('chest',(-6.05,sh-2.38,-3.6),(12.1,.4,.35),9)
        X('body',(-4.25,hip_for(name)+.2,-2.7),(8.5,.4,.35),9)
        for y in (sh-12,sh-11.3,sh-10.6):X('axe',(-7.65,y,-2.65),(1.8,.3,1.8),1)
    else:
        # Chisel planes expose joints, knuckles and lids without changing bulk.
        for side,sgn in [('left',1),('right',-1)]:
            ax=sgn*9
            for k in range(3):X('hand_'+side,(ax-2.55+k*1.8,sh-17.15,-3.78),(1.3,.8,.55),9)
            X('forearm_'+side,(ax-2.35,sh-9,-3.2),(4.7,.65,.5),14)
        X('head',(-3.65,hy+4.85,-6.5),(7.3,.45,.45),9)
        X('jaw',(-2.75,hy-1.35,-6.2),(5.5,.45,.45),1)
        for x,y in [(-5,sh-3),(-1,sh-5)]:X('chest',(x+.2,y+.5,-4.38),(.7,.8,.25),15)
    if name=='goblin_scout': scout_grip(a)
    return a


def scout_grip(a):
    """One rigid palm socket: hilt and curled fingers share every arm transform."""
    B=a.bone; X=a.box; scale=a.s
    B('grip_right','hand_right',(-4,.8,-1.65))
    a.m.by_name['dagger']['parent']='grip_right'
    # Replace the old straight fingers with a deliberately enclosed grip.
    hand=a.m.by_name['hand_right']
    palm=hand['cubes'][0]
    hand['cubes']=[palm]
    for i in range(3):
        y=.05+i*.58
        X('grip_right',(-5.1,y,-2.8),(1.7,.45,.65),0)
        X('grip_right',(-3.65,y,-2.7),(.55,.45,1.5),8)
    X('grip_right',(-5.2,1.35,-2.7),(.7,.7,1.55),8)
    # Short handle lies wholly in the enclosed palm, below the blade guard.
    dagger=a.m.by_name['dagger']
    dagger['cubes']=dagger['cubes'][:2]
    X('dagger',(-4.44,-.4,-2.04),(.88,1.65,.82),1)
    X('dagger',(-4.65,-.65,-2.2),(1.3,.45,1.1),2)
    # Stepped cranial cap and inset temples soften the original rectangular head.
    head=a.m.by_name['head']
    skull=head['cubes'][0]
    skull['size']=[5.4*scale,4.4*scale,4.6*scale]
    skull['origin']=[-2.7*scale,14*scale,-4.8*scale]
    X('head',(-2.3,18.25,-4.4),(4.6,.7,3.8),0)
    for sign in (-1,1):
        X('head',(sign*2.35-.4,14.8,-4.6),(.8,2.6,3.8),8,rot=(0,0,sign*9))


def hip_for(name):
    return 7 if name.startswith('goblin') else 15 if name=='minotaur' else 13 if name=='stone_troll' else 12

def animations(a,name):
    t=SPECS[name][2]/20; gob=name.startswith('goblin'); rate=570 if gob else 330 if name!='stone_troll' else 210
    secondary={'goblin_scout':['ear_left','ear_right','pouch'],'goblin_shaman':['ear_left','ear_right','pouch','robe_left','robe_right','talisman','rune'],'orc_warrior':['cape','shield'],'minotaur':['tail','tail_tip','loincloth'],'stone_troll':['moss']}[name]
    idle={'body':{'rotation':[3 if gob else 0,0,0],'position':[0,'math.sin(query.anim_time * 110) * 0.18',0]},'head':{'rotation':[0,'math.sin(query.anim_time * 55) * 4',0]},'jaw':{'rotation':['math.sin(query.anim_time * 110) * 2',0,0]}}
    if name=='minotaur':
        idle.update({'arm_left':{'rotation':[-25,0,-40]},'arm_right':{'rotation':[-20,0,15]},'forearm_left':{'rotation':[-30,0,0]},'forearm_right':{'rotation':[-20,0,0]}})
    for n in secondary: idle[n]={'rotation':['math.sin(query.anim_time * 105) * 3',0,'math.sin(query.anim_time * 75) * 2']}
    clips={'idle':clip(2,idle,True)}
    for state,mult,stride in [('walk',1,23),('run',1.5,40)]:
        r=rate*mult
        bones={'body':{'rotation':[12 if gob else 18 if name=='minotaur' and state=='run' else 5,0,f'math.sin(query.anim_time * {r}) * 3']},'head':{'rotation':[-5 if gob else 12 if name=='minotaur' and state=='run' else 0,0,0]}}
        for side,sgn in [('left',1),('right',-1)]:
            bones['leg_'+side]={'rotation':[f'math.sin(query.anim_time * {r}) * {stride*sgn}',0,0]}
            bones['arm_'+side]={'rotation':[f'math.sin(query.anim_time * {r}) * {-stride*.65*sgn}',0,-sgn*6]}
            bones['forearm_'+side]={'rotation':[-12,0,0]}
        for idx,n in enumerate(secondary):bones[n]={'rotation':[f'math.sin(query.anim_time * {r} - {30+idx*17}) * {4 if n=="shield" else 7}',0,f'math.sin(query.anim_time * {r} - 65) * 2']}
        for side,sgn in [('left',1),('right',-1)]:
            bones['foot_'+side]={'rotation':[f'math.sin(query.anim_time * {r} - 25) * {7*sgn}',0,0]}
        if name in ('orc_warrior','minotaur'):bones['arm_right']={'rotation':[-18 if name=='orc_warrior' else -20,0,12]}
        if name=='goblin_shaman':bones['arm_right']={'rotation':[-15,0,8]}
        clips[state]=clip(360/r,bones,True)
    for state in ('attack','heavy','cast'):
        heavy=state=='heavy'; caster=name=='goblin_shaman'; slam=name=='stone_troll'
        bones={'arm_right':{'rotation':keys(t,(-125,0,-20),(45,0,15),recovery=.4)},'forearm_right':{'rotation':keys(t,(-35,0,0),(15,0,0),recovery=.4)},'body':{'rotation':keys(t,(-14,-18,0),(20,22,0),recovery=.4)},'head':{'rotation':keys(t,(-8,10,0),(10,-12,0),recovery=.4)},'jaw':{'rotation':keys(t,(10,0,0),(18,0,0),recovery=.4)}}
        if name=='goblin_scout' and not heavy:
            bones['arm_right']={'rotation':keys(t,(-45,-30,-12),(-88,18,3),recovery=.4)}
            bones['forearm_right']={'rotation':keys(t,(-70,0,0),(8,0,0),recovery=.4)}
            bones['body']={'rotation':keys(t,(12,-22,-6),(20,16,4),recovery=.4)}
        if name=='minotaur':
            bones['arm_right']={'rotation':keys(t,(-75,-38,28),(35,48,20),recovery=.4)}
            bones['body']={'rotation':keys(t,(-8,-32,0),(18,35,0),recovery=.4)}
        if name=='orc_warrior' and not heavy:
            bones['arm_right']={'rotation':keys(t,(-85,-45,-30),(25,35,12),recovery=.4)}
            bones['shield']={'rotation':keys(t,(-18,-15,-8),(-10,15,-8),recovery=.4)}
        if heavy or caster or slam or name=='minotaur':bones['arm_left']={'rotation':keys(t,(-105,0,22),(35,0,-12),recovery=.4)}
        if name=='minotaur':bones['arm_left']={'rotation':keys(t,(-70,-25,-38),(35,40,-25),recovery=.4)}
        if caster:
            bones['staff']={'rotation':keys(t,(0,0,-25),(0,0,18),recovery=.4)}
            bones['rune']={'rotation':keys(t,(0,90,0),(0,180,0),final=(0,270,0),recovery=.4)}
            bones['talisman']={'rotation':keys(t,(-20,0,0),(28,0,0),recovery=.4)}
        for idx,n in enumerate(secondary):
            if n not in bones:
                bones[n]={'rotation':{'0.0':[0,0,0],str(round(t-.12,4)):[-4,0,-2],str(round(t,4)):[6,0,3],str(round(t+.13,4)):[-8,0,-3],str(round(t+.4,4)):[0,0,0]}}
        clips[state]=clip(t+.4,bones)
    clips['hurt']=clip(.4,{'body':{'rotation':keys(.08,(-4,0,0),(-15,0,8),recovery=.32)},'head':{'rotation':keys(.08,(0,0,0),(16,-8,0),recovery=.32)}})
    clips['death']=clip(.65,{'root':{'rotation':{'0.0':[0,0,0],'.14':[0,0,12],'.51':[0,0,86],'.65':[0,0,90]}},'arm_left':{'rotation':{'0.0':[0,0,0],'.18':[-20,0,-22],'.65':[15,0,-35]}},'jaw':{'rotation':{'0.0':[0,0,0],'.65':[20,0,0]}}})
    if name=='goblin_scout':
        clips['sneak']=clip(1.2,{'body':{'rotation':[22,0,-4]},'head':{'rotation':[-15,'math.sin(query.anim_time * 100) * 16',0]},'leg_left':{'rotation':['math.sin(query.anim_time * 300) * 15',0,0]},'leg_right':{'rotation':['-math.sin(query.anim_time * 300) * 15',0,0]}},True)
        clips['dodge']=clip(.45,{'body':{'rotation':keys(.18,(10,0,-12),(4,0,24),recovery=.27)},'root':{'position':keys(.18,(0,0,0),(2,0,0),recovery=.27)}})
    if name=='goblin_shaman': clips['ritual']=clip(2,{'arm_left':{'rotation':[-85,'math.sin(query.anim_time * 180) * 20',-25]},'staff':{'rotation':[0,0,'math.sin(query.anim_time * 180) * 15']},'rune':{'rotation':[0,'query.anim_time * 180',0]},'robe_left':{'rotation':['math.sin(query.anim_time * 180) * 6',0,0]}},True)
    if name=='minotaur': clips['charge']=clip(.6,{'body':{'rotation':[26,0,0]},'head':{'rotation':[18,0,0]},'arm_left':{'rotation':[-45,0,-35]},'arm_right':{'rotation':[-45,0,35]},'tail':{'rotation':[-25,'math.sin(query.anim_time * 600) * 18',0]}},True)
    if name=='stone_troll':
        clips['throw']=clip(t+.4,{'arm_right':{'rotation':keys(t,(-155,-20,-15),(65,15,10),recovery=.4)},'body':{'rotation':keys(t,(-15,-25,0),(25,25,0),recovery=.4)},'boulder':{'scale':{'0.0':[1,1,1],str(t-.05):[1,1,1],str(t):[.01,.01,.01],str(t+.4):[.01,.01,.01]}}})
    clips['guard']=clip(.8,{'arm_left':{'rotation':[-65,0,-15]},'arm_right':{'rotation':[-35,0,15]},'body':{'rotation':[4,-15,0]}},True)
    return clips

def main():
    pipeline.material_atlas=refined_atlas
    for name in SPECS:
        a=goblin(name) if name.startswith('goblin') else warrior() if name=='orc_warrior' else bull() if name=='minotaur' else troll()
        a=polish(a,name)
        w,h,_=SPECS[name]
        materials=list(MATERIALS)
        if name=='stone_troll':
            for i in (0,1,2,4,5,6,8,9,11,12,14): materials[i]='stone'
        if name=='minotaur':
            materials[0]=materials[8]='fur'; materials[2]=materials[9]='iron'
        write_creature(a.m,PALETTES[name],materials,animations(a,name),w,h,glow=(7,13) if name in ('goblin_shaman','stone_troll') else ())

if __name__=='__main__':main()
