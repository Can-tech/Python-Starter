import requests
from bs4 import BeautifulSoup
import smtplib
import time
import pprint

from dotenv import load_dotenv
import os

load_dotenv()

# Define the URL of the Amazon product you want to track
URL = 'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'

# Set the desired price threshold
PRICE_THRESHOLD = 100.0

# Set up the email parameters
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
RECIPIENT_ADDRESS = os.getenv('RECIPIENT_ADDRESS')

def check_price():
    time.sleep(5)
    # Send a GET request to the URL and get the HTML content of the page
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36", "Accept-Language":"tr-TR,tr;q=0.5","Cookie":"PHPSESSID=527828f52dbd4cfef6d00b45afd86f6a"}
    response = requests.get(URL, headers=headers)

    soup = BeautifulSoup(response.content, 'lxml')

    # Parse the HTML content using BeautifulSoup and extract the product title and price
    title_element = soup.find(id='productTitle')
    if title_element is not None:
        title = title_element.get_text().strip()
    else:
        title = 'Title not found'
    price = soup.find(class_='a-price-whole')
    if price is not None:
        price = price.get_text().strip()
    else:
        price = "0"
    price = float(price.replace('$', '').replace(',', ''))

    # Convert the price to a float and compare it to the desired price threshold
    if price < PRICE_THRESHOLD:
        # If the price is lower than the threshold, send an email alert using smtplib
        message = f'Subject: Amazon Price Alert\n\n{title} is now available at ${price}!\n{URL}'
        print(message)
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.sendmail(EMAIL_ADDRESS, RECIPIENT_ADDRESS, message.encode('utf-8'))
    else:
        print("not low enough")
# Call the check_price function
check_price()
