#!/usr/bin/env bash
# Install a local Xvfb without root; APT verifies the signed Debian index and package hashes.
set -euo pipefail
display_tools="${CLIENT_DISPLAY_TOOLS:-/workspace/toolchains/client-display}"
mkdir -p "$display_tools"/{apt/lists/partial,apt/cache/archives/partial,apt/empty.conf.d,apt/empty.sources.d,debs,root}
cat > "$display_tools/apt/sources.list" <<'EOF'
deb [signed-by=/usr/share/keyrings/debian-archive-keyring.gpg] https://deb.debian.org/debian trixie main
EOF
cat > "$display_tools/apt/apt.conf" <<EOF
Dir::Etc::parts "$display_tools/apt/empty.conf.d";
Dir::Etc::main "-";
Dir::Etc::sourcelist "$display_tools/apt/sources.list";
Dir::Etc::sourceparts "$display_tools/apt/empty.sources.d";
Dir::State::lists "$display_tools/apt/lists";
Dir::Cache "$display_tools/apt/cache";
APT::Get::List-Cleanup "0";
APT::Sandbox::User "$(id -un)";
EOF
export APT_CONFIG="$display_tools/apt/apt.conf"
/usr/bin/apt-get update
cd "$display_tools/debs"
/usr/bin/apt-get download xvfb mesa-utils-bin libgles2 xfonts-base
for package in ./*.deb; do dpkg-deb -x "$package" "$display_tools/root"; done
if ldd "$display_tools/root/usr/bin/Xvfb" | grep -q 'not found'; then
    printf '%s\n' 'Xvfb has missing native dependencies; inspect ldd output.' >&2
    exit 1
fi
