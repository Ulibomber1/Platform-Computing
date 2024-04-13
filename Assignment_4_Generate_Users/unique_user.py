from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random
import time


# random user variables
timeAdded = 0

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(0.5)
driver.set_page_load_timeout(20)


#driver.get("http://localhost:3000/")
driver.get("https://www.csusb.edu/")
startTime = time.time()

# get all images from document
lists = driver.find_elements(by=By.TAG_NAME, value='li')
images = driver.find_elements(by=By.TAG_NAME, value='img')

# add multiples of 10 to presence time for each link found
timeAdded += 2 * len(lists)
#subtract 5 seconds for every image found
timeAdded -= 5 * len(images)

if (timeAdded < 0):
    timeAdded = 0

siteTime = time.time()
elapsedTime = siteTime - startTime
print("Time on site: " + str(elapsedTime + timeAdded)) 
