#!/usr/bin/env python3
"""Merge generated language and survival loot after regenerating base assets."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
RES=ROOT/'src/main/resources'
lang=RES/'assets/mythic_realms_creatures/lang/en_us.json'
data=json.loads(lang.read_text())
for name in ('lang_items.json','lang_creatures_cd.json'):
    data.update(json.loads((ROOT/'tools'/name).read_text()))
lang.write_text(json.dumps(data,indent=2)+'\n')
DROPS={'goblin_scout': 'goblin_scrap', 'goblin_shaman': 'forest_essence', 'orc_warrior': 'orc_steel', 'grave_knight': 'orc_steel', 'minotaur': 'minotaur_horn', 'stone_troll': 'troll_heartstone', 'ancient_treant': 'living_wood', 'forest_dryad': 'forest_essence', 'moon_stag': 'forest_essence', 'griffin': 'griffin_feather', 'harpy': 'griffin_feather', 'dire_wolf': 'dire_fang', 'wild_wyvern': 'wyvern_scale', 'cave_basilisk': 'basilisk_scale', 'crystal_spider': 'crystal_shard', 'shadow_wraith': 'shadow_essence', 'flame_imp': 'infernal_ember', 'frost_elemental': 'frost_essence', 'slime_maiden': 'slime_pearl', 'demon_sorceress': 'shadow_essence'}
for creature,material in DROPS.items():
    p=RES/f'data/mythic_realms_creatures/loot_table/entities/{creature}.json'
    data=json.loads(p.read_text())
    materials=[material]+(['infernal_ember'] if creature=='demon_sorceress' else [])
    for item in materials:
        name='mythic_realms_creatures:'+item
        if any(e.get('name')==name for pool in data['pools'] for e in pool['entries']):continue
        data['pools'].append({'rolls':1,'entries':[{'type':'minecraft:item','name':name,'functions':[{'function':'minecraft:set_count','count':{'type':'minecraft:uniform','min':1,'max':2}}]}]})
    p.write_text(json.dumps(data,indent=2)+'\n')
