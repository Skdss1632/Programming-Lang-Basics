import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

# Use undetected-chromedriver to create a WebDriver instance
options = uc.ChromeOptions()
options.add_argument("--headless")  # Optional: Run Chrome in headless mode
driver = uc.Chrome(options=options)

# Maximize the window (optional)
driver.maximize_window()

# Navigate to the desired URL
driver.get('https://help.ipfoxy.com/docs/Developer-API')

try:
    # Wait for the presence of the element with the specified ID
    element = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, "element_id"))
    )
except TimeoutException:
    print("Loading took too much time!")

# Close the WebDriver instance
driver.quit()
