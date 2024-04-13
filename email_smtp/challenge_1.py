import smtplib
import datetime as dt
import random
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

# Set up the email parameters
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

my_email = os.getenv('my_email')
my_password = os.getenv('my_password')


now = dt.datetime.now()
weekday=now.weekday()
if weekday == 1:
    with open("email_smtp/quotes.txt") as file:
        data=file.readlines()
        quote_of_day=random.choice(data)

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="rosor85642@v1zw.com", msg=f"Subject:Monday motivation :=)\n\n{quote_of_day}")
