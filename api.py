import json
from fastapi import FastAPI, HTTPException
import uvicorn
from kpi_pvgis import calculate_kpi_pvgis
from models import Version, UserDataIn, KpiResult, QAItem, ChecklistItem, MastrDataOut
from mastr import get_data
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.get("/api")
async def version() -> Version:
    return Version()


@app.get("/api/info")
def info() -> list[QAItem]:
    f = open('qa.json')
    data = json.load(f)
    qa = [QAItem(question=item['question'], answer=item['answer'])
          for item in data]
    f.close()
    return qa


@app.post("/api/pvgis")
def pvgis(data: UserDataIn) -> KpiResult:
    res = calculate_kpi_pvgis(data)
    if res is None:
        raise HTTPException(
            status_code=400, detail="Datenverarbeitung nicht akzeptiert")
    return res


@app.get("/api/checklist")
def checklist() -> list[ChecklistItem]:
    f = open('checklist.json')
    data = json.load(f)
    checklist = [ChecklistItem(
        description=item, checked=False) for item in data]
    f.close()
    return checklist


@app.get("/api/mastr")
def mastr(city: str | None = None) -> list[MastrDataOut]:
    data = get_data(city)
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
