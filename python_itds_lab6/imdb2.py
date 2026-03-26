#Scatter plot
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("imdb_top_1000.csv")

df["IMDB_Rating"]=pd.to_numeric(df["IMDB_Rating"],errors="coerce")
df["Gross"]=df["Gross"].str.replace(",","",regex=False)
df["Gross"]=pd.to_numeric(df["Gross"],errors="coerce")

df=df.dropna(subset=["IMDB_Rating","Gross"])

plt.figure(figsize=(10,6))
plt.scatter(df["IMDB_Rating"],df["Gross"])
plt.title("Rating vs Zarada")
plt.xlabel("IMDB Rating")
plt.ylabel("Gross")
plt.tight_layout()
plt.show()