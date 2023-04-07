import os
from datetime import datetime
import requests

solcast_api = "https://api.solcast.com.au/data/historic/radiation_and_weather?"
solcast_params = "latitude={lat}&longitude={lng}&start={start}&end={end}&api_key={key}&output_parameters={output}&format=json&time_zone=utc"


def get_radiation(lat: float, lng: float, year: int) -> float:
    # Yearly Average of 2022 in Germany!
    return 1227.0
    # TODO: Retrieve radiation value from Solacast API
    # api_key = os.getenv('SOLCAST_API_KEY')
    # output = ["air_temp", "ghi", "relative_humidity",
    #           "wind_direction_10m", "wind_speed_10m", "zenith"]
    # start = datetime(year, 1, 1).isoformat()
    # end = datetime(year+1, 1, 1).isoformat()
    # api_url = (solcast_api + solcast_params).format(
    #     lat=lat, lng=lng, start=start, end=end, key=api_key, output=','.join(output))
    # res = requests.get(api_url)
    # if res.status_code != 200:
    #     return None
    # return res.json()
