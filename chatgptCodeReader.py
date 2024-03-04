import os
import pyautogui
import clipboard
import time
import pyperclip

# set the x & y coords of the chat input field
pyautogui.moveTo(752, 680)
pyautogui.click()

def open_file(file_path, lines_per_chunk=200):
    # Open the file
    with open(file_path, "r") as f:
        chunk = []
        for line in f:
            chunk.append(line)
            if len(chunk) == lines_per_chunk:
                # paste chunk
                clipboard.copy("".join(chunk))
                time.sleep(2)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press("enter")
                time.sleep(60)
                chunk = []
        # paste any remaining lines
        if chunk:
            # paste chunk
            clipboard.copy("".join(chunk))
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press("enter")
            time.sleep(60)


file_path = "code.js"
open_file(file_path)

