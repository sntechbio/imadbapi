from app.models.all_models import AgeGroup, PatientInformationCvd
from sqlalchemy.orm import Session


def get_age_groups(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AgeGroup).offset(skip).limit(limit).all()


def get_patient_information_cvd(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PatientInformationCvd).offset(skip).limit(limit).all()
