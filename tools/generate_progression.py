#!/usr/bin/env python3
"""Generate editable progression recipes, models and distinct original 32px item sprites.

Requires Pillow. Does not modify the shared language file: merge lang_items.json
into en_us.json when integrating. Better Combat presets match the published
bettercombat-fabric-3.0.0+1.21.10.jar (Modrinth version qaOWa2t6).
"""
from pathlib import Path
import json
from PIL import Image, ImageDraw
ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / 'src/main/resources'
NS = 'mythic_realms_creatures'
A = RES / 'assets' / NS
D = RES / 'data' / NS

def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2) + '\n')

MATERIALS = {
 'goblin_scrap': ('Goblin Scrap', '#8f997c', 'scrap'),
 'orc_steel': ('Orc Steel', '#82939b', 'ingot'),
 'minotaur_horn': ('Minotaur Horn', '#d2b587', 'horn'),
 'troll_heartstone': ('Troll Heartstone', '#879c76', 'stone'),
 'living_wood': ('Living Wood', '#b68b4e', 'wood'),
 'forest_essence': ('Forest Essence', '#6ad181', 'essence'),
 'griffin_feather': ('Griffin Feather', '#f0d68b', 'feather'),
 'dire_fang': ('Dire Fang', '#d2e6ec', 'fang'),
 'wyvern_scale': ('Wyvern Scale', '#6b9982', 'scale'),
 'basilisk_scale': ('Basilisk Scale', '#98b76c', 'scale'),
 'crystal_shard': ('Crystal Shard', '#bba2f3', 'crystal'),
 'shadow_essence': ('Shadow Essence', '#a076c9', 'essence'),
 'frost_essence': ('Frost Essence', '#98e3f4', 'snowflake'),
 'infernal_ember': ('Infernal Ember', '#ef9450', 'flame'),
 'slime_pearl': ('Slime Pearl', '#90deb9', 'pearl'),
}
FOODS = {
 'sunseed_biscuit': ('Sunseed Biscuit', '#dfae62', 'biscuit'),
 'hearty_meat': ('Hearty Meat', '#ad6748', 'meat'),
 'moonblossom': ('Moonblossom', '#c6d9ff', 'flower'),
 'venomous_morsel': ('Venomous Morsel', '#b3ba64', 'morsel'),
}
EQUIPMENT = {
 'griffin_saddle': ('Griffin Saddle', '#c08b4b', 'saddle'),
 'wyvern_harness': ('Wyvern Harness', '#789994', 'harness'),
 'crystal_fang_sword': ('Crystal Fang Sword', '#b8a1f2', 'sword'),
 'orc_war_axe': ('Orc War Axe', '#92a5ad', 'axe'),
 'basilisk_spear': ('Basilisk Spear', '#accb7c', 'spear'),
 'frostbound_staff': ('Frostbound Staff', '#9ce5f5', 'staff'),
 'twilight_relic': ('Twilight Relic', '#c3a1e9', 'relic'),
}
ITEMS = MATERIALS | FOODS | EQUIPMENT
OUTLINE = '#242933'
GOLD = '#dbb568'
WOOD = '#725340'

