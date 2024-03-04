import time
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Tor proxy configuration
tor_proxy = "socks5://127.0.0.1:9050"
profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.socks", "127.0.0.1")
profile.set_preference("network.proxy.socks_port", 9050)
profile.update_preferences()

# Create a new Firefox WebDriver instance with the configured profile
driver = webdriver.Firefox(firefox_profile=profile)

# Initialize page number
page_num = 1

# Initialize empty list to store the extracted data
all_items = []

while len(all_items) < 15400:  # Continue until you have 10,000 items
    wineDB_url = f"https://www.wine.com/list/wine/7155/{page_num}?sortBy=mostInteresting"
    driver.get(wineDB_url)

    names = driver.find_elements(By.XPATH, "//span[@class='listGridItemInfo_name']")
    prices = driver.find_elements(By.XPATH, "//div[@class='listGridItemPrice']") 
    birthplaces = driver.find_elements(By.XPATH, "//div[@class='listGridItemOrigin']")
    #print(birthplaces)
    
    # Loop through the elements and extract data
    for name_element, price_element, birthplace_element in zip(names, prices, birthplaces):
        name = name_element.text
        price = price_element.text
        birthplace = birthplace_element.text
        # Create a dictionary to store the data for each item
        item_data = {
            "name": name,
            "Price": price,
            "birthplace": birthplace
        }
        # Append the item dictionary to the list
        all_items.append(item_data)

    # Increment the page number
    page_num += 1

    # Print the current number of items
    print(all_items)
    print(f"Total items: {len(all_items)}")
    
# Quit the driver when done
# driver.quit()

#add a way to check for duplicate items
#add date of sale to item_data
#save all items to database
#add functionality to get more than 10,000 items


