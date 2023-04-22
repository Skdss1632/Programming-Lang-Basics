from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


driver = webdriver.Edge()
driver.get("https://www.facebook.com/")
driver.maximize_window()

# tag & id
# driver.find_element(By.CSS_SELECTOR, 'input#email').send_keys('abc')
# driver.find_element(By.CSS_SELECTOR, '#email').send_keys('abc')

# tag & class
# it is giving error bcz after this:- (inputtext) space is present and after space sometimes that value will not be considered
# driver.find_element(By.CSS_SELECTOR, ' input.inputtext _55r1 _61uy').send_keys('abc@gmail.com')
# driver.find_element(By.CSS_SELECTOR, ' input.inputtext').send_keys('abc@gmail.com')
# driver.find_element(By.CSS_SELECTOR, ' .inputtext').send_keys('abc@gmail.com')

# tag & attribute
# driver.find_element(By.CSS_SELECTOR, ' input[data-testid=royal_email]').send_keys('abc@gmail.com')
# driver.find_element(By.CSS_SELECTOR, ' [data-testid=royal_email]').send_keys('abc@gmail.com')

# tag & class & attribute
# driver.find_element(By.CSS_SELECTOR, ' [data-testid=royal_email]').send_keys('xyz') # for passing value in username box
# driver.find_element(By.CSS_SELECTOR, ' [data-testid=royal_pass]').send_keys('xyz') # for passing value in pass box
time.sleep(3)

