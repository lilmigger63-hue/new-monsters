#!/usr/bin/env python3
"""Strict V5.3 scope, single active species, timing and reviewed-art protection."""
from pathlib import Path
import hashlib,json,unittest,sys
ROOT=Path(__file__).resolve().parents[1];DOC=ROOT/'docs/monster-girl-v5-3'
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
    def test_ender_face_has_no_metallic_eye_frames(self):
        path=ROOT/'src/main/resources/assets/mythic_realms_creatures/geckolib/models/entity/ender_dragon_girl.geo.json'
        bones=json.loads(path.read_text())['minecraft:geometry'][0]['bones'];head=next(b for b in bones if b['name']=='head')
        for c in head['cubes']:
            u,v=c['uv']['north']['uv'];material=int(u//32+4*(v//32))
            self.assertFalse(material==6 and c['origin'][2]<-2.8,'Metallic rectangular eye frame must be replaced with a readable organic eye')
if __name__=='__main__':unittest.main()
