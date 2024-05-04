import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# @pytest.fixture()
# def driver():
#     driver = webdriver.Edge(r'"C:\Users\91707\Downloads\edgedriver_win64\msedgedriver.exe"')
#     yield driver


# pytest.fixture()
# def flights():
#     flights = {"depart_from": "Nwe Delhi", "going_to": "Mumbai", "Departure_Date": "31 Mar 23", ""}

def load():
    driver = webdriver.Edge(r'"C:\Users\91707\Downloads\edgedriver_win64\msedgedriver.exe"')
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//a[@title='https://www.yatra.com']//i[@class='ico-newHeaderLogo']").is_displayed()
    widget = driver.find_element(By.XPATH, "//p[@class='cmpyLinks ']")


