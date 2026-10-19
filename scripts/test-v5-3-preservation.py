#!/usr/bin/env python3
"""Strict V5.3 scope, single active species, timing and reviewed-art protection."""
from pathlib import Path
import hashlib,json,unittest,sys
ROOT=Path(__file__).resolve().parents[1];DOC=ROOT/'docs/monster-girl-v5-3'
sys.path.insert(0,str(ROOT/'tools'))
from visual_v3_geometry import minimum_y

class V53Preservation(unittest.TestCase):
    def test_gameplay_audio_renderer_and_original_twenty_unchanged(self):
        for path,digest in json.loads((DOC/'protected-baseline.json').read_text()).items():
            self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest,path)
    def test_only_one_active_species_and_completed_art_frozen(self):
        state=json.loads((DOC/'state.json').read_text());done=state['completed']
        for species,paths in state['paths'].items():
            if species==state['active']:continue
            for path in paths:
                digest=done[species]['files'][path] if species in done else state['baseline_hashes'][path]
                self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest,path)
    def test_all_clip_names_durations_loops_and_combat_motion_preserved(self):
        state=json.loads((DOC/'state.json').read_text())
        for species,paths in state['paths'].items():
            path=paths[1];before=json.loads((DOC/'baselines'/path).read_text())['animations'];after=json.loads((ROOT/path).read_text())['animations']
            self.assertEqual(set(before),set(after),species)
            for name,clip in before.items():
                for key in ('animation_length','loop'):self.assertEqual(clip.get(key),after[name].get(key),(species,name,key))
                if name in ('attack','heavy','cast','hurt','teleport'):self.assertEqual(clip,after[name],(species,name))
    def test_archived_baselines_match_initial_hashes(self):
        state=json.loads((DOC/'state.json').read_text())
        for path,digest in state['baseline_hashes'].items():
            cached=DOC/'baselines'/path
            if cached.exists():self.assertEqual(hashlib.sha256(cached.read_bytes()).hexdigest(),digest,path)
    def test_reviewed_authoring_source_reconstructs_live_geometry_and_pixels(self):
        import generate_v5_3 as source
        from PIL import Image
        state=json.loads((DOC/'state.json').read_text())
        for species in list(state['completed'])+([state['active']] if state['active'] else []):
            if species not in source.BUILDERS:continue
            m,palette,roles,_,_=source.BUILDERS[species]()
            expected=json.loads((ROOT/state['paths'][species][0]).read_text())['minecraft:geometry'][0]['bones']
            self.assertEqual(m.bones,expected,species)
            self.assertEqual(source.atlas(palette,roles,False,species).convert('RGBA').tobytes(),Image.open(ROOT/state['paths'][species][2]).convert('RGBA').tobytes(),species)
    def test_active_and_reviewed_corpses_rest_above_ground(self):
        state=json.loads((DOC/'state.json').read_text())
        for species in list(state['completed'])+([state['active']] if state['active'] else []):
            geo,anim=state['paths'][species][:2]
            bones=json.loads((ROOT/geo).read_text())['minecraft:geometry'][0]['bones'];death=json.loads((ROOT/anim).read_text())['animations']['death']['bones']
            final=lambda frames:max(frames.items(),key=lambda item:float(item[0]))[1]
            pose={name:final(channels['rotation']) for name,channels in death.items() if name!='root' and 'rotation' in channels}
            floor=minimum_y(bones,final(death['root']['rotation']),pose)+final(death['root']['position'])[1]
            self.assertAlmostEqual(floor,.1,delta=.25,msg=species+' corpse must reach the floor without burial')
    def test_authored_keyframes_stay_inside_exact_existing_duration(self):
        import generate_v5_3 as source
        for species,builder in source.BUILDERS.items():
            *_,animations=builder()
            for name,clip in animations.items():
                for bone,channels in clip.get('bones',{}).items():
                    for frames in channels.values():
                        if isinstance(frames,dict):
                            self.assertTrue(all(0<=float(t)<=clip['animation_length'] for t in frames),(species,name,bone))
    def test_ender_face_has_no_metallic_eye_frames(self):
        path=ROOT/'src/main/resources/assets/mythic_realms_creatures/geckolib/models/entity/ender_dragon_girl.geo.json'
        bones=json.loads(path.read_text())['minecraft:geometry'][0]['bones'];head=next(b for b in bones if b['name']=='head')
        for c in head['cubes']:
            u,v=c['uv']['north']['uv'];material=int(u//32+4*(v//32))
            self.assertFalse(material==6 and c['origin'][2]<-2.8,'Metallic rectangular eye frame must be replaced with a readable organic eye')
if __name__=='__main__':unittest.main()
