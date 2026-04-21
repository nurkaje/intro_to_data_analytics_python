import pandas as pd

kartice = pd.read_csv("pristupne_kartice.csv")
osumnjiceni = pd.read_csv("osumnjiceni.csv")

# Filtriraj i merge
tech_hub = kartice[(kartice["zgrada"] == "Tech Hub") &
                    (kartice["datum"] == "2026-03-15")]
spojeno = tech_hub.merge(osumnjiceni, on="ime_prezime")
print(spojeno[["ime_prezime", "vrijeme_ulaza", "vrijeme_izlaza",
                "veza_sa_zrtvom"]].to_string(index=False))

# Ko je bio u zgradi tokom ubistva (19:30-20:30)?
# Uslov: izašli NAKON 19:30 ili NISU izašli (NaN)
tokom = spojeno[
    (spojeno["vrijeme_izlaza"] > "19:30") |
    (spojeno["vrijeme_izlaza"].isna())
]
print(tokom[["ime_prezime", "vrijeme_ulaza",
              "vrijeme_izlaza"]].to_string(index=False))