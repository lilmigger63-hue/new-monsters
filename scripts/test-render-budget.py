#!/usr/bin/env python3
"""Check UV coverage before removing an otherwise redundant emissive mesh pass."""
from pathlib import Path
import json,re,unittest,sys
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
ASSET=ROOT/'src/main/resources/assets/mythic_realms_creatures'
SOURCE=(ROOT/'src/client/java/com/mythicrealms/creatures/client/MythicRealmsClient.java').read_text()
ACTIVE=set(re.findall(r'"([a-z_]+)"',SOURCE.split('EMISSIVE_SPECIES = java.util.Set.of(',1)[1].split(');',1)[0]))
def audit():
    rows={}
    for path in sorted((ASSET/'geckolib/models/entity').glob('*.geo.json')):
        species=path.name.removesuffix('.geo.json')
        bones=json.loads(path.read_text())['minecraft:geometry'][0]['bones']
        mask=ASSET/'textures/entity'/f'{species}_glowmask.png'
        alpha=Image.open(mask).convert('RGBA').getchannel('A') if mask.exists() else None
        cubes=[c for b in bones for c in b.get('cubes',[])]
        lit=0
        for cube in cubes:
            for face in cube['uv'].values():
                x,y=face['uv'];w,h=face['uv_size']
                rect=(min(x,x+w),min(y,y+h),max(x,x+w),max(y,y+h))
                if alpha is not None and alpha.crop(rect).getbbox():lit+=1
        rows[species]={'bones':len(bones),'cubes':len(cubes),'mapped_emissive_faces':lit,'emissive_pass':species in ACTIVE}
    return rows
class RenderBudget(unittest.TestCase):
    def test_every_enabled_emissive_pass_contributes(self):
        rows=audit()
        for species in ACTIVE:self.assertGreater(rows[species]['mapped_emissive_faces'],0,species)
    def test_removed_passes_remain_visually_empty(self):
        rows=audit()
        for species in ('wild_wyvern','slime_maiden','kobold'):
            self.assertNotIn(species,ACTIVE)
            self.assertEqual(rows[species]['mapped_emissive_faces'],0,species)
    def test_all_creatures_are_audited(self):self.assertEqual(len(audit()),33)
if __name__=='__main__':
    if '--report' in sys.argv:print(json.dumps(audit(),indent=2))
    else:unittest.main()
