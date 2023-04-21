import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import io


def clustermap_plot(file, width, height, palette):
    sns_palette = sns.color_palette(palette.value)
    df = pd.read_csv(file)

    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_str = csv_buffer.getvalue()
    df = pd.read_csv(io.StringIO(csv_str))
    corr_matrix = df.corr()

    plt.figure(figsize=(width, height))
    cluster_map = sns.clustermap(corr_matrix, cmap=sns_palette, annot=False, vmax=1, vmin=-1, linewidth=.4)

    png_buffer = io.BytesIO()
    cluster_map.figure.savefig(png_buffer, format='png')
    png_bytes = png_buffer.getvalue()

    plt.clf()

    return png_bytes
