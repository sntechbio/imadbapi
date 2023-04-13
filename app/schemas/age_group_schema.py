from pydantic import BaseModel
from typing import Optional


class AgeGroup(BaseModel):
    id: Optional[int]
    group: Optional[str]

    class Config:
        orm_mode = True


class PatientInformationCvd(BaseModel):
    id: int
    age: Optional[int]
    sex: Optional[str]
    profession: Optional[str]
    schooling: Optional[str]
    address: Optional[str]
    income: Optional[str]
    marital_status: Optional[str]
    imc: Optional[float]
    group: Optional[str]
    vaccination: Optional[str]

    class Config:
        orm_mode = True
