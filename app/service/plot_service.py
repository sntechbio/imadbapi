import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def clustermap_plot(file, width, height, palette):
    sns_palette = sns.color_palette(palette.value)
    df = pd.read_csv(file)
    corr_matrix = df.corr()

    plt.figure(figsize=(width, height))
    sns.heatmap(corr_matrix, annot=False, cmap=palette, vmax=1, vmin=-1)
    sns.clustermap(corr_matrix, cmap=sns_palette, annot=False, linewidth=.6)

    plt.savefig("heatmap.png")
