import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

df = pd.read_csv("imdb_top_1000.csv")

dir_counts = df["Director"].value_counts()
dirs_3plus = dir_counts[dir_counts >= 3].index

df_filtered = df[df["Director"].isin(dirs_3plus)]
best_dirs = (df_filtered.groupby("Director")["IMDB_Rating"]
                        .mean()
                        .sort_values(ascending=True)
                        .tail(10))

plt.figure(figsize=(10, 6))
plt.barh(best_dirs.index, best_dirs.values, color="darkgreen",
         edgecolor="white")
plt.title("Top 10 reditelja po prosječnom ratingu (min. 3 filma)")
plt.xlabel("Prosječni IMDB Rating")
plt.xlim(left=7.5)
plt.tight_layout()
plt.show()