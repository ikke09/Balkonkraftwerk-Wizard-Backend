from models import Coords, KpiResult, UserDataIn
from radiation import get_radiation


def get_area_factor(angle: float, alignment: str) -> float:
    return 1.0


def get_performance_ratio() -> float:
    return 0.75


def get_peak_power(power: int, count: int) -> float:
    module_power = power / 1000
    total_power = count * module_power
    # In germany the max power is 600Wp or 0.6kWp
    kWp = total_power if total_power <= 0.6 else 0.6
    return kWp


def get_amortization_rate(savings: float) -> float:
    # Assumption that the invest is 1000€
    unit_price = 1000.0

    # Amortization time in years
    amortization_time = unit_price / savings
    return amortization_time


def get_self_consumption() -> float:
    # Ciocia2021
    # Self-Consumption SC = (local_consumed / total_generated)
    # local_consumed = Direktverbrauchte Energie der PV-Anlage
    return 0.66


def get_self_sufficiency() -> float:
    # Ciocia2021
    # Sefl-Sufficiency SS = (local_consumed / total_consumed)
    return 0.16


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
    radiation = get_radiation(Coords(latitude=data.Location.latitude,
                              longitude=data.Location.longitude), 2022)

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

    # Amortization time in years
    amortization_time = get_amortization_rate(savings_per_year)

    # TODO: Calculate the other KPIs
    self_sufficiency = get_self_sufficiency()
    self_consumption = get_self_consumption()

    result = KpiResult(energy_output_per_year=energy_output, amortization=amortization_time,
                       savings=savings_per_year, self_consumption=self_consumption, self_sufficiency=self_sufficiency)

    return result


def calculate_kpi2(data: UserDataIn) -> KpiResult | None:
    if data.DataProcessingAccepted == False:
        return None
    # Wagner2010
    # Wd = GA * Fa * (Ppk / E0) * PR
    # Tagesenergieertrag (kWh) = Globalstrahlung * Flächenfaktor * (Peakleistung / Nennleistung) * Performance Ratio
    GA = get_radiation(Coords(latitude=data.Location.latitude,
                       longitude=data.Location.longitude), 2022)
    Fa = get_area_factor(data.PV.angle, data.Balcony.alignment)
    Ppk = get_peak_power(data.PV.module_power, data.PV.module_count)
    E0 = 1000
    PR = get_performance_ratio()
    Wd = GA * Fa * (Ppk / E0) * PR
    # Jahresenergieertrag (kWh) = 365 * Tagesenergieertrag
    Wa = 365 * Wd
    # Savings in €
    savings_per_year = Wa * data.Consumption.price
    self_consumption = get_self_consumption()
    self_sufficiency = get_self_sufficiency()
    amortization_rate = get_amortization_rate(savings_per_year)
    result = KpiResult(energy_output_per_year=Wa, amortization=amortization_rate,
                       savings=savings_per_year, self_consumption=self_consumption, self_sufficiency=self_sufficiency)
    return result
