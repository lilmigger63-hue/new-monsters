#!/usr/bin/env python3
"""Rebuild ten distinct C/D creature resource sets. Requires Python 3 and Pillow.

Bedrock geometry, GeckoLib animations and native editable Blockbench projects
share one articulated source. All distances are model pixels (16 = one block).
The generated language fragment is merged by the project owner, never here.
"""
from __future__ import annotations

import base64
import copy
import io
import json
import math
from pathlib import Path
import random
import uuid

from PIL import Image, ImageDraw

REPO = Path(__file__).resolve().parents[1]
RES = REPO / "src/main/resources"
NS = "mythic_realms_creatures"
ASSETS = RES / "assets" / NS

# primary, shade, secondary, trim, glow, ink, ivory, accent, skin, hair,
# leather, rune, crystal, cloth, metal, highlight. Each is a 32px atlas tile.
PALETTES = {
    "cave_basilisk": ["50674a", "2c3b30", "798354", "ad9753", "e6f483", "192723", "c5bea1", "77824d", "9b9c68", "42503a", "544738", "c7f58c", "7a9480", "64694c", "7b8068", "b0b77d"],
    "crystal_spider": ["333a57", "20273c", "6d527d", "a79ac9", "e1a4ff", "131b2c", "e6d7fa", "725a95", "4a4566", "30344e", "4c4666", "d38bf6", "a86adb", "57456a", "8e85ac", "efd4ff"],
    "shadow_wraith": ["343647", "1b2030", "4a4c63", "757890", "7debdc", "0e1723", "aaa6bd", "5c486a", "4c5a6d", "1f2636", "413648", "8dcce5", "738ba7", "454155", "51526c", "c8efeb"],
    "grave_knight": ["596778", "2c3645", "82939f", "b9a069", "84e8d9", "192333", "d4d2b8", "753d53", "777568", "494e5b", "594035", "81c6c0", "628892", "442d42", "9cabb5", "d5dfdc"],
    "flame_imp": ["be5238", "702f2f", "e27b40", "f8b453", "ffe986", "2e202c", "e7c69b", "8b3845", "e99a65", "a34632", "58392e", "ffb949", "ffd86b", "642b36", "b07a53", "ffe1a0"],
    "frost_elemental": ["72b6d1", "345e83", "a4d8e7", "d3f2f3", "e9ffff", "203b5e", "e5faf6", "5379a5", "96d1e4", "426a93", "5d92af", "8cf7ff", "74d5e8", "6489af", "a3c3d1", "f4ffff"],
    "moon_stag": ["62758b", "364657", "a9b9c5", "cab689", "a8e7f4", "182c3d", "e9e5cc", "53657b", "8a9da9", "47586f", "553d45", "c0eaff", "7eabc1", "43596f", "a4b6bf", "e5f1ef"],
    "slime_maiden": ["4db7ac", "267b83", "81d6c1", "c9f0db", "bdffe9", "1b4258", "effdf0", "597fc0", "b8e8df", "398f9c", "377b8e", "9feacb", "7fd8d5", "4facae", "88c8c6", "e2fff3"],
    "harpy": ["967b92", "4c405a", "d3b5b5", "e2d3ba", "e0bc73", "302b42", "f2e4d2", "72566c", "e2b99c", "694b6d", "695042", "dfc487", "99adb5", "55445f", "bfb1b6", "f4ddc4"],
    "demon_sorceress": ["583b67", "2f293f", "9871a1", "d4b175", "f59af1", "201b30", "ebcfb6", "9c405c", "d6acaa", "302e4c", "5d3c44", "e981dd", "bb72d5", "49304f", "9e8b9f", "f8d3ef"],
}
WINDUP = dict(zip(PALETTES, [20, 14, 18, 12, 14, 24, 8, 14, 12, 22]))
SIZE = dict(zip(PALETTES, [(1.2,.85),(1.4,1.1),(.7,2),(.8,2.1),(.5,.8),(1.1,2.4),(1.1,1.8),(.85,1.65),(.9,1.8),(.7,1.95)]))
LOOT = {
    "cave_basilisk": ("spider_eye", 2), "crystal_spider": ("amethyst_shard", 4),
    "shadow_wraith": ("phantom_membrane", 2), "grave_knight": ("iron_nugget", 5),
    "flame_imp": ("blaze_powder", 2), "frost_elemental": ("snowball", 4),
    "moon_stag": ("leather", 2), "slime_maiden": ("slime_ball", 3),
    "harpy": ("feather", 4), "demon_sorceress": ("glowstone_dust", 3),
}
BIOMES = {
    "cave_basilisk": ["minecraft:dripstone_caves", "minecraft:lush_caves"],
    "crystal_spider": ["minecraft:dripstone_caves", "minecraft:lush_caves"],
    "shadow_wraith": ["minecraft:dark_forest", "minecraft:soul_sand_valley"],
    "grave_knight": ["minecraft:dark_forest", "minecraft:old_growth_spruce_taiga"],
    "flame_imp": ["#minecraft:is_nether"],
    "frost_elemental": ["minecraft:snowy_plains", "minecraft:ice_spikes", "minecraft:frozen_peaks"],
    "moon_stag": ["#minecraft:is_forest", "minecraft:cherry_grove"],
    "slime_maiden": ["minecraft:swamp", "minecraft:mangrove_swamp", "minecraft:lush_caves"],
    "harpy": ["#minecraft:is_mountain", "minecraft:windswept_hills"],
    "demon_sorceress": ["minecraft:crimson_forest", "minecraft:nether_wastes"],
}
GLOW_MATERIALS = {
    "cave_basilisk": {4}, "crystal_spider": {4, 11, 12},
    "shadow_wraith": {4, 11}, "grave_knight": {4, 11},
    "flame_imp": {4, 11, 12}, "frost_elemental": {4, 11},
    "moon_stag": {4, 11}, "slime_maiden": {4, 11},
    "harpy": {4}, "demon_sorceress": {4, 11, 12},
}


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n")


def color(hex_value):
    return tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4))


