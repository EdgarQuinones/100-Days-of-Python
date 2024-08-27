import os

import requests

sheety_header = {
    "content-type": "application/json",
    # "Authorization": os.environ["TOKEN"]
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    pass

    def update_sheet(self, sheet_data):
        new_data = sheet_data[0]['iataCode']
        sheety_parameters = {
            "price": {
                "iataCode": new_data,

            }
        }

        for index in range(len(sheet_data)):
            sheety_put_endpoint = f"{os.environ["SHEETY_ENDPOINT"]}/{index + 2}"
            response = requests.put(url=sheety_put_endpoint, headers=sheety_header, json=sheety_parameters)
            response.raise_for_status()
            new_data = sheet_data[index]['iataCode']
