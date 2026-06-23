#!/usr/bin/env bash
set -euo pipefail

# Nix package manager
systemctl enable nix-daemon.service

cat > /etc/nix/nix.conf <<EOF
experimental-features = nix-command flakes
EOF

#  __  __ _____    _    
# |  \/  | ____|  / \   
# | |\/| |  _|   / _ \  
# | |  | | |___ / ___ \ 
# |_|  |_|_____/_/   \_\