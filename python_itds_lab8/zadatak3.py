import pandas as pd

telefoni = pd.read_csv("telefonski_zapisi.csv")
osumnjiceni = pd.read_csv("osumnjiceni.csv")

# 1. Merge za POZIVATELJA
sa_imenima = telefoni.merge(
    osumnjiceni[["ime_prezime", "telefon"]],
    left_on="telefon_pozivatelja",
    right_on="telefon", how="left")
sa_imenima = sa_imenima.rename(columns={"ime_prezime": "pozivatelj"})

# 2. Merge za PRIMAOCA (dvostruki merge!)
sa_imenima = sa_imenima.merge(
    osumnjiceni[["ime_prezime", "telefon"]],
    left_on="telefon_primaoca",
    right_on="telefon", how="left",
    suffixes=("", "_primalac"))
sa_imenima = sa_imenima.rename(columns={"ime_prezime": "primalac"})

# 3. Emirovi pozivi, 15. mart, nakon 20:00
emir_kasno = sa_imenima[
    (sa_imenima["pozivatelj"] == "Emir Begović") &
    (sa_imenima["datum"] == "2026-03-15") &
    (sa_imenima["vrijeme"] > "20:00")]
print(emir_kasno[["vrijeme", "telefon_primaoca", "primalac",
                   "trajanje_sekundi"]].sort_values("vrijeme")
      .to_string(index=False))
# NaN u koloni "primalac" = broj ne pripada nijednom osumnjičenom!