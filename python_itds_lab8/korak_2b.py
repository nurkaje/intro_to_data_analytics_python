import pandas as pd

kartice = pd.read_csv("pristupne_kartice.csv")
osumnjiceni = pd.read_csv("osumnjiceni.csv")

# Ko je NAJČEŠĆE dolazio u Tech Hub te sedmice?
tech_hub_sve = kartice[kartice["zgrada"] == "Tech Hub"]
sve = tech_hub_sve.merge(osumnjiceni, on="ime_prezime")
print(sve.groupby("ime_prezime")["datum"].nunique()
      .sort_values(ascending=False).to_string())

# Koliko ulazaka ima svaki osumnjičeni 15. marta?
print(u_zgradi["ime_prezime"].value_counts().to_string())