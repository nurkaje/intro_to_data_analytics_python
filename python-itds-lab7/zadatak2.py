import pandas as pd

df = pd.read_csv("network_edges.csv")

# 1. Učitavanje i provjera
edges = pd.read_csv("network_edges.csv")
print(edges.isnull().sum())         # ring_id: 3000 nedostaje

# 2. Uklanjanje redova bez ring_id
edges_clean = edges.dropna(subset=["ring_id"])
print(edges_clean.shape)            # (4411, 6)

# 3. Distribucija tipova veza
print(edges_clean["shared_type"].value_counts())

# 4. Bonus: top 5 fraud prstena
print(edges_clean["ring_id"].value_counts().head(5))