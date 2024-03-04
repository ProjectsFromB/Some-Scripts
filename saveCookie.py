from selenium import webdriver
import pickle
#from afile import save_cookie

driver = webdriver.Chrome()
driver.get('http://website.internets')

foo = input()

save_cookie(driver, '/tmp/cookie')
