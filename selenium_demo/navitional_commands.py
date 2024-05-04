import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# driver = webdriver.Edge()
driver = webdriver.Edge(r"C:\Users\91707\Downloads\edgedriver_win64\msedgedriver.exe")
driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.in/")
driver.maximize_window()

driver.back()  #snapdeal
driver.forward() #amazon

driver.refresh() #it refresh the page

driver.quit()