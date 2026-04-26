import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

df = pd.read_csv("imdb_top_1000.csv")
df["PrviZanr"] = df["Genre"].str.split(",").str[0].str.strip()

top5_zanrovi = df["PrviZanr"].value_counts().head(5).index
df_top5 = df[df["PrviZanr"].isin(top5_zanrovi)]
num_cols = ["IMDB_Rating", "Meta_score", "No_of_Votes", "Runtime"]


sns.pairplot(df[num_cols + ["PrviZanr"]].dropna(),
             hue="PrviZanr", palette="Set2",
             plot_kws={"alpha": 0.5, "s": 20})
plt.suptitle("Pairplot — IMDB Top 1000", y=1.02)
plt.show()
