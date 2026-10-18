#!/usr/bin/env python3
"""Original expansion art: dragon mage, succubus, valkyrie and nine-tail spirit.

Independently authored geometry and pixel painting. No third-party assets.
Run with Python 3 + Pillow from any working directory. Gameplay is external.
"""
import math
import itertools
from pathlib import Path
from PIL import Image, ImageDraw
import overhaul_asset_pipeline as pipeline
from overhaul_asset_pipeline import Model, clip, keys, write_creature

ROOT=Path(__file__).resolve().parents[1]
SPECS={
 'ender_dragon_girl':(.85,2.05,1.1),
 'succubus':(.75,1.9,1.1),
 'valkyrie':(.8,2,.7),
 'fox_spirit_girl':(.75,1.85,.8),
}
# Skin, shadow, costume, trim, luminous iris, outline, ivory, accent,
# warm skin, hair, leather, rune, highlight, inner cloth, metal, catchlight.
PALETTES={
 'ender_dragon_girl':['ac9aae','282436','211e2d','76627f','bf76ff','161420','d8cfcb','322b3c','c9afbd','211e2b','393141','b78bee','615269','362638','777180','f5eaff'],
 'succubus':['d4a79e','342131','28212c','a88a60','e49f9c','241722','e3cbb3','8c3049','efc2ae','d5b56c','53313a','e46a9b','ead293','4a263a','97838a','ffe5c6'],
 'valkyrie':['d3b5ab','34343e','8c99a7','c7b895','7ec3e7','21222e','dce1e2','963f4e','e9cbb6','cbcbd6','45404a','9bc5df','c1cbd2','4a4856','626c7d','fff2dc'],
 'fox_spirit_girl':['dfb49a','684231','a83b3c','d6aa58','76c77f','33252b','f2e1bd','c45e42','f2cdb0','d4a65d','68494a','b3e3a1','f4d592','692e3c','8d765e','fff2d2'],
}
MATERIALS={
 'ender_dragon_girl':['skin','scale','cloth','metal','glow','stone','horn','membrane','skin','hair','leather','rune','scale','cloth','metal','bone'],
 'succubus':['skin','horn','cloth','metal','glow','stone','bone','membrane','skin','hair','leather','rune','hair','cloth','metal','bone'],
 'valkyrie':['skin','feather','metal','metal','glow','stone','bone','cloth','skin','hair','leather','rune','metal','cloth','metal','bone'],
 'fox_spirit_girl':['skin','fur','cloth','metal','glow','stone','fur','cloth','skin','hair','leather','rune','fur','cloth','metal','bone'],
}
BASE_ATLAS=pipeline.material_atlas
ACTIVE_NAME=None


def painted_atlas(palette,materials,translucent=False):
    """Directional brushed metals, embroidery, strands and species insignia."""
    image=BASE_ATLAS(palette,materials,translucent);d=ImageDraw.Draw(image)
    for tile,role in enumerate(materials):
        x=tile%4*32;y=tile//4*32
        rgb=tuple(int(palette[tile][i:i+2],16) for i in (0,2,4))
        def ink(delta):return tuple(max(0,min(255,c+delta)) for c in rgb)+(255,)
        if role in ('cloth','leather'):
            # Woven grain, shaped brocade and hem stitching.
            for yy in range(5,28,4):
                for xx in range(5,28,4):d.point((x+xx,y+yy),fill=ink(8 if (xx+yy)%8 else -9))
            for xx in (7,24):
                d.line((x+xx,y+4,x+xx,y+27),fill=ink(20))
                for yy in (7,13,19,25):d.line((x+xx-1,y+yy,x+xx+1,y+yy+1),fill=ink(35))
            # Each species has its own recognisable original brocade symbol.
            if ACTIVE_NAME=='ender_dragon_girl':
                d.line([(x+12,y+22),(x+16,y+7),(x+21,y+22),(x+12,y+22)],fill=ink(29))
                d.line([(x+13,y+18),(x+20,y+18),(x+16,y+24)],fill=ink(17))
            elif ACTIVE_NAME=='succubus':
                d.arc((x+10,y+8,x+22,y+22),15,345,fill=ink(32));d.line((x+16,y+13,x+16,y+25),fill=ink(24))
            elif ACTIVE_NAME=='valkyrie':
                d.line([(x+11,y+10),(x+16,y+15),(x+21,y+10),(x+16,y+23),(x+11,y+10)],fill=ink(31))
            else:
                d.line([(x+10,y+12),(x+13,y+9),(x+16,y+13),(x+19,y+9),(x+22,y+12)],fill=ink(31))
                d.arc((x+11,y+12,x+21,y+23),0,180,fill=ink(31))
        elif role=='hair':
            for xx in (5,10,16,22,27):
                d.line([(x+xx,y+4),(x+xx-1,y+13),(x+xx+1,y+24),(x+xx,y+28)],fill=ink(-17))
                d.line([(x+xx+1,y+5),(x+xx+2,y+12),(x+xx+1,y+18)],fill=ink(22))
            d.arc((x+4,y+5,x+27,y+18),190,340,fill=ink(33))
        elif role=='membrane':
            d.line([(x+4,y+4),(x+15,y+15),(x+27,y+27)],fill=ink(-25),width=2)
            for yy in (10,17,24):
                d.line([(x+6,y+yy),(x+15,y+15),(x+26,y+yy-4)],fill=ink(17))
            d.arc((x+6,y+5,x+27,y+27),85,175,fill=ink(25))
        elif role=='metal':
            d.line([(x+4,y+25),(x+4,y+5),(x+26,y+5)],fill=ink(45))
            d.line([(x+7,y+26),(x+25,y+26),(x+25,y+8)],fill=ink(-27))
            d.polygon([(x+13,y+12),(x+16,y+8),(x+19,y+12),(x+16,y+18)],outline=ink(32))
            for xx,yy in ((7,8),(24,8),(7,24),(24,24)):d.point((x+xx,y+yy),fill=ink(60))
        elif role=='feather':
            for xx in (7,16,25):
                d.line((x+xx,y+5,x+xx-1,y+28),fill=ink(26))
                for yy in (8,12,16,20,24):
                    d.line((x+xx,y+yy,x+xx-5,y+yy-3),fill=ink(12))
                    d.line((x+xx+1,y+yy,x+xx+5,y+yy-4),fill=ink(-19))
        elif role=='fur':
            for yy in range(5,27,6):
                for xx in (6,14,23):d.line([(x+xx-2,y+yy),(x+xx,y+yy+4),(x+xx+2,y+yy+1)],fill=ink(20))
        elif role=='skin':
            d.arc((x+7,y+8,x+26,y+26),35,115,fill=ink(-11))
            d.rectangle((x+7,y+6,x+20,y+8),fill=ink(9))
    return image