def sprite(color, shape, name):
    im = Image.new('RGBA', (32,32)); p = ImageDraw.Draw(im)
    rgb = tuple(bytes.fromhex(color[1:])); light = tuple(min(255,c+35) for c in rgb); dark = tuple(int(c*.63) for c in rgb)
    def poly(points, fill=color, width=1): p.polygon(points, fill=fill, outline=OUTLINE, width=width)
    if shape in ('sword','spear','staff','axe'):
        p.line((5,27,23,9),fill=OUTLINE,width=6);p.line((5,27,23,9),fill=WOOD,width=3)
        for a in (8,11,14):p.line((a-1,30-a,a+2,29-a), fill=GOLD, width=1)
        if shape=='sword':
            poly([(12,17),(24,3),(29,2),(28,8),(16,21)])
            p.line((16,17,26,6),fill=light,width=2);p.line((10,17,17,24),fill=OUTLINE,width=5);p.line((10,17,17,24),fill=GOLD,width=3)
        elif shape=='spear':
            poly([(19,9),(28,1),(29,12),(23,15)])
            p.line((23,11,27,4),fill=light,width=2);p.line((19,13,24,18),fill=GOLD,width=2)
        elif shape=='axe':
            poly([(15,4),(22,5),(28,11),(29,18),(24,19),(16,11),(12,9)])
            p.line((23,7,28,12,28,16),fill=light,width=2);p.line((18,6,23,11),fill=GOLD,width=2)
        else:
            poly([(19,2),(27,2),(30,8),(26,15),(20,14),(16,8)],GOLD)
            poly([(22,3),(27,7),(24,12),(20,8)])
            p.line((21,5,23,4),fill=light,width=1)
            p.line((12,4,12,8),fill=light);p.line((10,6,14,6),fill=light)
    elif shape=='ingot':
        poly([(5,12),(21,7),(28,12),(26,23),(10,27),(4,22)])
        poly([(5,12),(21,7),(28,12),(11,18)],light)
        poly([(11,18),(28,12),(26,23),(10,27)],dark)
    elif shape=='scrap':
        poly([(5,9),(17,4),(24,8),(26,19),(21,26),(10,27),(6,21),(11,19),(4,16)])
        p.line((10,11,19,9,22,16,17,22),fill=light,width=2);p.rectangle((13,13,16,16),fill=OUTLINE)
    elif shape=='wood':
        poly([(4,13),(19,3),(27,8),(27,19),(13,28),(5,24)],WOOD)
        poly([(5,13),(13,17),(27,8),(19,3)],color)
        poly([(13,17),(27,8),(27,19),(13,28)],dark)
        p.line((16,18,23,14),fill=light,width=2);poly([(9,9),(10,3),(17,5),(15,10)],'#64a765')
    elif shape in ('horn','fang'):
        pts=[(6,6),(14,5),(22,10),(25,19),(23,27),(19,29),(18,21),(13,17),(8,15)] if shape=='horn' else [(8,5),(22,5),(24,11),(19,23),(12,29),(14,18),(9,13)]
        poly(pts);p.line((10,8,18,11,20,18),fill=light,width=2);p.line((9,5,20,7),fill=dark,width=3)
    elif shape=='feather':
        poly([(7,24),(5,17),(10,9),(21,3),(27,3),(27,10),(22,18),(15,24)],color)
        p.line((5,28,24,6),fill=OUTLINE,width=3);p.line((5,28,24,6),fill=GOLD)
        for x,y in [(10,19),(14,14),(19,9)]:p.line((x,y,x+7,y),fill=dark,width=1)
    elif shape=='scale':
        poly([(15,3),(27,10),(26,21),(16,29),(5,22),(4,11)])
        poly([(15,6),(23,12),(15,24),(8,19)],light)
        p.line((15,7,15,24),fill=dark,width=2)
        if name=='basilisk_scale':p.ellipse((13,12,18,18),fill=GOLD);p.line((16,12,16,18),fill=OUTLINE,width=2)
    elif shape=='crystal':
        poly([(13,2),(22,7),(27,22),(16,29),(6,19)])
        poly([(13,2),(16,16),(6,19)],light);poly([(16,16),(22,7),(27,22),(16,29)],dark)
        p.line((13,5,15,14),fill='#f1e7ff',width=2)
    elif shape in ('essence','pearl','stone'):
        poly([(12,4),(21,4),(27,11),(28,20),(22,27),(10,28),(4,20),(5,11)],dark)
        p.ellipse((7,6,25,25),fill=color)
        if shape=='essence':
            p.arc((10,8,23,22),20,290,fill=light,width=3);p.ellipse((13,13,18,18),fill=light)
            p.line((4,7,1,4),fill=color,width=2);p.line((26,26,29,29),fill=color,width=2)
        elif shape=='stone':
            p.line((14,6,12,13,18,17,15,25),fill=light,width=2);p.polygon([(17,10),(22,13),(19,18),(16,16)],fill='#c4df91')
        else:p.ellipse((10,8,15,12),fill=light);p.arc((8,9,25,25),5,100,fill=dark,width=2)
    elif shape=='snowflake':
        for pts in [(16,3,16,29),(4,9,28,23),(4,23,28,9)]:p.line(pts,fill=OUTLINE,width=5);p.line(pts,fill=color,width=3)
        for x,y,dx,dy in [(16,8,4,4),(16,24,4,-4),(8,12,0,-5),(24,20,0,5),(8,20,-4,0),(24,12,4,0)]:p.line((x-dx,y+dy,x,y,x+dx,y+dy),fill=light,width=2)
        p.ellipse((13,13,19,19),fill=light)
    elif shape=='flame':
        poly([(16,2),(19,12),(25,7),(24,17),(29,20),(24,28),(10,29),(4,22),(7,12),(11,17)])
        p.polygon([(16,12),(20,22),(23,19),(22,26),(12,27),(10,22)],fill='#ffdb87')
    elif shape=='biscuit':
        p.ellipse((4,5,28,28),fill=OUTLINE);p.ellipse((5,6,27,26),fill=color);p.arc((8,9,24,25),0,180,fill=dark,width=2)
        for x,y in [(10,11),(18,10),(21,17),(13,20),(8,17)]:p.line((x,y,x+1,y+2),fill='#f9d685',width=2)
    elif shape in ('meat','morsel'):
        poly([(4,16),(8,8),(18,5),(26,9),(29,17),(23,26),(12,28),(5,24)])
        p.arc((7,9,25,25),50,275,fill=light,width=3)
        p.ellipse((15,12,23,20),fill='#d4c09b' if shape=='meat' else '#66854a')
        if shape=='morsel':p.ellipse((10,8,14,12),fill='#b6de77');p.ellipse((9,19,12,22),fill='#b6de77')
    elif shape=='flower':
        p.line((15,28,15,13),fill='#588956',width=3);poly([(15,22),(6,17),(9,25),(15,26)],'#77b583')
        for pts in [(15,3,19,10,15,15,11,10),(5,8,12,7,15,14,8,17),(20,7,28,8,24,17,16,14),(8,18,13,13,18,16,16,23),(19,13,25,18,20,23,15,17)]:poly([pts[i:i+2] for i in range(0,len(pts),2)])
        p.rectangle((13,11,18,16),fill=GOLD)
    elif shape in ('saddle','harness'):
        poly([(4,9),(11,5),(22,5),(28,10),(27,18),(23,21),(22,28),(17,28),(18,21),(11,21),(12,28),(6,28),(6,19)])
        poly([(6,9),(12,7),(21,7),(26,10),(23,17),(9,17)],color)
        p.line((7,11,11,14,22,14,26,11),fill=light,width=2)
        p.rectangle((12,15,20,20),fill=OUTLINE);p.rectangle((13,16,19,19),outline=GOLD,width=2)
        p.rectangle((7,23,10,26),outline=GOLD);p.rectangle((18,23,21,26),outline=GOLD)
        if shape=='harness':p.line((6,7,25,26),fill=dark,width=3);p.line((25,7,7,26),fill=GOLD,width=2)
    else:
        poly([(15,3),(21,7),(27,14),(25,22),(16,29),(6,22),(4,14),(10,7)],GOLD)
        poly([(16,8),(23,15),(16,24),(8,16)],color)
        p.arc((10,9,23,23),85,270,fill=light,width=3);p.ellipse((16,12,20,18),fill=dark)
    return im

