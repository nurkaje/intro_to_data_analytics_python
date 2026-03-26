#Koji glumac se pojavljuje u najvise filmova
import pandas as pd

df=pd.read_csv("imdb_top_1000.csv")

glumci=pd.concat([df["Star1"],df["Star2"],df["Star3"],df["Star4"]]).dropna()
broj_pojavljivanja=glumci.value_counts()

for glumac,broj in broj_pojavljivanja.items():
    print(glumac,"-",broj)