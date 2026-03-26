#Skripta koja pronalazi najbolje ocjenjene filmove
#i ispisuje njihovo ime i release date

import pandas as pd

df=pd.read_csv("imdb_top_1000.csv")

df["IMDB_Rating"]=pd.to_numeric(df["IMDB_Rating"],errors="coerce")
df=df.dropna(subset=["IMDB_Rating"])

best_movie=df.loc[df["IMDB_Rating"].idxmax()]

print("Najbolje ocijenjen film je:")
print("Ime:",best_movie["Series_Title"])
print("Release date:",best_movie["Released_Year"])
print("Ocjena:",best_movie["IMDB_Rating"])