import requests

url = 'https://api.sheety.co/25e7cf05b17af6a4028ba3cd3e885871/myFlightDeals/prices'

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.destianation_data = {}
    def get_destination_data(self):
        response = requests.get(url=url)
        response.raise_for_status()
        data=response.json()
        self.destianation_data = data["prices"]
        return self.destianation_data
    def update_destination_codes(self):
        for city in self.destianation_data:
            body = {
                "price": {
                    "iataCode": city["iataCode"]
                }     
            }
            response=requests.put(url=f"{url}/{city['id']}",json=body)
            print(response.text)
    def get_customer_emails(self):
        response = requests.get(url="https://api.sheety.co/25e7cf05b17af6a4028ba3cd3e885871/myFlightDeals/users")
        return response.json()["users"]