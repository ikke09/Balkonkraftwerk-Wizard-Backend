
from models import KpiResult, UserDataIn
import requests

pvgis_url = "https://re.jrc.ec.europa.eu/api/PVcalc"


def calculate_kpi_pvgis(data: UserDataIn) -> KpiResult | None:
    if data.DataProcessingAccepted == False:
        return None
    orientation = {'S': 0.0, 'N': 180.0, 'W': 90.0,
                   'O': 270.0}[data.Balcony.alignment]
    investion = 1000.0
    params = {
        "lat": data.Location.latitude,
        "lon": data.Location.longitude,
        "peakpower": (data.PV.module_power * data.PV.module_count) / 1000,
        "mountingplace": "free",
        "angle": data.PV.angle,
        "loss": 14.0,
        "aspect": orientation,
        "pvprice": 1,
        "systemcost": investion,
        "interest": 0.0,
        "lifetime": data.TimePeriod,
        "outputformat": "json",
    }

    response = requests.get(pvgis_url, params=params)
    if response.status_code == 200:
        result = response.json()
        totals_result = result["outputs"]["totals"]["fixed"]
        energy_output_per_year = totals_result["E_y"]
        savings = (energy_output_per_year * data.Consumption.price) / 100
        savings_over_period = savings * data.TimePeriod - investion
        amortization = investion / savings
        price_per_kwh = totals_result["LCOE_pv"]
        return KpiResult(energy_output_per_year=energy_output_per_year, amortization=amortization, savings=savings, savings_over_period=savings_over_period, price_per_kwh=price_per_kwh)
    else:
        return None
