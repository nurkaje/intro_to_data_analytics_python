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
df["Runtime"] = df["Runtime"].str.replace(" min", "").astype(float)

korelacija = df[num_cols].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(korelacija, annot=True, cmap="coolwarm",
            center=0, fmt=".2f", linewidths=1)
plt.title("Korelacijska matrica — IMDB dataset")
plt.tight_layout()
plt.show()