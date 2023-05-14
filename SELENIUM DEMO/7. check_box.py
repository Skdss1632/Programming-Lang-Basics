import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# 1. select specific checkbox
driver.find_element(By.XPATH, "//input[@id='monday']").click()
time.sleep(2)

# 2. select all the weekday checkbox
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))

# approach1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()
#     time.sleep(2)
#
# # approach2
# for checkbox in  checkboxes:
#     checkbox.click()
#     time.sleep(2)


# select multiple checkboxes by choice
for checkbox in  checkboxes:
    weekname = checkbox.get_attribute('id')
    if weekname == 'monday' or weekname == 'sunday':
        checkbox.click()
        time.sleep(2)


# clearing all th checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
        time.sleep(3)




