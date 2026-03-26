#Skripta koja pronalazi redatelje koji imaju najvise filmova u top 1000
import pandas as pd

df=pd.read_csv("imdb_top_1000.csv")
df=df.dropna(subset=["Director"])

broj_filmova=df["Director"].value_counts()

print("Redatelji sa najvise filmova u top 1000:\n")
print(broj_filmova.head(10))