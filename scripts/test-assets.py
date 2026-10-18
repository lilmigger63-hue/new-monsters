#!/usr/bin/env python3
"""Validate all creature groups's actual resource and animation wiring."""
import json
from pathlib import Path
import struct
import unittest

ROOT = Path(__file__).resolve().parents[1] / 'src/main/resources'
IDS = ('goblin_scout', 'goblin_shaman', 'orc_warrior', 'minotaur', 'stone_troll', 'ancient_treant', 'forest_dryad', 'griffin', 'dire_wolf', 'wild_wyvern', 'cave_basilisk', 'crystal_spider', 'shadow_wraith', 'grave_knight', 'flame_imp', 'frost_elemental', 'moon_stag', 'slime_maiden', 'harpy', 'demon_sorceress')

class CreatureAssetsTest(unittest.TestCase):
    def test_language_has_all_creature_names(self):
        language=json.loads((ROOT/'assets/mythic_realms_creatures/lang/en_us.json').read_text())
        for name in IDS:
            self.assertIn(f'entity.mythic_realms_creatures.{name}',language)
            self.assertIn(f'item.mythic_realms_creatures.{name}_spawn_egg',language)

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
                states = ['idle', 'walk', 'run', 'attack', 'cast', 'hurt', 'death']
                if name in ('griffin', 'dire_wolf', 'wild_wyvern','moon_stag'):
                    states += ['sit', 'tame', 'ride']
                    self.assertTrue((asset / f'textures/entity/{name}_tamed.png').is_file())
                if name in ('griffin', 'wild_wyvern','shadow_wraith','flame_imp','harpy'):
                    states += ['fly', 'hover']
                if name == 'wild_wyvern':
                    self.assertTrue((asset / f'textures/entity/{name}_rare.png').is_file())
                for state in states:
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
        self.assertEqual(len(signatures), len(IDS), 'species must have distinct geometry')

if __name__ == '__main__':
    unittest.main()
