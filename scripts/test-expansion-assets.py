#!/usr/bin/env python3
"""Expansion identity, preservation, habitat and custom egg contracts."""
import hashlib
import json
from pathlib import Path
import re
import unittest
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / 'src/main/resources'
NS = 'mythic_realms_creatures'
ART = RES / 'assets' / NS
DOCS = ROOT / 'docs/monster-girl-expansion'
SPECIES = json.loads((DOCS / 'species.json').read_text())
BASE = json.loads((DOCS / 'preservation-baseline.json').read_text())


class ExpansionAssets(unittest.TestCase):
    def test_exact_thirteen_new_species_and_thirty_three_models(self):
        self.assertEqual(len(SPECIES), 13)
        models = {p.name.removesuffix('.geo.json') for p in (ART / 'geckolib/models/entity').glob('*.geo.json')}
        self.assertEqual(len(models), 33)
        self.assertTrue(set(SPECIES) <= models)
        self.assertIn('werecat', SPECIES)
        self.assertNotIn('ashen_wing_girl', models)

    def test_original_attributes_and_existing_animation_contracts_preserved(self):
        source = (ROOT / 'src/main/java/com/mythicrealms/creatures/entity/CreatureKind.java').read_text()
        attrs = {m[1]: re.sub(r'\s+', '', m[2]) for m in re.finditer(r'^\s*([A-Z_]+)\(([^\n]+)\)[,;]', source, re.M)}
        self.assertEqual(len(BASE['original_attributes']), 20)
        for name, params in BASE['original_attributes'].items():
            self.assertEqual(attrs[name], params, name)
        for path, digest in BASE['animations'].items():
            current=ROOT/path
            if hashlib.sha256(current.read_bytes()).hexdigest()==digest:continue
            # V3 explicitly permits appearance-only animation adjustments.
            adaptations=ROOT/'docs/monster-visual-overhaul-v3/animation-adaptations.json'
            allowed=json.loads(adaptations.read_text()) if adaptations.exists() else {}
            species=current.name.removesuffix('.animation.json')
            self.assertIn(species,allowed,path)
            original=ROOT/'tools/visual_v3_baselines'/current.name
            self.assertEqual(hashlib.sha256(original.read_bytes()).hexdigest(),digest,'original animation baseline must remain authentic')
            previous=json.loads(original.read_text())['animations'];actual=json.loads(current.read_text())['animations']
            self.assertEqual(set(actual),set(previous),species)
            for clip,before in previous.items():
                self.assertEqual(actual[clip]['animation_length'],before['animation_length'],species+'/'+clip)
                self.assertEqual(actual[clip].get('loop'),before.get('loop'),species+'/'+clip)
                if clip not in allowed[species]:self.assertEqual(actual[clip],before,species+'/'+clip)

    def test_only_allowed_original_habitat_tags_remain_populated(self):
        tags = RES / 'data' / NS / 'tags/worldgen/biome/spawns'
        populated = {p.stem for p in tags.glob('*.json') if json.loads(p.read_text())['values']}
        self.assertEqual(populated, set(SPECIES) | {'forest_dryad', 'slime_maiden'})

    def test_thirteen_distinct_original_eggs_have_real_item_models(self):
        pixels = set()
        lang = json.loads((ART / 'lang/en_us.json').read_text())
        for name in SPECIES:
            egg = name + '_spawn_egg'
            with Image.open(ART / 'textures/item' / (egg + '.png')) as image:
                self.assertEqual(image.size, (32, 32), name)
                self.assertEqual(image.mode, 'RGBA', name)
                self.assertGreater(len(image.getcolors(1025)), 4, name)
                pixels.add(hashlib.sha256(image.tobytes()).hexdigest())
            item = json.loads((ART / 'items' / (egg + '.json')).read_text())
            self.assertEqual(item['model']['model'], NS + ':item/' + egg)
            model = json.loads((ART / 'models/item' / (egg + '.json')).read_text())
            self.assertEqual(model['textures']['layer0'], NS + ':item/' + egg)
            self.assertIn('item.' + NS + '.' + egg, lang)
            loot = json.loads((RES / 'data' / NS / 'loot_table/entities' / (name + '.json')).read_text())
            self.assertTrue(loot['pools'], name)
        self.assertEqual(len(pixels), 13)


if __name__ == '__main__':
    unittest.main()