for name,(label,color,shape) in ITEMS.items():
    folder=A/'textures/item';folder.mkdir(parents=True,exist_ok=True)
    sprite(color,shape,name).save(folder/f'{name}.png')
    save(A/f'items/{name}.json',{'model':{'type':'minecraft:model','model':f'{NS}:item/{name}'}})
    save(A/f'models/item/{name}.json',{'parent':'minecraft:item/handheld' if shape in ('sword','axe','spear','staff') else 'minecraft:item/generated','textures':{'layer0':f'{NS}:item/{name}'}})
save(ROOT/'tools/lang_items.json',{f'item.{NS}.{name}':spec[0] for name,spec in ITEMS.items()})

def ingredient(item): return item if ':' in item else f'{NS}:{item}'
def recipe(name, ingredients, output=None, count=1, pattern=None):
    result={'id':ingredient(output or name),'count':count}
    if pattern:
        data={'type':'minecraft:crafting_shaped','category':'equipment','pattern':pattern,'key':{key:ingredient(value) for key,value in ingredients.items()},'result':result}
        trigger=next(iter(ingredients.values()))
    else:
        data={'type':'minecraft:crafting_shapeless','category':'misc','ingredients':[ingredient(i) for i in ingredients],'result':result};trigger=ingredients[0]
    save(D/f'recipe/{name}.json',data)
    save(D/f'advancement/recipes/{name}.json',{'parent':'minecraft:recipes/root','criteria':{'has_ingredient':{'trigger':'minecraft:inventory_changed','conditions':{'items':[{'items':ingredient(trigger)}]}},'has_the_recipe':{'trigger':'minecraft:recipe_unlocked','conditions':{'recipe':f'{NS}:{name}'}}},'requirements':[['has_ingredient','has_the_recipe']],'rewards':{'recipes':[f'{NS}:{name}']}})

