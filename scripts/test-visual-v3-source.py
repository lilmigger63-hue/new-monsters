#!/usr/bin/env python3
"""Read-only reconstruction guards against authoring code drifting from reviewed art."""
from pathlib import Path
import sys,json,unittest
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import generate_visual_overhaul_v3 as source
class AuthoringSource(unittest.TestCase):
    def test_all_builders_reproduce_reviewed_geometry(self):
        for species,builder in source.BUILDERS.items():
            model,*_=builder()
            expected=json.loads((ROOT/source.ASSET/'geckolib/models/entity'/f'{species}.geo.json').read_text())['minecraft:geometry'][0]['bones']
            self.assertEqual(model.bones,expected,species)
    def test_all_builders_reproduce_reviewed_texture_pixels(self):
        for species,builder in source.BUILDERS.items():
            _,palette,roles,_=builder()
            image=source.reference_atlas(palette,roles,species=='slime_maiden',species)
            expected=Image.open(ROOT/source.ASSET/'textures/entity'/f'{species}.png').convert('RGBA')
            self.assertEqual(image.convert('RGBA').tobytes(),expected.tobytes(),species)
if __name__=='__main__':unittest.main()
