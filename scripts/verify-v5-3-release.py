#!/usr/bin/env python3
"""Audit the final release against the preserved production binary and staged scope."""
from pathlib import Path
import json,hashlib
from zipfile import ZipFile
r=Path(__file__).resolve().parents[1];d=r/'docs/monster-girl-v5-3';s=json.loads((d/'state.json').read_text())
assert s['active'] is None and list(s['completed'])==s['order']
allowed=set(json.loads((d/'protected-baseline.json').read_text()))
allowed.update(path for paths in s['paths'].values() for path in paths)
for folder in ('src/main','src/client'):
 for path in (r/folder).rglob('*'):
  if path.is_file():assert str(path.relative_to(r)) in allowed,'Unexpected new production file: '+str(path)
old=r/'releases/1.3.0-rc.1/mythic-realms-creatures-1.3.0-rc.1.jar';new=r/'build/libs/mythic-realms-creatures-1.4.0-rc.1.jar'
with ZipFile(old) as a,ZipFile(new) as b:
 classes={n for n in a.namelist() if n.endswith('.class')};assert classes=={n for n in b.namelist() if n.endswith('.class')}
 assert len(classes)==76
 for name in classes:assert a.read(name)==b.read(name),name
 protected=json.loads((d/'protected-baseline.json').read_text());resources=0
 for path in protected:
  prefix='src/main/resources/'
  if path.startswith(prefix) and path!=prefix+'fabric.mod.json':
   name=path.removeprefix(prefix);assert a.read(name)==b.read(name)==(r/path).read_bytes(),name;resources+=1
 for paths in s['paths'].values():
  for path in paths:
   if path.startswith('src/main/resources/'):
    assert b.read(path.removeprefix('src/main/resources/'))==(r/path).read_bytes(),path
 report={'completed_species':13,'unchanged_production_classes':len(classes),'no_added_production_files':True,'unchanged_packaged_resources':resources,'all_thirteen_packaged_assets_match_live':True,'jar_sha256':hashlib.sha256(new.read_bytes()).hexdigest()}
(d/'test-results/final-preservation.json').write_text(json.dumps(report,indent=2)+'\n');print(report)
