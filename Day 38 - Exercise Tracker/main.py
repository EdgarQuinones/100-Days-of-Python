from datetime import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()

query = input("Tell me about your exercises: ")

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": os.environ["APP_ID"],
    "x-app-key": os.environ["API_KEY"],
}

parameters = {
    "query": query
}

response = requests.post(url=endpoint, headers=headers, json=parameters)
response.raise_for_status()
workout_data = response.json()

sheety_endpoint = os.environ["SHEET_ENDPOINT"]

# response = requests.get(url=sheety_get_endpoint)
# print(response.json())

sheety_header = {
    "content-type": "application/json",
    "Authorization": os.environ["TOKEN"]
}

for inputs in range(len(workout_data["exercises"])):
    sheety_parameters = {
        "workout": {
            "date": str(datetime.strftime(datetime.now(), "%m/%d/%Y")),
            "time": str(datetime.strftime(datetime.now(), "%H:%M:%S")),
            "exercise": str(workout_data["exercises"][inputs]["name"]),
            "calories": str(workout_data["exercises"][inputs]["nf_calories"]),
            "duration": str(workout_data["exercises"][inputs]["duration_min"]),
        }

    }

    response = requests.post(url=sheety_endpoint, headers=sheety_header, json=sheety_parameters)
    response.raise_for_status()
