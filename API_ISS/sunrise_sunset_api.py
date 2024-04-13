import requests
from datetime import datetime

MY_LAT=39.894829
MY_LONG=-32.781351

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0, 
}
respone = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
respone.raise_for_status()
data=respone.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now();
print(time_now.hour)