class Sculpt:
    def __init__(self,name):
        self.m=Model(name);self.scale=SPECS[name][1]*16/32
    def B(self,n,p,v,rot=None):self.m.bone(n,p,[x*self.scale for x in v],rot)
    def X(self,n,o,s,mat=0,rot=None,piv=None):
        self.m.box(n,[x*self.scale for x in o],[x*self.scale for x in s],mat,rot,[x*self.scale for x in piv] if piv else None)


def adult_frame(a):
    """Shared joint convention; each costume, face, hair and species is authored below."""
    name=a.m.name;B=a.B;X=a.X
    proportions={
        'ender_dragon_girl':(2.45,2.9,2.05,5.2,5.5),
        'succubus':(2.65,3.05,1.95,5.1,5.3),
        'valkyrie':(2.7,3.3,2.3,5.3,5.5),
        'fox_spirit_girl':(2.6,2.8,2,5.6,5.1),
    }
    hip,shoulder,waist,facew,faceh=proportions[name]
    B('body','root',[0,12.5,0]);B('chest','body',[0,20,0])
    X('body',[-hip,12,-1.8],[hip*2,4.2,3.6],2)
    X('body',[-hip+.4,12,-2],[hip*2-.8,2,4],13)
    X('body',[-waist,15.5,-1.65],[waist*2,4.5,3.3],2)
    X('chest',[-shoulder,19,-1.9],[shoulder*2,4.4,3.8],2)
    X('chest',[-shoulder+.45,22.8,-1.6],[shoulder*2-.9,1.1,3.2],8)
    for side in (-1,1):
        # Covered breast forms merge into a continuous bodice, underbust and collar.
        X('chest',[side*1.45-1.45,19.7,-2.65],[2.9,2.7,2],2,[0,side*8,-side*7])
    X('chest',[-2.2,19.1,-2.4],[4.4,.7,1],3)
    B('neck','chest',[0,23.5,0]);X('neck',[-.9,23.3,-.9],[1.8,2.2,1.8],8)
    B('head','neck',[0,25.4,0]);X('head',[-facew/2,25,-2.25],[facew,faceh,4.5],0)
    X('head',[-facew/2+.5,24.7,-2],[facew-1,1.2,4],8)
    # Distinct eyelid inclinations, iris shapes, mouth and cheek contour per face.
    eyey=27.35 if name=='fox_spirit_girl' else 27.6
    irisw=.55 if name=='ender_dragon_girl' else .7 if name=='succubus' else .63
    for side in (-1,1):
        center=side*1.18
        X('head',[center-.82,eyey-.12,-2.37],[1.64,1.12,.15],5)
        X('head',[center-.7,eyey,-2.49],[1.4,.83,.12],6)
        X('head',[center-irisw/2,eyey+.02,-2.59],[irisw,.8,.12],4)
        X('head',[center-.1,eyey+.05,-2.68],[.2,.65,.08],5)
        X('head',[center-.25,eyey+.53,-2.77],[.2,.2,.07],15)
        angle=side*(11 if name=='ender_dragon_girl' else 5 if name=='succubus' else -4 if name=='fox_spirit_girl' else 8)
        X('head',[center-.88,eyey+.88,-2.55],[1.75,.18,.15],9,[0,0,angle])
    X('head',[-.22,26.65,-2.55],[.44,.65,.38],8)
    X('head',[-.49,25.8,-2.34],[.98,.17,.15],7)
    if name=='succubus':X('head',[.25,25.85,-2.54],[.23,.35,.14],6,[0,0,-12])
    for side,n in ((-1,'right'),(1,'left')):
        B('arm_'+n,'chest',[side*(shoulder+.1),22.6,0])
        X('arm_'+n,[side*(shoulder+.65)-1,17.8,-1],[2,5.3,2],8,[0,0,-side*5])
        X('arm_'+n,[side*(shoulder+.6)-1.25,21,-1.25],[2.5,2.2,2.5],2,[0,0,-side*12])
        B('forearm_'+n,'arm_'+n,[side*(shoulder+.85),18.1,0])
        X('forearm_'+n,[side*(shoulder+.85)-.85,14.3,-.9],[1.7,4,1.8],10)
        B('hand_'+n,'forearm_'+n,[side*(shoulder+.85),14.4,0])
        X('hand_'+n,[side*(shoulder+.85)-.83,12.8,-.85],[1.66,1.8,1.7],8 if name=='fox_spirit_girl' else 10)
        # One visible finger-equivalent gripping/gesturing plate and articulated thumb.
        X('hand_'+n,[side*(shoulder+.85)-.75,12.4,-1],[1.5,.65,1.3],8 if name=='fox_spirit_girl' else 1,[12,0,0])
        X('hand_'+n,[side*(shoulder+.85)-side*.75-.3,13.2,-1.2],[.6,1,.65],8 if name=='fox_spirit_girl' else 10,[0,0,-side*20])
        B('leg_'+n,'body',[side*1.35,12.8,0])
        X('leg_'+n,[side*1.35-.98,7,-1],[1.96,5.8,2],13)
        B('shin_'+n,'leg_'+n,[side*1.35,7,0]);X('shin_'+n,[side*1.35-.8,1.7,-.85],[1.6,5.5,1.7],10)
        B('foot_'+n,'shin_'+n,[side*1.35,1.7,0]);X('foot_'+n,[side*1.35-1,0,-2],[2,2,3.2],10)
        X('foot_'+n,[side*1.35-.8,.1,-2.4],[1.6,1.1,1.1],3)


