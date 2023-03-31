# import time
# from deutschland import marktstammdaten
# from pprint import pprint
# from deutschland.marktstammdaten.api import daten_api
# from deutschland.marktstammdaten.model.einheit_einheit_json_get_erweiterte_oeffentliche_einheit_stromerzeugung_get200_response import EinheitEinheitJsonGetErweiterteOeffentlicheEinheitStromerzeugungGet200Response
# # Defining the host is optional and defaults to https://www.marktstammdatenregister.de/MaStR
# # See configuration.py for a list of all supported configuration parameters.
# configuration = marktstammdaten.Configuration(
#     host="https://www.marktstammdatenregister.de/MaStR"
# )


from typing import List
from models import MastrModel


def get_data(query: str) -> List[MastrModel]:
    return []
    # Enter a context with an instance of the API client
    # with marktstammdaten.ApiClient(configuration) as api_client:
    #     # Create an instance of the API class
    #     api_instance = daten_api.DatenApi(api_client)
    #     # str | Spalte, nach der auf- oder absteigend sortiert werden soll (optional)
    #     sort = "sort_example"
    #     page = 1  # int | Seite, die geladen werden soll (optional)
    #     page_size = 1  # int | Anzahl an Einträgen pro Seite (optional)
    #     # str | Syntax: Feld-name~[eq|neq|sw|ct|nct|ew|null|nn]~'Wert'~[and|or]~... (optional)
    #     filter = "filter_example"

    #     try:
    #         # Erweiterte öffentliche Daten zur Stromerzeugung
    #         api_response = api_instance.einheit_einheit_json_get_erweiterte_oeffentliche_einheit_stromerzeugung_get(
    #             sort=sort, page=page, page_size=page_size, filter=filter)
    #         pprint(api_response)
    #     except marktstammdaten.ApiException as e:
    #         print("Exception when calling DatenApi->einheit_einheit_json_get_erweiterte_oeffentliche_einheit_stromerzeugung_get: %s\n" % e)
