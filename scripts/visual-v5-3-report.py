#!/usr/bin/env python3
"""One species' actual client evidence, never synthetic renders."""
from pathlib import Path
import argparse,math
from PIL import Image,ImageOps,ImageDraw
p=argparse.ArgumentParser();p.add_argument('species');p.add_argument('evidence',type=Path);p.add_argument('--before',type=Path,required=True);a=p.parse_args()
out=Path(__file__).resolve().parents[1]/'docs/monster-girl-v5-3/previews';out.mkdir(exist_ok=True)
files=sorted((a.evidence/'screenshots').glob('*_creature-'+a.species+'-*.png'));assert files
sheet=Image.new('RGB',(1260,268*math.ceil(len(files)/3)),(25,27,33));d=ImageDraw.Draw(sheet)
for i,path in enumerate(files):
 im=ImageOps.contain(Image.open(path).convert('RGB'),(420,236));x=i%3*420;y=i//3*268;sheet.paste(im,(x,y));d.text((x+8,y+241),path.stem.split('creature-'+a.species+'-')[1],fill='white')
sheet.save(out/(a.species+'-states.jpg'),quality=90)
compare=Image.new('RGB',(1280,780),(25,27,33));d=ImageDraw.Draw(compare)
for col,(folder,label) in enumerate(((a.before,'1.3.0 baseline'),(a.evidence,'V5.3 reviewed candidate'))):
 for row,view in enumerate(('three-quarter','side')):
  path=next((folder/'screenshots').glob('*_creature-'+a.species+'-'+view+'.png'));im=ImageOps.contain(Image.open(path).convert('RGB'),(640,360));compare.paste(im,(col*640,row*390));d.text((col*640+8,row*390+365),label+' / '+view,fill='white')
compare.save(out/(a.species+'-comparison.jpg'),quality=92)
