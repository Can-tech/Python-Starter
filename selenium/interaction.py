from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count=driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# # article_count.click()
# print(article_count.text)

#Find elelmetn by Link Text
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

#Find the search <input> by Name attribute
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)

