from datetime import datetime

import requests
from twilio.rest import Client

weather_parameters = {
    "OWM_Endpoint": "https://api.openweathermap.org/data/2.5/forecast",
    "appid": "id",
    "lat": 40,
    "lon": 40,
    "units": "imperial",
    "cnt": 5,
}
now = datetime.now()

while True:

    if now.hour == 7:
        data = requests.get(weather_parameters["OWM_Endpoint"], params=weather_parameters)
        data.raise_for_status()
        weather_data = data.json()

        welcome_text = "Good Morning,\n\n"
        todays_weather = welcome_text + "Today's Forcast:\n"
        # add all the weather forecasts
        previous = ""
        current_hour = 600
        for hour in weather_data["list"]:
            current_weather = hour["weather"][0]["description"]

            if previous == current_weather:
                pass
            else:
                if current_hour < 1000:
                    string_hour = f"0{current_hour}"
                else:
                    string_hour = current_hour
                todays_weather += f"{string_hour}: {current_weather}\n"
                previous = current_weather
            current_hour += 300

        # print(todays_weather)

        # Send text of forcast
        account_sid = 'id'
        auth_token = 'token'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='sender',
            body=todays_weather,
            to='receiver'
        )
