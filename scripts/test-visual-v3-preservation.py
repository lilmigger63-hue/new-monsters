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
    def test_finished_creatures_are_not_overwritten(self):
        records=json.loads((DOC/'completed-art.json').read_text())
        for species,record in records.items():
            for path,digest in record['files'].items():
                self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest,species+': '+path)
    def test_succubus_death_rests_on_ground_with_folded_wings(self):
        asset=ROOT/'src/main/resources/assets/mythic_realms_creatures/geckolib'
        bones=json.loads((asset/'models/entity/succubus.geo.json').read_text())['minecraft:geometry'][0]['bones']
        death=json.loads((asset/'animations/entity/succubus.animation.json').read_text())['animations']['death']['bones']
        final=lambda frames:max(frames.items(),key=lambda item:float(item[0]))[1]
        pose={name:final(channels['rotation']) for name,channels in death.items() if name!='root' and 'rotation' in channels}
        floor=minimum_y(bones,final(death['root']['rotation']),pose)+final(death['root']['position'])[1]
        self.assertAlmostEqual(floor,.1,delta=.2,msg='The compact folded wings must not leave the corpse hovering')
        bodybones=[{**bone,'cubes':[] if bone['name'].startswith(('wing_','wingtip_')) else bone.get('cubes',[])} for bone in bones]
        bodyfloor=minimum_y(bodybones,final(death['root']['rotation']),pose)+final(death['root']['position'])[1]
        self.assertLess(bodyfloor,1.5,'Folded wings must allow the torso/arms to reach the ground')
    def test_dryad_death_does_not_bury_attached_limbs(self):
        asset=ROOT/'src/main/resources/assets/mythic_realms_creatures/geckolib'
        bones=json.loads((asset/'models/entity/forest_dryad.geo.json').read_text())['minecraft:geometry'][0]['bones']
        root=json.loads((asset/'animations/entity/forest_dryad.animation.json').read_text())['animations']['death']['bones']['root']
        rotation=max(root['rotation'].items(),key=lambda item:float(item[0]))[1]
        position=max(root['position'].items(),key=lambda item:float(item[0]))[1]
        self.assertGreaterEqual(minimum_y(bones,rotation)+position[1],0,'Dryad corpse geometry must remain above the ground')
if __name__=='__main__':unittest.main()
