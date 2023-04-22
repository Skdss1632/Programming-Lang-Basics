import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome(r'"C:\Users\pc\Downloads\chromedriver_win32\chromedriver.exe"')
    yield driver


pytest.fixture(scope="session")
def wait(driver):
    wait = WebDriverWait(driver, 10)
    yield wait


def load_web_page(driver, wait):
    driver.get("https://www.google.com/")
    driver.maximize_window()
    wait(EC.presence_of_element_located((By.NAME, "q")))
    search_box = driver.find_element(By.NAME, "q")
    assert search_box.is_displayed()

def test_demo(driver):
    load_web_page(driver)
    search_box_1 = driver.find_element(By.NAME, "q")
#     search_box_1.send_keys("selenium")
#     search_box_1.submit()  # it will work like enter key
#     driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()
#     time.sleep(3)




