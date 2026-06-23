#!/usr/bin/env python3
import curses
import subprocess
import sys
import os
import shlex
import re
# Removed 'import time' since it's no longer needed for a fixed delay

# Set Escape key delay
os.environ.setdefault('ESCDELAY', '25')

# --- CONFIGURATION ---
# ddcutil command is now only used for reading, the helper does the setting.
DDCUTIL_CMD = "sudo /usr/bin/ddcutil"
DDC_HELPER = os.path.expanduser("~/scripts/ddc-helper.sh") # <--- NEW HELPER SCRIPT
PACTL_CMD = "/usr/bin/pactl"
MAX_BRIGHTNESS = 100
MAX_VOLUME = 150 

# --- Helper Functions ---

def run_command(command: str, wait: bool = True) -> tuple[int, str]:
    """Runs a shell command and returns status code and stdout/stderr."""
    try:
        if wait:
            # Synchronous execution (used for reading values)
            result = subprocess.run(
                command, 
                shell=True,
                capture_output=True, 
                text=True, 
                check=False
            )
            return result.returncode, result.stdout.strip()
        else:
            # Asynchronous execution (used for fast setting of values)
            # This is how we call the helper script.
            subprocess.Popen(
                command, 
                shell=True,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL, 
                stderr=subprocess.DEVNULL
            )
            return 0, ""

    except FileNotFoundError:
        return 127, f"Error: Command not found: {command.split()[0]}"
    except Exception as e:
        return 1, f"Execution error: {e}"

# --- Brightness Functions ---

def get_brightness() -> int:
    """Gets the current monitor brightness (0-100). (No change)"""
    code, output = run_command(f"{DDCUTIL_CMD} getvcp 10")
    if code != 0: return -1
    
    try:
        value_line = [line for line in output.split('\n') if 'current value' in line]
        if not value_line: return -1
        return int(value_line[0].split('=')[1].strip().split(',')[0])
    except:
        return -1

def set_brightness(value: int) -> bool:
    """
    Sets the monitor brightness using the helper script.
    The TUI updates instantly, and the shell helper handles cancellation.
    """
    # 1. Cap value
    value = max(0, min(MAX_BRIGHTNESS, value))
    
    # 2. Construct the asynchronous command using sudo to run the helper
    command_async = f"sudo {shlex.quote(DDC_HELPER)} {value}"
    
    # 3. Execute asynchronously (wait=False)
    # The TUI continues to refresh instantly while this command runs in the background.
    code, _ = run_command(command_async, wait=False)
    return code == 0

# --- Volume Functions (No change) ---

def get_volume() -> int:
    """Gets the current master volume percentage using regex for robustness."""
    code, output = run_command(f"{PACTL_CMD} get-sink-volume @DEFAULT_SINK@")
    if code != 0: return -1
    
    try:
        match = re.search(r'(\d+)%', output)
        if match:
            return int(match.group(1))
        else:
            return -1
    except:
        return -1

def set_volume(value: int) -> bool:
    """Sets the master volume percentage. Runs asynchronously."""
    value = max(0, min(MAX_VOLUME, value))
    
    # Run asynchronously to prevent delay
    code, _ = run_command(f"{PACTL_CMD} set-sink-volume @DEFAULT_SINK@ {value}%", wait=False)
    return code == 0

# --- TUI Drawing and Logic (No significant change required) ---

def draw_bar(stdscr, y, x, width, label, value, max_val, bar_color_pair=2, highlight_attr=1):
    """Draws a label and a horizontal progress bar with safe calculations."""
    
    # 1. Cap value for drawing the bar fill (bar fill never exceeds 100%)
    draw_value = min(value, 100)
    
    # 2. Calculate space
    RESERVED_SPACE = len(label) + 10 
    bar_length = max(1, width - RESERVED_SPACE) 
    
    fill_length = int(bar_length * (draw_value / 100)) 
    empty_length = bar_length - fill_length
    
    # 3. Draw entire line background using the highlight attribute
    stdscr.attron(highlight_attr)
    stdscr.addstr(y, x, " " * width) 

    # 4. Draw Label (over the background)
    label_str = f" {label} "
    stdscr.addstr(y, x, label_str) 
    
    # 5. Draw Bar (filled)
    bar_x = x + len(label_str) 
    
    # Draw filled part (using bar color and reverse)
    stdscr.attron(curses.color_pair(bar_color_pair) | curses.A_REVERSE) 
    stdscr.addstr(y, bar_x, " " * fill_length)
    stdscr.attroff(curses.color_pair(bar_color_pair) | curses.A_REVERSE)
    
    # 6. Draw empty part (using the highlight background color)
    stdscr.addstr(y, bar_x + fill_length, " " * empty_length)
    
    # 7. Draw Value (Display actual value, uncapped, but safe for brightness)
    value_to_display = min(value, max_val) 
    value_str = f" {value_to_display}% " 
    value_x = bar_x + bar_length 
    
    if value_x + len(value_str) < x + width:
        stdscr.addstr(y, value_x, value_str)
        
    stdscr.attroff(highlight_attr) 


