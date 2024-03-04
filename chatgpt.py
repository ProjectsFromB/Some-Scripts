import os
import pyautogui
import clipboard
import time
import pyperclip

pyautogui.moveTo(569, 689)
pyautogui.click()

def split_file(file_path, chunk_size=100):
    # Open the file
    with open(file_path, "r") as f:
        # Read the entire file into a string
        file_text = f.read()
    # Split the file text into chunks of the specified size
    chunks = [file_text[i:i+chunk_size] for i in range(0, len(file_text), chunk_size)]
    return chunks


file_path = "code.js"
chunks = split_file(file_path)
for chunk in chunks:
    clipboard.copy(chunk)
    time.sleep(2)
    #clipboard.paste()
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("enter")
    
    
    
    
    
