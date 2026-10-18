#!/usr/bin/env python3
"""Compose labeled actual-game captures; never generate creature imagery."""
import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageOps

parser = argparse.ArgumentParser()
parser.add_argument('--before', type=Path, required=True)
parser.add_argument('--after', type=Path, required=True)
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
args.output.mkdir(parents=True, exist_ok=True)
ids = 'goblin_scout goblin_shaman orc_warrior minotaur stone_troll ancient_treant griffin dire_wolf wild_wyvern cave_basilisk forest_dryad shadow_wraith grave_knight frost_elemental moon_stag slime_maiden harpy demon_sorceress'.split()


def capture(folder, creature, state):
    matches = list(folder.glob('*_creature-' + creature + '-' + state + '.png'))
    if len(matches) != 1:
        raise ValueError((folder, creature, state, matches))
    return Image.open(matches[0]).convert('RGB')


def panel(canvas, picture, x, y, label):
    canvas.paste(ImageOps.contain(picture, (640, 360)), (x, y + 24))
    ImageDraw.Draw(canvas).text((x + 8, y + 6), label, fill='white')


preview = Image.new('RGB', (1920, 6 * 384), '#202020')
for index, creature in enumerate(ids):
    comparison = Image.new('RGB', (1920, 768), '#202020')
    for row, folder in enumerate((args.before, args.after)):
        for col, state in enumerate(('idle', 'side', 'back')):
            panel(comparison, capture(folder, creature, state), col * 640, row * 384,
                  creature + ' / ' + ('BEFORE' if row == 0 else 'V2') + ' / ' + state)
    comparison.save(args.output / (creature + '-comparison.jpg'), quality=88)
    states = ['idle', 'side', 'back', 'distant', 'attack', 'probe-walk', 'probe-run',
              'probe-heavy', 'probe-cast', 'probe-hurt', 'probe-death']
    if creature in ('wild_wyvern', 'harpy', 'griffin'):
        states += ['probe-fly', 'probe-fly-phase-1', 'probe-fly-phase-2',
                   'probe-fly-phase-3', 'probe-hover']
    sheet = Image.new('RGB', (2560, ((len(states) + 3) // 4) * 384), '#202020')
    for i, state in enumerate(states):
        panel(sheet, capture(args.after, creature, state), (i % 4) * 640,
              (i // 4) * 384, creature + ' / ' + state)
    sheet.save(args.output / (creature + '-states.jpg'), quality=88)
    panel(preview, capture(args.after, creature, 'idle'), (index % 3) * 640,
          (index // 3) * 384, creature)
preview.save(args.output / 'overview.jpg', quality=88)
print('Composed 18 comparisons, 18 state sheets and overview from actual screenshots')
