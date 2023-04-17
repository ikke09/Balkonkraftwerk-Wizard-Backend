
from models import KpiResult, UserDataIn
import pvlib
from pvlib.modelchain import ModelChain
from pvlib.location import Location
from pvlib.pvsystem import PVSystem
from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS
import pandas as pd


def calculate_kpi_pvlib(data: UserDataIn) -> KpiResult | None:
    if data.DataProcessingAccepted == False:
        return None

    location = Location(latitude=data.Location.latitude, longitude=data.Location.longitude,
                        altitude=data.Location.altitude, tz='Europe/Berlin')
    modules = pvlib.pvsystem.retrieve_sam('sandiamod')
    inverters = pvlib.pvsystem.retrieve_sam('cecinverter')
    module = modules['Canadian_Solar_CS5P_220M___2009_']
    inverter = inverters['ABB__MICRO_0_25_I_OUTD_US_208__208V_']
    temperature_model_parameters = TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_glass']
    azimuth = {'S': 180, 'N': 0, 'W': 270, 'O': 90}[data.Balcony.alignment]
    system = PVSystem(surface_tilt=data.PV.angle, surface_azimuth=azimuth, module_parameters=module,
                      inverter_parameters=inverter, temperature_model_parameters=temperature_model_parameters)
    times = pd.date_range(start='2021-01-01',
                          end='2021-12-31', freq='1M', tz=location.tz)

    radiation = location.get_clearsky(times)
    model = ModelChain(system, location)
    model.run_model(radiation)
    energy_output_monthly = model.results.ac
    energy_output_per_year = pd.Series.sum(
        energy_output_monthly) if energy_output_monthly is not None else 0.0

    return KpiResult(energy_output_per_year=energy_output_per_year)
