import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Edge()

driver.implicitly_wait(10)

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox = driver.find_element(By.NAME, 'q')
searchbox.send_keys("selenium")

searchbox.submit()  # it will work like enter key

driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()
time.sleep(3)

