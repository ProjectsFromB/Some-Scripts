#!/bin/bash

# Find the terminal window ID
window_id=$(xdotool search --onlyvisible --class zsh | head -1)

# Send key combination to open a new tab
xdotool key --clearmodifiers --window "$window_id" Ctrl+Shift+t

# Wait for the new tab to appear
sleep 0.5

# Find the new tab's window ID
new_tab_id=$(xdotool search --onlyvisible --class zsh | grep -v "$window_id" | head -1)

# Activate the new tab
xdotool windowactivate "$new_tab_id"

# Type the desired command
xdotool type --clearmodifiers --window "$new_tab_id" "sudo pacman -Syu"

# Send key combination to execute the command
xdotool key --clearmodifiers --window "$new_tab_id" Return

# Activate the original tab/window
xdotool windowactivate "$window_id"

