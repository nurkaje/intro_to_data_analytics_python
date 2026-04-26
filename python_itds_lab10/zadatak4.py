import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Učitavanje dataset-a
df = pd.read_csv("imdb_top_1000.csv")

# Izdvajanje prvog žanra
df["PrviZanr"] = df["Genre"].str.split(",").str[0].str.strip()

# Pretvaranje Runtime kolone iz npr. "142 min" u broj
df["Runtime_num"] = df["Runtime"].str.replace(" min", "", regex=False).astype(float)

# Pretvaranje godine u broj
df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors="coerce")

# Kreiranje kolone Decenija
df["Decenija"] = (df["Released_Year"] // 10) * 10

# Uzimanje top 5 žanrova
top5_zanrovi = df["PrviZanr"].value_counts().head(5).index

# Filtriranje samo top 5 žanrova
df_top5 = df[df["PrviZanr"].isin(top5_zanrovi)].copy()

# Kreiranje dashboarda 2x2
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Graf 1: Distribucija IMDB ocjena
sns.histplot(
    data=df,
    x="IMDB_Rating",
    bins=20,
    kde=True,
    ax=axes[0, 0],
    color="steelblue"
)
axes[0, 0].set_title("Distribucija IMDB ocjena")

# Graf 2: Runtime po žanru
sns.boxplot(
    data=df_top5,
    x="PrviZanr",
    y="Runtime_num",
    ax=axes[0, 1],
    palette="Set2"
)
axes[0, 1].set_title("Runtime po žanru")
axes[0, 1].tick_params(axis="x", rotation=30)

# Graf 3: Rating vs broj glasova
sns.scatterplot(
    data=df_top5,
    x="IMDB_Rating",
    y="No_of_Votes",
    hue="PrviZanr",
    alpha=0.5,
    ax=axes[1, 0]
)
axes[1, 0].set_title("Rating vs Glasovi")

# Graf 4: Prosječna ocjena po deceniji
prosjek = df.groupby("Decenija")["IMDB_Rating"].mean().reset_index()
prosjek = prosjek[prosjek["Decenija"] >= 1960]

sns.barplot(
    data=prosjek,
    x="Decenija",
    y="IMDB_Rating",
    ax=axes[1, 1],
    color="coral"
)
axes[1, 1].set_title("Prosjek po deceniji")
axes[1, 1].tick_params(axis="x", rotation=45)

plt.suptitle("IMDB Top 1000 — Seaborn Dashboard", fontsize=16)
plt.tight_layout()
plt.show()