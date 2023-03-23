from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy


app = FastAPI()


@app.post("/heatmap")
async def heatmap(file: UploadFile = File(...), width: int = 10, height: int = 10):
    df = pd.read_csv(file.file)
    corr_matrix = df.corr()
    plt.figure(figsize=(width,height))
    sns.heatmap(corr_matrix, annot=False, cmap="viridis", vmax=1, vmin=-1)
    sns.clustermap(corr_matrix, cmap="viridis", annot=False)
    plt.savefig("heatmap.png")
    return FileResponse("heatmap.png", media_type="image/png")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
