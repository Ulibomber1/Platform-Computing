from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

# random user variables
stepTime = .05 * random.randrange(10, 100)



driver = webdriver.Chrome()

driver.get("http://localhost:3000/")
startTime = time.time()
pageTitle = driver.title

driver.implicitly_wait(stepTime)

driver.find_element()

driver.quit()
endTime = time.time()

elapsedTime = endTime - startTime