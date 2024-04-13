import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

# Set up the email parameters
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
news_api_key = os.getenv('news_api_key')
account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
gen_from_ = os.getenv('from_')
gen_to = os.getenv('to')



STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
api_address="https://www.alphavantage.co/query"
key="GWQ1GZADGIBWZ1D3"
parameters={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": key
}
response=requests.get(url=api_address, params=parameters)
response.raise_for_status()
data=response.json()
data_list=data["Time Series (Daily)"]
count=0
last_two_days_closing=[]
for att,val in data_list.items():
    last_two_days_closing.append(float(val["4. close"]))
    count+=1
    if count==2: break
daily_diff=round(last_two_days_closing[0]-last_two_days_closing[1],1)
daily_diff_percentage=round((daily_diff/last_two_days_closing[1])*100,1)
print(daily_diff)
print(f"{daily_diff_percentage}%")




## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_api_params= {
    "q": COMPANY_NAME,
    "from": "2023-08-24",
    "sortBy":"popularity",
    "language": "en",
    "apiKey":news_api_key
}
news_list=[]
def get_news():
    global news_list, news_api_params
    news_response=requests.get(url="https://newsapi.org/v2/everything", params=news_api_params)
    news_response.raise_for_status()
    news_data=news_response.json()["articles"]
    news_list=news_data[:2]


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

def send_message():
    get_news() 
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_= gen_from_,
    to = gen_to,
    body=f"""
    TSLA: {"🔺↑" if daily_diff_percentage > 0 else "🔻 ↓"}🔻🔻↓☻{daily_diff_percentage}%
    News 1:
    Headline: {news_list[0]["title"]} 
    Brief: {news_list[0]["description"]} 
    News 2:
    Headline: {news_list[1]["title"]} 
    Brief: {news_list[1]["description"]} 
    """
    )
    print(message.status)



if abs(daily_diff_percentage)>1:
    print("get news")
    send_message()



