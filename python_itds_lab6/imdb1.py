#Osnovna skripta

import pandas as pd

df = pd.read_csv('imdb_top_1000.csv')

print(df.head())
print(df.shape)

print(df.info())
print(df.describe())
