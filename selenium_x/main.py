from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

# Set up the email parameters
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
twitter_email = os.getenv('twitter_username')
twitter_password = os.getenv('twitter_password')
twitter_username = os.getenv('twitter_username')

promissed_upload = 10
promissed_download = 35


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

driver.get("https://twitter.com")
sleep(3)
driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a').click()
sleep(3)
email = driver.find_element(By.NAME, "text")
if email.text == "":
    email.click()
    sleep(1)
    email.send_keys(twitter_email)
sleep(2)
driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span').click()
sleep(2)
username = driver.find_element(By.CSS_SELECTOR, value='input')
if username.text == "":
    username.click()
    username.send_keys(twitter_username)
sleep(2)

button = driver.find_element(By.CSS_SELECTOR, '[data-testid="ocfEnterTextNextButton"]').click()

sleep(2)

password = driver.find_element(By.NAME, value='password')
if password.text == "":
    password.click()
    password.send_keys(twitter_password)
sleep(1)
driver.find_element(By.CSS_SELECTOR, value='[data-testid="LoginForm_Login_Button"]').click()
sleep(5)

##After Login
tweet_textarea = driver.find_element(By.CSS_SELECTOR, value='[data-testid="tweetTextarea_0"]')
tweet_textarea.click()
sleep(1)
tweet_textarea.send_keys("this is james")
sleep(1)
tweet_button = driver.find_element(By.CSS_SELECTOR, value='[data-testid="tweetButtonInline"]')
tweet_button.click()







