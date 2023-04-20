from fastapi import FastAPI
import pandas as pd
import io
from app.models.Palettes import Palette
from app.models.clinical_classification import ClinicalClassification
from app.service.handle_data_access import get_cytokines_by_classification, remover_chaves
from fastapi import File, UploadFile
from app.service import plot_service
from fastapi.responses import FileResponse

app = FastAPI(title="ImadbAPI", version=0.1,
              description="Imunnoaging Database API - Analysis endpoints and data access")


@app.get("/buscar-citocinas-por-grupo")
def search_cytokines_by_classification(classification: ClinicalClassification):
    data_all_informations_cytokines = get_cytokines_by_classification(classification)
    data_all_informations_cytokines = remover_chaves(data_all_informations_cytokines)

    data_frame_cytokines_filter_by_classification = pd.json_normalize(data_all_informations_cytokines)
    csv_buffer = io.StringIO()
    data_frame_cytokines_filter_by_classification.to_csv(csv_buffer, index=False)
    csv_str = csv_buffer.getvalue()

    csv_final = pd.read_csv(io.StringIO(csv_str))

    return data_all_informations_cytokines


@app.post("/heatmap")
async def heatmap(file: UploadFile = File(...), width: int = 10, height: int = 10, palette: Palette = Palette.VIRIDIS):
    plot_service.clustermap_plot(file.file, width, height, palette)
    return FileResponse("heatmap.png", media_type="image/png")
