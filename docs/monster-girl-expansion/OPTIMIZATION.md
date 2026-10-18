# Shared-system optimization audit

Scope: all 33 species share the entity renderer; hostile, guardian and mount combat, projectile lifetime/collision, spell presentation, spawning/configuration and animation-controller paths were inspected for recurring work. This is a focused audit of the whole mod architecture, not a claim that every possible bottleneck is eliminated.

## Implemented

- Cache normal/tamed/rare texture ResourceLocations once per renderer model. Previously the override concatenated a path and allocated a ResourceLocation every texture query. The same namespace, paths and tamed-before-rare selection priority are retained. No texture pixels, geometry or resource-pack reload behavior changed.
- Cache held death RawAnimation in the shared guardian/mount controller, matching the existing cached hostile/locomotion approach. The same clip and timing are retained.
- Precompute exact unit-ring coordinates for every supported particle count (1–24). Each ring previously evaluated sine and cosine for each point; emission now does bounded table reads. The cache uses 600 doubles plus array headers, once per process. Radius, particle type, order, count, intensity clamp, viewer range and network packets are unchanged.
- Reuse the immutable stone BlockParticleOption for Minotaur/Troll telegraphs.

Existing safeguards were retained: configurable pursuit update interval, bounded periodic healing/recruitment, limited projectile overlap checks and 100-tick projectile lifetime, nearby-viewer particle guard/count caps, server-only authoritative combat, cached looping animations and vanilla entity synchronization. No new mixins, dependencies, tick handlers or global entity scans were introduced. Models, UVs, animation curves, attack delays, spawning and gameplay were not simplified for performance.

## Measurement

The standalone Java 21 coordinate-kernel benchmark alternates before/after ordering for seven rounds of 500,000 rings after warm-up, varying all 24 counts and seven radii. All 300 unit-circle points are bit-identical to the previous formulas.

Median cost: **384.884 ns → 26.253 ns per ring** (14.66× for this coordinate kernel). [Raw samples](particle-benchmark.json).

This isolates coordinate calculation; it excludes packet sending, pathfinding and GPU work. It is **not an overall Minecraft FPS/TPS gain**, allocation-profiler result or hardware performance certification. Texture/death changes eliminate the identified recurring object construction by inspection; their end-to-end speedup has not been measured.

Reproduce with Java 21 from the repository root:

```sh
mkdir -p /tmp/mythic-ring-bench
javac -d /tmp/mythic-ring-bench src/main/java/com/mythicrealms/creatures/magic/ParticleRing.java scripts/benchmarks/ParticleRingBenchmark.java
java -cp /tmp/mythic-ring-bench com.mythicrealms.creatures.magic.ParticleRingBenchmark
```

A live JFR attachment attempt timed out before obtaining a recording; no whole-client JFR profile or allocation count is claimed.

Final optimized build/server/client outcomes are recorded in the expansion README validation section.
