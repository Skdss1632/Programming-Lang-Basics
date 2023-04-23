import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Edge()
driver.get("https://www.amazon.in/")
driver.maximize_window()

search_box = driver.find_element(By.NAME, "field-keywords")
search_box.clear()
time.sleep(2)
search_box.send_keys("watch")
time.sleep(2)

print("result of text:", search_box.text) # text return inner text,inner text is not present that's why
# it does not return anything
print("result of get_attribute():", search_box.get_attribute('value')) # watch
print("result of get_attribute():", search_box.get_attribute('id'))