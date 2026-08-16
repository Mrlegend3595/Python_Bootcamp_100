import requests

"""
1XX : Hold on باید صبر کنی یه سری چیزا در جریانه
2XX: Here you go درخواست موفق هست
3XX: Go Away مجوز نداری - برو
4XX: you screwed up تو خراب کردی . چیزی برای نمایش وجود نداره
5XX: I screwed up من خراب کردم. شاید سایت یا سرور یا ... خراب باشه و شرمندتم
"""
#
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)

# if response.status_code != 200:
#     raise Exception("Bad Response")

# if response.status_code == 404:
#     raise Exception("that response was not found")
# elif response.status_code == 401:
#     raise Exception("you are not authorized")


#best way
response.raise_for_status()

#Httpstatuses.com

data = response.json()
position = data['iss_position']
latitude = position['latitude']
longitude = position['longitude']
print(data)
print(position)
print(latitude)
print(longitude)

iss_position = (longitude, latitude)
print(iss_position)

#---------------------------------------------------
# from datetime import datetime
# #Sunrise and Sunset api
# MY_LAT = 27.136740
# My_LNG = 57.079281
#
# parameters = {
#     "lat": MY_LAT,
#     'lng': My_LNG,
#     'formatted': 0, #24 hour formatted
# }
#
# response=requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
#
# data = response.json()
#
# sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
# sunset = data['results']['sunset'].split('T')[1].split(':')[0]
#
# print(sunrise)
# print(sunset)
# time_now = datetime.now()
# print(time_now.hour)

