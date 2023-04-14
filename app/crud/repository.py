from app.models.all_models import AgeGroup, PatientInformationCvd, NutricionalData, FrequencyFoodConsumption, \
    FoodConsumption, CytokinesCovid
from sqlalchemy.orm import Session


def get_age_groups(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AgeGroup).offset(skip).limit(limit).all()


def get_patient_information_cvd(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PatientInformationCvd).offset(skip).limit(limit).all()


def get_nutricional_data(db: Session, skip: int = 0, limit: int = 100):
    return db.query(NutricionalData).offset(skip).limit(limit).all()


def get_frequency_food_consumption(db: Session, skip: int = 0, limit: int = 100):
    return db.query(FrequencyFoodConsumption).offset(skip).limit(limit).all()


def get_food_consumption(db: Session, skip: int = 0, limit: int = 100):
    return db.query(FoodConsumption).offset(skip).limit(limit).all()

def get_cytokines_covid(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CytokinesCovid).offset(skip).limit(limit).all()
