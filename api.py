import json
from fastapi import FastAPI, HTTPException
import uvicorn
from coords import get_coords
from kpi import calculate_kpi
from models import Version, Coords, UserDataIn, KpiResult, BalconyImageIn, BalconyImageOut, QAItem, ChecklistItem, MastrDataOut
from balcony_metadata import extract_metadata

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()


@app.get("/api")
async def version() -> Version:
    return Version()


@app.get("/api/coords")
def coords(zip: int, city: str) -> Coords:
    coordinates = get_coords(zip, city)
    if coordinates is None:
        raise HTTPException(
            status_code=400, detail=f"Could not retrieve coordinates for {zip}")
    return coordinates


@app.get("/api/info")
def info() -> list[QAItem]:
    f = open('qa.json')
    data = json.load(f)
    qa = [QAItem(question=item['question'], answer=item['answer'])
          for item in data]
    f.close()
    return qa


@app.post("/api/balcony")
def balcony(data: BalconyImageIn) -> BalconyImageOut:
    res = extract_metadata(balcony=data)
    if res is None:
        raise HTTPException(
            status_code=400, detail="Image could not be processed")
    return res


@app.post("/api/kpi")
def kpi(data: UserDataIn) -> KpiResult:
    res = calculate_kpi(data)
    return res


@app.get("/api/ar")
def ar():
    return "AR-Modell", 200


@app.get("/api/checklist")
def checklist() -> list[ChecklistItem]:
    f = open('checklist.json')
    data = json.load(f)
    checklist = [ChecklistItem(
        description=item, checked=False) for item in data]
    f.close()
    return checklist


@app.get("/api/mastr")
def mastr(q: str | None) -> list[MastrDataOut]:
    data = mastr.get_data(q)
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
