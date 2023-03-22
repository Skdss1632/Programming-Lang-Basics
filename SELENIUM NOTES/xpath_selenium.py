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

driver = webdriver.Chrome(r'"C:\Users\91707\Downloads\edgedriver_win64\msedgedriver.exe"')
driver.get("https://automationexercise.com/")
driver.implicitly_wait(15)
driver.maximize_window()
# scrolling the web page
python = driver.find_element(By.XPATH, "//h2[normalize-space()='recommended items']")
driver.execute_script('arguments[0].scrollIntoView(true)', python)
time.sleep(5)







