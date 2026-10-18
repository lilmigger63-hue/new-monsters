#!/usr/bin/env python3
"""Original species-specific expansion anatomy, artwork and editable native exports."""
from pathlib import Path
import base64, io, json, math
from PIL import Image, ImageDraw
from overhaul_asset_pipeline import Model, clip, keys, write_creature, material_atlas, ASSET, ROOT
from generate_groups_cd_assets import blockbench, validate, save

SPEC={
 'centaur':((1.25,2.15),.5,['775137','3c302b','ae8459','435c70','d5b568','222535','f0dfc2','744637','dfb29c','342b31','5e4136','b38953','a7bfc6','334958','8d9fa9','f4e3bc']),
 'holstaurus':((.8,1.9),.7,['e4ddd4','30333a','b9b1ab','50667f','dcb96b','272837','fff0df','8c6374','e8bcae','a8a0b4','58474b','9e8baf','b5bccc','3a4c69','8f9ba9','fff4dc']),
 'sahuagin':((.7,1.85),.5,['549a9f','28566d','86bec0','347d8e','e7cc91','173342','dfede0','926f82','96c7bd','286a88','33575d','6bb8af','89dbcd','285465','8eabab','edffe0']),
 'werecat':((.7,1.8),.8,['677283','303a50','aeb6bc','45556d','c45c69','252638','ece6df','957980','dfc2ba','aab1bd','48485b','8498b6','bac9d6','29374d','8d9fb3','fff0dd'])}
ROLES=['fur','fur','fur','armor','gold','skin','bone','cloth','skin','hair','leather','cloth','crystal','cloth','iron','glow']

def bn(m,n,p,v,r=None):m.bone(n,p,v,rotation=r);return n
def bx(m,b,o,s,k=0,r=None):m.box(b,o,s,material=k,rotation=r)
def facet(m,b,o,s,k=0):
 bx(m,b,o,s,k)
 bx(m,b,[o[0]+s[0]*.12,o[1]+s[1]*.78,o[2]+s[2]*.1],[s[0]*.76,s[1]*.32,s[2]*.8],k)

def upper(m,base):
 n=m.name;aquatic=n=='sahuagin';cow=n=='holstaurus'
 bn(m,'body','root',[0,base,0]);bn(m,'chest','body',[0,base+4,0])
 facet(m,'body',[-2.5,base,-1.8],[5,3.3,3.6],13)
 facet(m,'chest',[-2,base+3,-1.55],[4,3,3.1],13)
 bx(m,'chest',[-2.9,base+5,-1.8],[5.8,3.3,3.6],3)
 for s in (-1,1):
  bx(m,'chest',[s*1.25-1.18,base+5.3,-2.6],[2.36,2.5,1.7],3,[0,0,-s*8])
  bx(m,'chest',[s*2.4-.6,base+6,-1.3],[1.2,2,3],14,[0,0,s*13])
 bx(m,'body',[-2.65,base+1,-1.95],[5.3,.8,4],10)
 bx(m,'body',[-.65,base+.9,-2.2],[1.3,1.1,.5],4)
 bx(m,'chest',[-.5,base+7,-2.05],[1,1,.5],12)
 bn(m,'neck','chest',[0,base+8,0]);bx(m,'neck',[-.9,base+7.8,-.85],[1.8,2,1.7],8)
 bn(m,'head','neck',[0,base+10,0])
 facet(m,'head',[-2.7,base+9,-2.3],[5.4,5.3,4.6],8)
 bx(m,'head',[-2.2,base+8.65,-1.9],[4.4,1.6,3.7],8)
 # Individual eyes have sclera, iris, pupil, catchlight and upper lash.
 for s in (-1,1):
  x=s*1.3
  bx(m,'head',[x-.72,base+10.8,-2.48],[1.44,.95,.2],6)
  bx(m,'head',[x-.36,base+10.86,-2.65],[.72,.87,.18],4)
  bx(m,'head',[x-.13,base+10.89,-2.79],[.26,.72,.14],5)
  bx(m,'head',[x-.28,base+11.35,-2.88],[.22,.24,.1],15)
  bx(m,'head',[x-.82,base+11.75,-2.6],[1.64,.18,.23],5,[0,0,-s*5])
 bx(m,'head',[-.26,base+10.1,-2.55],[.52,.7,.48],8)
 bx(m,'head',[-.63,base+9.5,-2.48],[1.26,.16,.18],7)
 # Full scalp cap, overlapping bangs, long independent side/back locks.
 bx(m,'head',[-2.9,base+13,-2.4],[5.8,1.5,4.9],9)
 bx(m,'head',[-2.85,base+10.5,1.4],[5.7,3.5,1.4],9)
 for s in (-1,1):
  for j in range(2):bx(m,'head',[s*(.8+j*1.2)-.9,base+12.2-j*.35,-2.7],[1.8,1.9,1],9,[0,0,s*(9+j*8)])
  h='hair_'+str(s);bn(m,h,'head',[s*2.4,base+13,0])
  for j in range(2):facet(m,h,[s*(2.35+j*.3)-.65,base+5+j*.8,-.7+j*1.6],[1.3,8-j*.6,1.5],9)
 bn(m,'hair_back','head',[0,base+13,1.8])
 for j in range(3):facet(m,'hair_back',[-2.5+j*1.7,base+4+j%2*.7,1.7],[1.7,9-j%2*.7,1.3],9)
 for s in (-1,1):
  arm='arm_'+('left' if s>0 else 'right');bn(m,arm,'chest',[s*3.2,base+7,0])
  facet(m,arm,[s*3.2-1,base+2.8,-1],[2,4.5,2.3],8)
  bx(m,arm,[s*3.2-1.25,base+5.8,-1.3],[2.5,1.8,2.8],3,[0,0,s*10])
  fore='fore_'+('left' if s>0 else 'right');bn(m,fore,arm,[s*3.2,base+3,0])
  facet(m,fore,[s*3.2-.85,base-.6,-1],[1.7,3.7,2.1],14 if n!='holstaurus' else 13)
  hand='hand_'+('left' if s>0 else 'right');bn(m,hand,fore,[s*3.2,base-.5,0])
  bx(m,hand,[s*3.2-.8,base-2,-1],[1.6,1.6,2],8)
  # Closed curled fingers wrap around the handle axis, not the blade.
  bx(m,hand,[s*3.2-.85,base-1.7,-1.3],[1.7,1,.55],8)
  bx(m,hand,[s*3.2-.8,base-1.7,.8],[.55,1.2,.6],8)
 return m

