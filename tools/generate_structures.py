#!/usr/bin/env python3
"""Rebuild editable exploration structures and vanilla 1.21.10 worldgen data.

No third-party Python modules. Pass --minecraft-jar to read the target DataVersion
from the actual Minecraft version.json; defaults to the retained cloud cache.
"""
import argparse
import gzip
import json
import math
from pathlib import Path
import struct
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'src/main/resources/data/mythic_realms_creatures'
NS = 'mythic_realms_creatures:'

# Typed NBT values: (tag ID, payload). Compound/list writers preserve numeric types.
def integer(n): return (3, n)
def byte(n): return (1, n)
def string(s): return (8, s)
def double(n): return (6, n)
def floating(n): return (5, n)
def compound(d): return (10, d)
def sequence(t, values): return (9, (t, values))
def ints(values): return sequence(3, list(values))
def doubles(values): return sequence(6, list(values))
def utf(s):
    b = s.encode('utf8')
    return struct.pack('>H', len(b)) + b

def payload(t, v):
    if t == 1: return struct.pack('>b', v)
    if t == 3: return struct.pack('>i', v)
    if t == 5: return struct.pack('>f', v)
    if t == 6: return struct.pack('>d', v)
    if t == 8: return utf(v)
    if t == 9:
        subtype, values = v
        return bytes([subtype]) + struct.pack('>i', len(values)) + b''.join(payload(subtype, x) for x in values)
    if t == 10:
        return b''.join(bytes([st]) + utf(k) + payload(st, sv) for k, (st, sv) in v.items()) + b'\0'
    raise ValueError(t)


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + '\n')


class Template:
    def __init__(self, name, size):
        self.name, self.size = name, size
        self.blocks, self.entities = {}, []
        # Explicit air carves navigable interiors (especially the partially buried crypt).
        for x in range(size[0]):
            for y in range(size[1]):
                for z in range(size[2]): self.put(x, y, z, 'air')

    def put(self, x, y, z, block, properties=None, nbt=None):
        self.blocks[x, y, z] = (block, properties or {}, nbt)

    def box(self, a, b, block, properties=None):
        for x in range(a[0], b[0] + 1):
            for y in range(a[1], b[1] + 1):
                for z in range(a[2], b[2] + 1): self.put(x, y, z, block, properties)

    def chest(self, x, y, z):
        self.put(x, y, z, 'chest', {'facing': 'south', 'type': 'single', 'waterlogged': 'false'},
                 {'id': string('minecraft:chest'), 'LootTable': string(NS + 'chests/' + self.name)})

    def inhabitant(self, kind, x, y, z):
        # Structure generation is natural spawning too; keep only the two
        # original inhabitants permitted by the expansion's population policy.
        if kind not in ('forest_dryad', 'slime_maiden'): return
        self.entities.append({'pos': doubles([x, y, z]), 'blockPos': ints([math.floor(x), math.floor(y), math.floor(z)]),
            'nbt': compound({'id': string(NS + kind), 'Pos': doubles([x, y, z]),
                'Rotation': sequence(5, [0., 0.]), 'PersistenceRequired': byte(1), 'OnGround': byte(1)})})

    def save(self, version):
        # An upward facing entry connector also makes /place jigsaw and the server tests useful.
        cx, cz = self.size[0] // 2, self.size[2] // 2
        self.put(cx, 0, cz, 'jigsaw', {'orientation': 'up_north'}, {
            'id': string('minecraft:jigsaw'), 'name': string(NS + 'entry'), 'target': string('minecraft:empty'),
            'pool': string('minecraft:empty'), 'final_state': string('minecraft:mossy_cobblestone'),
            'joint': string('rollable'), 'selection_priority': integer(0), 'placement_priority': integer(0)})
        palette, lookup, blocks = [], {}, []
        for (x, y, z), (name, props, nbt) in sorted(self.blocks.items()):
            key = (name, tuple(sorted(props.items())))
            if key not in lookup:
                lookup[key] = len(palette)
                state = {'Name': string('minecraft:' + name)}
                if props: state['Properties'] = compound({k: string(v) for k, v in props.items()})
                palette.append(state)
            entry = {'pos': ints([x, y, z]), 'state': integer(lookup[key])}
            if nbt: entry['nbt'] = compound(nbt)
            blocks.append(entry)
        tag = {'DataVersion': integer(version), 'size': ints(self.size),
               'palette': sequence(10, palette), 'blocks': sequence(10, blocks), 'entities': sequence(10, self.entities)}
        path = DATA / 'structure' / (self.name + '.nbt')
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(gzip.compress(bytes([10, 0, 0]) + payload(10, tag), mtime=0))
        print(f'{self.name}: {len(blocks)} blocks, {len(palette)} states, {len(self.entities)} inhabitants, DataVersion {version}')


