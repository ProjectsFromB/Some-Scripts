import os
from selenium import webdriver
import pickle
#Write me a python script that takes a very long one line javascript file and breaks it down into blurbs of #100 lines then uses selenium to paste each blurb here.
# specify the path to the JavaScript file
file_path = "code.js" #in same dir...

# open the file and read its contents
with open(file_path, "r") as file:
    javascript = file.read()

# split the file into chunks of 100 lines
lines_per_chunk = 100
javascript_chunks = [javascript[i:i+lines_per_chunk] for i in range(0, len(javascript), lines_per_chunk)]

# initialize Selenium webdriver
driver = webdriver.Firefox()

# navigate to the website where the chunks will be pasted
driver.get("https://chat.openai.com/chat")

# paste each chunk into the website
for chunk in javascript_chunks:
    # locate the textarea element
    textarea = driver.find_element_by_id("code_input")
    # clear the textarea
    textarea.clear()
    # paste the chunk into the textarea
    textarea.send_keys(chunk)
    # submit the form
    driver.find_element_by_id("submit_button").click()

# close the browser
driver.quit()

