from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Developer\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://orteil.dashnet.org/cookieclicker/")

timeout = time.time() + 60*0.3

while time.time() < timeout:
    cookies = driver.find_element_by_id("bigCookie")
    cookies.click()

per_second = driver.find_element_by_xpath('/div')
print(per_second.text)

# driver.close()