"""
    This program  monitors the price of a particular stock, in this case tesla
    if the price between 2 consecutive days decreases by more than 5 percent,
    the program searches the news and sends a text alert
   
   ** Note because I have a trial account with the news api, I can only get news less than a month old
    so I modified the script accordingly just to test however if you have a paid accout, you can set prod_env to true, 
    to get the news returned from the correct date [not tested] **
    
    In order to run this program, without modifying it, you can have a secret.txt file in the same directory with the 
    twilio account_sid and auth_token, news_api_key, alphavantage_api_key each in a separate line in the listed order.
"""

import json

import requests
from twilio.rest import Client
import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
prod_env = False
message = ""

try:
    file = open('secret.txt')
    twilio_account_sid = file.readline().strip()
    twilio_auth_token = file.readline().strip()
    news_api_key = file.readline().strip()
    alphavantage_api_key = file.readline().strip()
except:
    print("Error Getting the API keys from the secret file")


# STEP 1: Use https://www.alphavantage.co
def get_stock_data():
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": alphavantage_api_key
    }
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    # print(json.dumps(response.json(), indent=4))
    return response.json()


# When STOCK price decreases by 5% or more between yesterday
# and the day before yesterday then print("News ...").
# and calls tries to get news
def did_decrease(json_data, percent=-5):
    previous_date = 0
    stock_data = json_data["Time Series (Daily)"]
    for current_date in reversed(stock_data):
        if previous_date == 0:
            previous_date = current_date
        else:
            # Calculate percent difference
            previous_close = float(stock_data[previous_date]["4. close"])
            current_close = float(stock_data[current_date]["4. close"])
            percent_diff = (current_close - previous_close) / previous_close * 100

            if percent_diff < percent:
                global message
                message += f"News on {current_date}, previous close = {previous_close}, current close = {current_close}," \
                           f"percent difference is {percent_diff}"
                print()
                get_news(from_date=previous_date, to_date=current_date)

            # resetting previous date to be current date because next iter switches date
            previous_date = current_date


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news(from_date, to_date):
    # Due to limitation on the API, I can only get news less than a month old,
    # I change the values received just to get some data
    if not prod_env:
        from_date = datetime.datetime.now() - datetime.timedelta(days=15)
        to_date = datetime.datetime.now()

    url = "https://newsapi.org/v2/everything"
    params = {
        "apiKey": news_api_key,
        "q": COMPANY_NAME,
        "from": from_date,
        "to": to_date,
        # The number of results to return per page.,
        # default # of page is 1 that's why "page param not set
        "pageSize": 1
    }
    response = requests.get(url=url, params=params)
    print(json.dumps(response.json(), indent=4))
    news_article = response.json()['articles'][0]
    global message
    message += '\n --- Headline: ' +  news_article['title']
    send_sms_alert()


# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and a article's title
def send_sms_alert():
    global message
    client = Client(twilio_account_sid, twilio_auth_token)
    txt_msg = client.messages \
        .create(
        body=message,
        from_='+18722393155',
        to='7743601056'
    )
    message = ""


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

if __name__ == "__main__":
    json_data = get_stock_data()
    did_decrease(json_data)
