import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# select specific checkbox
# driver.find_element(By.XPATH, "//input[@id='monday']").click()

# select all the checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
print(len(checkboxes)) # 7
time.sleep(2)
for checkbox in checkboxes:
    checkbox.click()
time.sleep(2)

# -------------------------------------------------------------------------------------------------------

# select multipale checkboxes by choice
for checkbox in checkboxes:
    weekname = checkbox.get_attribute('id')
    if weekname == "monday" or weekname == "sunday":
        checkbox.click()
time.sleep(2)

# -------------------------------------------------------------------------------------------------------

# select last 2 checkbox
# for i in range(len(checkboxes)-2, len(checkboxes)):
#     checkboxes[i].click()
# time.sleep(2)

# ----------------------------------------------------------------------------------------------------------

# unselecting all the checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
time.sleep(2)

