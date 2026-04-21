import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

df = pd.read_csv("imdb_top_1000.csv")

df["Gross_clean"] = df["Gross"].str.replace(",", "").astype(float)
df["PrviZanr"] = df["Genre"].str.split(",").str[0].str.strip()

zarada_po_zanru = (df.groupby("PrviZanr")["Gross_clean"]
                     .mean()
                     .dropna()
                     .sort_values(ascending=True)
                     .tail(10))

plt.figure(figsize=(10, 6))
plt.barh(zarada_po_zanru.index, zarada_po_zanru.values / 1e6,
         color="goldenrod", edgecolor="white")
plt.title("Prosječna zarada po žanru (IMDB Top 1000)", fontsize=14)
plt.xlabel("Prosječna zarada (milioni $)")
plt.tight_layout()
plt.show()