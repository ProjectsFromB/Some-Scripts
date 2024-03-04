
#Remember to start tor in the background first with: "sudo tor"
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

# Set up Tor proxy configuration
tor_proxy = "socks5://127.0.0.1:9050"
profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.socks", "127.0.0.1")
profile.set_preference("network.proxy.socks_port", 9050)
profile.update_preferences()

# Create a new Firefox WebDriver instance with the configured profile
driver = webdriver.Firefox(firefox_profile=profile)

#Go to url & check our ip to see if Tor is working with Selenium:
driver.get("h:ttps://nordvpn.com/what-is-my-ip/")

# Close the browser
driver.quit()


