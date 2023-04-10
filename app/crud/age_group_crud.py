from app.models.age_group import AgeGroup
from sqlalchemy.orm import Session


def get_age_groups(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AgeGroup).offset(skip).limit(limit).all()
