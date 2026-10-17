#!/usr/bin/env bash
set -euo pipefail
mkdir -p /workspace/toolchains /workspace/gradle-distributions
jdk_archive=/workspace/toolchains/temurin21.tar.gz
gradle_archive=/workspace/gradle-distributions/gradle-9.7.1-bin.zip
if [ ! -f "$jdk_archive" ]; then
  curl -fL --retry 2 'https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.8%2B9/OpenJDK21U-jdk_x64_linux_hotspot_21.0.8_9.tar.gz' -o "$jdk_archive"
fi
printf '%s  %s\n' f2dc5418092c43003db8f9005c4a286e1c0104fea96ccdd49e8ebd037cac9219 "$jdk_archive" | sha256sum --check
if [ ! -x /workspace/toolchains/jdk-21.0.8+9/bin/javac ]; then
  tar -xzf "$jdk_archive" -C /workspace/toolchains
fi
if [ ! -f "$gradle_archive" ]; then
  curl -fL --retry 2 https://services.gradle.org/distributions/gradle-9.7.1-bin.zip -o "$gradle_archive"
fi
printf '%s  %s\n' acd53f1edaf02f1a8ff99879f8a34b302661a057d9b063ae9e35b552f804d20a "$gradle_archive" | sha256sum --check
if [ ! -d /workspace/toolchains/gradle-9.7.1 ]; then
  python3 -c 'import zipfile; zipfile.ZipFile("/workspace/gradle-distributions/gradle-9.7.1-bin.zip").extractall("/workspace/toolchains")'
fi
chmod +x /workspace/toolchains/gradle-9.7.1/bin/gradle
export JAVA_HOME=/workspace/toolchains/jdk-21.0.8+9
export PATH="$JAVA_HOME/bin:$PATH"
export GRADLE_USER_HOME=/workspace/.gradle-cache
cd /workspace/mobs-
./scripts/test-combat.sh
# This prepares retained tools. Use scripts/cloud-gradle.py build to build the mod.
