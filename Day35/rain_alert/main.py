import requests
import os
from kavenegar import *
api_key = os.environ.get("API_KEY")
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": 27.136740,
    "lon": 57.079281,
    "appid": api_key,
}
response = requests.get(url=OWM_endpoint, params=weather_params)
response.raise_for_status()

data = response.json()
weather_slice = data['list'][:4]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]

    if condition_code < 700:
        will_rain = True


if will_rain:
    api = KavenegarAPI(os.environ.get("KAVENEGAR_API_KEY"))
    params = {
        'sender' : 'ُsender',
        'receptor': 'reciever number',
        'message' :" بارش بارونه.چتر همراهت ببر حتما.😉"
    }
    response = api.sms_send(params)

#environment variable shows ->>  set _ Get-ChildItem env:
#environment variable def ->> export Key=Value

