#!/usr/bin/env bash
set -euo pipefail

systemctl enable nix-daemon.service
systemctl enable NetworkManager
systemctl enable bluetooth

cat > /etc/nix/nix.conf <<EOF
experimental-features = nix-command flakes
EOF

echo 'export NIXPKGS_ALLOW_UNFREE=1
alias nixpi="nix profile install --impure"
alias nixpr="nix profile remove"
alias nixps="nix search"
alias nixpu="nix profile upgrade"' >> /root/.zshrc