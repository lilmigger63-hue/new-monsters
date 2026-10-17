#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
java_bin="${JAVA_HOME:+$JAVA_HOME/bin/}java"
javac_bin="${JAVA_HOME:+$JAVA_HOME/bin/}javac"
output_dir=$(mktemp -d)
trap 'rm -rf "$output_dir"' EXIT
"$javac_bin" --release 21 -d "$output_dir" \
  src/main/java/com/mythicrealms/creatures/entity/combat/AttackTimeline.java \
  src/test/java/com/mythicrealms/creatures/entity/combat/AttackTimelineTest.java
"$java_bin" -cp "$output_dir" com.mythicrealms.creatures.entity.combat.AttackTimelineTest