def biped(m,base):
 for s in (-1,1):
  leg='leg_'+('left' if s>0 else 'right');x=s*1.45
  bn(m,leg,'body',[x,base,0]);facet(m,leg,[x-1.12,6,-1.2],[2.24,base-6,2.5],13)
  lower=leg+'_lower';bn(m,lower,leg,[x,6,0]);facet(m,lower,[x-.9,1.5,-1],[1.8,4.8,2.2],3)
  bx(m,lower,[x-1.05,5,-1.25],[2.1,1.5,2.6],14)
  paw=leg+'_foot';bn(m,paw,lower,[x,1.5,0]);bx(m,paw,[x-1.1,0,-2.5],[2.2,1.8,3.8],10)
  bx(m,paw,[x-.95,.3,-2.75],[1.9,.9,1],14)
  if m.name=='sahuagin':
   bx(m,paw,[x-1.55,.2,-3.6],[3.1,.5,3.2],2,[0,s*12,0])
   for j in range(3):bx(m,paw,[x-1.2+j*.9,.1,-4],[.45,.55,2],6)


def build(n):
 m=Model(n);base=17 if n=='centaur' else 12
 upper(m,base)
 if n=='centaur':
  bn(m,'horse_body','body',[0,15,5])
  facet(m,'horse_body',[-4.5,11,-1],[9,6,18],0)
  bx(m,'horse_body',[-3.5,13,-2],[7,5,8],0,[8,0,0])
  facet(m,'horse_body',[-4.2,11,12],[8.4,5.8,7],0)
  for front in (True,False):
   for s in (-1,1):
    x=s*3.3;z=0 if front else 15;leg=('front_' if front else 'hind_')+('left' if s>0 else 'right')
    bn(m,leg,'horse_body',[x,13,z]);facet(m,leg,[x-1.35,7.5,z-1.5],[2.7,6,3],0)
    lower=leg+'_lower';bn(m,lower,leg,[x,8,z]);bx(m,lower,[x-.8,2,z-.85],[1.6,6.1,1.9],0,[-5 if front else 9,0,0])
    bx(m,lower,[x-1,2,z-1.1],[2,1.3,2.3],2)
    foot=leg+'_foot';bn(m,foot,lower,[x,1.5,z]);bx(m,foot,[x-1.35,0,z-1.8],[2.7,2,3.5],1)
    bx(m,foot,[x-1.2,1.4,z-1.6],[2.4,.8,3],2)
  bn(m,'tail','horse_body',[0,15,18]);bx(m,'tail',[-.9,10,17.5],[1.8,5.5,2.5],9,[-20,0,0])
  bn(m,'tail_tip','tail',[0,11,20]);facet(m,'tail_tip',[-1.2,4.5,19],[2.4,7,2.7],9)
  weapon(m,base)
 else:
  biped(m,base)
  if n=='holstaurus':
   for s in (-1,1):
    bx(m,'head',[s*2.3-.7,base+13.8,-.2],[1.4,2.5,1.5],6,[0,0,-s*20])
    bx(m,'head',[s*2.9-.5,base+15.8,-.4],[1,1.6,1.1],6,[0,0,s*20])
    bx(m,'head',[s*3.4-1.2,base+11.4,-.2],[2.4,1.1,2],0,[0,0,-s*18])
    bx(m,'head',[s*3.5-.7,base+11.5,-.45],[1.4,.5,.5],7)
   for s in (-1,1):
    bx(m,'chest',[s*2.2-.55,base+4,-1.9],[1.1,3.6,.6],0,[0,0,-s*8])
    arm='arm_'+('left' if s>0 else 'right')
    bx(m,arm,[s*3.2-1.05,base+3.2,-1.05],[2.1,2.7,2.5],0)
    fore='fore_'+('left' if s>0 else 'right')
    bx(m,fore,[s*3.2-.95,base+.2,-1.1],[1.9,1,2.3],0)
   bn(m,'tail','body',[0,base+1,1.6]);bx(m,'tail',[-.35,4,2],[.7,9,1],0,[-12,0,0]);facet(m,'tail',[-.75,3,3],[1.5,2.3,1.8],1)
   bx(m,'body',[-.8,base-1,-2.4],[1.6,1.6,1.3],4);bx(m,'body',[-.2,base-1.3,-2.5],[.4,.5,.5],1)
   for s in (-1,1):bx(m,'body',[s*2.1-1.1,base-2.5,-1.9],[2.2,4,3.6],13,[0,0,-s*9])
  elif n=='sahuagin':
   for s in (-1,1):
    bn(m,'fin_head_'+str(s),'head',[s*2.5,base+11,0])
    for j in range(3):bx(m,'fin_head_'+str(s),[s*(2.6+j*.7)-.3,base+10+j*.3,-.4],[.6,3-j*.6,2.5],12,[0,0,-s*(20+j*12)])
    fore='fore_'+('left' if s>0 else 'right')
    for j in range(3):bx(m,fore,[s*(4+j*.5)-.25,base+.2+j*.7,0],[.5,2.3,2.3],12,[0,0,-s*(15+j*12)])
   bn(m,'tail','body',[0,base+1,1.5]);bx(m,'tail',[-.8,7,1.5],[1.6,6,2],0,[-23,0,0])
   bn(m,'tail_tip','tail',[0,7,4]);bx(m,'tail_tip',[-.6,5,3],[1.2,4,2],0,[-25,0,0])
   for s in (-1,1):bx(m,'tail_tip',[s*1.4-1.4,3.8,4],[2.8,3.3,.65],12,[0,0,s*28])
   weapon(m,base,trident=True)
  else:
   for s in (-1,1):
    ear='ear_'+str(s);bn(m,ear,'head',[s*2,base+14,0])
    # Low broad feline triangles: stepped taper, slight outward cant,
    # pointed 0.3-unit tips rather than parallel tall rabbit-like posts.
    for j,(width,height,offset) in enumerate([(2.2,.9,0),(1.6,.75,.75),(.95,.65,1.35),(.3,.5,1.9)]):
     x=s*(2+j*.13)
     bx(m,ear,[x-width/2,base+13.8+offset,-.6+j*.1],[width,height,1.7-j*.25],9)
    bx(m,ear,[s*2.1-.45,base+14.15,-.78],[.9,.8,.24],7)
    bx(m,ear,[s*2.3-.22,base+14.9,-.67],[.44,.65,.22],7)
    hand='hand_'+('left' if s>0 else 'right')
    for j in range(3):bx(m,hand,[s*3.2-.6+j*.5,base-2.4,-1.4],[.25,1.2,.4],6,[15,0,0])
   # Bone articulation keeps the shared joint inside both unrotated cube
   # volumes regardless of renderer cube Euler/sign conventions.
   bn(m,'tail','body',[0,base+1,1.8],[-25,0,0])
   bx(m,'tail',[-.65,7,1.5],[1.3,6.4,2],9)
   joint=[0,7,2.5]
   bn(m,'tail_tip','tail',joint,[18,0,0])
   bx(m,'tail_tip',[-.75,6.25,2],[1.5,1.5,6],9)
 return m


