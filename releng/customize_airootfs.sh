#!/usr/bin/env bash
set -euo pipefail

systemctl enable nix-daemon.service
systemctl enable NetworkManager
systemctl enable bluetooth

mkdir -p /etc/nix
echo 'experimental-features = nix-command flakes' >> /etc/nix/nix.conf

mkdir -p /root/
echo 'export NIXPKGS_ALLOW_UNFREE=1
alias nixpi="nix profile install --impure"
alias nixpr="nix profile remove"
alias nixps="nix search"
alias nixpu="nix profile upgrade"' >> /root/.zshrc