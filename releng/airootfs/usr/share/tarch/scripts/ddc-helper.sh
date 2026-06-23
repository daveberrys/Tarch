#!/bin/bash
# ----------------------------------------------------------------------
# ddc-helper.sh: Debouncing wrapper for ddcutil.
# $1: Brightness value (0-100)
# ----------------------------------------------------------------------

DDCUTIL_BIN="/usr/bin/ddcutil"

# 1. Kill any previous ddcutil commands launched by this script.
# 'pkill -f' matches the full command line, cancelling any old processes.
# This is the core of the debounce logic.
/usr/bin/pkill -f "ddcutil setvcp 10"

# 2. Launch the new ddcutil command in the background.
# We add a tiny sleep to ensure pkill has time to finish, though usually unnecessary.
( sleep 0.05 && "$DDCUTIL_BIN" setvcp 10 "$1" ) & disown
