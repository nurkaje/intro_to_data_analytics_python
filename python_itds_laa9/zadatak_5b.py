import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

df = pd.read_csv("imdb_top_1000.csv")

df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors="coerce")
df["Decenija"] = (df["Released_Year"] // 10) * 10
po_deceniji = df.groupby("Decenija").size()

plt.figure(figsize=(10, 5))
bars = plt.bar(po_deceniji.index.astype(int), po_deceniji.values,
               width=8, color="steelblue", edgecolor="white")

for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
             str(int(bar.get_height())), ha="center", fontsize=9)

plt.title("Broj filmova u IMDB Top 1000 po deceniji", fontsize=14)
plt.xlabel("Decenija")
plt.ylabel("Broj filmova")
plt.tight_layout()
plt.show()