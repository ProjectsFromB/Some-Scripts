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
    cocktailDB_url = f"https://www.cocktail.com/list/cocktail/7155/{page_num}?sortBy=mostInteresting"
    driver.get(cocktailDB_url)

    names = driver.find_elements(By.XPATH, "//span[@class='listGridItemInfo_name']")

    # Loop through the elements and extract data
    for name_element in names:
        name = name_element.text

        # Click on the item to navigate to its page
        item_element = name_element.find_element(By.XPATH, "..")
        item_link = item_element.find_element(By.TAG_NAME, "a")
        item_link.click()

        # Extract ingredients from the item's page
        ingredients = []
        ingredient_elements = driver.find_elements(By.XPATH, "//table[@class='no-margin ingredients-table']//td[@class='text-left']")
        for ingredient_element in ingredient_elements:
            ingredients.append(ingredient_element.text)

        # Create a dictionary to store the data for each item, including ingredients
        item_data = {
            "name": name,
            "ingredients": ingredients
        }
        # Append the item dictionary to the list
        all_items.append(item_data)

        item_title = driver.find_element(By.XPATH, "//h1[@class='item-title']").text
        print("Item Title:", item_title)

        # Navigate back to the original page
        driver.back()

    # Increment the page number
    page_num += 1

    # Print the current number of items
    print(f"Total items: {len(all_items)}")

# Quit the driver when done
driver.quit()

# ... (rest of your code)

