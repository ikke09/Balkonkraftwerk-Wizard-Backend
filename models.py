import os
from pydantic import BaseModel


class Coords(BaseModel):
    latitude: float
    longitude: float
    altitude: int


class Version(BaseModel):
    major: int = 0
    minor: int = 0
    patch: int = 1
    version: str = f'{major}.{minor}.{patch}'


class QAItem(BaseModel):
    question: str
    answer: str


class ChecklistItem(BaseModel):
    description: str
    checked: bool = False


class UserDataBalcony(BaseModel):
    alignment: str = 'S'
    shadowing: str = 'None'


class UserDataPV(BaseModel):
    module_count: int = 2
    module_power: int = 300
    angle: int = 90
    investment: int = int(os.getenv('INVEST_PRICE', 1000))


class UserDataConsumption(BaseModel):
    amount: int = 2500
    price: int = 40


class UserDataIn(BaseModel):
    DataProcessingAccepted: bool = False
    Location: Coords
    PV: UserDataPV
    Balcony: UserDataBalcony
    Consumption: UserDataConsumption
    TimePeriod: int = 1


class KpiResult(BaseModel):
    energy_output_per_year: float = 0.0
    usable_energy_per_year: float = 0.0
    amortization: float = 0.0
    savings: float = 0.0
    savings_over_period: float = 0.0
    price_per_kwh: float = 0.0
    self_consumption: float = 0.0
    realistic_savings: float = 0.0


class MastrDataOut(BaseModel):
    id: str = ''
    name: str = ''
    state: str | None = None
    zip: int | None = None
    city: str | None = None
    street: str | None = None
    link: str | None = None