def hair(a):
    name=a.m.name;X=a.X;B=a.B
    w=5.9 if name=='fox_spirit_girl' else 5.7
    # Complete cap covers top AND upper sides, with a softly stepped crown.
    X('head',[-w/2,29.55,-2.6],[w,1.65,5.2],9)
    X('head',[-w/2+.5,31.1,-2.15],[w-1,.65,4.3],12 if name=='succubus' else 9)
    for side in (-1,1):
        X('head',[side*2.45-.55,28.4,-1.4],[1.1,2.2,3.2],9)
        X('head',[side*.9-1,28.9,-2.75],[2,1.5,1],9,[0,0,-side*(19 if name=='fox_spirit_girl' else 12)])
    length=13 if name=='ender_dragon_girl' else 15 if name=='succubus' else 11.5 if name=='valkyrie' else 12.2
    for i in range(5):
        x=(i-2)*1.05;bottom=30-length+abs(i-2)*.8
        B('hair_back_'+str(i),'head',[x,30,2])
        X('hair_back_'+str(i),[x-.7,bottom,1.65],[1.4,30-bottom,1.5],9,[4,0,(i-2)*2])
        X('hair_back_'+str(i),[x-.48,bottom-.6,1.8],[.96,2,1.2],12 if name=='fox_spirit_girl' else 9,[5,0,(i-2)*3])
    for side,n in ((-1,'right'),(1,'left')):
        B('hair_side_'+n,'head',[side*2.55,29.8,-1.5])
        X('hair_side_'+n,[side*2.6-.7,19.5 if name!='valkyrie' else 21,-2.05],[1.4,10.5 if name!='valkyrie' else 9,1.55],9,[0,0,-side*4])
        X('hair_side_'+n,[side*2.6-.43,18.8 if name!='valkyrie' else 20.5,-1.95],[.86,2.2,1.25],12 if name=='succubus' else 9)


def membrane_wings(a,dragon):
    X=a.X;B=a.B
    for side,n in ((-1,'right'),(1,'left')):
        B('wing_'+n,'chest',[side*2.3,22,1.5])
        X('wing_'+n,[side*3.6-.65,19.8,1.4],[1.3,4,1.3],1,[0,0,-side*38])
        B('wingtip_'+n,'wing_'+n,[side*5.1,20.1,2])
        X('wingtip_'+n,[side*7.3-.6,18.6,1.6],[1.2,5,1.1],1,[0,0,-side*65])
        # Segmented broad membrane bays share their attachment line and overlap.
        # Each bay has a diagonal outer rib plus a tapered stepped trailing edge.
        for j in range(3):
            x=side*(6.7+j*3.5);top=21.2-j*.6
            height=(8.2,10.2,8.3)[j] if dragon else (7.8,9.3,7.1)[j]
            X('wingtip_'+n,[x-2.2,top-height,2.05],[4.4,height,.42],7,[0,0,-side*(10+j*5)])
            X('wingtip_'+n,[x-1.45,top-height-1.25,2.07],[2.9,2.2,.38],7,[0,0,-side*(10+j*5)])
            X('wingtip_'+n,[x-.7,top-height-2.1,2.08],[1.4,1.8,.35],7,[0,0,-side*(10+j*5)])
            X('wingtip_'+n,[x-.32,top-height-.8,1.75],[.64,height+1.8,.8],1,[0,0,-side*(11+j*5)])
        X('wing_'+n,[side*3.8-1.7,16,2.05],[3.4,5.5,.45],7,[0,0,-side*18])
        # No detached terminal decorations: the dark bay ribs already provide
        # the supported outer edge. Pale material is reserved for head horns.


