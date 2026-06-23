#!/bin/bash

while true; do
    # Get the status and title using playerctl
    STATUS=$(playerctl status 2>/dev/null)
    TITLE=$(playerctl metadata title 2>/dev/null)

    if [ "$STATUS" = "Playing" ]; then
        echo "▶ $TITLE"
    elif [ "$STATUS" = "Paused" ]; then
        echo "⏸ $TITLE"
    else
        echo "? Nothing is playing."
    fi
    sleep 1
done