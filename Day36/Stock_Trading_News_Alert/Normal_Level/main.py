import requests
import smtplib
from email.message import EmailMessage
from kavenegar import *

MyEmail = "<EMAIL>"
MyPassword = "<PASSWORD>"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_apikey = "<apikey>"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_apikey,
}

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list  = [info for time , info in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference/float(yesterday_closing_price)) * 100)
if abs(diff_percent) > 4 :

    news_apikey = "api key"
    news_params = {
        "apiKey": news_apikey,
        'q': COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.




    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

    formatted_articles= [f"Headline: {articles['title']}\nBrief: {articles['description']}" for article in three_articles]
    for article in formatted_articles:
        subject = f"{STOCK_NAME} {up_down}{diff_percent}%"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MyEmail, MyPassword)
            msg = EmailMessage()
            msg["From"] = MyEmail
            msg["To"] = "<Email>"
            msg["Subject"] = subject
            msg.set_content(article)
            connection.send_message(msg=msg)

        api = KavenegarAPI('kavenegar apikey')
        params = {'sender': 'number_of_kavenegar', 'receptor': 'your_number', 'message': f"{subject}\n{article}"}
        response = api.sms_send(params)

#Optional  Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

