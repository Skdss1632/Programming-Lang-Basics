import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")

# find element():- return single webelement

# locator matching with single webelement
# element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# element.send_keys("apple Macbook pro 13- inch")

# locator matching with multiple webelements:- return only first link text bcz i am using find element
# element1 = driver.find_element(By.XPATH, "//a[normalize-space()='Sitemap']") # own path:-
# # //div[@class='footer']//a
# print(element1.text) # sitemap

# ------------------------------------------------------------------------------------------------------------


# find elements:- return multiple webelements
# elements1 = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
# print(len(elements1)) # 1
# elements1[0].send_keys("apple Macbook pro 13- inch")
# time.sleep(2)

elements2 = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
print(len(elements2)) # 23
# print(elements2[0].text)
for ele in elements2:
    print(ele.text)


# if element not available on webpage then find_elements does not show any exception
elements3 = driver.find_elements(By.LINK_TEXT, "log")
print("elements returned", len(elements3))






