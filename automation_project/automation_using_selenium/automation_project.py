import time

import undetected_chromedriver as uc
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Use undetected-chromedriver to create a WebDriver instance
options = uc.ChromeOptions()
options.add_argument("--disable-notifications")
# options.add_argument("--headless")  # Optional: Run Chrome in headless mode
driver = uc.Chrome(options=options)
# Maximize the window (optional)
driver.maximize_window()
actions = ActionChains(driver)


driver.get('https://www.irctc.co.in/nget/train-search')
login_btn_element = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.CLASS_NAME, "search_btn")))
login_btn_element.click()
time.sleep(10)




driver.quit()