def draw_controls(stdscr):
    # Setup and colors
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK) # Default
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) # Bar Fill
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK) # Selected Item
    
    # Initial state
    current_selected = 0 
    brightness_val = get_brightness()
    volume_val = get_volume()
    
    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        
        # --- Draw Header ---
        header_text = "System Control Panel"
        stdscr.attron(curses.A_BOLD)
        stdscr.addstr(1, (w - len(header_text)) // 2, header_text)
        stdscr.attroff(curses.A_BOLD)
        stdscr.hline(2, 0, curses.ACS_HLINE, w)

        # --- Define Bar positions ---
        x_start = 2
        y_start = 5
        bar_width = w - x_start * 2 
        
        # --- Draw Brightness Control ---
        y_bright = y_start
        bright_label = "BRIGHTNESS"
        
        if current_selected == 0:
            highlight_attr = curses.color_pair(3) | curses.A_REVERSE
        else:
            highlight_attr = curses.color_pair(1) 

        if brightness_val != -1:
            draw_bar(
                stdscr, y_bright, x_start, bar_width, bright_label, 
                brightness_val, MAX_BRIGHTNESS, 2, highlight_attr 
            )
        else:
             stdscr.addstr(y_bright, x_start, f"{bright_label}: ERROR (ddcutil issue or monitor not supported/off)")
             
        
        # --- Draw Volume Control ---
        y_vol = y_start + 4
        vol_label = "VOLUME"
        
        if current_selected == 1:
            highlight_attr = curses.color_pair(3) | curses.A_REVERSE
        else:
            highlight_attr = curses.color_pair(1)

        if volume_val != -1:
            draw_bar(
                stdscr, y_vol, x_start, bar_width, vol_label, 
                volume_val, MAX_VOLUME, 2, highlight_attr 
            )
        else:
             stdscr.addstr(y_vol, x_start, f"{vol_label}: ERROR (pactl issue or no audio sink)")

        # --- Footer ---
        stdscr.addstr(h - 2, 2, "Use UP/DOWN to switch. LEFT/RIGHT to adjust. ESC to exit.")
        stdscr.refresh()

        # --- Input Handling ---
        key = stdscr.getch()

        if key == curses.KEY_UP or key == curses.KEY_DOWN:
            current_selected = 1 - current_selected 
            
        elif key == curses.KEY_RIGHT or key == curses.KEY_LEFT:
            delta = 5 if key == curses.KEY_RIGHT else -5

            if current_selected == 0:
                # 1. Update internal value and cap it (instant visual update)
                new_val = max(0, min(MAX_BRIGHTNESS, brightness_val + delta))
                if set_brightness(new_val):
                    brightness_val = new_val # Apply internal change immediately
            
            elif current_selected == 1:
                # 1. Update internal value and cap it (instant visual update)
                new_val = max(0, min(MAX_VOLUME, volume_val + delta))
                if set_volume(new_val):
                    volume_val = new_val # Apply internal change immediately

        elif key == 27: # ESC key exit
            sys.exit(0)
            
        # Error handling for initial state
        if brightness_val == -1 and current_selected == 0:
            current_selected = 1 
        if volume_val == -1 and current_selected == 1:
            current_selected = 0


if __name__ == "__main__":
    try:
        # Check for ddcutil requirements early
        code, _ = run_command(f"{DDCUTIL_CMD} getvcp 10")
        if code == 1 and os.getuid() != 0:
            print("ddcutil requires sudo privileges to run. Please ensure you can run 'sudo ddcutil' without a password for this script to work fully.")
        
        curses.wrapper(draw_controls)
        
    except curses.error as e:
        print(f"Curses Error: {e}. Try a different terminal or increase window size.")
        sys.exit(1)