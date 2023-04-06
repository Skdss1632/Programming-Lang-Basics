from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time



driver = webdriver.Edge()
driver.get("https://www.amazon.in/")
driver.maximize_window()

# absolute xpath or full xpath
# driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input').send_keys('watch')
# driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input').click()

# relative xpath or partial xpath
driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys('watch')
# driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()

# text()
# driver.find_element(By.XPATH, "//a[text()='Amazon miniTV']").click()

