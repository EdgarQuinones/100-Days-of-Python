import requests
from flight_search import FlightSearch
import os
from dotenv import load_dotenv

load_dotenv()

flight_search = FlightSearch()



class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self._token = flight_search._get_new_token()

    def get_price(self, city):
        code_header = {
            "Authorization": "Bearer " + self._token,
            "accept": "application/json",
        }

        flight_finder_endpoint = os.environ["FLIGHT_FINDER_ENDPOINT"]
        code_params = {
            "originLocationCode": "NYC",
            "destinationLocationCode": city,
            "departureDate": "2024-09-06",
            "returnDate": "2024-09-11",
            "adults": 1,
            "travelClass": "ECONOMY",
            "nonStop": "true",
            "currencyCode": "USD",
            "max": "250",
        }
        response = requests.get(flight_finder_endpoint, headers=code_header, params=code_params)
        try:
            calc_priced = self.get_lowest_price(response.json()["data"])
        except KeyError:
            return "No Data"

        return calc_priced

    def get_lowest_price(self, prices):
        try:
            lowest_price = float(prices[0]["price"]["total"])
            for index in range(len(prices)):
                current_price = float(prices[index]["price"]["total"])
                if current_price < lowest_price:
                    lowest_price = current_price
            return f"${lowest_price}"
        except IndexError:
            return "No Data"
        except KeyError:
            return "No Data"
