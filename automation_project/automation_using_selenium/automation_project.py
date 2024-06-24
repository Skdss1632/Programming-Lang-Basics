from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Specify the path to the ChromeDriver executable
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
driver.get('http://example.com')

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "element_id"))
    )
except TimeoutException:
    print("Loading took too much time!")

driver.quit()
