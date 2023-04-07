import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Edge()
driver.get("https://www.yatra.com/")
driver.maximize_window()

# is_displayed() & is_enabled()
hotels = driver.find_element(By.XPATH, "//a[normalize-space()='Non Stop Flights']")
print("display status:", hotels.is_displayed()) #true
print("display status:", hotels.is_enabled()) #true

# is_selected():- for radio buttons
rd_btn_student_fare = driver.find_element(By.XPATH, "//a[normalize-space()='Student Fare']")
rd_btn_armed_forces = driver.find_element(By.XPATH, "//a[normalize-space()='Armed Forces']")
rd_btn_student_fare.click() # it will selcet the student fare radio button
rd_btn_armed_forces.click() # it will select the armed forces radio button
print(rd_btn_student_fare.is_selected()) # true
