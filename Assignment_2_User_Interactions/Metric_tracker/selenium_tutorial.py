from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() #start a webdriver instance

driver.get("https://www.selenium.dev/selenium/web/web-form.html") #get the webpage

title = driver.title # return the title of the webpage

driver.implicitly_wait(0.5) #set the wait duration between webdriver actions

# get various elements from the webpage
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# submit text through the webpage's form
text_box.send_keys("Selenium")
submit_button.click()

# get information from an element
message = driver.find_element(by=By.ID, value="message")
text = message.text

driver.quit() # End the webdriver session