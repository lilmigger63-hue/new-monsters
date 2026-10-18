# Creature overhaul implementation plan

> For agentic workers: execute independent scoped batches with the parallel-agents skill; root integrates, tests and performs final review.

**Goal:** Upgrade all20 existing creatures with original reference-informed geometry, material textures, animation and game presentation.
**Architecture:** Keep common/server gameplay. Use one offline model/atlas/native-project pipeline and four disjoint group exporters; preserve existing generator entrypoints. Integrate synchronized state/effects at shared runtime boundaries.
**Tech stack:** Minecraft1.21.10, Fabric, Java21, GeckoLib5.3-alpha-3, Python/Pillow offline, optional Better Combat3.0.0.
**Spec:** [SPEC.md](SPEC.md); design:[DESIGN_GUIDE.md](DESIGN_GUIDE.md).

## Global constraints

- Preserve registered IDs, all gameplay systems, compatibility, original history and main branch.
- Use original art; document inspected genuine references and uncertain attribution/licensing honestly.
- Retain128×128 maps, renderer-supported alpha/emissive behavior and server windups.
- No automatic merge/release/publication for this overhaul.

## Review focus

- Regeneration must preserve upgrades without rewriting survival loot/spawns/recipes.
- Tamed/rare UV maps and glowmasks must match the normal geometry.
- Quadrupeds, two-legged wyverns and eight-legged spiders need distinct anatomically coherent skeletons.
- Action hit frames, movement clips and shared controllers must agree; guard/reaction states must not cancel dangerous windups.
- Rune/impact effects must obey intensity/distance budgets and remain off authoritative gameplay paths.

## Task1: Baseline and inspected research

Files: docs/creature-overhaul/{SPEC,REFERENCE_ATLAS,DESIGN_GUIDE,PROGRESS,VALIDATION}.md, references.json.
- [x] Create isolated feature branch and inspect all supplied moodboard panels.
- [x] Run `python3 scripts/cloud-gradle.py build runGametest`: baseline passes,34tests.
- [x] Record at least3 inspected real references per species, exact URLs/credits/restrictions and original translation notes.

## Task2: Export pipeline and meaningful asset checks

Files: tools/overhaul_asset_pipeline.py; scripts/test-overhaul-assets.py; tests for offline exporter.
Interfaces: `Model(name).bone(name,parent,pivot,rotation=None)`, `.box(bone,origin,size,material=0,rotation=None,pivot=None)`, `.by_name`, `.bones`; `clip(length,bones,loop=False)`; `keys(t,prepare,impact,final=(0,0,0),start=(0,0,0),recovery=.3)`; `write_creature(model,palette,materials,animations,width,height,glow=(),variants=None,translucent=False)`.
- [x] Add asset validity/export tests and observe missing native-art prerequisites.
- [x] Provide deterministic material-specific atlases and reusable native Blockbench export.
- [x] Validate per-face UVs, parent acyclicity, positive cube dimensions, clip bone references and source PNG/animation parity.

## Tasks3–6: GroupsA,B,C,D

Files: tools/generate_overhaul_group_{a,b,c,d}.py; only that group's entity geometry/animations/PNG variants/glowmasks and tools/blockbench/<id>.bbmodel.
Interfaces: use Task2 exports and actual CreatureKind windup/height/width. Group generators expose `main()` and do not change gameplay data.
- [x] Audit assigned group, inspect assigned atlas references, build original distinctive geometry.
- [x] Paint material maps and all alternate skins/masks; author species-specific animation and secondary motion.
- [x] Validate exports, actual rendered shots and gameplay before committing each batch.

## Task7: Runtime presentation and fair combat

Files: shared MythicCreature/MythicHostileEntity controllers, SpellEffects and bounded client presentation; focused server tests.
- [x] Reproduce any chosen AI/state issue in a focused test before changing behavior.
- [x] Wire supported action/state clips and bounded species-specific cast/impact effects without client damage or new movement authority.
- [x] Preserve taming/riding/spawn/loot/config and optional Better Combat.

## Task8: Integration and delivery

Files: original generator entrypoints, scripts/client-smoke.gradle and client harness if needed; progress/validation docs; compiled artifacts outside tracked releases until publication is authorized.
- [x] Test regeneration/UV/native source parity and preserve gameplay-data hashes.
- [x] Run clean build, server checks and actual client visuals/riding with/without Better Combat.
- [x] Review full branch and fix important regressions, record honest limits, produce downloadable candidate JAR/source.
