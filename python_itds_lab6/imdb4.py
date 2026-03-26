#Program koji poredi koliko ima drama i komedija filmova,
#kao i njihovu prosjecnu ocjenu
import pandas as pd

df=pd.read_csv("imdb_top_1000.csv")
df["IMDB_Rating"]=pd.to_numeric(df["IMDB_Rating"],errors="coerce")
df=df.dropna(subset=["Genre","IMDB_Rating"])

drame=df[df["Genre"].str.contains("Drama",case=False,na=False)]
komedije=df[df["Genre"].str.contains("Comedy",case=False,na=False)]
broj_drama=len(drame)
broj_komedija=len(komedije)
prosjek_drama=drame["IMDB_Rating"].mean()
prosjek_komedija=komedije["IMDB_Rating"].mean()

print("Drama:")
print("Broj filmova:",broj_drama)
print("Prosjecna ocjena:",round(prosjek_drama,2))

print("\nComedy:")
print("Broj filmova:",broj_komedija)
print("Prosjecna ocjena:",round(prosjek_komedija,2))