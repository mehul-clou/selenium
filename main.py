from selenium import webdriver


chrome_driver_path = "C:\Developer\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")

# price = driver.find_element_by_class_name("a-price-whole")
# print(price.text)

# search = driver.find_element_by_name("q")
# print(search.get_property("placeholder"))

# link = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[3]/div/h2')
# print(link.text)
# print(link.tag_name)

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.text)
# print(logo.tag_name)
# print(logo.size)

# dock_link = driver.find_element_by_css_selector(".documentation-widget  a")
# print(dock_link.text)
# print(dock_link.tag_name)
#
# tt = driver.find_element_by_xpath('//*[@id="container"]/li[4]/ul/li[14]/a')
# print(tt.text)
# print(tt.tag_name)
# print(tt.get_attribute("href"))


# h2 = driver.find_element_by_tag_name("h1")
# print(h2.text)

dates=[]
tag=[]
info={}

mehul = driver.find_elements_by_css_selector(".event-widget time")
link = driver.find_elements_by_css_selector(".event-widget a")

for i in range(len(mehul)):
    info[i]={
        "name":mehul[i].text,
        "date":link[i].text
    }
print(info)










driver.close()
# driver.quit()