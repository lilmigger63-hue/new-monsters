#!/usr/bin/env python3
"""Check editable/export parity and render-safe geometry, not artistic ratings."""
import base64
import io
import json
import copy
import itertools
import math
from pathlib import Path
import sys
import unittest
from PIL import Image

REPO=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(REPO/'tools'))
try:
    import overhaul_asset_pipeline as pipeline
except ImportError:
    pipeline=None
IDS='goblin_scout goblin_shaman orc_warrior minotaur stone_troll ancient_treant forest_dryad griffin dire_wolf wild_wyvern cave_basilisk crystal_spider shadow_wraith grave_knight flame_imp frost_elemental moon_stag slime_maiden harpy demon_sorceress'.split()

# Expansion exports use the same runtime/native/UV contracts.
expansion_manifest=REPO/'docs/monster-girl-expansion/species.json'
if expansion_manifest.exists():
    IDS += sorted(json.loads(expansion_manifest.read_text()))

class ExporterTests(unittest.TestCase):
    def test_material_paint_is_deterministic_and_preserves_spectral_alpha(self):
        self.assertIsNotNone(pipeline,'Shared original-material exporter is missing')
        palette=['687b8a']*16;materials=['metal','bark','fur','feather','glow','skin','bone','scales','leather','cloth','moss','rune','crystal','slime','ice','hair']
        first=pipeline.material_atlas(palette,materials,translucent=True)
        self.assertEqual(first.tobytes(),pipeline.material_atlas(palette,materials,translucent=True).tobytes())
        self.assertEqual(first.size,(128,128))
        self.assertLess(first.getpixel((16,112))[3],255)
        self.assertNotEqual(first.crop((0,0,32,32)).tobytes(),first.crop((32,0,64,32)).tobytes())

    def test_invalid_hierarchy_and_dimensions_are_rejected_before_export(self):
        self.assertIsNotNone(pipeline,'Shared geometry validator is missing')
        m=pipeline.Model('test')
        with self.assertRaises(ValueError):m.bone('child','missing',[0,0,0])
        m.bone('body','root',[0,1,0])
        with self.assertRaises(ValueError):m.bone('body','root',[0,0,0])
        with self.assertRaises(ValueError):m.box('body',[0,0,0],[1,0,1])

