from sqlalchemy import Column, Integer, String
from app.database import Base


class AgeGroup(Base):
    __tablename__ = "age_group"

    id = Column(Integer, primary_key=True, index=True)
    group = Column(String(60), index=True)
