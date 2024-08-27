import os

parameters = {
    "app_key": os.environ["FLIGHT_API_KEY"],
    "password": os.environ["FLIGHT_PASSWD"],
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def get_code(self, city):
        code = "more tests"

        return code