class EditableAssetsTests(unittest.TestCase):
    def test_scout_dagger_and_curled_grip_share_rigid_attachment(self):
        root=REPO/'src/main/resources/assets/mythic_realms_creatures/geckolib'
        geometry=json.loads((root/'models/entity/goblin_scout.geo.json').read_text())['minecraft:geometry'][0]
        bones={b['name']:b for b in geometry['bones']}
        self.assertEqual(bones['grip_right']['parent'],'hand_right')
        self.assertEqual(bones['dagger']['parent'],'grip_right')
        self.assertEqual(len(bones['grip_right']['cubes']),7) # three bent fingers and thumb
        clips=json.loads((root/'animations/entity/goblin_scout.animation.json').read_text())['animations']
        for name,animation in clips.items():
            for rigid in ('grip_right','dagger'):
                self.assertNotIn(rigid,animation['bones'],f'{name} must move the wrist, not detach the grip')

    def test_crystal_spider_transformed_soles_and_alternating_stance(self):
        root=REPO/'src/main/resources/assets/mythic_realms_creatures/geckolib'
        geometry=json.loads((root/'models/entity/crystal_spider.geo.json').read_text())['minecraft:geometry'][0]
        animations=json.loads((root/'animations/entity/crystal_spider.animation.json').read_text())['animations']
        bones={b['name']:b for b in geometry['bones']}
        feet=[f'leg_{side}_{i}_knee' for side in (-1,1) for i in range(4)]

        def sample(value,t):
            if not isinstance(value,dict):return value
            frames=sorted((float(k),v) for k,v in value.items())
            if t<=frames[0][0]:return frames[0][1]
            for (ta,va),(tb,vb) in zip(frames,frames[1:]):
                if t<=tb:return [a+(b-a)*(t-ta)/(tb-ta) for a,b in zip(va,vb)]
            return frames[-1][1]

        def rotate(point,pivot,degrees):
            x,y,z=[v-p for v,p in zip(point,pivot)]
            # Gecko's Bedrock model coordinates use clockwise Y/Z rotations.
            rx,ry,rz=[math.radians(v)*sign for v,sign in zip(degrees,(1,-1,-1))]
            y,z=y*math.cos(rx)-z*math.sin(rx),y*math.sin(rx)+z*math.cos(rx)
            x,z=x*math.cos(ry)+z*math.sin(ry),-x*math.sin(ry)+z*math.cos(ry)
            x,y=x*math.cos(rz)-y*math.sin(rz),x*math.sin(rz)+y*math.cos(rz)
            return [x+pivot[0],y+pivot[1],z+pivot[2]]

        def sole(table,name,animation=None,t=0):
            cube=table[name]['cubes'][0];heights=[]
            for corner in itertools.product(*[(o,o+s) for o,s in zip(cube['origin'],cube['size'])]):
                point=rotate(corner,cube.get('pivot',[0,0,0]),cube.get('rotation',[0,0,0]))
                cursor=name
                while cursor in table:
                    bone=table[cursor];channels=(animation or {}).get('bones',{}).get(cursor,{})
                    angles=[a+b for a,b in zip(bone.get('rotation',[0,0,0]),sample(channels.get('rotation',[0,0,0]),t))]
                    point=rotate(point,bone['pivot'],angles)
                    point=[a+b for a,b in zip(point,sample(channels.get('position',[0,0,0]),t))]
                    cursor=bone.get('parent')
                heights.append(point[1])
            return min(heights)

        for name in feet:
            self.assertAlmostEqual(sole(bones,name),0,places=6,msg=f'Floating or buried sole: {name}')
        # Reconstruct the reported defective geometry: stacked leg bends lift
        # every nominal .5px sole. This proves the check detects that regression.
        old=copy.deepcopy(bones)
        for side in (-1,1):
            for i in range(4):
                leg=old[f'leg_{side}_{i}'];leg['parent']='body';leg['rotation'][2]=side*-14
                foot=old[f'leg_{side}_{i}_knee'];foot['rotation']=[side*7,0,side*-20]
                foot['cubes'][0]['origin'][1]=.5;foot['cubes'][0]['size'][1]=7.5
        self.assertTrue(all(sole(old,name)>.2 for name in feet),'Old hovering geometry must fail grounding')
        for state in ('walk','run'):
            animation=animations[state]
            for step in range(101):
                t=animation['animation_length']*step/100
                heights=[sole(bones,name,animation,t) for name in feet]
                self.assertGreaterEqual(min(heights),-1e-6,f'Buried foot: {state}@{t}')
                self.assertGreaterEqual(sum(abs(y)<1e-6 for y in heights),4,f'Lost stance: {state}@{t}')

    def test_all_editable_projects_match_distributed_png_geometry_and_clips(self):
        for creature in IDS:
            with self.subTest(creature=creature):
                path=REPO/'tools/blockbench'/f'{creature}.bbmodel'
                self.assertTrue(path.is_file(),f'Native editable source missing for {creature}')
                native=json.loads(path.read_text())
                root=REPO/'src/main/resources/assets/mythic_realms_creatures'
                geometry=json.loads((root/f'geckolib/models/entity/{creature}.geo.json').read_text())['minecraft:geometry'][0]
                animations=json.loads((root/f'geckolib/animations/entity/{creature}.animation.json').read_text())['animations']
                embedded=Image.open(io.BytesIO(base64.b64decode(native['textures'][0]['source'].split(',',1)[1]))).convert('RGBA')
                actual=Image.open(root/f'textures/entity/{creature}.png').convert('RGBA')
                self.assertEqual(embedded.tobytes(),actual.tobytes(),f'Native PNG is stale: {creature}')
                self.assertEqual(len(native['elements']),sum(len(b.get('cubes',[])) for b in geometry['bones']))
                self.assertEqual({a['name'] for a in native['animations']},set(animations))
                bones={b['name']:b for b in geometry['bones']}
                self.assertEqual(len(bones),len(geometry['bones']))
                if creature in ('griffin','dire_wolf','wild_wyvern'):
                    joint=bones['tail_tip']['pivot']
                    for segment in ('tail','tail_tip'):
                        self.assertTrue(any(all(cube['origin'][i]<=joint[i]<=cube['origin'][i]+cube['size'][i] for i in range(3)) for cube in bones[segment]['cubes']),f'Detached tail joint: {creature}/{segment}')
                for name,bone in bones.items():
                    seen=set();cursor=name
                    while cursor in bones:
                        self.assertNotIn(cursor,seen,f'Bone cycle: {creature}/{cursor}')
                        seen.add(cursor);cursor=bones[cursor].get('parent')
                    for cube in bone.get('cubes',[]):
                        self.assertTrue(all(size>0 for size in cube['size']))
                        for face in cube['uv'].values():
                            self.assertTrue(all(0<=face['uv'][i]<face['uv'][i]+face['uv_size'][i]<=128 for i in (0,1)))
                self.assertLessEqual(animations['death']['animation_length'],.7,'Death plus5blend ticks must finish before vanilla corpse removal')
                for clip in animations.values():
                    self.assertTrue(set(clip['bones'])<=bones.keys())
                    for transforms in clip['bones'].values():
                        for frames in transforms.values():
                            if isinstance(frames,dict):self.assertTrue(all(0<=float(t)<=clip['animation_length'] for t in frames))

if __name__=='__main__':unittest.main()
