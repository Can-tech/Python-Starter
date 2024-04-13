from twilio.rest import Client
from smtplib import SMTP
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

# Set up the email parameters
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
my_email = os.getenv('my_email')
my_password = os.getenv('my_password')

TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
TWILIO_VIRTUAL_NUMBER = "YOUR TWILIO VIRTUAL NUMBER"
TWILIO_VERIFIED_NUMBER = "YOUR TWILIO VERIFIED NUMBER"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
    def send_emails(self, message, emails_to_send):
        with SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            for email in emails_to_send:
                connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject: New low priced flight \n\n{message}".encode('utf-8'))

