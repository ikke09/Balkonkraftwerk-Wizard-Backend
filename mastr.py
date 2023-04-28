import pandas as pd
from models import MastrDataOut


def _map_to_MastrDataOut(index, row: pd.Series) -> MastrDataOut:
    return MastrDataOut(
        id=index,
        name=row['Name'],
        state=row['Bundesland'],
        zip_code=row['PLZ'],
        city=row['Ort'],
        street=f"{row['Straße']} {row['Hausnummer']}",
    )


def get_data(query: int | None) -> list[MastrDataOut]:
    columns = ['MaStR-Nr.', 'Name des Marktakteurs', 'Bundesland',
               'Postleitzahl', 'Ort', 'Straße', 'Hausnummer', 'Tätigkeitsstatus']
    data = pd.read_csv('Public_Electricity_Provider.csv',
                       sep=';', index_col=0, header=0, usecols=columns)
    names = ["ID", "Name", "Bundesland", "PLZ",
             "Ort", "Straße", "Hausnummer", "Status"]
    data.rename(columns=dict(zip(columns, names)), inplace=True)
    data.index.names = [names[0]]
    active_providers = data[data['Status'] == 'Aktiv']
    if query:
        active_providers = active_providers[active_providers['PLZ'] == query]

    out = [_map_to_MastrDataOut(index, row)
           for index, row in active_providers.iterrows()]
    return out
