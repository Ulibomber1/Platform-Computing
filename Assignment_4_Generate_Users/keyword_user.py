from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random
import time


# user variables
timeOnWebsite = .01 * random.randrange(10, 250)
timeAdded = 0
keyword = "student"

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(0.5)
driver.set_page_load_timeout(20)

driver.get("http://localhost:3000/")
#driver.get("https://www.csusb.edu/")
startTime = time.time()

# get all paragraph and header text from document
paragraphs = driver.find_elements(by=By.TAG_NAME, value='p')

# count occurences of keyword in the paragraphs and headers
for element in paragraphs:
    if (element.text.count(keyword) > 0):
        timeAdded += 10
        break

# add time according to occurences of keyword

leaveTime = time.time()
elapsedTime = leaveTime - startTime
print("Time on site: " + str(elapsedTime + timeAdded))
   