
from models import KpiResult, UserDataIn
import requests

pvgis_url = "https://re.jrc.ec.europa.eu/api/PVcalc"


def calculate_kpi_pvgis(data: UserDataIn) -> KpiResult | None:
    if data.DataProcessingAccepted == False:
        return None
    orientation = {'S': 0.0, 'SW': 45.0, 'W': 90.0, 'NW': 135.0, 'N': -180.0,
                   'NO': -135.0, 'O': -90.0, 'SO': -45.0}[data.Balcony.alignment]
    invest = data.PV.investment
    self_consumption = 0.70
    params = {
        "lat": data.Location.latitude,
        "lon": data.Location.longitude,
        "peakpower": (data.PV.module_power * data.PV.module_count) / 1000,
        "mountingplace": "free",
        "angle": data.PV.angle,
        "loss": 14.0,
        "aspect": orientation,
        "pvprice": 1,
        "systemcost": invest,
        "interest": 0.0,
        "lifetime": data.TimePeriod,
        "outputformat": "json",
    }

    response = requests.get(pvgis_url, params=params)
    if response.status_code == 200:
        result = response.json()
        totals_result = result["outputs"]["totals"]["fixed"]
        energy_output_per_year = totals_result["E_y"]
        usable_energy_per_year = energy_output_per_year * self_consumption
        energy_price_in_eur = data.Consumption.price / 100
        savings = usable_energy_per_year * energy_price_in_eur
        realistic_savings = savings * self_consumption
        savings_over_period = savings * data.TimePeriod - invest
        amortization = invest / savings
        price_per_kwh = totals_result["LCOE_pv"]
        return KpiResult(energy_output_per_year=energy_output_per_year,
                         usable_energy_per_year=usable_energy_per_year,
                         amortization=amortization, savings=savings,
                         savings_over_period=savings_over_period,
                         price_per_kwh=price_per_kwh,
                         self_consumption=self_consumption,
                         realistic_savings=realistic_savings)
    else:
        return None
