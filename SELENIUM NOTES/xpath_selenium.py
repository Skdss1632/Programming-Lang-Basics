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

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(r'C:\drivers of browser\chromedriver_win32\chromedriver.exe')
driver.get("https://automationexercise.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[7]/a').click()
time.sleep(5)







