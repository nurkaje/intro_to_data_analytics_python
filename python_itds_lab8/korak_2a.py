import pandas as pd

kartice = pd.read_csv("pristupne_kartice.csv")
osumnjiceni = pd.read_csv("osumnjiceni.csv")


# Filtriramo kartice: samo Tech Hub, 15. mart
tech_hub_15 = kartice[(kartice["zgrada"] == "Tech Hub") &
                       (kartice["datum"] == "2026-03-15")]

# MERGE: spajamo s listom osumnjičenih
u_zgradi = tech_hub_15.merge(osumnjiceni, on="ime_prezime")

print(f"Ukupno ulazaka: {len(tech_hub_15)}")
print(f"Od toga osumnjičeni: {len(u_zgradi)}")
print(u_zgradi[["ime_prezime", "vrijeme_ulaza",
                 "vrijeme_izlaza", "veza_sa_zrtvom"]].to_string(index=False))