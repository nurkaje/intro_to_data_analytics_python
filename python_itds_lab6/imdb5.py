#Koji je najnoviji film

import pandas as pd

df=pd.read_csv("imdb_top_1000.csv")
df["Released_Year"]=pd.to_numeric(df["Released_Year"],errors="coerce")
df=df.dropna(subset=["Released_Year"])

najnoviji=df.loc[df["Released_Year"].idxmax()]

print("Najnoviji film je:")
print("Ime:",najnoviji["Series_Title"])
print("Godina:",int(najnoviji["Released_Year"]))