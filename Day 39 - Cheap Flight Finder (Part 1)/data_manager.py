# import os
# import requests
# from dotenv import load_dotenv
#
# load_dotenv()
#
# sheety_header = {
#     "content-type": "application/json",
#     "Authorization": os.environ["TOKEN"]
# }
#
#
# class DataManager:
#     # This class is responsible for talking to the Google Sheet.
#     pass
#
#     def update_symbols(self, sheet_data):
#
#         for index in range(len(sheet_data)):
#             # for index in range(1):
#             sheety_parameters = {
#                 "price": {
#                     "iataCode": sheet_data[index]['iataCode'],
#                 }
#             }
#             # sheety_put_endpoint = f"{os.environ["SHEETY_ENDPOINT"]}/{index + 2}"
#             # response = requests.put(url=sheety_put_endpoint, headers=sheety_header, json=sheety_parameters)
#             # response.raise_for_status()
#
#     def update_prices(self, sheet_data):
#
#         for index in range(len(sheet_data)):
#             # for index in range(1):
#             sheety_parameters = {
#                 "price": {
#                     "lowestPrice": sheet_data[index]['lowestPrice'],
#                 }
#             }
#             # sheety_put_endpoint = f"{os.environ["SHEETY_ENDPOINT"]}/{index + 2}"
#             # response = requests.put(url=sheety_put_endpoint, headers=sheety_header, json=sheety_parameters)
#             # response.raise_for_status()
