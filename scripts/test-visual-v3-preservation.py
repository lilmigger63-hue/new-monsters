#!/usr/bin/env python3
"""Protect gameplay and the sixteen species outside the V3 request."""
from pathlib import Path
import hashlib,json,unittest,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"tools"))
from visual_v3_geometry import minimum_y
ROOT=Path(__file__).resolve().parents[1]
DOC=ROOT/'docs/monster-visual-overhaul-v3'
TARGETS='harpy forest_dryad slime_maiden minotaur vampire valkyrie succubus ender_dragon_girl centaur fox_spirit_girl anubis kobold cyclops dhampir sahuagin holstaurus werecat'.split()
class Preservation(unittest.TestCase):
    def test_all_server_gameplay_data_and_spawn_eggs_unchanged(self):
        for path,digest in json.loads((DOC/'gameplay-baseline.json').read_text()).items():
            self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest,path)
    def test_non_target_species_art_unchanged(self):
        for path,digest in json.loads((DOC/'art-baseline.json').read_text()).items():
            name=Path(path).name
            if any(name.startswith(id+'.') or name.startswith(id+'_') for id in TARGETS):continue
            self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest,path)
    def test_dryad_death_does_not_bury_attached_limbs(self):
        asset=ROOT/'src/main/resources/assets/mythic_realms_creatures/geckolib'
        bones=json.loads((asset/'models/entity/forest_dryad.geo.json').read_text())['minecraft:geometry'][0]['bones']
        root=json.loads((asset/'animations/entity/forest_dryad.animation.json').read_text())['animations']['death']['bones']['root']
        rotation=max(root['rotation'].items(),key=lambda item:float(item[0]))[1]
        position=max(root['position'].items(),key=lambda item:float(item[0]))[1]
        self.assertGreaterEqual(minimum_y(bones,rotation)+position[1],0,'Dryad corpse geometry must remain above the ground')
if __name__=='__main__':unittest.main()
