#!/usr/bin/env python3
"""Create labeled evidence sheets from actual client screenshots, one species."""
import argparse,math
from pathlib import Path
from PIL import Image,ImageDraw,ImageOps
p=argparse.ArgumentParser();p.add_argument('species');p.add_argument('evidence',type=Path);p.add_argument('--before',type=Path);a=p.parse_args()
repo=Path(__file__).resolve().parents[1];out=repo/'docs/monster-visual-overhaul-v3/previews';out.mkdir(exist_ok=True)
files=sorted((a.evidence/'screenshots').glob('*_creature-'+a.species+'-*.png'));assert files,'No actual species screenshots'
sheet=Image.new('RGB',(1260,268*math.ceil(len(files)/3)),(25,27,33));draw=ImageDraw.Draw(sheet)
for n,path in enumerate(files):
 im=ImageOps.contain(Image.open(path).convert('RGB'),(420,236));x=n%3*420;y=n//3*268;sheet.paste(im,(x+(420-im.width)//2,y));draw.text((x+8,y+240),path.stem.split('creature-'+a.species+'-')[1],fill='white')
sheet.save(out/(a.species+'-states.jpg'),quality=90)
if a.before:
 compare=Image.new('RGB',(1280,780),(25,27,33));d=ImageDraw.Draw(compare)
 for col,(folder,label) in enumerate([(a.before,'Previous grounded visual pass'),(a.evidence,'Final candidate visual pass')]):
  for row,view in enumerate(['three-quarter','side']):
   path=next((folder/'screenshots').glob('*_creature-'+a.species+'-'+view+'.png'))
   im=ImageOps.contain(Image.open(path).convert('RGB'),(640,360));compare.paste(im,(col*640,row*390));d.text((col*640+10,row*390+365),label+' / '+view,fill='white')
 compare.save(out/(a.species+'-comparison.jpg'),quality=92)
print('Saved real render evidence for',a.species)
