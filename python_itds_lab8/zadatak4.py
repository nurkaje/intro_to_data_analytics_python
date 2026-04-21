import pandas as pd

finansije = pd.read_csv("finansijski_zapisi.csv")
finansije["iznos_KM"] = finansije["iznos_KM"].astype(float)

# Bilans po osobi
bilans = finansije.groupby("ime_prezime")["iznos_KM"].sum().sort_values()
print(bilans)

# Zapisi o osiguranju
osiguranje = finansije[finansije["kategorija"] == "osiguranje"]
print(osiguranje[["ime_prezime", "iznos_KM", "opis"]].to_string(index=False))

# Neuspjele transakcije (iznos = 0)
neuspjele = finansije[finansije["iznos_KM"] == 0]
print(neuspjele[["ime_prezime", "datum", "opis"]].to_string(index=False))