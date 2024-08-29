import os
import requests

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.getenv("FLIGHT_API_KEY")
        self._api_secret = os.getenv("FLIGHT_PASSWD")
        self._token = ""

    def get_code(self, city):
        code = ""



        return code
