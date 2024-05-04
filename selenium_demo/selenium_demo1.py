from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

# we can automate the web using this driver path
# serv_obj = Service(r'"C:\Users\91707\Downloads\edgedriver_win64\msedgedriver.exe"')
# driver = webdriver.Edge(service=serv_obj)
"""if we do not want to give the driver path again and again then we need to save the driver of any browser in python
 script directory first then we can simply use the below line of code
 """

driver = webdriver.Edge()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
WebDriverWait(driver, 15).until(ec.presence_of_element_located((By.NAME, "username")))
driver.find_element(By.NAME, 'username').send_keys('Admin')
time.sleep(3)
driver.find_element(By.NAME, 'password').send_keys('admin123')
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
time.sleep(3)
# act_title = driver.title
# exp_title = ""

