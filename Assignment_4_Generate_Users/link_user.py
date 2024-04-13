from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random
import time


# random user variables
timeOnWebsite = .01 * random.randrange(10, 250)
timeAdded = 0

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

# get all images from document
links = driver.find_elements(by=By.TAG_NAME, value='a')
print("Test: " + str(links[0].get_attribute('href')))

# add multiples of 10 to presence time for each link found
timeAdded += 10 * len(links)

for link in links:
    if ("#" in str(link.get_attribute("href"))):
        continue
    tempstr = str(link.get_attribute("href"))
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(tempstr)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


# add time according to occurences of keyword
siteTime = time.time()
elapsedTime = siteTime - startTime
print("Time on site: " + str(elapsedTime + timeAdded)) 
