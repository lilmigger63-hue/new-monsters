#!/usr/bin/env python3
"""Validate the first creature group's actual resource and animation wiring."""
import json
from pathlib import Path
import struct
import unittest

ROOT = Path(__file__).resolve().parents[1] / 'src/main/resources'
IDS = ('goblin_scout', 'goblin_shaman', 'orc_warrior', 'minotaur', 'stone_troll')

class CreatureAssetsTest(unittest.TestCase):
    def test_complete_distinct_creature_assets(self):
        signatures = set()
        for name in IDS:
            with self.subTest(creature=name):
                asset = ROOT / 'assets/mythic_realms_creatures'
                path = asset / f'geckolib/models/entity/{name}.geo.json'
                self.assertTrue(path.is_file(), f'missing model: {name}')
                geometry = json.loads(path.read_text())['minecraft:geometry'][0]
                bones = geometry['bones']
                names = {b['name'] for b in bones}
                cubes = [c for b in bones for c in b.get('cubes', [])]
                self.assertGreaterEqual(len(cubes), 12)
                signatures.add(json.dumps(bones, sort_keys=True))
                for bone in bones:
                    if 'parent' in bone:
                        self.assertIn(bone['parent'], names)
                animations = json.loads((asset / f'geckolib/animations/entity/{name}.animation.json').read_text())['animations']
                for state in ('idle', 'walk', 'attack', 'death'):
                    self.assertIn(state, animations)
                    self.assertGreater(animations[state]['animation_length'], 0)
                    for b in animations[state].get('bones', {}):
                        self.assertIn(b, names)
                png = (asset / f'textures/entity/{name}.png').read_bytes()
                self.assertEqual(png[:8], b'\x89PNG\r\n\x1a\n')
                self.assertEqual(struct.unpack('>II', png[16:24]), (128, 128))
                self.assertTrue((asset / f'items/{name}_spawn_egg.json').is_file())
                loot = ROOT / f'data/mythic_realms_creatures/loot_table/entities/{name}.json'
                self.assertTrue(json.loads(loot.read_text())['pools'])
        self.assertEqual(len(signatures), 5, 'species must have distinct geometry')

if __name__ == '__main__':
    unittest.main()
