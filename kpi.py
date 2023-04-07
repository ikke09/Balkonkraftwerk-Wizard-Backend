from models import KpiResult, UserDataIn
from radiation import get_radiation


def calculate_kpi(data: UserDataIn) -> KpiResult | None:
    if data.DataProcessingAccepted == False:
        return None

    # Calculation based on the following source:
    # https://photovoltaic-software.com/principle-ressources/how-calculate-solar-energy-power-pv-systems
    # E = A * r * H * PR
    # E = Energy (kWh)
    # A = Total solar panel Area (m2)
    # r = solar panel yield or efficiency(%)
    # H = Annual average solar radiation on tilted panels (shadings not included)
    # PR = Performance ratio, coefficient for losses (range between 0.5 and 0.9, default value = 0.75)

    # Annual solar radiation at the user location for 2022 in kWh/m2
    radiation = get_radiation(data.Location.latitude,
                              data.Location.longitude, 2022)

    # kW of the PV
    # module_powes is in W
    module_power = data.PV.module_power / 1000
    total_power = data.PV.module_count * module_power
    # In germany the max power is 600Wp or 0.6kWp
    kWp = total_power if total_power <= 0.6 else 0.6
    # Average Module is 1x1.7m
    average_module_area = 1.7
    total_moduale_area = data.PV.module_count * average_module_area
    solar_panel_efficiency = kWp / total_moduale_area
    # Tilt of the PV
    # TODO: Use the tilt of the PV
    module_tilt = data.PV.angle
    # PR
    performance_ratio = 0.75
    # Energy output in kWh
    energy_output = total_moduale_area * \
        solar_panel_efficiency * radiation * performance_ratio

    # Savings in €
    savings_per_year = energy_output * data.Consumption.price
    # shadowing factor = 1 => no shadow on the PV
    # shadowing factor = 0 => PV is completly covered with shadow
    # user input is a percentage from 0 - 100%
    # TODO: Use Shadowing factor
    shadowing = 1 - data.Balcony.shadowing
    # TODO: Use the alignment of the PV
    alignment = data.Balcony.alignment

    # Assumption that the invest is 1000€
    unit_price = 1000.0

    # Electricity bill of the user
    electricity_bill = data.Consumption.amount * data.Consumption.price

    # Amortization time in years
    amortization_time = (unit_price + electricity_bill) / savings_per_year

    # TODO: Calculate the other KPIs
    self_sufficiency = 0.16
    self_consumption = 0.66

    result = KpiResult(energy_output_per_year=energy_output, amortization=amortization_time,
                       savings=savings_per_year, self_consumption=self_consumption, self_sufficiency=self_sufficiency)

    return result
