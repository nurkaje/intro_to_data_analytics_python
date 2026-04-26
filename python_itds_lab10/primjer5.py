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

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.boxplot(data=df_top5, x="PrviZanr", y="IMDB_Rating",
            ax=axes[0], palette="Set2")
axes[0].set_title("Boxplot — Ocjene po žanru")

sns.violinplot(data=df_top5, x="PrviZanr", y="IMDB_Rating",
               ax=axes[1], palette="Set2")
axes[1].set_title("Violinplot — Ocjene po žanru")

plt.tight_layout()
plt.show()