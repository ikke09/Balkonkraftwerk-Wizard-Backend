import pandas as pd
from models import MastrDataOut
import requests


def extract_data_item(item):
    return MastrDataOut(
        id=item['MaStRNummer'],
        name=item['NameConcealed'],
        state=item['Bundesland'],
        zip=int(item['Postleitzahl']),
        city=item['OrtConcealed'],
        street=f"{item['StrasseConcealed']} {item['HausnummerConcealed']}",
        link=f"https://www.marktstammdatenregister.de/MaStR/Akteur/Marktakteur/DetailOeffentlich/{item['Id']}"
    )


def get_data(city: str | None = None):
    url = "https://www.marktstammdatenregister.de/MaStR/Akteur/MarktakteurJson/GetOeffentlicheMarktakteure?page=1&pageSize=1000&filter=T%C3%A4tigkeitsstatus~eq~%272511%27~and~MaStR-Nr.~sw~%27SNB%27"
    if city:
        url += f"~and~Ort~ct~'{city}'"

    response = requests.get(url)
    data = response.json()
    results = [extract_data_item(item) for item in data['Data']]
    return results
