import smtplib
import datetime as dt
import random

MY_EMAIL = ""
MY_PASSWORD = ""

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open('quotes.txt') as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="test@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n{quote}")