recipe('sunseed_biscuit',['minecraft:wheat','minecraft:wheat','minecraft:golden_carrot','minecraft:sunflower'],count=4)
recipe('hearty_meat',['minecraft:cooked_beef','minecraft:sweet_berries','minecraft:cooked_chicken'],count=3)
recipe('moonblossom',['minecraft:glow_berries','minecraft:sweet_berries','minecraft:lily_of_the_valley'],count=3)
recipe('venomous_morsel',['minecraft:rotten_flesh','minecraft:spider_eye','minecraft:fermented_spider_eye'],count=3)
recipe('griffin_saddle',{'F':'griffin_feather','L':'minecraft:leather','I':'minecraft:iron_ingot'},pattern=['FLF','LLL','I I'])
recipe('wyvern_harness',{'S':'wyvern_scale','L':'minecraft:leather','P':'slime_pearl','I':'minecraft:iron_ingot'},pattern=['SLS','LPL','I I'])
recipe('crystal_fang_sword',{'C':'crystal_shard','F':'dire_fang','I':'minecraft:iron_ingot'},pattern=[' C ',' F ',' I '])
recipe('orc_war_axe',{'S':'orc_steel','E':'infernal_ember','I':'minecraft:stick'},pattern=['SS ','SE ',' I '])
recipe('basilisk_spear',{'H':'minotaur_horn','S':'basilisk_scale','I':'minecraft:stick'},pattern=[' SH',' IS','I  '])
recipe('frostbound_staff',{'F':'frost_essence','C':'crystal_shard','W':'living_wood'},pattern=[' FC',' WF','W  '])
recipe('twilight_relic',{'S':'shadow_essence','F':'forest_essence','T':'troll_heartstone','G':'minecraft:gold_ingot'},pattern=['GSG','FTF','GSG'])
recipe('salvaged_iron',['goblin_scrap']*9,output='minecraft:iron_ingot')
recipe('living_wood_planks',['living_wood'],output='minecraft:oak_planks',count=8)
recipe('forest_bonemeal',['forest_essence','minecraft:bone_meal'],output='minecraft:bone_meal',count=8)
for name,preset in [('crystal_fang_sword','sword'),('orc_war_axe','axe'),('basilisk_spear','spear'),('frostbound_staff','staff')]:
    save(D/f'weapon_attributes/{name}.json',{'parent':f'bettercombat:{preset}'})
save(D/'tags/item/orc_steel_repair.json',{'replace':False,'values':[f'{NS}:orc_steel']})
# Vanilla enchantment and combat classification, available with or without Better Combat.
for tag,values in {'swords':['crystal_fang_sword','basilisk_spear'], 'axes':['orc_war_axe'], 'enchantable/durability':['crystal_fang_sword','basilisk_spear','orc_war_axe','frostbound_staff'], 'enchantable/weapon':['crystal_fang_sword','basilisk_spear','orc_war_axe','frostbound_staff'], 'enchantable/sword':['crystal_fang_sword','basilisk_spear'], 'enchantable/sharp_weapon':['crystal_fang_sword','basilisk_spear','orc_war_axe']}.items():
    save(RES/f'data/minecraft/tags/item/{tag}.json',{'replace':False,'values':[f'{NS}:{v}' for v in values]})
print(f'Generated {len(ITEMS)} textured items, 14 recipes and unlock advancements, and 4 Better Combat presets.')
