import requests
import datetime
from data import data
from twilio.rest import Client

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_parameters = {
    "Endpoint": "https://www.alphavantage.co/query",
    "symbol": "GAW.LON",
    "apikey": "key",
    "function": "TIME_SERIES_DAILY"
}

# Ran out of api requests for the day
# data = requests.get(stock_parameters["Endpoint"], params=stock_parameters)
# data.raise_for_status()
stock_data = data

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
day_before_yesterday = yesterday - datetime.timedelta(days=1)

yesterday_closing_price = data[str(yesterday)]["4. close"]
day_before_yesterday_closing_price = data[str(day_before_yesterday)]["4. close"]

percent_change = round(
    (float(yesterday_closing_price) - float(day_before_yesterday_closing_price)) / float(yesterday_closing_price) * 100,
    2)

if percent_change > 0:
    percent_change = f"🔺{percent_change}%"
elif percent_change < 0:
    percent_change = f"🔻{percent_change}%"

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

news_parameters = {
    "Endpoint": "https://newsapi.org/v2/everything",
    "sortBy": "publishedAt",
    "q": "Games Workshop Group PLC",
    "apiKey": "key",
}
data = requests.get(news_parameters["Endpoint"], params=news_parameters)
data.raise_for_status()

percent_change_news = f"GAW: {percent_change}"
title = "Headline: " + data.json()["articles"][0]["title"]
details = "Brief: " + data.json()["articles"][0]["description"]
url = "Link: " + data.json()["articles"][0]["url"]
published_at = "Published: " + data.json()["articles"][0]["publishedAt"].split("T")[0]
extra_links = "Other Reports:"
second_link = data.json()["articles"][1]["url"]
third_link = data.json()["articles"][2]["url"]

news = percent_change_news + "\n" + title + "\n" + details + "\n" + url + "\n" + published_at + "\n" + extra_links + "\n" + second_link + "\n" + third_link

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

account_sid = 'id'
auth_token = 'token'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='sender',
    body=news,
    to='receiver'
)
