#!/usr/bin/env bash
set -euo pipefail

# Nix package manager
systemctl enable nix-daemon.service
systemctl enable NetworkManager
systemctl enable bluetooth

cat > /etc/nix/nix.conf <<EOF
experimental-features = nix-command flakes
EOF
