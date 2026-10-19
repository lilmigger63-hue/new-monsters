#!/usr/bin/env python3
"""Freeze one actually reviewed species; advance only after its separate commit."""
import argparse,hashlib,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];DOC=ROOT/'docs/monster-girl-v5-3'
p=argparse.ArgumentParser();p.add_argument('species');p.add_argument('evidence',type=Path);p.add_argument('--passes',type=int,required=True);p.add_argument('--notes',type=Path,required=True);a=p.parse_args()
state=json.loads((DOC/'state.json').read_text());assert state['active']==a.species and a.species not in state['completed']
log=(a.evidence/'gradle.log').read_text();assert 'BUILD SUCCESSFUL' in log and 'CLIENT_SMOKE_PASS 33 resource sets and synced entities; 1 species presented' in log
subprocess.run(['python3','scripts/test-v5-3-preservation.py'],cwd=ROOT,check=True)
subprocess.run(['python3','scripts/visual-v5-3-report.py',a.species,str(a.evidence),'--before',str(a.evidence.parent/'before')],cwd=ROOT,check=True)
files=state['paths'][a.species];geo=json.loads((ROOT/files[0]).read_text())['minecraft:geometry'][0]
record={'commit':'V5.3: refine '+a.species,'passes':a.passes,'evidence':str(a.evidence),'files':{path:hashlib.sha256((ROOT/path).read_bytes()).hexdigest() for path in files}}
state['completed'][a.species]=record;state['active']=None;(DOC/'state.json').write_text(json.dumps(state,indent=2)+'\n')
(DOC/(a.species+'.md')).write_text(a.notes.read_text().strip()+'\n\n'+f"Final model: {len(geo['bones'])} bones / {sum(len(b.get('cubes',[])) for b in geo['bones'])} cubes. Actual reviewed baseline plus {a.passes} corrective client runs; each corrective run bakes/syncs all33 resource sets and presents one selected species.\n\n[Actual final states](previews/{a.species}-states.jpg) · [Actual baseline/final comparison](previews/{a.species}-comparison.jpg).\n")
f=ROOT/'docs/monster-girl-v5-3-progress.md';lines=f.read_text().splitlines()
for i,line in enumerate(lines):
 if line.startswith('| '+a.species+' |'):
  cells=[v.strip() for v in line.strip('|').split('|')];cells[2:]=['Complete',str(a.passes)+' corrective runs inspected','Focused client +35 asset/source/preservation checks pass','See per-species report',record['commit'],'Commit this stage; then next creature'];lines[i]='| '+' | '.join(cells)+' |'
f.write_text('\n'.join(lines)+'\n');print('Frozen one reviewed species; commit before advancing:',a.species)
