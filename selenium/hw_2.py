from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

name = driver.find_element(By.NAME, value="fName")
name.send_keys("jason")

name = driver.find_element(By.NAME, value="lName")
name.send_keys("koll")

name = driver.find_element(By.NAME, value="email")
name.send_keys("koll.jason@mail.com")

button = driver.find_element(By.CSS_SELECTOR,value="button")
button.click()

