from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

FORM_ENDPOINT = "https://docs.google.com/forms/d/e/1FAIpQLSdTkHcuciGHFCFhr5TzW8zxmd4N18M-F8AM6xH7GWhQ-7WaIg/viewform"
RENTAL_WEBSITE_ENDPOINT = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(RENTAL_WEBSITE_ENDPOINT)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

list_of_a = soup.find_all('a', attrs={"data-test":"property-card-link"})
list_of_links = [link['href'] for link in list_of_a if 'href' in link.attrs]

list_of_prices_span = soup.find_all("span", attrs={"data-test": "property-card-price"})
list_of_prices = [price.text.split("+")[0].split("/")[0] for price in list_of_prices_span]

list_of_address_elements = soup.find_all("address", attrs={"data-test":"property-card-addr"})
list_of_addresses = [address.text.strip() for address in list_of_address_elements]

####Google Form
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

driver.get(FORM_ENDPOINT)

for i in range(len(list_of_links)):
    sleep(2)
    address_input = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    address_input.click()
    address_input.send_keys(list_of_addresses[i])
    sleep(1)
    price_input = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_input.click()
    price_input.send_keys(list_of_prices[i])
    sleep(1)
    link_property = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_property.click()
    link_property.send_keys(list_of_links[i])
    driver.find_element(By.XPATH, value="//span[contains(text(), 'Gönder')]").click()
    sleep(2)
    send_another = driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    send_another.click()



