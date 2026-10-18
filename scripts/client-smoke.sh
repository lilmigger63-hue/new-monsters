#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
display_root="${CLIENT_DISPLAY_ROOT:-/workspace/toolchains/client-display/root}"
export JAVA_HOME="${JAVA_HOME:-/workspace/toolchains/jdk-21.0.8+9}"
export GRADLE_USER_HOME="${GRADLE_USER_HOME:-/workspace/.gradle-cache}"
export PATH="$JAVA_HOME/bin:$PATH"
export LIBGL_ALWAYS_SOFTWARE=1
export LP_NUM_THREADS="${LP_NUM_THREADS:-4}"
export MESA_SHADER_CACHE_DIR="$PWD/build/client-smoke-shader-cache"
mkdir -p build/client-smoke-evidence "$MESA_SHADER_CACHE_DIR"
# Keep evidence specific to this run, including focused suites.
rm -rf -- build/client-smoke/screenshots
evidence_dir="${CLIENT_SMOKE_EVIDENCE_DIR:-/workspace/validation/client-base}"
for argument in "$@"; do
    if [[ "$argument" == -PwithBetterCombat* ]]; then
        evidence_dir="${CLIENT_SMOKE_EVIDENCE_DIR:-/workspace/validation/client-better-combat}"
    fi
done
if [[ -z "${DISPLAY:-}" ]]; then
    export DISPLAY=:98
    "$display_root/usr/bin/Xvfb" "$DISPLAY" -screen 0 1280x720x24 -nolisten tcp \
        -fp "$display_root/usr/share/fonts/X11/misc" > build/client-smoke-evidence/xvfb.log 2>&1 &
    display_pid=$!
    trap 'kill "$display_pid" 2>/dev/null || true' EXIT
    for attempt in {1..50}; do
        if "$display_root/usr/bin/glxinfo.x86_64-linux-gnu" -B > build/client-smoke-evidence/opengl.txt 2>&1; then break; fi
        sleep 0.1
    done
fi
python3 scripts/cloud-gradle.py --no-configuration-cache runClientSmoke "$@" 2>&1 | tee build/client-smoke-evidence/gradle.log
grep -q 'CLIENT_SMOKE_PASS' build/client-smoke-evidence/gradle.log
mkdir -p "$evidence_dir"
cp -a build/client-smoke/screenshots "$evidence_dir/"
cp -a build/client-smoke-evidence/{gradle.log,opengl.txt,xvfb.log} "$evidence_dir/"
printf 'Graphical smoke test passed. Preserved evidence: %s\n' "$evidence_dir"
