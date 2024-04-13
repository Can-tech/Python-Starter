import smtplib
import datetime as dt
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

# Set up the email parameters
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

my_email = os.getenv('my_email')
my_password = os.getenv('my_password')
# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# connection.starttls()
# connection.login(user=my_email, password=my_password)
# connection.sendmail(from_addr=my_email, to_addrs="test-4ev63mn3c@srv1.mail-tester.com", msg="Subject:Hello\n\nThis is the body!")
# connection.close()

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email, to_addrs="test-4ev63mn3c@srv1.mail-tester.com", msg="Subject:Hello\n\nThis is the body2!")
    
now=dt.datetime.now()
year = now.year
if year == 2023:
    print("True year")
day_of_week=now.weekday()
print(year)

data_of_birth=dt.datetime(year=1995,month=12,day=15)
print(data_of_birth)
