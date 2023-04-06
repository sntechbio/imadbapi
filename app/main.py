from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from app.models.Palettes import Palette
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import io
import base64
from enum import Enum
import scipy
import numpy as np

app = FastAPI(title="ImadbAPI", version=0.1,
              description="Imunnoaging Database API - Analysis endpoints and data access")


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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
