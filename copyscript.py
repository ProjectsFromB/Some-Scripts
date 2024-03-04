import os
import pyautogui
import clipboard
import time
import pyperclip

pyautogui.moveTo(735, 1453)
pyautogui.click()

# Open the JavaScript file in read mode
with open('code2.html', 'r') as file:
    # Read the contents of the file
    js_contents = file.read()

# Loop through the contents of the file and copy and paste 10,000 characters at a time
for i in range(0, len(js_contents), 5000):
    # Get the next 10,000 characters
    chunk = js_contents[i:i+5000]

    # Print the chunk (or paste it to another application as needed)
    print("chunk copied")
    clipboard.copy(chunk)	
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("enter")