def atlas(name, palette, tame=False):
    """Material tiles have edge shading and controlled species-specific pixels."""
    image = Image.new("RGBA", (128, 128))
    rng = random.Random(name + ("tamed" if tame else "wild"))
    for mat, value in enumerate(palette):
        rgb = color(value)
        ox, oy = mat % 4 * 32, mat // 4 * 32
        for y in range(32):
            for x in range(32):
                # Sparse stepped grain preserves readable block silhouettes.
                shade = rng.choice([-5, -2, 0, 0, 0, 2, 4])
                shade += 5 if y < 4 else (-6 if y > 27 else 0)
                if name == "cave_basilisk" and mat in (0, 1, 2):
                    shade += -11 if y % 5 == 0 and (x + y // 5 * 2) % 6 < 5 else 0
                elif name in ("crystal_spider", "frost_elemental") and mat in (0, 2, 12):
                    shade += 14 if (x + y//2) % 15 < 2 else (-10 if (x-y) % 19 == 0 else 0)
                elif name in ("shadow_wraith", "demon_sorceress") and mat in (0, 1, 13):
                    shade += -8 if x % 7 < 2 else (4 if x % 7 == 3 else 0)
                elif name == "grave_knight" and mat in (0, 1, 2, 14):
                    shade += 8 if y % 8 == 0 else (-9 if y % 8 == 7 else 0)
                elif name in ("moon_stag", "harpy") and mat in (0, 1, 2, 13):
                    shade += 5 if (x//3 + y//4) % 5 == 0 else 0
                elif name == "slime_maiden" and mat in (0, 1, 2, 12, 13):
                    shade += 14 if (x-8)**2 + (y-9)**2 < 9 else 0
                elif name == "flame_imp" and mat in (0, 2, 12):
                    shade += 8 if (x + y*2) % 17 < 2 else 0
                alpha = 255
                if name == "shadow_wraith" and mat in (0, 1, 2, 13):
                    alpha = 190 if mat != 1 else 220
                if name == "slime_maiden" and mat in (0, 1, 2, 12, 13):
                    alpha = 212 if mat in (0, 2, 12) else 232
                image.putpixel((ox+x, oy+y), tuple(max(0, min(255, c+shade)) for c in rgb)+(alpha,))
        draw = ImageDraw.Draw(image)
        # Metal studs, embroidered seams, discrete runes and crystal facets.
        if mat in (3, 10, 14):
            draw.line((ox+2, oy+3, ox+29, oy+3), fill=tuple(min(255,c+22) for c in rgb)+(255,))
            for x, y in ((4,5), (25,5), (4,25), (25,25)):
                draw.rectangle((ox+x,oy+y,ox+x+1,oy+y+1),fill=tuple(min(255,c+28) for c in rgb)+(255,))
        if mat == 11:
            dark = tuple(max(0,c-55) for c in rgb)+(255,)
            draw.rectangle((ox+3,oy+3,ox+28,oy+28), fill=dark)
            for x, y in ((8,8),(20,8),(8,20),(20,20)):
                draw.line([(ox+x,oy+y+5),(ox+x+3,oy+y),(ox+x+6,oy+y+5),(ox+x,oy+y+5)],fill=rgb+(255,),width=1)
                draw.line((ox+x+3,oy+y+2,ox+x+3,oy+y+8),fill=rgb+(255,))
        if mat == 12:
            draw.line((ox+5,oy+25,ox+17,oy+4,ox+25,oy+20), fill=tuple(min(255,c+30) for c in rgb)+(255,),width=2)
    return image


class Model:
    def __init__(self, name):
        self.name = name
        self.bones = [{"name": "root", "pivot": [0,0,0]}]
        self.by_name = {"root": self.bones[0]}

    def bone(self, name, parent, pivot, rotation=None):
        value = {"name": name, "parent": parent, "pivot": pivot, "cubes": []}
        if rotation:
            value["rotation"] = rotation
        self.bones.append(value)
        self.by_name[name] = value
        return name

    def box(self, bone, origin, size, material=0, rotation=None, pivot=None):
        x, y = material % 4 * 32 + 2, material // 4 * 32 + 2
        width, height, depth = [max(1, min(27, round(v * 1.8))) for v in size]
        # Face-specific mapping keeps vertical grain and top panels oriented.
        sizes = {"north": (width,height), "south": (width,height), "west": (depth,height),
                 "east": (depth,height), "up": (width,depth), "down": (width,depth)}
        uv = {face: {"uv": [x,y], "uv_size": list(wh)} for face, wh in sizes.items()}
        cube = {"origin": origin, "size": size, "uv": uv}
        if rotation:
            cube["rotation"] = rotation
            cube["pivot"] = pivot or [origin[i]+size[i]/2 for i in range(3)]
        self.by_name[bone]["cubes"].append(cube)

    def pair_eyes(self, head, x, y, z, size=1):
        for side in (-1,1):
            self.box(head, [side*x-size/2,y,z], [size,size*.65,.35], 4)

    def expressive_eyes(self, *, x, y, z, width=1.5, iris=4):
        """Small dark lashes, visible irises and one-pixel highlights."""
        for side in (-1,1):
            left=side*x-width/2
            self.box("head",[left-.12,y-.08,z],[width+.24,1.35,.22],5)
            self.box("head",[left+.12,y+.12,z-.12],[width-.24,.95,.2],6)
            self.box("head",[side*x-.34,y+.12,z-.25],[.68,1.04,.18],iris)
            self.box("head",[side*x-.23,y+.7,z-.38],[.27,.3,.16],15)
            self.box("head",[left-.16,y+1.2,z-.08],[width+.32,.22,.2],5)

    def humanoid(self, *, height=30, skin=8, torso=0, robe=False):
        """Arms, elbows, hips and knees are independently editable/animated."""
        s = height/30
        self.bone("body", "root", [0,15*s,0])
        self.box("body", [-3*s,14*s,-2*s], [6*s,9*s,4*s], torso)
        self.bone("head", "body", [0,23*s,0])
        self.box("head", [-3.3*s,23*s,-3*s], [6.6*s,6.5*s,6*s], skin)
        self.pair_eyes("head",1.55*s,26*s,-3.25*s,1.15*s)
        self.box("head",[-.7*s,24.5*s,-3.2*s],[1.4*s,.35*s,.3*s],7)
        for side, suffix in ((-1,"right"),(1,"left")):
            arm = self.bone("arm_"+suffix, "body", [side*3.5*s,22*s,0])
            self.box(arm, [(side*3.5-1.25)*s,17*s,-1.25*s], [2.5*s,5*s,2.5*s], skin)
            forearm = self.bone("forearm_"+suffix,arm,[side*3.5*s,17*s,0])
            self.box(forearm,[(side*3.5-1.05)*s,12.5*s,-1.1*s],[2.1*s,4.5*s,2.2*s],skin)
            self.box(forearm,[(side*3.5-1.2)*s,11.5*s,-1.25*s],[2.4*s,1.8*s,2.5*s],skin)
            leg = self.bone("leg_"+suffix,"root",[side*1.7*s,14*s,0])
            self.box(leg,[(side*1.7-1.3)*s,7*s,-1.5*s],[2.6*s,7*s,3*s],torso if robe else skin)
            shin = self.bone("shin_"+suffix,leg,[side*1.7*s,7*s,0])
            self.box(shin,[(side*1.7-1.2)*s,1*s,-1.3*s],[2.4*s,6*s,2.6*s],torso)
            self.box(shin,[(side*1.7-1.4)*s,0,-2.8*s],[2.8*s,2*s,4.2*s],1)
        return s


def make_basilisk(m):
    m.bone("body","root",[0,6,0]); m.box("body",[-5.4,4,-7],[10.8,5,17],0)
    m.box("body",[-4.5,3.7,-6],[9,1.5,15],2)
    m.bone("head","body",[0,8,-7]);m.box("head",[-4.8,6.5,-14],[9.6,4.5,9],0)
    m.box("head",[-3.9,5.8,-19],[7.8,3.2,7],2)
    m.box("head",[-2.9,8.3,-19.2],[5.8,.8,.4],1)
    m.pair_eyes("head",3.3,9.3,-14.3,1.7)
    m.bone("jaw","head",[0,6,-12]);m.box("jaw",[-3.7,4.8,-18.8],[7.4,1.2,7.5],3)
    for side in (-1,1):
        m.box("head",[side*3.7-.6,10.5,-11],[1.2,3.1,2],6,[0,0,-side*25])
        for z in (-17,-13):m.box("head",[side*2.9-.25,5.5,z],[.5,1.2,.7],6)
        for front in (True,False):
            key=("arm_" if front else "leg_")+("left" if side>0 else "right")
            z=-4 if front else 7
            m.bone(key,"body",[side*4.5,6,z])
            m.box(key,[side*5.4-1.6,2,z-1.5],[3.2,4,3],0,[0,0,-side*28])
            foot=m.bone(key+"_foot",key,[side*6.2,2,z])
            m.box(foot,[side*6.6-2.8,0,z-2],[5.6,1.6,4],1)
            for j in (-1,0,1):m.box(foot,[side*6.6+j*1.6-.35,.2,z-3.1],[.7,.7,1.8],6)
    m.bone("tail","body",[0,6,9]);m.box("tail",[-3.3,4.5,9],[6.6,3.8,10],0)
    m.bone("tail_tip","tail",[0,6,18]);m.box("tail_tip",[-2,4.7,18],[4,2.7,9],2)
    m.box("tail_tip",[-.8,5,26],[1.6,1.5,6],1)
    for z in (-4,1,6,11,16,21):
        m.box("body" if z<10 else "tail" if z<19 else "tail_tip",[-.7,8.1 if z<10 else 7,z],[1.4,3.1 if z<10 else 1.8,2.7],3,[12,0,0])


def make_spider(m):
    m.bone("body","root",[0,8,2]);m.box("body",[-4.4,6,-1],[8.8,6,11],0)
    m.box("body",[-3.3,7,8],[6.6,4,4],2)
    m.bone("head","body",[0,8,-2]);m.box("head",[-3.8,5.5,-7],[7.6,5.5,7],1)
    for x,y in [(-2.4,9),(-.8,9.5),(.8,9.5),(2.4,9),(-2,7.5),(2,7.5)]:
        m.box("head",[x-.45,y,-7.25],[.9,.8,.4],4)
    for side in (-1,1):
        fang=m.bone("fang_"+("left" if side>0 else "right"),"head",[side*2,6,-6])
        m.box(fang,[side*2-.6,3.9,-8.5],[1.2,2.6,2.6],3,[25,0,-side*18])
        for index,z in enumerate((-4,-.7,2.6,6)):
            suffix=("left" if side>0 else "right")+str(index+1)
            upper=m.bone("leg_"+suffix,"body",[side*3.6,8,z])
            # Thin angled beams, each with a separate knee and grounded toe.
            angle=side*(31+index*3)
            m.box(upper,[side*6.1-3.1,7.6,z-1],[6.2,1.9,2],0,[0,side*(index-1.5)*8,angle])
            knee=m.bone("knee_"+suffix,upper,[side*8.7,9.6,z+.5])
            m.box(knee,[side*9.9-1,0,z-.4],[2,10.3,1.8],1,[0,0,side*12])
            m.box(knee,[side*10.5-1.2,0,z-1.2],[2.4,1.3,3],3)
            m.box(upper,[side*7-.8,9.6,z-.8],[1.6,3,1.6],12,[0,0,-side*22])
    m.bone("crystal_crown","body",[0,11,4])
    for x,y,z,w,h,d,rot in [(-2,10,2,4,7.6,4,-12),(-4.4,10,5,2.8,5,3,22),(2.3,10.5,6,2.8,4.8,3,-25),(-1.1,11,9,2.2,4.5,2.2,8)]:
        m.box("crystal_crown",[x,y,z],[w,h,d],12,[0,0,rot])
        m.box("crystal_crown",[x+.3,y+h-.8,z+.3],[max(.5,w-.6),.9,max(.5,d-.6)],15)


def make_wraith(m):
    m.bone("body","root",[0,16,0]);m.box("body",[-4,14,-2.5],[8,10,5],0)
    m.box("body",[-4.6,18,-3],[9.2,5,6],1)
    m.box("body",[-.55,13,-2.8],[1.1,11,.5],11)
    # Hood is physically hollow around a black face and luminous eye cubes.
    m.bone("head","body",[0,24,0]);m.box("head",[-3,24,-2.2],[6,6,4.2],5)
    m.box("head",[-4.7,24,-3.3],[1.7,6,6.6],1)
    m.box("head",[3,24,-3.3],[1.7,6,6.6],1)
    m.box("head",[-4.7,30,-3.3],[9.4,2,6.6],0)
    m.box("head",[-4.4,24,2],[8.8,6,1.5],0)
    m.pair_eyes("head",1.6,27.5,-2.55,1.5)
    for side in (-1,1):
        suffix="left" if side>0 else "right"
        arm=m.bone("arm_"+suffix,"body",[side*4,22,0])
        m.box(arm,[side*4.5-1.5,15,-1.8],[3,7,3.6],0,[0,0,side*12])
        fore=m.bone("forearm_"+suffix,arm,[side*5,16,0])
        m.box(fore,[side*5-1.2,10,-1.5],[2.4,6,3],1)
        for finger in range(3):m.box(fore,[side*5-1+finger*.75,7.8,-1.4],[.5,3.2,.7],8,[10,0,side*8])
    for i in range(5):
        x=-4.8+i*2
        ribbon=m.bone("shroud_"+str(i),"body",[x+1,15,0])
        m.box(ribbon,[x,4.5+(i%2)*1.8,-2.2],[2.5,11-(i%2)*1.5,4.4],0 if i%2 else 13,[0,0,(i-2)*5])
        m.box(ribbon,[x+.4,2.5+(i%2)*1.8,-1.5],[1.5,3,3],2)
    m.bone("halo","head",[0,28,0])
    for side in (-1,1):m.box("halo",[side*5.4-.45,24,-.6],[.9,6,1.2],11,[0,0,-side*18])


def make_knight(m):
    s=m.humanoid(height=33.6,skin=1,torso=0)
    m.box("body",[-3.8,17,-2.9],[7.6,9,5.8],0)
    m.box("body",[-3.2,18,-3.2],[6.4,5,.6],14)
    m.box("body",[-.6,17.5,-3.6],[1.2,7,.6],3)
    m.box("body",[-4,15.5,-3],[8,2,6],10)
    m.box("body",[-.9,15.4,-3.4],[1.8,2.2,.8],3)
    m.box("head",[-4,26,-3.8],[8,7.6,7.6],0)
    m.box("head",[-4.3,28,-4],[8.6,3.8,1],14)
    m.box("head",[-3.4,29.1,-4.3],[6.8,1,.45],5)
    m.pair_eyes("head",1.7,29.3,-4.6,1.5)
    m.box("head",[-.45,26.5,-4.7],[.9,6,1],3)
    m.box("head",[-2.5,33,-.5],[5,1.2,2.2],7)
    for side,suffix in ((-1,"right"),(1,"left")):
        m.box("arm_"+suffix,[side*5-2,22,-2.6],[4,4,5.2],0,[0,0,-side*14])
        m.box("arm_"+suffix,[side*5-2.2,24,-2.8],[4.4,1,5.6],14)
        m.box("forearm_"+suffix,[side*4-.2-1.5,12,-1.8],[3.1,5,3.6],14)
        m.box("leg_"+suffix,[side*2-1.65,9,-2],[3.3,6.5,4],0)
        m.box("shin_"+suffix,[side*2-1.6,1,-2],[3.2,7,4],14)
        m.box("leg_"+suffix,[side*2-1.6,8,-2.6],[3.2,2.3,1.4],3)
    m.bone("sword","forearm_right",[-4.2,13,-1],[-30,0,-20])
    m.box("sword",[-4.8,8,-1.5],[1.2,7,1.2],10)
    m.box("sword",[-7.3,14,-2.3],[6.2,1.2,2.8],3)
    m.box("sword",[-5.5,15,-1.7],[2.6,14,.8],14)
    m.box("sword",[-4.5,15,-2],[.6,13,.4],11)
    m.box("sword",[-5.1,29,-1.7],[1.8,2,.8],6)
    m.bone("shield","forearm_left",[4,14,-1])
    m.box("shield",[2.5,9,-4.4],[5,8,1.4],0)
    m.box("shield",[3,10,-4.9],[4,6.5,.7],7)
    m.box("shield",[4.4,10,-5.2],[1.1,6,.5],3)
    m.bone("cape","body",[0,25,2.7]);m.box("cape",[-4,6,2.6],[8,18,1],13,[8,0,0])
    for side in (-1,1):m.box("cape",[side*3-1,4,4],[2,3,.8],7)


def make_imp(m):
    m.humanoid(height=11.8,skin=0,torso=1)
    m.box("head",[-1.6,9.4,-1.45],[3.2,3,2.9],0)
    m.pair_eyes("head",.8,10.9,-1.7,.7)
    for side,suffix in ((-1,"right"),(1,"left")):
        m.box("head",[side*1.2-.25,11.5,.1],[.5,1.3,.6],6,[0,0,-side*25])
        m.box("head",[side*1.7-.3,10,-.25],[.6,1.3,1.3],2,[0,0,-side*50])
        wing=m.bone("wing_"+suffix,"body",[side*1.2,8,1])
        m.box(wing,[side*3-2,7.1,1],[4,.65,1.1],1,[0,0,side*20])
        for step in range(3):
            x=side*(3.2+step*1.25)
            m.box(wing,[x-.9,5.5-step*.6,.7],[1.8,2.6+step*.3,.5],7,[0,0,side*15])
            m.box(wing,[x-.17,5.1-step*.6,.3],[.34,4,.4],1,[0,0,side*20])
        m.box("forearm_"+suffix,[side*1.35-.5,4.3,-.7],[1,1,.8],2)
    m.bone("tail","body",[0,5,1]);m.box("tail",[-.4,2.5,1],[.8,.8,4.5],1,[22,0,0])
    m.bone("tail_tip","tail",[0,3,4.6]);m.box("tail_tip",[-.8,3.3,4.4],[1.6,2.4,.7],12,[0,0,45])
    m.bone("flame","forearm_left",[1.6,5,-1]);
    m.box("flame",[.6,4.5,-2],[2,2,2],12,[0,15,12]);m.box("flame",[1,6,-1.7],[1.2,2,1.3],4,[0,0,-12])


def make_frost(m):
    m.bone("body","root",[0,22,0]);m.box("body",[-5,17,-3.5],[10,11,7],0,[0,12,0])
    m.box("body",[-3.8,18,-4.2],[7.6,8,1.5],12,[0,0,8])
    m.box("body",[-1.5,21,-5.1],[3,3,.7],4,[0,0,45])
    m.bone("head","body",[0,28,0]);m.box("head",[-3.8,28,-3],[7.6,7,6],2,[0,-8,0])
    m.box("head",[-3.5,28,-3.4],[7,2,.7],1)
    m.pair_eyes("head",1.8,31,-3.4,1.8)
    for x,h,rot in [(-3.8,4.2,19),(-1,5.4,-9),(2.1,4.6,-24)]:
        m.box("head",[x,33,0],[1.7,h,2],12,[0,0,rot])
    for side,suffix in ((-1,"right"),(1,"left")):
        arm=m.bone("arm_"+suffix,"body",[side*5,26,0])
        m.box(arm,[side*6.5-2,21,-2.5],[4,6,5],0,[0,0,-side*20])
        m.box(arm,[side*7-1.2,25,-1.6],[2.4,6,3.2],2,[0,0,-side*28])
        fore=m.bone("forearm_"+suffix,arm,[side*7.5,20.5,0])
        m.box(fore,[side*8-2,14,-2.6],[4,7,5.2],12,[0,side*15,0])
        for j in (-1,1):m.box(fore,[side*8+j*1.4-.4,11.5,-2],[.8,3.4,2],3,[0,0,j*12])
    m.bone("core_shards","body",[0,15,0])
    for x,y,z,w,h,d,rot in [(-3,9,-2,6,8,5,13),(-1.3,4,-1.2,2.6,6,2.4,-9),(-5.3,11,2,2.5,6,3,25),(3.2,10,1,2.5,6,3,-26)]:
        m.box("core_shards",[x,y,z],[w,h,d],0 if y>8 else 12,[0,8,rot])
    for i in range(5):
        angle=i*math.tau/5
        x,z=math.cos(angle)*7,math.sin(angle)*5
        key=m.bone("orbit_"+str(i),"root",[0,15,0])
        m.box(key,[x-1,8+(i%3)*3,z-1],[2,4,2],2,[15,i*23,22])


def make_stag(m):
    m.bone("body","root",[0,13,0]);m.box("body",[-4.1,11,-7],[8.2,8,15],0)
    m.box("body",[-3.8,10,-6],[7.6,3,13],2)
    m.bone("neck","body",[0,17,-6]);m.box("neck",[-2.5,16,-9],[5,7.5,5],0,[-20,0,0])
    m.box("neck",[-2.1,16,-10.4],[4.2,6.4,1.1],2,[-20,0,0])
    m.bone("head","neck",[0,22,-9]);m.box("head",[-2.7,21,-13],[5.4,4.5,6],0)
    m.box("head",[-1.9,20.7,-16.3],[3.8,2.8,4.5],2)
    m.box("head",[-1.6,21.5,-16.6],[3.2,1.1,.5],5)
    for side in (-1,1):
        m.box("head",[side*3.8-1.7,23,-10.8],[3.4,1.2,2.2],0,[0,0,-side*22])
        m.box("head",[side*3.8-1.1,23.3,-11],[2.2,.6,1.1],2,[0,0,-side*22])
        m.box("head",[side*2.7-.25,23,-12],[.5,1.1,1.3],4)
        antler=m.bone("antler_"+("left" if side>0 else "right"),"head",[side*1.8,25,-9])
        m.box(antler,[side*2-.45,24.5,-9.5],[.9,4,.9],6,[0,0,-side*18])
        m.box(antler,[side*3.4-2,27,-9.1],[4,.8,.8],6,[0,0,side*12])
        for step in range(3):
            x=side*(2.5+step*1.5)
            m.box(antler,[x-.3,26.8,-9.1],[.6,2-step*.3,.65],6,[0,0,-side*(10+step*7)])
        for front in (True,False):
            key=("arm_" if front else "leg_")+("left" if side>0 else "right")
            z=-4.8 if front else 5.5
            m.bone(key,"root",[side*2.8,13,z])
            m.box(key,[side*2.8-1,6,z-1.1],[2,7.5,2.2],0)
            shin=m.bone(key+"_shin",key,[side*2.8,6.5,z])
            m.box(shin,[side*2.8-.65,1,z-.8],[1.3,5.5,1.6],2)
            m.box(shin,[side*2.8-.9,0,z-1.7],[1.8,1.8,2.7],1)
    m.bone("tail","body",[0,15,7.4]);m.box("tail",[-1.1,13.5,7.5],[2.2,2.6,4.5],2,[-20,0,0])
    m.box("body",[-.5,18,-4],[1,1.3,5],11)
    # Distinct harness remains visible as grey leather when wild and gold when tamed.
    m.box("body",[-4.3,11,-1],[8.6,8,1.4],10)
    m.box("body",[-3.4,19,-.4],[6.8,.6,5.8],10)
    for side in (-1,1):m.box("body",[side*4.15-.35,14,-1.4],[.7,2,2.3],3)


def make_slime(m):
    m.humanoid(height=26.4,skin=8,torso=0,robe=True)
    # Rounded stepped jelly silhouette and fully covered bodice/gelatin skirt.
    m.box("body",[-3.3,12,-2.4],[6.6,7.6,4.8],0)
    m.box("body",[-2.8,17.8,-2.6],[5.6,1.4,.5],3)
    m.box("body",[-.5,13,-2.9],[1,4.4,.5],11)
    m.bone("skirt","body",[0,13,0])
    m.box("skirt",[-4,7,-3.2],[8,6,6.4],0)
    m.box("skirt",[-5,4.2,-4],[10,3.5,8],2)
    m.box("skirt",[-5.7,2.7,-4.5],[11.4,2.2,9],0)
    for i in range(5):m.box("skirt",[-5.6+i*2.2,1.8+(i%2)*.5,-4.2],[2,2,8.4],2)
    for x,y,z in [(-3,6,-4.2),(2,8,-3.4),(-1,4,-4.7),(3.4,3,-4.6)]:
        m.box("skirt",[x,y,z],[.8,.8,.35],3)
    m.bone("hair","head",[0,24,0])
    m.box("hair",[-3.3,24,-3],[6.6,2.4,6],9)
    m.box("hair",[-3.6,20,1.5],[7.2,5.5,1.4],9)
    m.box("hair",[-3.5,21,-2.9],[1.1,4.2,4.5],0)
    m.box("hair",[2.4,21,-2.9],[1.1,4.2,4.5],0)
    m.box("hair",[-3,23.7,-3.1],[2,1.4,.6],9,[0,0,10])
    m.box("hair",[.4,23.7,-3.1],[2.6,1.2,.6],9,[0,0,-12])
    m.box("hair",[2.3,25,-2.3],[1.5,1.1,1.5],4,[0,0,22])
    m.box("head",[-2.2,21.5,-2.9],[.8,.3,.25],7);m.box("head",[1.4,21.5,-2.9],[.8,.3,.25],7)
    m.expressive_eyes(x=1.45,y=22.1,z=-3.2,width=1.55,iris=7)
    m.box("head",[-.5,21.3,-3.2],[1,.25,.3],5)
    for side,suffix in ((-1,"right"),(1,"left")):
        m.box("arm_"+suffix,[side*3.1-1.2,16,-1.4],[2.4,3.5,2.8],2)
        m.box("forearm_"+suffix,[side*3.1-1.2,11,-1.4],[2.4,2.1,2.8],0)
    for i,x,z in [(0,-6,1),(1,5,0),(2,-4,4)]:
        bubble=m.bone("bubble_"+str(i),"root",[x,10+i*3,z])
        m.box(bubble,[x,9+i*3,z],[1.3,1.3,1.3],12,[0,20,20])


def make_harpy(m):
    m.humanoid(height=27.8,skin=8,torso=13)
    m.box("body",[-3,14,-2.25],[6,7,4.5],13)
    # Layered overlapping feather tunic, never exposed torso.
    for row in range(3):
        for column in range(3):m.box("body",[-3+column*2,13+row*2,-2.7],[2,3,.9],2 if (row+column)%2 else 0,[8,0,(column-1)*8])
    m.bone("hair","head",[0,26,0]);m.box("hair",[-3.2,25,-2.8],[6.4,2.8,5.8],9)
    m.box("hair",[-3.2,21.5,1.5],[6.4,5,1.5],9)
    for side in (-1,1):
        m.box("hair",[side*2.6-.6,26,-.5],[1.2,2.8,2],0,[0,0,-side*22])
        m.box("head",[side*3.1-.45,23.5,-.8],[.9,2.2,1.5],8,[0,0,-side*28])
    m.expressive_eyes(x=1.45,y=23.5,z=-3.1,width=1.45,iris=4)
    m.box("head",[-.35,22.8,-3.15],[.7,.4,.65],8)
    for side,suffix in ((-1,"right"),(1,"left")):
        wing=m.bone("wing_"+suffix,"body",[side*3.1,21.5,1])
        m.box(wing,[side*5-2,20,.4],[4,2,2.3],0,[0,0,side*10])
        outer=m.bone("wing_tip_"+suffix,wing,[side*7,21,1])
        for i in range(6):
            x=side*(7+i*1.7)
            m.box(outer,[x-1.1,19.5-i*.4,1],[2.2,1.4,7.5-i*.6],2 if i%2 else 6,[12,0,-side*(6+i*2)])
            m.box(outer,[x-.6,20.5-i*.4,1],[1.2,.6,5.5-i*.4],0)
        # Digitigrade shins and three toe talons.
        m.box("shin_"+suffix,[side*1.6-.8,1.2,-.7],[1.6,5.1,1.4],3,[-10,0,0])
        for toe in (-1,0,1):
            m.box("shin_"+suffix,[side*1.6+toe*.7-.2,.1,-3.3],[.4,.7,3.3],3)
            m.box("shin_"+suffix,[side*1.6+toe*.7-.22,.1,-3.8],[.44,.55,.9],5)
    m.bone("tail","body",[0,14,2]);
    for i in range(5):m.box("tail",[-3.6+i*1.5,9,2],[1.6,1,7-abs(i-2)],0 if i%2 else 2,[25,0,(i-2)*9])


def make_sorceress(m):
    m.humanoid(height=28.5,skin=8,torso=13,robe=True)
    m.box("body",[-3.2,13.5,-2.3],[6.4,8.3,4.6],0)
    m.box("body",[-2.8,14,-2.65],[5.6,6.8,.5],13)
    m.box("body",[-3.5,13.8,-2.8],[7,1.4,5.6],3)
    m.box("body",[-.55,15,-3],[1.1,5.3,.6],11)
    m.bone("skirt","body",[0,14,0]);m.box("skirt",[-3.5,7,-2.7],[7,7,5.4],13)
    m.box("skirt",[-4.4,1,-3.4],[8.8,6.5,6.8],0)
    m.box("skirt",[-4.6,.3,-3.6],[9.2,1.4,7.2],3)
    for side in (-1,1):m.box("skirt",[side*3.2-.45,2,-3.7],[.9,10,.5],7,[0,0,-side*5])
    m.bone("hair","head",[0,26,1]);m.box("hair",[-3.4,26,-3],[6.8,2.8,6.4],9)
    m.box("hair",[-3.5,18,1.4],[7,9,2],9)
    m.box("hair",[-3.4,23,-3.2],[1.35,4,.8],9,[0,0,10])
    m.box("hair",[2.05,23,-3.2],[1.35,4,.8],9,[0,0,-10])
    m.expressive_eyes(x=1.3,y=24.8,z=-3.1,width=1.35,iris=4)
    m.box("head",[-.45,23.8,-3.2],[.9,.25,.3],7)
    for side,suffix in ((-1,"right"),(1,"left")):
        horn=m.bone("horn_"+suffix,"head",[side*2.2,27,0])
        m.box(horn,[side*2.5-.7,27,-.7],[1.4,3.5,1.4],1,[0,0,-side*25])
        m.box(horn,[side*3.5-.45,29.2,-.5],[.9,2,1],3,[0,0,side*15])
        m.box("arm_"+suffix,[side*3.5-1.5,18,-1.8],[3,3.8,3.6],0)
        m.box("forearm_"+suffix,[side*3.3-1.4,12.3,-1.7],[2.8,3.2,3.4],13)
        m.box("forearm_"+suffix,[side*3.3-1.55,12,-1.85],[3.1,.8,3.7],3)
    m.bone("staff","forearm_right",[-4,14,-1]);m.box("staff",[-4.5,.5,-1.4],[.9,26,.9],10)
    m.box("staff",[-5,2,-1.9],[1.9,1.3,1.9],3)
    m.box("staff",[-5.5,24,-2.4],[3,1,3],3)
    m.box("staff",[-5.1,25,-2],[2.2,3.6,2.2],12,[0,0,17])
    for side in (-1,1):m.box("staff",[-4+side*1.8-.4,25,-1.5],[.8,4,.9],3,[0,0,-side*18])
    m.bone("orb","staff",[-4,27,-1]);m.box("orb",[-4.7,26.1,-1.7],[1.4,1.4,1.4],4,[15,30,20])


BUILDERS = dict(zip(PALETTES, [make_basilisk,make_spider,make_wraith,make_knight,make_imp,make_frost,make_stag,make_slime,make_harpy,make_sorceress]))


def keyframes(windup, prepare, impact, final=(0,0,0), start=(0,0,0), recovery=.35):
    return {"0.0": list(start), str(round(windup-.05,3)): list(prepare), str(round(windup,3)): list(impact), str(round(windup+recovery,3)): list(final)}


def make_animations(m):
    name=m.name;bn=set(m.by_name);t=WINDUP[name]/20
    floating=name in ("shadow_wraith","frost_elemental","flame_imp")
    idle={"body":{"position":[0,f"math.sin(query.anim_time * {120 if floating else 150}) * {0.55 if floating else .15}",0]}}
    idle["head"]={"rotation":[0,"math.sin(query.anim_time * 65) * 3",0]}
    if "tail" in bn:idle["tail"]={"rotation":[0,"math.sin(query.anim_time * 130) * 7",0]}
    if "jaw" in bn:idle["jaw"]={"rotation":["math.sin(query.anim_time * 130) * 2 + 2",0,0]}
    if "cape" in bn:idle["cape"]={"rotation":["math.sin(query.anim_time * 100) * 3",0,0]}
    if "hair" in bn:idle["hair"]={"rotation":["math.sin(query.anim_time * 110) * 1.5",0,0]}
    if "skirt" in bn:idle["skirt"]={"scale":["1 + math.sin(query.anim_time * 140) * .015",1,"1 + math.sin(query.anim_time * 140) * .015"]}
    for key in bn:
        if key.startswith("shroud_"):
            i=int(key.rsplit("_",1)[1]);idle[key]={"rotation":[f"math.sin(query.anim_time * 120 + {i*35}) * 5",0,f"math.sin(query.anim_time * 90 + {i*30}) * 4"]}
        if key.startswith("orbit_"):
            i=int(key.rsplit("_",1)[1]);idle[key]={"rotation":[0,f"query.anim_time * 24 + {i*20}",0],"position":[0,f"math.sin(query.anim_time * 140 + {i*60}) * .7",0]}
        if key.startswith("bubble_"):
            i=int(key.rsplit("_",1)[1]);idle[key]={"position":[0,f"math.sin(query.anim_time * 170 + {i*80}) * 1.1",0],"scale":["1 + math.sin(query.anim_time * 150) * .1"]*3}
    def locomotion(rate, amplitude):
        values={"body":{"position":[0,f"math.abs(math.sin(query.anim_time * {rate})) * {0.5 if name=='slime_maiden' else .35}",0]}}
        for key,sign in (("arm_left",-1),("arm_right",1),("leg_left",1),("leg_right",-1)):
            if key in bn:values[key]={"rotation":[f"math.sin(query.anim_time * {rate}) * {sign*amplitude}",0,0]}
        for key in bn:
            if key.startswith("leg_") and key[-1:].isdigit():
                index=int(key[-1]);side=1 if "left" in key else -1
                values[key]={"rotation":[f"math.sin(query.anim_time * {rate} + {index*80+side*50}) * {amplitude*.5}",f"math.sin(query.anim_time * {rate} + {index*80+side*50}) * {amplitude*.6}",0]}
            if key.startswith("knee_"):
                index=int(key[-1]);values[key]={"rotation":[0,0,f"math.sin(query.anim_time * {rate} + {index*80}) * {amplitude*.3}"]}
        if "tail" in bn:values["tail"]={"rotation":[0,f"math.sin(query.anim_time * {rate}) * 12",0]}
        if floating:values["body"]={"rotation":[-8,0,0],"position":[0,f"math.sin(query.anim_time * {rate}) * .65",0]}
        if name=="slime_maiden":values["body"]["scale"]=[f"1 + math.sin(query.anim_time * {rate}) * .035",f"1 - math.sin(query.anim_time * {rate}) * .045",f"1 + math.sin(query.anim_time * {rate}) * .035"]
        return values
    attack={"body":{"rotation":keyframes(t,[-10,0,0],[12,0,0])},"head":{"rotation":keyframes(t,[-15,0,0],[18,0,0])}}
    if name=="cave_basilisk":
        attack["jaw"]={"rotation":keyframes(t,[32,0,0],[5,0,0])}
        attack["head"]["position"]=keyframes(t,[0,.6,1],[0,-.5,-3])
        attack["tail"]={"rotation":keyframes(t,[0,-28,0],[0,22,0])}
    elif name=="crystal_spider":
        attack["body"]["position"]=keyframes(t,[0,1,1],[0,-1,-2.5])
        for side in ("left","right"):
            attack["leg_"+side+"1"]={"rotation":keyframes(t,[-40,0,0],[30,0,0])}
            attack["fang_"+side]={"rotation":keyframes(t,[-25,0,0],[35,0,0])}
    else:
        if "arm_right" in bn:attack["arm_right"]={"rotation":keyframes(t,[-115,-20,-15],[40,25,15])}
        if "forearm_right" in bn:attack["forearm_right"]={"rotation":keyframes(t,[-35,0,0],[10,0,0])}
        if name in ("shadow_wraith","frost_elemental","slime_maiden"):
            attack["arm_left"]={"rotation":keyframes(t,[-80,0,25],[25,0,-15])}
        if name=="harpy":
            attack["leg_left"]={"rotation":keyframes(t,[-20,0,-8],[-85,0,-8])}
            attack["leg_right"]={"rotation":keyframes(t,[-20,0,8],[-85,0,8])}
        if name=="moon_stag":
            attack["head"]={"rotation":keyframes(t,[-15,0,0],[48,0,0])}
            attack["neck"]={"rotation":keyframes(t,[-8,0,0],[20,0,0])}
        if name=="slime_maiden":
            attack["body"]["scale"]=keyframes(t,[1.12,.78,1.12],[.9,1.18,.9],final=(1,1,1),start=(1,1,1))
    heavy=copy.deepcopy(attack)
    for transforms in heavy.values():
        for channel, frames in transforms.items():
            if channel=="rotation":
                for key,v in frames.items():frames[key]=[round(n*1.25,3) for n in v]
    cast={"head":{"rotation":keyframes(t,[-15,0,0],[8,0,0])},"body":{"position":keyframes(t,[0,.8,0],[0,0,0])}}
    for side in ("left","right"):
        if "arm_"+side in bn:
            cast["arm_"+side]={"rotation":keyframes(t,[-105,0,-18 if side=="right" else 18],[-75,0,-8 if side=="right" else 8])}
    if "staff" in bn:cast["staff"]={"rotation":keyframes(t,[-20,0,0],[25,0,0])}
    if "jaw" in bn:cast["jaw"]={"rotation":keyframes(t,[25,0,0],[40,0,0])}
    if "crystal_crown" in bn:cast["crystal_crown"]={"scale":keyframes(t,[1.08,1.08,1.08],[1.15,1.15,1.15],start=(1,1,1),final=(1,1,1))}
    result={
        "idle":{"loop":True,"animation_length":3,"bones":idle},
        "walk":{"loop":True,"animation_length":1,"bones":locomotion(360,24)},
        "run":{"loop":True,"animation_length":.6,"bones":locomotion(600,38)},
        "attack":{"animation_length":round(t+.35,3),"bones":attack},
        "heavy":{"animation_length":round(t+.35,3),"bones":heavy},
        "cast":{"animation_length":round(t+.35,3),"bones":cast},
        "hurt":{"animation_length":.35,"bones":{"body":{"rotation":{"0.0":[0,0,0],".08":[-12,0,7],".35":[0,0,0]},"position":{"0.0":[0,0,0],".08":[0,0,1],".35":[0,0,0]}}}},
        "death":{"animation_length":1.1,"bones":{"root":{"rotation":{"0.0":[0,0,0],".4":[0,0,12],"1.1":[0,0,88]},"position":{"0.0":[0,0,0],"1.1":[0,-2,0]}},"head":{"rotation":{"0.0":[0,0,0],"1.1":[25,0,0]}}}},
    }
    if name in ("shadow_wraith","flame_imp","harpy","frost_elemental"):
        for state,rate,angle in (("fly",620,38),("hover",480,26)):
            values={"body":{"position":[0,"math.sin(query.anim_time * 180) * .7",0],"rotation":[-10 if state=="fly" else 0,0,0]}}
            for side,sign in (("left",1),("right",-1)):
                if "wing_"+side in bn:values["wing_"+side]={"rotation":[0,0,f"math.sin(query.anim_time * {rate}) * {angle*sign} + {10*sign}"]}
                if "wing_tip_"+side in bn:values["wing_tip_"+side]={"rotation":[0,0,f"math.sin(query.anim_time * {rate} - 40) * {sign*18}"]}
                if "leg_"+side in bn:values["leg_"+side]={"rotation":[-35,0,0]}
            if name in ("shadow_wraith","frost_elemental"):
                values.update({key:v for key,v in idle.items() if key.startswith(("shroud_","orbit_"))})
            result[state]={"loop":True,"animation_length":1,"bones":values}
    if name=="moon_stag":
        result["sit"]={"loop":True,"animation_length":1,"bones":{"body":{"position":[0,-6.5,0]},"neck":{"rotation":[-12,0,0]},**{key:{"rotation":[-72 if key.startswith("leg") else 70,0,0]} for key in ("arm_left","arm_right","leg_left","leg_right")}}}
        result["tame"]={"animation_length":1.2,"bones":{"head":{"rotation":{"0.0":[0,0,0],".3":[12,-12,0],".6":[-8,12,0],"1.2":[0,0,0]}},"tail":{"rotation":{"0.0":[0,0,0],".3":[0,20,0],".6":[0,-20,0],"1.2":[0,0,0]}}}}
        result["ride"]={"loop":True,"animation_length":.75,"bones":locomotion(480,32)}
    return result


def uid(name):
    return str(uuid.uuid5(uuid.NAMESPACE_URL, "mythic-realms:"+name))


def blockbench(m, image, animations):
    """Native .bbmodel: embedded atlas, editable groups/cubes and keyframes.

    Uses Blockbench's built-in bedrock format so no editor plugin is required
    to open it; the parallel .geo.json / .animation.json are runtime exports.
    """
    elements=[];groups={};count=0
    for bone in m.bones:
        key=bone["name"]
        groups[key]={"name":key,"uuid":uid(m.name+"/bone/"+key),"origin":bone["pivot"],"rotation":bone.get("rotation",[0,0,0]),"export":True,"isOpen":False,"visibility":True,"autouv":0,"children":[]}
    for bone in m.bones:
        key=bone["name"]
        if "parent" in bone:groups[bone["parent"]]["children"].append(groups[key])
        for cube in bone.get("cubes",[]):
            cube_uid=uid(m.name+"/cube/"+str(count));count+=1
            faces={face:{"uv":[*values["uv"],values["uv"][0]+values["uv_size"][0],values["uv"][1]+values["uv_size"][1]],"texture":0} for face,values in cube["uv"].items()}
            elements.append({"name":key+"_"+str(count),"type":"cube","uuid":cube_uid,"from":cube["origin"],"to":[cube["origin"][i]+cube["size"][i] for i in range(3)],"origin":cube.get("pivot",bone["pivot"]),"rotation":cube.get("rotation",[0,0,0]),"box_uv":False,"autouv":0,"color":count%8,"faces":faces,"visibility":True,"export":True,"rescale":False,"locked":False})
            groups[key]["children"].append(cube_uid)
    native_animations=[]
    for anim_name,animation in animations.items():
        animators={}
        for bone_name,transforms in animation["bones"].items():
            frames=[]
            for channel,values in transforms.items():
                values=values if isinstance(values,dict) else {"0.0":values}
                for time,value in values.items():
                    if len(value)==1:value=value*3
                    frames.append({"channel":channel,"data_points":[dict(zip(("x","y","z"),map(str,value)))],"uuid":uid(m.name+"/anim/"+anim_name+"/"+bone_name+"/"+channel+"/"+time),"time":float(time),"color":-1,"interpolation":"linear"})
            group_uid=groups[bone_name]["uuid"]
            animators[group_uid]={"name":bone_name,"type":"bone","keyframes":frames}
        native_animations.append({"uuid":uid(m.name+"/anim/"+anim_name),"name":anim_name,"loop":"loop" if animation.get("loop") else "once","override":False,"length":animation["animation_length"],"snapping":20,"selected":False,"anim_time_update":"","blend_weight":"","start_delay":"","loop_delay":"","animators":animators})
    buffer=io.BytesIO();image.save(buffer,format="PNG")
    return {"meta":{"format_version":"4.10","model_format":"bedrock","box_uv":False},"name":m.name,"model_identifier":m.name,"visible_box":[6,6,2],"variable_placeholders":"","resolution":{"width":128,"height":128},"elements":elements,"outliner":[groups["root"]],"textures":[{"path":"","name":m.name+".png","folder":"entity","namespace":NS,"id":"0","width":128,"height":128,"uv_width":128,"uv_height":128,"particle":False,"visible":True,"internal":True,"saved":True,"uuid":uid(m.name+"/texture"),"source":"data:image/png;base64,"+base64.b64encode(buffer.getvalue()).decode()}],"animations":native_animations}


def egg(name, palette):
    image=Image.new("RGBA",(16,16));draw=ImageDraw.Draw(image)
    primary,shade,glow=map(color,(palette[0],palette[1],palette[4]))
    draw.polygon([(6,1),(9,1),(11,3),(13,7),(13,11),(11,14),(9,15),(5,15),(2,12),(2,8),(4,4)],fill=primary+(255,),outline=shade+(255,))
    draw.line([(5,4),(4,7),(4,10)],fill=tuple(min(255,c+35) for c in primary)+(255,),width=1)
    for i,(x,y) in enumerate(((7,4),(9,7),(5,10),(8,12))):
        draw.rectangle((x,y,x+(i%2),y+1),fill=glow+(255,))
    draw.line((5,14,9,14),fill=shade+(255,))
    return image


def validate(m, animations, image, native):
    bones=set(m.by_name)
    assert len(bones)==len(m.bones)
    assert image.size==(128,128)
    assert len([cube for bone in m.bones for cube in bone.get("cubes",[])])>=20
    for bone in m.bones:
        assert bone.get("parent","root") in bones
        for cube in bone.get("cubes",[]):
            assert all(size>0 for size in cube["size"])
            for values in cube["uv"].values():
                assert all(0<=values["uv"][i]<values["uv"][i]+values["uv_size"][i]<=128 for i in range(2))
    assert {"idle","walk","run","attack","heavy","cast","hurt","death"}<=animations.keys()
    for animation in animations.values():
        assert animation["animation_length"]>0
        assert set(animation["bones"])<=bones
        for transforms in animation["bones"].values():
            for frames in transforms.values():
                if isinstance(frames,dict):assert all(0<=float(time)<=animation["animation_length"] for time in frames)
    assert len(native["elements"])==sum(len(b.get("cubes",[])) for b in m.bones)
    assert len(native["animations"])==len(animations)
    # Confirm that the atlas embedded in the editable project really decodes.
    embedded=Image.open(io.BytesIO(base64.b64decode(native["textures"][0]["source"].split(",",1)[1])))
    assert embedded.size==image.size


def main():
    language={}
    for name,palette in PALETTES.items():
        m=Model(name);BUILDERS[name](m)
        animations=make_animations(m)
        image=atlas(name,palette)
        native=blockbench(m,image,animations)
        validate(m,animations,image,native)
        texture_dir=ASSETS/"textures/entity";texture_dir.mkdir(parents=True,exist_ok=True)
        image.save(texture_dir/(name+".png"))
        mask=Image.new("RGBA",image.size)
        for material in GLOW_MATERIALS[name]:
            x,y=material%4*32,material//4*32
            mask.paste(image.crop((x,y,x+32,y+32)),(x,y))
        mask.save(texture_dir/(name+"_glowmask.png"))
        if name=="moon_stag":
            tame=list(palette);tame[10]="9e704b";tame[3]="e9c967"
            atlas(name,tame,tame=True).save(texture_dir/(name+"_tamed.png"))
            mask.save(texture_dir/(name+"_tamed_glowmask.png"))
        width,height=SIZE[name]
        save(ASSETS/f"geckolib/models/entity/{name}.geo.json",{"format_version":"1.12.0","minecraft:geometry":[{"description":{"identifier":"geometry."+name,"texture_width":128,"texture_height":128,"visible_bounds_width":max(4,width*3),"visible_bounds_height":max(4,height*2),"visible_bounds_offset":[0,height/2,0]},"bones":m.bones}]})
        save(ASSETS/f"geckolib/animations/entity/{name}.animation.json",{"format_version":"1.8.0","animations":animations})
        save(REPO/f"tools/blockbench/{name}.bbmodel",native)
        item_dir=ASSETS/"textures/item";item_dir.mkdir(parents=True,exist_ok=True)
        egg(name,palette).save(item_dir/(name+"_spawn_egg.png"))
        save(ASSETS/f"items/{name}_spawn_egg.json",{"model":{"type":"minecraft:model","model":f"{NS}:item/{name}_spawn_egg"}})
        save(ASSETS/f"models/item/{name}_spawn_egg.json",{"parent":"minecraft:item/generated","textures":{"layer0":f"{NS}:item/{name}_spawn_egg"}})
        drop,count=LOOT[name]
        save(RES/f"data/{NS}/loot_table/entities/{name}.json",{"type":"minecraft:entity","pools":[{"rolls":1,"entries":[{"type":"minecraft:item","name":"minecraft:"+drop,"functions":[{"function":"minecraft:set_count","count":{"type":"minecraft:uniform","min":1,"max":count}}]}]}]})
        save(RES/f"data/{NS}/tags/worldgen/biome/spawns/{name}.json",{"replace":False,"values":[{"id":value,"required":False} for value in BIOMES[name]]})
        title=name.replace("_"," ").title()
        language[f"entity.{NS}.{name}"]=title
        language[f"item.{NS}.{name}_spawn_egg"]=title+" Spawn Egg"
        print(f"{name}: {len(m.bones)} bones, {len(native['elements'])} cubes, {len(animations)} animations; UV/PNG/BBModel validated")
    save(REPO/"tools/lang_creatures_cd.json",language)


if __name__=="__main__":
    main()