def weapon(m,base,trident=False):
 # Handle goes through the closed right palm; everything follows wrist hierarchy.
 bn(m,'weapon','hand_right',[-3.2,base-1,0])
 bx(m,'weapon',[-3.55,base-5,-.35],[.7,9 if trident else 5,.7],10)
 if trident:
  bx(m,'weapon',[-5.2,base+3,-.5],[4,1,.9],14)
  for j in range(3):bx(m,'weapon',[-5.2+j*1.65,base+3.7,-.5],[.65,3+(1 if j==1 else 0),.9],12)
 else:
  bx(m,'weapon',[-5.1,base-.2,-.65],[3.8,.7,1.3],4)
  bx(m,'weapon',[-3.8,base+.5,-.4],[1.2,8,.8],14)
  bx(m,'weapon',[-3.5,base+8.5,-.3],[.6,1.8,.6],14)


def animations(m,t):
 n=m.name;horse=n=='centaur';out={}
 idle={'chest':{'rotation':['math.sin(query.anim_time * 100) * 1',0,0]},'head':{'rotation':[0,'math.sin(query.anim_time * 100) * 2',0]}}
 for bn_ in m.by_name:
  if bn_.startswith(('hair_','fin_')):idle[bn_]={'rotation':['math.sin(query.anim_time * 100 - 25) * 2',0,0]}
 if 'tail' in m.by_name:idle['tail']={'rotation':[0,'math.sin(query.anim_time * 100) * 6',0]}
 out['idle']=clip(3.6,idle,True)
 for state,rate,amp in [('walk',300,19),('run',480,32)]:
  b={'chest':{'rotation':[f'math.sin(query.anim_time * {rate}) * 2',0,0]}}
  for name in m.by_name:
   if name.startswith(('front_','hind_')) and not name.endswith(('_lower','_foot')) or name.startswith('leg_') and not name.endswith(('_lower','_foot')):
    phase=(0 if name.endswith('left') else 180)+(180 if name.startswith('hind_') else 0)
    # Lift on swing half only; no positive global root offset / hovering.
    b[name]={'rotation':[f'math.sin(query.anim_time * {rate} + {phase}) * {amp}',0,0],
             'position':[0,f'math.max(0, math.sin(query.anim_time * {rate} + {phase})) * {.7 if horse else .45}',0]}
    b[name+'_lower']={'rotation':[f'math.max(0, math.sin(query.anim_time * {rate} + {phase} - 30)) * {20 if horse else 24}',0,0]}
    b[name+'_foot']={'rotation':[f'-math.sin(query.anim_time * {rate} + {phase}) * {amp} - math.max(0, math.sin(query.anim_time * {rate} + {phase} - 30)) * {20 if horse else 24}',0,0]}
   if name.startswith(('hair_','tail')):b[name]={'rotation':[f'math.sin(query.anim_time * {rate} - 35) * 5',f'math.sin(query.anim_time * {rate}) * 3',0]}
  for side,sign in [('left',1),('right',-1)]:
   b['arm_'+side]={'rotation':[f'math.sin(query.anim_time * {rate}) * {sign*13}',0,sign*3]}
   b['fore_'+side]={'rotation':[-8,0,0]}
  out[state]=clip(360/rate,b,True)
 for state in ('attack','heavy','cast'):
  magic=n=='werecat' or state=='cast';amp=70 if magic else 95
  b={'chest':{'rotation':keys(t,[-8,-12,0],[9,14,0])},'head':{'rotation':keys(t,[-8,0,0],[10,0,0])}}
  for side,sgn in [('left',1),('right',-1)]:
   b['arm_'+side]={'rotation':keys(t,[-amp,sgn*12,sgn*18],[-40 if magic else 25,0,sgn*8])}
   b['fore_'+side]={'rotation':keys(t,[-35,0,0],[12 if magic else -5,0,0])}
   b['hand_'+side]={'rotation':keys(t,[10,sgn*12,0],[-18,0,sgn*9])}
  if n=='holstaurus':b['body']={'position':keys(t,[0,-1,0],[0,1.2,0])}
  for name in m.by_name:
   if name.startswith(('hair_','tail','fin_')):b[name]={'rotation':keys(t,[5,0,0],[-9,8,0])}
  out[state]=clip(t+.3,b)
 out['hurt']=clip(.4,{'chest':{'rotation':{'0':[0,0,0],'.08':[-13,0,5],'.4':[0,0,0]}}})
 # Root collapse is solved against every rotated geometry corner below.
 out['death']=clip(.65,{'root':{'rotation':{'0':[0,0,0],'.25':[0,0,25],'.65':[0,0,85]},'position':{'0':[0,0,0],'.25':[0,0,0],'.65':[0,0,0]}}})
 if n=='holstaurus':
  out['hop']=clip(.7,{'body':{'position':{'0':[0,0,0],'.15':[0,-1,0],'.35':[0,2.5,0],'.55':[0,.3,0],'.7':[0,0,0]}},'leg_left':{'rotation':{'0':[0,0,0],'.2':[-18,0,0],'.5':[12,0,0],'.7':[0,0,0]}},'leg_right':{'rotation':{'0':[0,0,0],'.2':[-18,0,0],'.5':[12,0,0],'.7':[0,0,0]}}},True)
 if n=='sahuagin':
  for state,rate in [('swim',300),('idle_swim',160)]:
   b={'root':{'rotation':[65 if state=='swim' else 18,0,0]},'chest':{'rotation':['math.sin(query.anim_time * '+str(rate)+') * 3',0,0]}}
   for side,sgn in [('left',1),('right',-1)]:
    b['leg_'+side]={'rotation':[f'math.sin(query.anim_time * {rate}) * {sgn*24}',0,0]}
    b['leg_'+side+'_lower']={'rotation':[f'16 + math.sin(query.anim_time * {rate} - 40) * {sgn*14}',0,0]}
    b['arm_'+side]={'rotation':[f'-35 + math.sin(query.anim_time * {rate} - 30) * 12',sgn*10,sgn*25]}
   for name in m.by_name:
    if name.startswith(('fin_','tail','hair_')):b[name]={'rotation':[f'math.sin(query.anim_time * {rate} - 35) * 8',f'math.sin(query.anim_time * {rate}) * 12',0]}
   out[state]=clip(360/rate,b,True)
 return out


