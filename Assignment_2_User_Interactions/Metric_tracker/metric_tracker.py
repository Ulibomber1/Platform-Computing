from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pymysql
import random
import time

#connect to localhost database
dbConn = pymysql.connect(
    host='localhost:3306',
    user='root',
    password='1208Ilikemysql!!',
    database='schema2',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)


# random user variables
timeOnAboutMe = .05 * random.randrange(10, 250)
timeOnGithub = .05 * random.randrange(10, 150)

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(0.5)
driver.set_page_load_timeout(20)


driver.get("http://localhost:3000/")
startTime = time.time()
print("\n\nWebpage Title: " + driver.title)

time.sleep(timeOnAboutMe)
siteTime = time.time()
elapsedTime = siteTime - startTime
print("Time on site: " + str(elapsedTime)) 

link = driver.find_element(by = By.CLASS_NAME , value="App-Link")
linkURL = link.get_attribute('href')
driver.get(linkURL)
print("Github page Title: " + driver.title + "\nGithub page URL: " + linkURL)
time.sleep(timeOnGithub)

endTime = time.time()
elapsedTime = endTime - startTime
print("Time on Github: " + str(elapsedTime) + "\n\n")


try:
    with dbConn.cursor() as cursor:
        sql = "INSERT INTO 'user' ('id', 'browser', 'clicked_github_link', 'time_on_about_me') VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, ())
    dbConn.commit()
    print("Row added successfully!")
finally:
    dbConn.close()