#!/usr/bin/env python3
"""Record ONE visually reviewed V3 stage; never edits/generates another species."""
import argparse,hashlib,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('species');p.add_argument('title');p.add_argument('doc');p.add_argument('evidence',type=Path);p.add_argument('--passes',type=int,required=True);p.add_argument('--tests',type=int,required=True);p.add_argument('--animation',required=True);p.add_argument('--notes',type=Path,required=True);a=p.parse_args()
DOC=ROOT/'docs/monster-visual-overhaul-v3';ASSET=ROOT/'src/main/resources/assets/mythic_realms_creatures';subject='Visual overhaul: '+a.title+' reference accuracy'
assert 'BUILD SUCCESSFUL' in (a.evidence/'gradle.log').read_text(),'Need actual final successful client build'
assert list((a.evidence/'screenshots').glob('*_creature-'+a.species+'-three-quarter.png')),'Need actual final species views'
model=json.loads((ASSET/f'geckolib/models/entity/{a.species}.geo.json').read_text())['minecraft:geometry'][0]
subprocess.run(['python3','scripts/visual-v3-report.py',a.species,str(a.evidence),'--before',str(a.evidence.parent/'before')],cwd=ROOT,check=True)
f=DOC/'completed-art.json';records=json.loads(f.read_text());assert a.species not in records,'Stage already frozen'
paths=[ASSET/f'geckolib/{folder}/entity/{a.species}.{suffix}.json' for folder,suffix in [('models','geo'),('animations','animation')]]+[ASSET/f'textures/entity/{a.species}.png',ROOT/f'tools/blockbench/{a.species}.bbmodel']
glow=ASSET/f'textures/entity/{a.species}_glowmask.png'
if glow.exists():paths.append(glow)
records[a.species]={'commit':subject,'files':{str(x.relative_to(ROOT)):hashlib.sha256(x.read_bytes()).hexdigest() for x in paths}};f.write_text(json.dumps(records,indent=2)+'\n')
f=DOC/a.doc;s=f.read_text().replace('Active after','V3 stage complete after '+str(a.passes)+' visual passes. Started after').replace('Actual corrective comparison pending.','Actual corrective comparison completed.');s+='\n\n'+a.notes.read_text().strip()+'\n\n'+f'[Final actual state sheet](previews/{a.species}-states.jpg) · [Released/final comparison](previews/{a.species}-comparison.jpg).\n';f.write_text(s)
f=ROOT/'docs/monster-visual-overhaul-progress.md';lines=f.read_text().splitlines();cubes=sum(len(b.get('cubes',[])) for b in model['bones']);bones=len(model['bones'])
for n,line in enumerate(lines):
 if line.startswith('| ') and ' | '+a.species+' | ' in line:
  cells=[v.strip() for v in line.strip('|').split('|')];cells[3:]=['Complete',f'{cubes} cubes/{bones} bones','Original V3 atlas',a.animation,f'{a.passes} passes inspected',f'Client/build +{a.tests} asset tests pass',subject,'Original hidden-back/lighting and still-frame limits'];lines[n]='| '+' | '.join(cells)+' |'
lines[2]=f'Baseline: `50dfab973a053e6c6761f45771e72c898f3963d4`. Completed in order: **'+', '.join(records)+'**. Last completed: **'+a.title+'**. Continue the next requested creature only after committing this stage.'
for n,line in enumerate(lines):
 if line.startswith('Next step:'):lines[n]='Next step: commit this validated stage, then inspect the next creature in the requested order. No later creature has been edited.'
f.write_text('\n'.join(lines)+'\n')
print('Recorded review and frozen art for',a.species,'— commit separately:',subject)