def painted(n,p):
 roles=list(ROLES)
 if n=='sahuagin':roles[0]=roles[1]=roles[2]='scales'
 im=material_atlas(p,roles);d=ImageDraw.Draw(im)
 # Original hand-painted panels, seams, stitching and species motifs.
 for tile in (3,13,14):
  x,y=tile%4*32,tile//4*32
  d.line([(x+5,y+6),(x+16,y+11),(x+26,y+6)],fill='#b8b6a2',width=1)
  d.line([(x+5,y+22),(x+16,y+27),(x+26,y+22)],fill='#202e42',width=2)
  for xx in (6,24):d.rectangle((x+xx,y+8,x+xx+1,y+9),fill='#cfbc84')
 if n=='holstaurus':
  for tile in (0,2):
   x,y=tile%4*32,tile//4*32
   for ox,oy in ((4,5),(19,13),(8,23)):
    d.polygon([(x+ox,y+oy),(x+ox+6,y+oy-2),(x+ox+9,y+oy+3),(x+ox+5,y+oy+7),(x+ox-1,y+oy+4)],fill='#33343e')
 elif n=='sahuagin':
  for tile in (8,12):
   x,y=tile%4*32,tile//4*32
   for yy in (6,14,22):d.line([(x+3,y+yy),(x+14,y+yy+4),(x+26,y+yy)],fill='#c8e7cd',width=1)
 elif n=='centaur':
  x,y=0,0
  for yy in (5,11,18,24):d.line([(5,yy),(14,yy+2),(26,yy-1)],fill='#886044',width=1)
 else:
  x,y=3%4*32,3//4*32
  d.polygon([(x+16,y+5),(x+22,y+14),(x+16,y+22),(x+10,y+14)],outline='#b1bdc8')
 return im


