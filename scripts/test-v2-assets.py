#!/usr/bin/env python3
"""V2 release contracts; artistic acceptance still needs the game client."""
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'src/main/resources'
GEO = ASSETS / 'assets/mythic_realms_creatures/geckolib/models/entity'
ANIM = ASSETS / 'assets/mythic_realms_creatures/geckolib/animations/entity'
BASE = json.loads((ROOT / 'docs/test-results/v2-baseline-assets.json').read_text())['hashes']
EXCLUDED = ('crystal_spider', 'flame_imp')


def geometry(name):
    return {b['name']: b for b in json.loads((GEO / (name + '.geo.json')).read_text())['minecraft:geometry'][0]['bones']}


class V2Contracts(unittest.TestCase):
    def test_all_eighteen_targets_have_real_model_and_animation_updates(self):
        models = [p for p in GEO.glob('*.geo.json') if str(p.relative_to(ASSETS)) in BASE]
        self.assertEqual(len(models), 20)
        for model in models:
            name = model.name.removesuffix('.geo.json')
            if name in EXCLUDED:
                continue
            for path in (model, ANIM / (name + '.animation.json')):
                self.assertNotEqual(hashlib.sha256(path.read_bytes()).hexdigest(), BASE[str(path.relative_to(ASSETS))], str(path))

    def test_finished_spider_and_imp_assets_are_unchanged(self):
        for name, digest in BASE.items():
            if not any(creature in name for creature in EXCLUDED):
                continue
            path = ROOT / name if name.startswith('tools/') else ASSETS / name
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), digest, name)

    def test_weapons_inherit_palms_without_independent_animation(self):
        for name, weapon, socket, palm in (
            ('goblin_scout', 'dagger', 'grip_right', 'hand_right'),
            ('goblin_shaman', 'staff', 'grip_right', 'hand_right'),
            ('orc_warrior', 'cleaver', 'grip_right', 'hand_right'),
            ('minotaur', 'axe', 'grip_right', 'hand_right'),
            ('grave_knight', 'sword', 'arm_1_hand', 'arm_1_forearm'),
        ):
            bones = geometry(name)
            self.assertEqual(bones[weapon]['parent'], socket, name)
            self.assertEqual(bones[socket]['parent'], palm, name)
            animations = json.loads((ANIM / (name + '.animation.json')).read_text())['animations']
            for clip in animations.values():
                self.assertNotIn(weapon, clip['bones'], name)
                if socket == 'grip_right':
                    self.assertNotIn(socket, clip['bones'], name)

    def test_fedora_attachment_and_controlled_geometry_budget(self):
        basilisk = geometry('cave_basilisk')
        self.assertEqual(basilisk['fedora']['parent'], 'head')
        for path in GEO.glob('*.geo.json'):
            bones = geometry(path.name.removesuffix('.geo.json'))
            self.assertLessEqual(sum(len(b.get('cubes', [])) for b in bones.values()), 180, path.name)
            self.assertLessEqual(len(bones), 55, path.name)

    def test_knight_vertical_carry_sword_does_not_start_below_floor(self):
        # The previous vertical carry revision put its blade tip at Y=-8.2.
        # This checks exported rest geometry; runtime poses are reviewed too.
        sword = geometry('grave_knight')['sword']
        self.assertTrue(sword['cubes'])
        self.assertGreater(min(c['origin'][1] for c in sword['cubes']), 0)


if __name__ == '__main__':
    unittest.main()
