from app.models.all_models import AgeGroup, PatientInformationCvd, NutricionalData, FrequencyFoodConsumption, \
    FoodConsumption, CytokinesCovid, Ethnicity, BloodCountData

from sqlalchemy.orm import Session, aliased, joinedload
from sqlalchemy import cast, String, select


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


def get_ethnicity(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Ethnicity).offset(skip).limit(limit).all()


def get_blood_count_data(db: Session, skip: int = 0, limit: int = 100):
    return db.query(BloodCountData).offset(skip).limit(limit).all()


def get_cytokines_by_group_covid(db: Session, group: str):
    query = select([CytokinesCovid.patient_information_id, PatientInformationCvd.id]) \
        .select_from(
        CytokinesCovid.join(PatientInformationCvd, CytokinesCovid.patient_information_id == PatientInformationCvd.id)) \
        .where(cast(PatientInformationCvd.group, String) == group) \
        .columns(CytokinesCovid.patient_information_id, PatientInformationCvd.id)

    return query.all()


def get_patient_information_by_group(db: Session, group: str):
    query = db.query(PatientInformationCvd).filter(cast(PatientInformationCvd.group, String) == group)
    return query.all()