def egg(n,p):
 im=Image.new('RGBA',(32,32));d=ImageDraw.Draw(im)
 d.polygon([(12,2),(19,2),(25,8),(28,18),(26,26),(20,30),(10,30),(4,25),(3,17),(7,8)],fill='#'+p[0],outline='#'+p[1])
 d.line([(10,6),(7,13),(7,20)],fill='#'+p[15],width=2)
 d.line([(7,25),(14,27),(23,25)],fill='#'+p[4],width=2)
 if n=='centaur': # horseshoe rune
  d.arc((10,8,24,24),0,180,fill='#'+p[4],width=3);d.line((10,15,10,9),fill='#'+p[4],width=3);d.line((23,15,23,9),fill='#'+p[4],width=3)
 elif n=='holstaurus':
  d.polygon([(10,11),(13,15),(20,15),(24,10),(22,18),(17,22),(12,19)],fill='#'+p[4]);d.rectangle((15,18,19,24),fill='#'+p[13])
 elif n=='sahuagin':
  d.polygon([(10,10),(20,12),(23,9),(23,22),(19,19),(10,21),(13,16)],fill='#'+p[12]);d.point((15,14),fill='#'+p[5])
 else:
  d.polygon([(10,10),(15,13),(21,10),(22,20),(16,24),(9,20)],fill='#'+p[2]);d.point((13,17),fill='#'+p[4]);d.point((19,17),fill='#'+p[4])
 return im


