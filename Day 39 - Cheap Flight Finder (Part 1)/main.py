# # This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
#
# import os
# import requests
# from data_manager import DataManager
# from flight_search import FlightSearch
# from dotenv import load_dotenv
# # from flight_data import FlightData
#
# load_dotenv()
#
# sheety_endpoint = os.environ["SHEETY_ENDPOINT"]
#
# sheety_header = {
#     "content-type": "application/json",
#     "Authorization": os.environ["TOKEN"]
# }
#
# response = requests.get(url=sheety_endpoint, headers=sheety_header)
# response.raise_for_status()
# sheet_data = response.json()["prices"]
# cities = []
# flight_search = FlightSearch()
# flight_data = FlightData()
# data_manager = DataManager()
# for column in sheet_data:
#     code = flight_search.get_code(column["city"])
#     column['iataCode'] = code
# data_manager.update_symbols(sheet_data)
#
# for column in sheet_data:
#     destination = column['iataCode']
#     price = flight_data.get_price(destination)
#     column['Lowest Price'] = price
#
# data_manager.update_prices(sheet_data)
#
#
# # response = requests.post(url=sheety_endpoint, headers=sheety_header, json=sheety_parameters)
# # response.raise_for_status()
