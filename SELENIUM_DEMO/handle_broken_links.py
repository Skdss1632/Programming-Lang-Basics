import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests as requests

driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
time.sleep(2)

alllinks = driver.find_elements(By.TAG_NAME, "a")
count = 0

for link in alllinks:
    url = link.get_attribute('href')
    try:
        responce = requests.head(url)
    except:
        None
    if responce.status_code >= 400:
        print(url, "is valid link")
    else:
        print(url, "is broken link")
        count += 1
print("total no of broken links", count)
