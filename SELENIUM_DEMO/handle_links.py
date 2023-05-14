import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(2)

# click on link
driver.find_element(By.TAG_NAME, "Books").click()
time.sleep(2)

# find num of links in a page
# links = driver.find_elements(By.TAG_NAME, "Digital downloads ")
# # links1 = driver.find_elements(By.XPATH, "//a")
# print("total number of links", len(links))
# # print all the links
#
# for link in links:
#     print(link.text)