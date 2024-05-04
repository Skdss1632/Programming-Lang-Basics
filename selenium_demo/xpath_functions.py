import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.amazon.in/ref=nav_logo")
driver.maximize_window()


