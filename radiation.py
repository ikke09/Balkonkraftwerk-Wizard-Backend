from datetime import datetime
import os
import requests

from models import Coords

solcast_api = "https://api.solcast.com.au/data/forecast/radiation_and_weather"


def get_radiation(coordinates: Coords, year: int) -> float:
    # Yearly Average of 2022 in Germany!
    return 1227.0
    # TODO: Retrieve radiation value from Solacast API
    # api_key = os.getenv('SOLCAST_API_KEY')
    # output = ["air_temp", "ghi", "relative_humidity",
    #           "wind_direction_10m", "wind_speed_10m", "zenith"]
    # start = datetime(year, 1, 1).isoformat()
    # end = datetime(year+1, 1, 1).isoformat()
    # params = {
    #     'latitude': coordinates.latitude,
    #     'longitude': coordinates.longitude,
    #     'api_key': api_key,
    #     'start': start,
    #     'end': end,
    #     'output_parameters': ','.join(output),
    #     'format': 'json',
    #     'time_zone': 'utc'
    # }
    # solcast_api = "https://api.solcast.com.au/data/forecast/radiation_and_weather?latitude=-33.856784&longitude=151.215297&output_parameters=air_temp,dni,ghi&format=json&api_key=DWMxqwi68GFqt8u1nZNIWo9dZAY57PZJ"
    # res = requests.get(solcast_api)
    # if res.status_code != 200:
    #     return None
    # data = res.json()
    # forecasts = data['forecasts']
    # ghi = [f['ghi'] for f in forecasts]
    # return sum(ghi) / len(ghi)
