# Mythic Realms: Creatures

**Status: early development foundation, not a playable creature mod.**
Target: Minecraft **1.21.10 exactly**, Fabric, Java 21, official Mojang mappings.

## Current implementation

- Official Fabric 1.21.10 Gradle project foundation and checksum-pinned Gradle wrapper.
- Common mod entrypoint without client-only dependencies.
- Server-tick combat timeline: windup, one impact, recovery, interruption and retry protection.
- Eleven executable combat checks; no external test dependencies.

No creatures, models, animations, items, spawning, structures, mounts, magic or GeckoLib integration are implemented yet. Better Combat compatibility has not been tested. Do not install this as the requested complete mod.

## Development

Use a full JDK 21, not a JRE. Set JAVA_HOME and put its bin directory on PATH.

```sh
./gradlew build
./gradlew combatTest
./scripts/test-combat.sh
./gradlew runClient
./gradlew runServer
```

The build produces normal and source JARs under `build/libs` **only if it succeeds**. Server startup requires reviewing Minecraft's EULA. No server has been started and no EULA accepted by this setup.

In the current cloud instance, verified tools are retained outside the checkout:

```sh
export JAVA_HOME=/workspace/toolchains/jdk-21.0.8+9
export PATH="$JAVA_HOME/bin:$PATH"
export GRADLE_USER_HOME=/workspace/.gradle-cache
./scripts/test-combat.sh
/workspace/toolchains/gradle-9.7.1/bin/gradle --no-daemon build
```

## Dependency provenance and blocker

Project foundation: FabricMC/fabric-example-mod branch `1.21.10`, commit `375edb9b242a5c790c0abbb2248614cf7488f21d`. Loader `0.19.5`, API `0.138.4+1.21.10` and Loom `1.18-SNAPSHOT` are copied from that upstream template; Maven publication resolution remains unverified because Fabric endpoints return HTTP 403 in this instance. The snapshot must be replaced with a verified compatible published release before release packaging.

Gradle 9.7.1 and Temurin JDK 21.0.8+9 were downloaded from their official distribution sources and checked against published SHA-256 checksums. Gradle itself starts. The build fails resolving Fabric Loom before Java compilation. GeckoLib 5 and optional Better Combat versions must be resolved from actual published 1.21.10 Fabric releases before adding coordinates; none are guessed here.

Network additions have been saved as a cloud configuration draft; they do not automatically apply to this running instance. Review/save environment settings and publish the environment, then retry dependency resolution.

## Remaining work

See [original requirements](docs/REQUIREMENTS.md), [implementation plan](docs/IMPLEMENTATION_PLAN.md), and [progress](docs/PROGRESS.md). The original requirements include all 20 creature descriptions. There is no user configuration file yet, and no runtime dependency list is final until GeckoLib resolution succeeds.

License: CC0-1.0 (inherited from the Fabric example template).