def connected_tail(a,dragon):
    """Collinear local beams overlap their real joints, without cube rotations.

    Curvature belongs to the hierarchical bones. GeckoLib's cube X convention
    differs from a naive Y-up Euler preview, so never tilt isolated tail cubes.
    Every child pivot lies on its parent's unrotated beam centerline; both sides
    inherit the same ancestor transform and cannot separate when animated.
    """
    B=a.B;X=a.X
    y=13 if dragon else 12.5
    zs=(1.8,6.5,11.5,16) if dragon else (2,6.5,10,13.4)
    widths=(1.6,1.2,.8) if dragon else (.9,.7,.5)
    names=('tail_base','tail_mid','tail_tip')
    for i,n in enumerate(names):
        w=widths[i];start=[0,y,zs[i]]
        B(n,'body' if i==0 else names[i-1],start,[-8 if i==0 else -6,0,0])
        X(n,[-w/2,y-w/2,zs[i]-.4],[w,w,zs[i+1]-zs[i]+.8],12 if dragon and i==2 else 1)
    size=1.5 if dragon else 1.3
    X('tail_tip',[-size/2,y-size/2,zs[-1]-.8],[size,size,1.8],7,[0,45,0])


def dragon_tail(a):
    connected_tail(a,True)


def ender():
    a=Sculpt('ender_dragon_girl');adult_frame(a);hair(a);X=a.X;B=a.B
    for side,n in ((-1,'right'),(1,'left')):
        B('horn_'+n,'head',[side*1.8,30.5,.1])
        # Large pale horns sweep out, then unmistakably forward over the brow.
        X('horn_'+n,[side*2-.65,30.3,-.4],[1.3,3.1,1.5],6,[17,0,-side*27])
        X('horn_'+n,[side*2.8-.55,32,-2],[1.1,2.5,2.1],6,[43,0,-side*12])
        X('horn_'+n,[side*2.9-.32,32.7,-4.1],[.64,1.2,2.5],6,[12,0,0])
        X('chest',[side*2.7-.5,21.4,-1.4],[1,2.6,2.7],12,[0,0,-side*28])
        X('body',[side*2-.65,12.5,-2.2],[1.3,5.2,.65],3,[0,0,-side*12])
        B('skirt_'+n,'body',[side*1.5,14,0]);X('skirt_'+n,[side*1.6-1.55,3.8,-1.8],[3.1,10.4,3.6],2,[0,0,-side*7])
        X('skirt_'+n,[side*2.8-.25,3.8,-2],[.5,10,.55],7,[0,0,-side*7])
        # Dark dragon claws stay part of the palm.
        for j in range(2):X('hand_'+n,[side*3.75-.65+j*.8,11.6,-1.15],[.5,1.3,.65],6,[-15,0,0])
    X('chest',[-.75,21.3,-3],[1.5,1.7,.55],11,[0,0,45])
    membrane_wings(a,True);dragon_tail(a)
    return a.m


def succubus():
    a=Sculpt('succubus');adult_frame(a);hair(a);B=a.B;X=a.X
    for side,n in ((-1,'right'),(1,'left')):
        B('horn_'+n,'head',[side*1.9,30.5,.2])
        for j,(dx,y,z,ang) in enumerate(((0,30.3,.2,-34),(.9,32.2,.3,-8),(.8,34,.2,35))):
            X('horn_'+n,[side*(1.9+dx)-(.55 if j<2 else .35),y,z],[1.1 if j<2 else .7,2.7 if j<2 else 2,1.1 if j<2 else .7],1,[0,0,side*ang])
        B('gown_'+n,'body',[side*1.45,14,0])
        X('gown_'+n,[side*1.55-1.8,1,-2.15],[3.6,13.2,4.3],2,[0,0,-side*7])
        X('gown_'+n,[side*2.8-.4,1,-2.3],[.8,12.6,.6],7,[0,0,-side*7])
        X('gown_'+n,[side*1.7-1.5,1.1,-2.4],[3,1,.6],3)
        X('forearm_'+n,[side*3.9-1.1,14.4,-1.1],[2.2,4.1,2.2],2)
        B('earring_'+n,'head',[side*2.7,26.7,0]);X('earring_'+n,[side*2.7-.3,24.7,-.25],[.6,2,.5],3)
        X('earring_'+n,[side*2.7-.35,24.5,-.4],[.7,.8,.45],11,[0,0,45])
    X('body',[-2.1,16,-2],[4.2,1,4],3)
    X('chest',[-.6,22.4,-2.6],[1.2,1.2,.6],7,[0,0,45])
    membrane_wings(a,False)
    connected_tail(a,False)
    return a.m


