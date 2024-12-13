from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
query = 'laptop'
driver.get(f"https://www.amazon.in/s?k={query}&crid=2AJJXDI37TZRN&sprefix=laptop%2Caps%2C250&ref=nb_sb_noss_1")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
time.sleep(6)
driver.close()