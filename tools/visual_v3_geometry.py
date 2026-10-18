"""Offline geometry floor evaluation in GeckoLib's mirrored Euler convention."""
import math
import numpy as np

def around(pivot,angles):
    x,y,z=map(math.radians,(-angles[0],angles[1],-angles[2]))
    cx,sx=math.cos(x),math.sin(x);cy,sy=math.cos(y),math.sin(y);cz,sz=math.cos(z),math.sin(z)
    rx=np.array([[1,0,0],[0,cx,-sx],[0,sx,cx]])
    ry=np.array([[cy,0,sy],[0,1,0],[-sy,0,cy]])
    rz=np.array([[cz,-sz,0],[sz,cz,0],[0,0,1]])
    rotation=rz@ry@rx;matrix=np.eye(4);matrix[:3,:3]=rotation
    pivot=np.array(pivot);matrix[:3,3]=pivot-rotation@pivot
    return matrix

def minimum_y(bones,root_rotation):
    by_name={b['name']:b for b in bones};matrices={}
    def matrix(name):
        if name not in matrices:
            b=by_name[name];local=around(b['pivot'],root_rotation if name=='root' else b.get('rotation',[0,0,0]))
            matrices[name]=matrix(b['parent'])@local if 'parent' in b else local
        return matrices[name]
    result=math.inf
    for bone in bones:
        for cube in bone.get('cubes',[]):
            transform=matrix(bone['name'])@around(cube.get('pivot',bone['pivot']),cube.get('rotation',[0,0,0]))
            points=np.array([[*(cube['origin'][i]+(cube['size'][i] if bits&(1<<i) else 0) for i in range(3)),1] for bits in range(8)])
            result=min(result,float((transform@points.T)[1].min()))
    return result

def support_death(model,animations):
    """Adapt only cosmetic Y support; retain rotation curve and clip duration."""
    root=animations['death']['bones']['root'];keys=sorted((float(k),v) for k,v in root['rotation'].items())
    duration=animations['death']['animation_length'];positions={}
    for sample in range(129):
        time=duration*sample/128
        lower=max((p for p in keys if p[0]<=time),default=keys[0]);upper=min((p for p in keys if p[0]>=time),default=keys[-1])
        fraction=(time-lower[0])/(upper[0]-lower[0]) if upper[0]>lower[0] else 0
        rotation=[a+(b-a)*fraction for a,b in zip(lower[1],upper[1])]
        positions[str(round(time,6))]=[0,max(0,.1-minimum_y(model.bones,rotation)),0]
    root['position']=positions