def feather_wings(a):
    B=a.B;X=a.X
    for side,n in ((-1,'right'),(1,'left')):
        B('wing_'+n,'chest',[side*2.6,22.3,1.9]);X('wing_'+n,[side*3.5-.9,19.6,1.8],[1.8,4,1.7],1,[0,0,-side*35])
        B('wingtip_'+n,'wing_'+n,[side*5.1,20.5,2.3]);X('wingtip_'+n,[side*7.1-.7,18.6,2],[1.4,4,1.3],1,[0,0,-side*60])
        for j in range(4):
            x=side*(3.4+j*1.1)
            X('wing_'+n,[x-1.15,16.2-j*.25,1.45],[2.3,6,.85],1,[0,0,side*(14+j*6)])
        for j in range(7):
            x=side*(6.2+j*.9);y=20-j*.38;length=9+(3-abs(3-j))*.65;p=[x,y,2.5];angle=side*(24+j*6)
            X('wingtip_'+n,[x-1.15,y-length*.75,2.45],[2.3,length*.75,.85],1,[0,0,angle],p)
            X('wingtip_'+n,[x-.7,y-length-1,2.5],[1.4,length*.32+1,.7],5,[0,0,angle],p)
            X('wingtip_'+n,[x-1.1,y-3.1,1.8],[2.2,3.4,.7],1,[0,0,angle],p)


def valkyrie():
    a=Sculpt('valkyrie');adult_frame(a);hair(a);X=a.X;B=a.B
    # Fitted silver breastplate with beveled shoulders, red waist and faulds.
    X('chest',[-2.5,21.8,-2.5],[5,1.2,.7],12)
    X('body',[-2.5,15,-2],[5,1.3,4],7)
    for side,n in ((-1,'right'),(1,'left')):
        X('arm_'+n,[side*3.6-1.4,21.2,-1.5],[2.8,2.8,3],12,[0,0,-side*18])
        X('arm_'+n,[side*4-1,20.5,-1.7],[2,1.3,3.2],14,[0,0,-side*12])
        X('shin_'+n,[side*1.35-1,2.2,-1.05],[2,4.7,2.1],2)
        X('shin_'+n,[side*1.35-.7,5.9,-1.2],[1.4,1.6,.7],12,[0,0,side*9])
        B('fauld_'+n,'body',[side*1.8,14.5,0]);X('fauld_'+n,[side*2-1.35,10,-2.2],[2.7,4.6,4.4],2,[0,0,-side*13])
        X('fauld_'+n,[side*2-1.25,10,-2.35],[2.5,.65,.6],3)
        X('head',[side*2.45-.6,27.8,-1.6],[1.2,3,3.2],2)
        # Helmet winglets form a distinct swept profile, not a hidden hair cap.
        for j in range(2):X('head',[side*(2.7+j*.65)-.5,30.1+j*.35,.1],[1,2.8-j*.4,1.1],12,[0,0,-side*(32+j*15)])
    X('head',[-2.3,30.4,-2.5],[4.6,.8,4.8],2)
    X('head',[-.45,29.2,-2.75],[.9,2.1,.6],3,[0,0,0])
    # Sword grip is inside the right palm; all geometry inherits the wrist.
    # Hand center x=-4.15,y13.5, grip extends along local Z through the palm.
    B('sword','hand_right',[-4.15,13.5,-.1])
    X('sword',[-4.5,13.12,-1.8],[.7,.75,3.6],10)
    X('sword',[-4.8,12.9,-2.3],[1.3,1.2,.7],3)
    X('sword',[-6.3,13.1,1.5],[4.3,.8,.7],3)
    X('sword',[-4.7,13.2,2],[1.1,.55,9.6],2)
    X('sword',[-4.4,13.1,2],[.5,.75,9.7],12)
    X('sword',[-4.5,13.25,11.3],[.7,.45,1.8],12,[0,25,0])
    # Finger curl closes visibly around the actual handle, not the blade.
    X('hand_right',[-5.05,12.75,-1.05],[.65,1.35,1.6],2)
    X('hand_right',[-4.65,12.6,-.8],[1.2,.5,1.3],2)
    B('shield','forearm_left',[4.25,16,-1.2])
    X('shield',[3.55,14.6,-2.4],[1.4,2.4,1.6],10)
    X('shield',[2.6,12.1,-3.1],[3.3,6.7,.8],14)
    X('shield',[2.9,12.6,-3.65],[2.7,5.7,.7],2)
    X('shield',[3.4,11.5,-3.45],[1.7,1.8,.65],14,[0,0,0])
    X('shield',[3.9,13,-3.9],[.7,4.8,.3],3)
    X('shield',[3.3,15.4,-3.9],[1.9,.7,.3],3)
    feather_wings(a)
    return a.m


