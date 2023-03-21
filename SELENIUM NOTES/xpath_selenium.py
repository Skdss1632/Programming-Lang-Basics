# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(r'C:\drivers of browser\chromedriver_win32\chromedriver.exe')
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# time.sleep(5)
#
# driver.find_element(By.XPATH, '//*[@id="nav-xshop"]/a[1]').click()
# time.sleep(10)
# ......................................................................................................................
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(r'C:\drivers of browser\chromedriver_win32\chromedriver.exe')
    yield driver

def load_web_project(driver):
    driver.get("https://leetcode.com/problemset/all/?sorting=W3sic29"
               "ydE9yZGVyIjoiQVNDRU5ESU5HIiwib3JkZXJCeSI6IkRJRkZJQ1VMVFkifV0%3D&page=2")
    driver.maximize_window()
    time.sleep(5)

def test_first(driver):
    load_web_project(driver)
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/di'
                                  'v[1]/div[6]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/a').click()
    time.sleep(15)
    driver.find_element(By.CLASS_NAME, 'whitespace-nowrap').click()
    time.sleep(4)










