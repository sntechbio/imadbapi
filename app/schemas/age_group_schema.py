from pydantic import BaseModel
from typing import Optional


class AgeGroup(BaseModel):
    id: Optional[int]
    group: Optional[str]

    class Config:
        orm_mode = True
