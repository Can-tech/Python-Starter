import requests
from twilio.rest import Client
import os

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

OWM_Endpoint="https://api.openweathermap.org/data/2.5/forecast"
api_key =  os.environ.get("OWM_API_KEY")
weather_params = {
        "lat": 41.026089,
        "lon": 40.518929,
        "appid": api_key
}

response=requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
data=response.json()
weather_data=data["list"]

for i in range(3):
    if weather_data[i]["weather"][0]["id"]<=700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        from_='+18149923361',
        to=os.environ.get("MY_PHONE_NUMBER"),
        body='Rainy! Take the Umbrella!',
        )
        print(message.status)
        break


