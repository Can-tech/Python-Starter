from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

page = driver.get("https://python.org")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")

for e in event_times:
    print(e.text)
          

mydictionary = {}
for i in range(len(event_names)):
    mydictionary[i] = {'time': event_times[i].text, 'name': f'{event_names[i].text}'}

print(mydictionary)
driver.quit()