def tower():
    t = Template('goblin_watchtower', (11, 16, 11))
    t.box((1, 0, 1), (9, 1, 9), 'mossy_cobblestone')
    for x in (2, 8):
        for z in (2, 8): t.box((x, 2, z), (x, 13, z), 'dark_oak_log')
    for y in range(2, 8):
        for p in range(2, 9):
            for x, z in ((2, p), (8, p), (p, 2), (p, 8)):
                if (x, z) == (5, 2) and y < 5: continue
                if y in (4, 5) and (x, z) in ((2, 5), (8, 5), (5, 8)): continue
                t.put(x, y, z, 'cobblestone' if (x+y+z)%4 else 'mossy_cobblestone')
    t.box((2, 8, 2), (8, 8, 8), 'dark_oak_planks')
    for y in range(2, 9): t.put(3, y, 7, 'ladder', {'facing': 'east', 'waterlogged': 'false'})
    t.put(3, 8, 7, 'air')
    for p in range(1, 10):
        for x, z in ((1, p), (9, p), (p, 1), (p, 9)):
            if (x+z)%5: t.put(x, 9, z, 'dark_oak_fence')
    t.box((1, 13, 1), (9, 13, 9), 'dark_oak_slab', {'type': 'bottom', 'waterlogged': 'false'})
    t.box((3, 14, 3), (7, 14, 7), 'dark_oak_planks')
    t.box((4, 15, 4), (6, 15, 6), 'dark_oak_slab', {'type': 'bottom', 'waterlogged': 'false'})
    t.put(8, 13, 2, 'air'); t.put(9, 13, 2, 'air')
    t.put(6, 2, 6, 'campfire', {'lit': 'false', 'facing': 'north', 'signal_fire': 'false', 'waterlogged': 'false'})
    t.chest(7, 2, 7); t.chest(7, 9, 6)
    t.inhabitant('goblin_scout', 5.5, 2, 4.5)
    t.inhabitant('goblin_scout', 6.5, 9, 4.5)
    t.inhabitant('goblin_shaman', 5.5, 9, 6.5)
    return t


def shrine():
    t = Template('forest_shrine', (15, 10, 15))
    for x in range(1, 14):
        for z in range(1, 14):
            if (x-7)**2+(z-7)**2 < 44:
                t.put(x, 0, z, 'mossy_stone_bricks' if (x+z)%3 else 'moss_block')
    for x, z in ((3, 3), (11, 3), (3, 11), (11, 11)):
        t.box((x, 1, z), (x, 5 if x+z!=14 else 3, z), 'mossy_stone_bricks')
        t.put(x, 6 if x+z!=14 else 4, z, 'chiseled_stone_bricks')
    t.box((3, 6, 3), (11, 6, 3), 'stone_brick_slab', {'type': 'bottom', 'waterlogged': 'false'})
    t.box((3, 6, 3), (3, 6, 8), 'stone_brick_slab', {'type': 'bottom', 'waterlogged': 'false'})
    t.box((6, 1, 7), (8, 1, 9), 'chiseled_stone_bricks')
    t.put(7, 2, 8, 'amethyst_block'); t.put(7, 3, 8, 'small_amethyst_bud', {'facing':'up','waterlogged':'false'})
    for x, z in ((4, 3), (3, 4), (10, 3), (11, 10), (4, 11)):
        t.box((x, 1, z), (x+1, 2, z+1), 'azalea_leaves', {'persistent': 'true', 'distance': '1', 'waterlogged': 'false'})
    for x, z in ((5, 5), (10, 9), (4, 9), (9, 4)):
        t.put(x, 1, z, 'moss_carpet')
        t.put(x, 0, z, 'glowstone')
    t.chest(9, 1, 9)
    t.inhabitant('forest_dryad', 6.5, 1, 5.5)
    t.inhabitant('ancient_treant', 10.5, 1, 6.5)
    return t


