from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Chrome()
driver.get("https://www.easemytrip.com/charters/flight.html")
driver.maximize_window()
time.sleep(2)

# drpcountry_ele = driver.find_element(By.ID, "input-country")
drp_country = Select(driver.find_element(By.ID, "nooftrav"))

# selecting option form dropdown
# drp_country.select_by_visible_text("1-3 Traveller")
# time.sleep(2)

# capture all the ele and print them
alloptions = drp_country.options
print("total no of options", len(alloptions))

for opt in alloptions:
    print(opt.text)


# select option from dropdown without using built in method
for opt in alloptions:
    if opt.text == "8-11 Traveller":
        opt.click()
        break
time.sleep(2)