def floor_y(m,rotation):
 # Exact rest-pose cube corner transforms, including authored cube/bone rotations.
 import numpy as np
 def transform(p,r):
  x,y,z=[math.radians(v) for v in r];cx,sx,cy,sy,cz,sz=math.cos(x),math.sin(x),math.cos(y),math.sin(y),math.cos(z),math.sin(z)
  rx=np.array([[1,0,0],[0,cx,-sx],[0,sx,cx]]);ry=np.array([[cy,0,sy],[0,1,0],[-sy,0,cy]]);rz=np.array([[cz,-sz,0],[sz,cz,0],[0,0,1]])
  a=np.eye(4);a[:3,:3]=rz@ry@rx;a[:3,3]=np.array(p)-a[:3,:3]@np.array(p);return a
 mats={};low=1e9
 for b in m.bones:
  mat=transform(b['pivot'],rotation if b['name']=='root' else b.get('rotation',[0,0,0]));mat=mats.get(b.get('parent'),np.eye(4))@mat;mats[b['name']]=mat
  for c in b.get('cubes',[]):
   cm=mat@transform(c.get('pivot',b['pivot']),c.get('rotation',[0,0,0]))
   for xx in (0,1):
    for yy in (0,1):
     for zz in (0,1):
      v=cm@np.array([c['origin'][0]+xx*c['size'][0],c['origin'][1]+yy*c['size'][1],c['origin'][2]+zz*c['size'][2],1]);low=min(low,v[1])
 return low


def main():
 for n,(dims,t,p) in SPEC.items():
  m=build(n);a=animations(m,t)
  # Dense collapse samples keep every rotated corner on/above floor;
  # recovery ends before normal server death removal at 20 ticks.
  death=a['death']['bones']['root'];death['rotation']={};death['position']={}
  for i in range(27):
   tm=round(i*.025,4);angle=25*(tm/.25) if tm<=.25 else 25+60*(tm-.25)/.4
   r=[0,0,angle];lift=max(0,-floor_y(m,r))
   death['rotation'][str(tm)]=r;death['position'][str(tm)]=[0,lift+.015 if i else 0,0]
   assert floor_y(m,r)+lift>=-.0001
  write_creature(m,p,ROLES,a,*dims)
  im=painted(n,p);native=blockbench(m,im,a);validate(m,a,im,native)
  # Preserve bounds written by the shared export; native texture matches runtime.
  old=json.loads((ROOT/f'tools/blockbench/{n}.bbmodel').read_text());native['visible_box']=old['visible_box']
  im.save(ASSET/f'textures/entity/{n}.png');save(ROOT/f'tools/blockbench/{n}.bbmodel',native)
  egg(n,p).save(ASSET/f'textures/item/{n}_spawn_egg.png')
  assert len(m.bones)<=55 and len(native['elements'])<=180
  assert floor_y(m,[0,0,0])>=-.01,(n,floor_y(m,[0,0,0]))
  print(n,'custom atlas/native parity, exact rest/death corner floor and budget checks passed')

if __name__=='__main__':main()
