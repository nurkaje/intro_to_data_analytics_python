import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Učitavanje dataset-a
df = pd.read_csv("imdb_top_1000.csv")

# Izdvajanje prvog žanra
df["PrviZanr"] = df["Genre"].str.split(",").str[0].str.strip()

# Pretvaranje godine u broj
df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors="coerce")

# Kreiranje kolone Decenija
df["Decenija"] = (df["Released_Year"] // 10) * 10

# Uzimanje top 5 žanrova
top5_zanrovi = df["PrviZanr"].value_counts().head(5).index

# Filtriranje samo top 5 žanrova
df_top5 = df[df["PrviZanr"].isin(top5_zanrovi)].copy()

# Pivot tabela: prosječna IMDB ocjena po deceniji i žanru
pivot = pd.pivot_table(
    df_top5,
    values="IMDB_Rating",
    index="Decenija",
    columns="PrviZanr",
    aggfunc="mean"
)

# Prikaz samo od 1950. godine
pivot = pivot.loc[pivot.index >= 1950]

# Crtanje heatmap grafa
plt.figure(figsize=(10, 8))
sns.heatmap(
    pivot,
    annot=True,
    cmap="YlOrRd",
    fmt=".1f",
    linewidths=0.5
)

plt.title("Prosječna IMDB ocjena — Decenija vs Žanr")
plt.xlabel("Žanr")
plt.ylabel("Decenija")
plt.tight_layout()
plt.show()