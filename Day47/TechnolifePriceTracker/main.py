from bs4 import BeautifulSoup
import requests
import smtplib

URL = "https://www.technolife.com/product-60492/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D9%84%D9%86%D9%88%D9%88-15.6-%D8%A7%DB%8C%D9%86%DA%86%DB%8C-%D9%85%D8%AF%D9%84-ideapad-slim-3-i3-1315u-8gb-512gb"
MY_EMAIL_ADDRESS = ""
MY_EMAIL_PASSWORD = ""

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

price = soup.find("p",  class_="text-[19px] font-semiBold !leading-5 xl:text-[22px] text-primary-shade-1")
price_as_float = float(price.getText().replace(",",""))


print(price_as_float)

if price_as_float < 98_000_000 :
    message = f"""Subject: تغییر قیمت محصول\n\n
                  لپتاپ لنوو که میخواتستمی قیمتش تغییر کرد\n
                    {price_as_float}قیمت الانش:\n
                  {URL}""".encode("utf-8")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL_ADDRESS, MY_EMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL_ADDRESS,
                            to_addrs=MY_EMAIL_ADDRESS,
                            msg=message)