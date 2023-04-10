import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from fastapi import Depends, FastAPI
from typing import List
from fastapi import File, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.crud.age_group_crud import get_age_groups
from app.schemas.age_group_schema import AgeGroup
from app.models import age_group
from app.models.Palettes import Palette

app = FastAPI(title="ImadbAPI", version=0.1,
              description="Imunnoaging Database API - Analysis endpoints and data access")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/heatmap")
async def heatmap(file: UploadFile = File(...), width: int = 10, height: int = 10, palette: Palette = Palette.VIRIDIS):
    sns_palette = sns.color_palette(palette.value)

    df = pd.read_csv(file.file)
    corr_matrix = df.corr()

    plt.figure(figsize=(width, height))
    sns.heatmap(corr_matrix, annot=False, cmap=palette, vmax=1, vmin=-1)
    sns.clustermap(corr_matrix, cmap=sns_palette, annot=False, linewidth=.6)

    plt.savefig("heatmap.png")
    return FileResponse("heatmap.png", media_type="image/png")


@app.get("/buscar-age-groups", response_model=List[AgeGroup])
def buscar_age_groups(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    age_groups = get_age_groups(db=db, skip=skip, limit=limit)
    return age_groups


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
