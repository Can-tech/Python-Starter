from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

page = driver.get("https://python.org")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".last .menu > li > a")
event_names = [e for e in event_names if e.text != '']
event_years_elements = driver.find_elements(By.CSS_SELECTOR, value=".last .menu > li > time")

# for e in event_years_elements:
#     print(e.get_attribute("datetime").split("T")[0])

mydictionary = {}
for i in range(len(event_years_elements)-1):
    mydictionary[i] = {'time': event_years_elements[i].get_attribute("datetime").split("T")[0], 'name': f'{event_names[i].text}'}

print(mydictionary)
driver.quit()