def fox():
    a=Sculpt('fox_spirit_girl');adult_frame(a);hair(a);X=a.X;B=a.B
    for side,n in ((-1,'right'),(1,'left')):
        B('ear_'+n,'head',[side*1.9,30.4,0])
        X('ear_'+n,[side*2-.9,30.4,-.4],[1.8,3.2,1.6],9,[0,0,-side*15])
        X('ear_'+n,[side*2.3-.6,33,-.3],[1.2,1.6,1.3],1,[0,0,-side*22])
        X('ear_'+n,[side*2-.5,31,-.55],[1,2,.4],6,[0,0,-side*15])
        B('tunic_'+n,'body',[side*1.5,14,0]);X('tunic_'+n,[side*1.5-1.5,8.6,-2],[3,5.5,4],2,[0,0,-side*9])
        X('tunic_'+n,[side*1.5-1.35,8.6,-2.2],[2.7,.8,.5],3)
        X('arm_'+n,[side*3.5-1.25,18.2,-1.25],[2.5,3.5,2.5],2,[0,0,-side*8])
        X('forearm_'+n,[side*3.65-1.05,14.3,-1.1],[2.1,1.3,2.2],6)
        # Light stockings distinguish the silhouette from black booted mages.
        a.m.by_name['leg_'+n]['cubes'][0]['uv']=a.m.by_name['head']['cubes'][1]['uv'].copy()
        X('shin_'+n,[side*1.35-.85,2,-.9],[1.7,5,1.8],6)
    X('body',[-2.2,15,-2],[4.4,1.3,4],3)
    X('body',[-.9,14.4,-2.6],[1.8,2,.65],7,[0,0,45])
    X('chest',[-2,21.4,-2.9],[4,.55,.5],6,[0,0,-12])
    X('chest',[-2,20.9,-2.95],[4,.55,.5],6,[0,0,12])
    # Nine separate two-joint tail anchors: three levels of a broad radial fan.
    # Bulky base, broad middle and tapering ivory tips remain individually legible.
    for i in range(9):
        angle=(i-4)*19;row=i%3
        anchor=[(i-4)*.25,12.2+row*.35,1.8]
        B('tail_'+str(i),'body',anchor,[-(8+row*8),angle,0])
        X('tail_'+str(i),[anchor[0]-.85,anchor[1]-.9,1.8],[1.7,1.8,3.7],9,[-10-row*8,0,0])
        B('tailtip_'+str(i),'tail_'+str(i),[anchor[0],anchor[1]+.2,5],[-(25+row*13),0,0])
        X('tailtip_'+str(i),[anchor[0]-1.45,anchor[1]-1,4.7],[2.9,3,5.5],9,[-17-row*10,0,0])
        X('tailtip_'+str(i),[anchor[0]-1.7,anchor[1]-.6,8.2],[3.4,3.4,3.4],12,[-20-row*10,0,0])
        X('tailtip_'+str(i),[anchor[0]-1.2,anchor[1]+.25,10.5],[2.4,2.4,2.8],6,[-23-row*10,0,0])
        X('tailtip_'+str(i),[anchor[0]-.65,anchor[1]+.9,12.6],[1.3,1.4,2],6,[-26-row*10,0,0])
    return a.m


def wave(L,start,end,phase=0):
    return {str(round(L*i/12,6)):[x+(y-x)*(1-math.cos(math.tau*i/12+phase))/2 for x,y in zip(start,end)] for i in range(13)}


def grounded_death(m):
    """Full 3D all-corner support envelope, including cube and rest rotations."""
    def rotate(p,pivot,angles):
        x,y,z=[p[i]-pivot[i] for i in range(3)]
        for axis,angle in enumerate(angles):
            c=math.cos(math.radians(angle));s=math.sin(math.radians(angle))
            if axis==0:y,z=y*c-z*s,y*s+z*c
            elif axis==1:x,z=x*c+z*s,-x*s+z*c
            else:x,y=x*c-y*s,x*s+y*c
        return [x+pivot[0],y+pivot[1],z+pivot[2]]
    static={}
    if m.name!='fox_spirit_girl':
        for side,n in ((-1,'right'),(1,'left')):
            static['wing_'+n]=[0,side*15,-side*53]
            static['wingtip_'+n]=[0,-side*12,side*15]
    points=[]
    for b in m.bones:
        for c in b.get('cubes',[]):
            for corner in itertools.product((0,1),repeat=3):
                p=[c['origin'][i]+corner[i]*c['size'][i] for i in range(3)]
                p=rotate(p,c.get('pivot',b['pivot']),c.get('rotation',[0,0,0]));cursor=b
                while cursor['name']!='root':
                    angles=[x+y for x,y in zip(cursor.get('rotation',[0,0,0]),static.get(cursor['name'],[0,0,0]))]
                    p=rotate(p,cursor['pivot'],angles);cursor=m.by_name[cursor['parent']]
                points.append(p)
    frames={};L=.65
    for i in range(129):
        u=i/128;angle=86*(u*u*(3-2*u))
        minimum=min(rotate(p,[0,0,0],[0,0,angle])[1] for p in points)
        frames[str(round(L*u,6))]=[0,max(0,.1-minimum),0]
    bones={n:{'rotation':{'0':v}} for n,v in static.items()}
    bones['root']={'rotation':{str(round(L*i/128,6)):[0,0,86*((i/128)**2*(3-2*i/128))] for i in range(129)},'position':frames}
    return clip(L,bones)


