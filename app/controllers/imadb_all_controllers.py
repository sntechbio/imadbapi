from fastapi import FastAPI
from app.crud.repository import get_age_groups, get_patient_information_cvd, get_nutricional_data, \
    get_frequency_food_consumption, get_food_consumption, get_cytokines_covid
from app.schemas.all_schemas import AgeGroup, PatientInformationCvd, NutricionalData, FrequencyFoodConsumption, \
    FoodConsumption, CytokinesCovid
from app.models.Palettes import Palette
from typing import List
from fastapi import File, UploadFile, Depends
from app.service import plot_service
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.config.dependency import get_db

app = FastAPI(title="ImadbAPI", version=0.1,
              description="Imunnoaging Database API - Analysis endpoints and data access")


@app.post("/heatmap")
async def heatmap(file: UploadFile = File(...), width: int = 10, height: int = 10, palette: Palette = Palette.VIRIDIS):
    plot_service.clustermap_plot(file.file, width, height, palette)
    return FileResponse("heatmap.png", media_type="image/png")


@app.get("/buscar-age-groups", response_model=List[AgeGroup])
def buscar_age_groups(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    age_groups = get_age_groups(db=db, skip=skip, limit=limit)
    return age_groups


@app.get("/buscar-patient-information-cvd", response_model=List[PatientInformationCvd])
def buscar_patient_information_cvd(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    patient_information_cvd = get_patient_information_cvd(db=db, skip=skip, limit=limit)
    return patient_information_cvd


@app.get("/buscar-nutricional-data", response_model=List[NutricionalData])
def buscar_nutricional_data(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    nutricional_data = get_nutricional_data(db=db, skip=skip, limit=limit)
    return nutricional_data


@app.get("/buscar-frequency-food-consumption", response_model=List[FrequencyFoodConsumption])
def buscar_frequency_food_consumption(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    frequency_food_consumption = get_frequency_food_consumption(db=db, skip=skip, limit=limit)
    return frequency_food_consumption


@app.get("/buscar-food-consumption", response_model=List[FoodConsumption])
def buscar_food_consumption(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    food_consumption = get_food_consumption(db=db, skip=skip, limit=limit)
    return food_consumption


@app.get("/buscar-cytokines-covid", response_model=List[CytokinesCovid])
def buscar_cytokines_covid(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cytokines_covid = get_cytokines_covid(db=db, skip=skip, limit=limit)
    return cytokines_covid
