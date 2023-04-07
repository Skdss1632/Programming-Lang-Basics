import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Edge()
driver.get("https://www.amazon.in/")
driver.maximize_window()

print(driver.title) # Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in
print(driver.current_url) # https://www.amazon.in/
# print(driver.page_source) # it returns the sourece code of the webpage