def motions(m):
    name=m.name;t=SPECS[name][2];bones=m.by_name
    idle={'chest':{'rotation':wave(2.4,(-1,0,-.5),(1,0,.5))},'head':{'rotation':wave(2.4,(0,-3,0),(1.5,3,0))}}
    a={'idle':clip(2.4,idle,True)}
    for fast,L in ((False,1.1),(True,.65)):
        state='run' if fast else 'walk';amp=30 if fast else 19
        b={'body':{'position':wave(L,(0,0,0),(0,.65 if fast else .25,0)),'rotation':wave(L,(-3,0,-2),(-3,0,2))},'chest':{'rotation':wave(L,(0,-4,0),(0,4,0))}}
        for side,n in ((-1,'right'),(1,'left')):
            b['leg_'+n]={'rotation':wave(L,(side*amp,0,0),(-side*amp,0,0))}
            b['shin_'+n]={'rotation':wave(L,(4,0,0),(24 if fast else 14,0,0),phase=side*.8)}
            b['foot_'+n]={'rotation':wave(L,(-6,0,0),(8,0,0),phase=side*.8)}
            b['arm_'+n]={'rotation':wave(L,(-side*amp*.65,0,side*3),(side*amp*.65,0,-side*3))}
            b['forearm_'+n]={'rotation':wave(L,(-14,0,0),(-30 if fast else -21,0,0),phase=side*.7)}
        a[state]=clip(L,b,True)
    if name=='valkyrie':
        attack={'body':{'rotation':keys(t,(-7,-16,-4),(9,20,3))},'chest':{'rotation':keys(t,(0,-12,0),(0,20,0))},'arm_right':{'rotation':keys(t,(-68,-18,-28),(45,26,12))},'forearm_right':{'rotation':keys(t,(-55,0,0),(-15,0,0))},'hand_right':{'rotation':keys(t,(0,-12,-8),(12,12,8))},'arm_left':{'rotation':keys(t,(-33,10,12),(-42,0,8))}}
    else:
        attack={'body':{'rotation':keys(t,(-7,-11,-3),(7,12,3))},'chest':{'rotation':keys(t,(0,-7,0),(0,10,0))},'head':{'rotation':keys(t,(-5,-7,0),(4,6,0))}}
        for side,n in ((-1,'right'),(1,'left')):
            attack['arm_'+n]={'rotation':keys(t,(-40,side*15,-side*18),(-70,-side*12,side*8))}
            attack['forearm_'+n]={'rotation':keys(t,(-60,0,0),(-10,0,0))}
            attack['hand_'+n]={'rotation':keys(t,(-12,side*20,side*15),(-32,-side*18,-side*9))}
    a['attack']=clip(t+.45,attack)
    import copy
    heavy=copy.deepcopy(attack);heavy['body']={'rotation':keys(t,(-11,-19,-5),(13,25,5),recovery=.4)}
    a['heavy']=clip(t+.55,heavy)
    cast={'body':{'rotation':keys(t,(-5,0,-2),(4,0,2))},'head':{'rotation':keys(t,(-8,0,0),(2,0,0))}}
    for side,n in ((-1,'right'),(1,'left')):
        cast['arm_'+n]={'rotation':keys(t,(-35,side*22,-side*18),(-72,side*4,-side*9))}
        cast['forearm_'+n]={'rotation':keys(t,(-60,0,side*10),(-18,0,0))}
        cast['hand_'+n]={'rotation':keys(t,(10,-side*25,side*10),(-30,side*12,-side*10))}
    a['cast']=clip(t+.5,cast)
    a['hurt']=clip(.4,{'body':{'rotation':{'0':[0,0,0],'.12':[-10,0,7],'.4':[0,0,0]}},'head':{'rotation':{'0':[0,0,0],'.12':[-8,0,-6],'.4':[0,0,0]}}})
    if name!='fox_spirit_girl':
        for state,L,amp in (('fly',.7,36),('hover',1.1,24)):
            b={'body':{'position':wave(L,(0,.6,0),(0,1.2,0)),'rotation':wave(L,(8,0,-1),(13,0,1))}}
            for side,n in ((-1,'right'),(1,'left')):
                b['wing_'+n]={'rotation':wave(L,(0,side*5,side*amp),(0,-side*6,-side*amp))}
                b['wingtip_'+n]={'rotation':wave(L,(3,0,side*14),(-8,0,-side*20),phase=-.65)}
                b['leg_'+n]={'rotation':wave(L,(18,0,0),(24,0,0))}
                b['shin_'+n]={'rotation':wave(L,(32,0,0),(39,0,0))}
            a[state]=clip(L,b,True)
        fold={}
        for side,n in ((-1,'right'),(1,'left')):
            fold['wing_'+n]={'rotation':{'0':[0,0,0],'.4':[0,side*15,-side*53],'.8':[0,side*15,-side*53]}}
            fold['wingtip_'+n]={'rotation':{'0':[0,0,0],'.48':[0,-side*12,side*15],'.8':[0,-side*12,side*15]}}
        a['fold']=clip(.8,fold)
        a['levitate']=clip(2.4,copy.deepcopy(idle),True)
        a['teleport']=clip(1.1,{'root':{'scale':{'0':[1,1,1],'.4':[.3,1.15,.3],'.55':[.05,.05,.05],'1.1':[1,1,1]}}})
    for state,anim in a.items():
        L=anim['animation_length'];b=anim['bones'];loop=anim.get('loop',False)
        for i,n in enumerate(n for n in bones if n.startswith(('hair_','tail','gown_','skirt_','tunic_','fauld_','earring_'))):
            if loop:
                amp=3.5 if n.startswith('hair') else 5
                b[n]={'rotation':wave(L,(-amp,-2,-1),(amp,2,1),phase=-i*.27)}
            elif state in ('attack','heavy','cast'):
                b[n]={'rotation':keys(t,(7,-3,-2),(-6,3,2))}
        if name!='fox_spirit_girl' and state not in ('fly','hover','fold'):
            for side,n in ((-1,'right'),(1,'left')):
                b['wing_'+n]={'rotation':wave(L,(0,side*15,-side*53),(1,side*17,-side*51)) if loop else {'0':[0,side*15,-side*53]}}
                b['wingtip_'+n]={'rotation':wave(L,(0,-side*12,side*15),(1,-side*13,side*17)) if loop else {'0':[0,-side*12,side*15]}}
        if name=='fox_spirit_girl' and loop:
            for i in range(9):
                # Additive channels retain the baked radial fan; offset phase
                # prevents nine tails from moving as one rigid accessory.
                b['tail_'+str(i)]={'rotation':wave(L,(-3,-4,-2),(3,4,2),phase=-i*.36)}
                b['tailtip_'+str(i)]={'rotation':wave(L,(-5,-3,-1),(5,3,1),phase=-i*.36-.65)}
    a['death']=grounded_death(m)
    return a