def crypt():
    t = Template('grave_crypt', (13, 11, 17))
    t.box((1, 0, 1), (11, 0, 15), 'deepslate_tiles')
    t.box((1, 1, 5), (11, 6, 15), 'cracked_deepslate_bricks')
    t.box((2, 1, 6), (10, 5, 14), 'air')
    for x in (3, 9):
        for z in (7, 11):
            t.box((x, 1, z), (x, 4, z), 'polished_basalt', {'axis':'y'})
    # Stairway exits at local y=6; generation starts five blocks below terrain.
    for z in range(1, 8):
        y = 7-z
        t.box((5, 0, z), (7, y, z), 'stone_bricks')
        t.box((5, y+1, z), (7, min(y+4, 10), z), 'air')
        for x in range(5, 8): t.put(x, y, z, 'stone_brick_stairs', {'facing':'north','half':'bottom','shape':'straight','waterlogged':'false'})
    t.box((4, 7, 1), (4, 9, 3), 'mossy_stone_bricks')
    t.box((8, 7, 1), (8, 9, 3), 'mossy_stone_bricks')
    t.box((4, 10, 1), (8, 10, 3), 'stone_brick_slab', {'type':'bottom','waterlogged':'false'})
    for z in (9, 13):
        for x in (3, 9):
            t.box((x, 1, z), (x+1, 1, z+1), 'chiseled_deepslate')
            t.put(x, 2, z, 'skeleton_skull', {'rotation':'0'})
    for x, z in ((2, 8), (10, 12)):
        t.put(x, 4, z, 'soul_lantern', {'hanging':'true','waterlogged':'false'})
        t.put(x, 5, z, 'chain', {'axis':'y','waterlogged':'false'})
    t.chest(6, 1, 14)
    t.inhabitant('grave_knight', 6.5, 1, 11.5)
    t.inhabitant('shadow_wraith', 8.5, 2, 8.5)
    return t


def nest():
    t = Template('wyvern_nest', (17, 8, 17))
    for x in range(17):
        for z in range(17):
            r = (x-8)**2+(z-8)**2
            if r <= 59:
                t.put(x, 0, z, 'stone' if (x+z)%3 else 'andesite')
                t.put(x, 1, z, 'coarse_dirt' if r<28 else 'stripped_spruce_log', {'axis':'x'} if r>=28 else None)
            if 37 < r <= 64:
                t.put(x, 2, z, 'spruce_log', {'axis': 'x' if z%2 else 'z'})
                if (x+z)%3: t.put(x, 3, z, 'spruce_fence')
            if r < 26: t.put(x, 2, z, 'hay_block', {'axis':'y'})
    for x, z in ((5, 8), (11, 7), (9, 11)):
        t.put(x, 3, z, 'bone_block', {'axis':'y'})
    # Turtle eggs are decorative; the chest contains actual wyvern-taming food.
    t.put(7, 3, 7, 'turtle_egg', {'eggs':'3', 'hatch':'0'})
    t.put(8, 3, 7, 'turtle_egg', {'eggs':'2', 'hatch':'0'})
    t.chest(6, 3, 10)
    t.inhabitant('wild_wyvern', 9, 3, 9)
    return t


