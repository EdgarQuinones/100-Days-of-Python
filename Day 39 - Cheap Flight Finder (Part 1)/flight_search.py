# import os
# import requests
# from dotenv import load_dotenv
#
# load_dotenv()
#
# class FlightSearch:
#     # This class is responsible for talking to the Flight Search API.
#     def __init__(self):
#         self._api_key = os.environ["FLIGHT_API_KEY"]
#         self._api_secret = os.environ["FLIGHT_PASSWD"]
#
#         self.flight_endpoint = os.environ["FLIGHT_ENDPOINT"]
#
#         self.flight_header = {
#             "Content-Type": "application/x-www-form-urlencoded",
#         }
#
#         self.flight_params = {
#             "grant_type": "client_credentials",
#             "client_id": self._api_key,
#             "client_secret": self._api_secret,
#         }
#         self._token = self._get_new_token()
#
#     def get_code(self, city):
#         code_header = {
#             "Authorization": "Bearer " + self._token,
#             "Accept": "application/json",
#         }
#         code_params = {
#             "keyword": city,
#             "include": "AIRPORTS"
#         }
#         flight_code_endpoint = f"https://test.api.amadeus.com/v1/reference-data/locations/cities"
#         response = requests.get(flight_code_endpoint, params=code_params, headers=code_header)
#         code = response.json()["data"][0]["iataCode"]
#         return code
#
#     def _get_new_token(self):
#         response = requests.post(url=self.flight_endpoint, headers=self.flight_header, data=self.flight_params)
#         response.raise_for_status()
#         sheet_data = response.json()
#         return sheet_data["access_token"]