def egg(name,palette):
    """32px original fantasy relic eggs with individually readable emblems."""
    image=Image.new('RGBA',(32,32));d=ImageDraw.Draw(image)
    def c(i):return '#'+palette[i]
    d.ellipse((5,5,26,29),fill=c(5));d.polygon([(9,6),(13,2),(18,2),(23,8),(27,20),(24,27),(8,27),(5,20)],fill=c(2))
    d.arc((6,3,26,29),170,290,fill=c(3),width=2);d.line((11,6,17,4),fill=c(15),width=2)
    d.line((8,24,24,24),fill=c(3));d.line((10,27,22,27),fill=c(1))
    if name=='ender_dragon_girl':
        d.polygon([(8,12),(13,15),(16,10),(19,15),(25,12),(22,20),(17,22),(11,20)],fill=c(7))
        d.polygon([(16,13),(20,17),(16,21),(12,17)],fill=c(11));d.rectangle((15,16,17,18),fill=c(15))
    elif name=='succubus':
        d.polygon([(7,13),(13,16),(16,12),(19,16),(25,13),(22,21),(18,20),(16,23),(14,20),(10,21)],fill=c(7))
        d.arc((11,9,20,20),190,350,fill=c(3),width=2);d.rectangle((15,17,17,21),fill=c(11))
    elif name=='valkyrie':
        d.polygon([(7,11),(13,14),(14,20),(9,17)],fill=c(12));d.polygon([(25,11),(19,14),(18,20),(23,17)],fill=c(12))
        d.rectangle((15,10,17,23),fill=c(3));d.line((12,18,20,18),fill=c(15),width=2)
        d.polygon([(16,8),(18,12),(14,12)],fill=c(12))
    else:
        for i in range(5):
            x=8+i*4;d.line([(16,22),(x,16),(x,11)],fill=c(9),width=2);d.rectangle((x,10,x+1,12),fill=c(6))
        d.polygon([(11,15),(13,12),(16,15),(19,12),(21,15),(19,21),(16,23),(13,21)],fill=c(12))
        d.point((14,17),fill=c(4));d.point((18,17),fill=c(4));d.rectangle((15,20,17,20),fill=c(5))
    out=pipeline.ASSET/'textures/item'/f'{name}_spawn_egg.png';out.parent.mkdir(parents=True,exist_ok=True);image.save(out)


def main():
    global ACTIVE_NAME
    pipeline.material_atlas=painted_atlas
    for maker in (ender,succubus,valkyrie,fox):
        m=maker();ACTIVE_NAME=m.name;w,h,_=SPECS[m.name]
        write_creature(m,PALETTES[m.name],MATERIALS[m.name],motions(m),w,h,glow=(4,11))
        egg(m.name,PALETTES[m.name])

if __name__=='__main__':main()
