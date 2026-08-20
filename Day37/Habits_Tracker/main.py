import requests
from datetime import datetime as dt

TODAY = dt.now().today().strftime("%Y%m%d")
USERNAME = "<optional username>"
TOKEN = "<optional private token>"
GRAPH_ID = "<optional graph id>"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params,)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "momiji",
}

header = {
    "X-USER-TOKEN": TOKEN,
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=header)


add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"



add_pixel_params = {
    "date": TODAY,
    "quantity": "25",
}

response = requests.post(url=add_pixel_endpoint, json=add_pixel_params, headers=header)




#update pixel
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"
#
# update_params = {
#     "quantity": "5"
# }
#
# response = requests.put(url=update_endpoint, json=update_params, headers=header)

#delete pixel
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20260818"
# response = requests.delete(url=delete_endpoint, headers=header)
# print(response.text)