from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Developer\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# article_count = driver.find_element_by_css_selector("#articlecount a")
# # article_count.click()
#
# sciene = driver.find_element_by_link_text("Science")
# # sciene.click()
#
#
# search = driver.find_element_by_name("search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)


driver.get("http://secure-retreat-92358.herokuapp.com/")

name = driver.find_element_by_name("fName")
name.send_keys("Mehul")

lname = driver.find_element_by_name("lName")
lname.send_keys("Jain")

email = driver.find_element_by_name("email")
email.send_keys("mehul.jainleo@gmail.com")

button = driver.find_element_by_class_name("btn-block")
button.click()








# driver.close()