#Skripta koja poredi koja decenija ima najvise filmova i koji je broj filmova
import pandas as pd

df=pd.read_csv("imdb_top_1000.csv")
df["Released_Year"]=pd.to_numeric(df["Released_Year"],errors="coerce")
df=df.dropna(subset=["Released_Year"])
df["Decenija"]=(df["Released_Year"]//10)*10

broj_po_deceniji=df["Decenija"].value_counts().sort_index()

print("Broj filmova po decenijama:\n")
for decenija,broj in broj_po_deceniji.items():
    print(f"{int(decenija)}-e: {broj} filmova")

najvise_decenija=broj_po_deceniji.idxmax()
najvise_broj=broj_po_deceniji.max()

print("\nDecenija sa najvise filmova je:")
print(f"{int(najvise_decenija)}-e")
print(f"Broj filmova: {najvise_broj}")