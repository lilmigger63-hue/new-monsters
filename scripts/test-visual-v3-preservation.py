#!/usr/bin/env python3
"""Protect gameplay and the sixteen species outside the V3 request."""
from pathlib import Path
import hashlib,json,unittest
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
if __name__=='__main__':unittest.main()
