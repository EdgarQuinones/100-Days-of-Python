import requests
from datetime import datetime

USER = "user"
TOKEN = "token"

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"

graph_parameters = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "Pages",
    "Type": "int",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

value_endpoint = f"{graph_endpoint}/{graph_parameters["id"]}"

# today = str(datetime.today())
# today = today.split(" ")[0].replace("-","")
today = datetime(year=2024, month=8, day=22).strftime("%Y%m%d")

value_parameters = {
    "date": today,
    "quantity": "20"
}

# response = requests.post(url=value_endpoint, headers=headers, json=value_parameters)
# print(response.text)

update_endpoint = f"{value_endpoint}/{today}"

updated_parameters = {
    "color": "ajisai",
    "quantity": "10"
}

# response = requests.put(url=update_endpoint, headers=headers, json=value_parameters)
# print(response.text)

delete_endpoint = f"{value_endpoint}/{today}"

response = requests.delete(delete_endpoint, headers=headers)
print(response.text)
