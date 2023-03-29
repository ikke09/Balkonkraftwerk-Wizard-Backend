import geocoder
import os
from models import Coords


def get_coords(zip: int, city: str) -> Coords | None:
    g = geocoder.google(
        location=f'{zip}, {city}', region='DE', key=os.getenv('GOOGLE_API_KEY'))
    if not g.ok or g.error:
        return None
    res = g.json
    return Coords(res['lat'], res['lng'])
