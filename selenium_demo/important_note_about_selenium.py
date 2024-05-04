from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

login_widget = driver.find_element(By.CLASS_NAME, "header-fix kgfjkfh") # in any locator if we give the value
# with spaces most of the time it will not locate the element so avoid spaces in locator value
# (header-fix kgfjkfh) here remove value after space