from fastapi import FastAPI, Response, Query
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


@app.get("/clustermap-citocinas-por-grupo", description="Returns clustermap plots of Imadb cytokines by clinical classification group.")
async def clustermap_cytokines_by_classification(clinical_classification: ClinicalClassification, color: Palette = Palette.RED_YELLOW, width: int = 10, height: int = 10):
    data_all_informations_cytokines = get_cytokines_by_classification(clinical_classification)
    data_all_informations_cytokines = remover_chaves(data_all_informations_cytokines)

    # csv em memória
    data_frame_cytokines_filter_by_classification = pd.json_normalize(data_all_informations_cytokines)
    csv_buffer = io.StringIO()
    data_frame_cytokines_filter_by_classification.to_csv(csv_buffer, index=False)
    csv_str = csv_buffer.getvalue()
    csv_final = pd.read_csv(io.StringIO(csv_str))

    # Plot em memória
    plt.figure(figsize=(width, height))
    heatmap_graph = sns.clustermap(csv_final.corr(), annot=False, cmap=color, vmax=1, vmin=-1, linewidth=.4)

    # Salva o plot em memória como um PNG em memória
    png_buffer = io.BytesIO()
    heatmap_graph.figure.savefig(png_buffer, format='png')
    png_bytes = png_buffer.getvalue()
    plt.clf()

    return Response(content=png_bytes, media_type="image/png")


@app.post("/heatmap")
async def heatmap(file: UploadFile = File(...), width: int = 10, height: int = 10, palette: Palette = Palette.RED_YELLOW):
    png_plotin_bytes = plot_service.clustermap_plot(file.file, width, height, palette)
    return Response(content=png_plotin_bytes, media_type="image/png")
