#Auto Birthday wisher 
import datetime as dt
import smtplib
import pandas
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

# Set up the email parameters
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

my_email = os.getenv('my_email')
my_password = os.getenv('my_password')

def send_email(email,name):
    with smtplib.SMTP("smtp.gmail.com", port=587) as conneciton:
        conneciton.starttls()
        conneciton.login(user=my_email, password=my_password)
        conneciton.sendmail(from_addr=my_email, to_addrs=email,msg=f"Subject:Happy Birthday!\nHave a wonderful life! Happy birthday {name}!")


data=pandas.read_csv("email_smtp/birthdays.csv")
data_dict_array=data.to_dict("records")

now = dt.datetime.now()
day = now.day
month = now.month

for dict_elem in data_dict_array:
    if dict_elem["month"] == month and dict_elem["day"] == day: 
        send_email(dict_elem["email"],dict_elem["name"])