def loot(entries, rolls):
    return {'type':'minecraft:chest','pools':[{'rolls':{'type':'minecraft:uniform','min':rolls[0],'max':rolls[1]},
        'entries':[{'type':'minecraft:item','name':name if ':' in name else 'minecraft:'+name,'weight':weight,
            'functions':[{'function':'minecraft:set_count','count':{'type':'minecraft:uniform','min':low,'max':high}}]}
                   for name, weight, low, high in entries]}]}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--minecraft-jar', type=Path, default=Path('/workspace/.gradle-cache/caches/fabric-loom/1.21.10/minecraft-common.jar'))
    args=parser.parse_args()
    with zipfile.ZipFile(args.minecraft_jar) as jar:
        version=json.loads(jar.read('version.json'))
        if version['id'] != '1.21.10': raise SystemExit('Only Minecraft 1.21.10 templates are supported')
        dv=version['world_version']
    specs=[
        (tower(),30,10,9037141,0,['minecraft:plains','#minecraft:is_forest','#minecraft:is_savanna']),
        (shrine(),34,12,9037142,0,['#minecraft:is_forest']),
        (crypt(),36,12,9037143,-5,['minecraft:dark_forest','minecraft:pale_garden','minecraft:taiga','minecraft:old_growth_pine_taiga']),
        (nest(),52,20,9037144,0,['#minecraft:is_mountain'])]
    for t, spacing, separation, salt, offset, biomes in specs:
        t.save(dv)
        write_json(DATA/'worldgen/structure'/f'{t.name}.json', {
            'type':'minecraft:jigsaw', 'biomes':'#'+NS+'has_structure/'+t.name,
            'step':'surface_structures', 'terrain_adaptation':'beard_thin', 'spawn_overrides':{},
            'start_pool':NS+t.name+'/start', 'size':1, 'start_height':{'absolute':offset},
            'project_start_to_heightmap':'WORLD_SURFACE_WG','max_distance_from_center':32,'use_expansion_hack':False})
        write_json(DATA/'worldgen/structure_set'/f'{t.name}.json', {
            'fabric:load_conditions':[{'condition':NS+'structure_enabled','structure':t.name}],
            'structures':[{'structure':NS+t.name,'weight':1}],
            'placement':{'type':'minecraft:random_spread','spacing':spacing,'separation':separation,'salt':salt,
                         'exclusion_zone':{'other_set':'minecraft:villages','chunk_count':6}}})
        write_json(DATA/'worldgen/template_pool'/t.name/'start.json', {'fallback':'minecraft:empty','elements':[
            {'weight':1,'element':{'element_type':'minecraft:single_pool_element','location':NS+t.name,
                                  'processors':{'processors':[]},'projection':'rigid'}}]})
        optional_tags = {
            'goblin_watchtower':['c:is_plains','c:is_forest','c:is_savanna'],
            'forest_shrine':['c:is_forest'], 'grave_crypt':['c:is_taiga'], 'wyvern_nest':['c:is_mountain']}
        write_json(DATA/'tags/worldgen/biome/has_structure'/f'{t.name}.json', {'replace':False,
            'values':biomes + [{'id':'#'+tag,'required':False} for tag in optional_tags[t.name]]})
    loot_specs={
        'goblin_watchtower':([('iron_nugget',8,3,12),('arrow',6,3,10),('bread',6,1,3),('emerald',2,1,2),('glow_berries',4,2,5),(NS+'goblin_scrap',4,1,3)],(2,4)),
        'forest_shrine':([('amethyst_shard',7,2,5),('glow_berries',6,2,6),('gold_nugget',4,2,8),('experience_bottle',2,1,2),(NS+'forest_essence',4,1,2),(NS+'living_wood',4,1,3),(NS+'twilight_relic',1,1,1)],(3,5)),
        'grave_crypt':([('bone',8,3,8),('iron_ingot',5,1,3),('gold_nugget',5,2,8),('spectral_arrow',4,3,8),(NS+'shadow_essence',3,1,2),('echo_shard',1,1,1)],(3,5)),
        'wyvern_nest':([(NS+'venomous_morsel',9,2,4),(NS+'wyvern_scale',4,1,3),('fermented_spider_eye',4,1,3),('rabbit',6,2,5),('gold_ingot',3,1,3),('saddle',2,1,1),('diamond',1,1,2)],(3,5))}
    for name,(entries,rolls) in loot_specs.items():write_json(DATA/'loot_table/chests'/f'{name}.json',loot(entries,rolls))

if __name__=='__main__':main()
