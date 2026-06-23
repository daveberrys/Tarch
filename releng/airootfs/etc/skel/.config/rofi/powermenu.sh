#!/usr/bin/env bash

OPTIONS="Shutdown\nReboot\nLogout\nCancel"

# Display the menu using Rofi
# -dmenu: Run Rofi in dmenu mode (script mode)
# -p: Prompt text
# -config: Point to your existing config file for styling
choice=$(echo -e "$OPTIONS" | rofi -dmenu -p "Power: " -config ~/.config/rofi/config.rasi)

case "$choice" in
    Shutdown)
        # Use loginctl or systemctl for power management
        systemctl poweroff
        ;;
    Reboot)
        systemctl reboot
        ;;
    Logout)
        # Use 'labwc-exit' to log out of the Labwc session
        labwc -exit
        ;;
    Cancel)
        exit 0
        ;;
    *)
        # Default action for empty or invalid input
        exit 0
        ;;
esac
