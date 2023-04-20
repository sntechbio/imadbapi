from fastapi import FastAPI, Response
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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

    # csv em memória
    data_frame_cytokines_filter_by_classification = pd.json_normalize(data_all_informations_cytokines)
    csv_buffer = io.StringIO()
    data_frame_cytokines_filter_by_classification.to_csv(csv_buffer, index=False)
    csv_str = csv_buffer.getvalue()

    csv_final = pd.read_csv(io.StringIO(csv_str))

    heatmap_graph = sns.heatmap(csv_final.corr(), annot=False, vmax=1, vmin=-1)

    # Salva o plot em memória como um PNG em memória
    png_buffer = io.BytesIO()
    heatmap_graph.figure.savefig(png_buffer, format='png')
    png_bytes = png_buffer.getvalue()
    plt.clf()
    return Response(content=png_bytes, media_type="image/png")


@app.post("/heatmap")
async def heatmap(file: UploadFile = File(...), width: int = 10, height: int = 10, palette: Palette = Palette.VIRIDIS):
    plot_service.clustermap_plot(file.file, width, height, palette)
    return FileResponse("heatmap.png", media_type="image/png")
