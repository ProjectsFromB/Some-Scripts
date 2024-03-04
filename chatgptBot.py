import os
import pyautogui
import clipboard
import time
import pyperclip

#set the x & y coords of the chat input field
pyautogui.moveTo(569, 689)
pyautogui.click()

def open_file(file_path):
    # Open the file
    with open(file_path, "r") as f:
        # Read the entire file into a string
        file_text = f.read()
        return (file_text)

file_path = "test"
text = open_file(file_path)

clipboard.copy(text)
time.sleep(2)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press("enter")
    
    
    
    
    
