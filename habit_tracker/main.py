import requests
from datetime import datetime
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

# Set up the email parameters
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
USERNAME = os.getenv('USERNAME')
TOKEN = os.getenv('TOKEN')

pixels_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":"svbert47jf2sfd2as",
    "username": "hoompy",
    "agreeTermsOfService":"yes", 
    "notMinor":"yes"

}

# response = requests.post(url=pixels_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixels_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":"graph-1",
    "name":"Coding Graph",
    "unit":"Hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


post_to_graph_endpoint=f"{pixels_endpoint}/{USERNAME}/graphs/graph-1"

today = datetime.now()

graph_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":"1"
}

# response = requests.post(url=post_to_graph_endpoint, json=graph_data,headers=headers)
# print(response.text)

put_to_graph_endpoint=f"{pixels_endpoint}/{USERNAME}/graphs/graph-1/{today.strftime('%Y%m%d')}"

new_graph_data = {
    "quantity":"4"
}

# response = requests.put(url=put_to_graph_endpoint, json=new_graph_data,headers=headers)
# print(response.text)

delete_from_graph_endpoint=f"{pixels_endpoint}/{USERNAME}/graphs/graph-1/{today.strftime('%Y%m%d')}"


response = requests.delete(url=delete_from_graph_endpoint, headers=headers)
print(response.text)
