from fastapi import FastAPI
from app.models.Palettes import Palette
from app.models.clinical_classification import ClinicalClassification
from app.service.get_cytokines_by_classification import get_cytokines_by_classification
from fastapi import File, UploadFile
from app.service import plot_service
from fastapi.responses import FileResponse

app = FastAPI(title="ImadbAPI", version=0.1,
              description="Imunnoaging Database API - Analysis endpoints and data access")


@app.get("/buscar-citocinas-por-grupo")
def search_cytokines_by_classification(classification: ClinicalClassification):
    data = get_cytokines_by_classification(classification)
    return data


@app.post("/heatmap")
async def heatmap(file: UploadFile = File(...), width: int = 10, height: int = 10, palette: Palette = Palette.VIRIDIS):
    plot_service.clustermap_plot(file.file, width, height, palette)
    return FileResponse("heatmap.png", media_type="image/png")
