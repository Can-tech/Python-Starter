import requests
from datetime import datetime
import smtplib
import time
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

# Set up the email parameters
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
my_email = os.getenv('EMAIL_ADDRESS')
my_password = os.getenv('EMAIL_PASSWORD')
RECIPIENT_ADDRESS = os.getenv('RECIPIENT_ADDRESS')

MY_LAT=39.894829
MY_LONG=-32.781351
iss_location = None

def get_iss_pos():
    global iss_location
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude=float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    iss_location = (latitude,longitude)

def is_iss_visible():
    get_iss_pos()
    if MY_LAT-5 <= iss_location[0] <= MY_LAT+5 and MY_LONG-5 <= iss_location[1] <= MY_LONG+5:
        return True
    else:
        return False
    
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0, 
    }
    respone = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    respone.raise_for_status()
    data=respone.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)
    time_now = int(datetime.now().hour);

    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False

while True:
    print(is_iss_visible(), is_night())
    time.sleep(60)
    if is_iss_visible() and is_night():
        with smtplib.SMTP("smtp.gamil.com", port=576) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs="", msg="Subject:Look out!\n The ISS is in your region!")