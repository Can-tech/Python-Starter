import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions().add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(3)

lang_element = driver.find_element(By.ID, value="langSelect-EN")
lang_element.click()

time.sleep(3)

cookie = driver.find_element(By.ID, value="bigCookie")
while True: 
    products = driver.find_elements(By.CSS_SELECTOR, value="#products .enabled")
    for p in products:
        time.sleep(20/1000)
        try:
            p.click()
        except:
            print("no element")
        
    time.sleep(16/1000)
    cookie.click()
