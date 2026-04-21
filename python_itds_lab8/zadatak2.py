import pandas as pd

svjedoci = pd.read_csv("izjave_svjedoka.csv")

# Izjave o Emiru
emir_izjave = svjedoci[svjedoci["spominje_osumnjicenog"] == "Emir Begović"]
print(emir_izjave[["izjava_id", "vrijeme", "svjedok", "opis"]].to_string(index=False))

# Izjave o Dinu
dino_izjave = svjedoci[svjedoci["svjedok"] == "Dino Delić"]
print(dino_izjave[["vrijeme", "lokacija", "opis"]].to_string(index=False))

# Izjave bez imenovanog osumnjičenog
nepoznati = svjedoci[svjedoci["spominje_osumnjicenog"].isna() |
                      (svjedoci["spominje_osumnjicenog"] == "")]
print(nepoznati[["izjava_id", "vrijeme", "opis"]].to_string(index=False))

# Ko odgovara opisu "visok, tamna kosa"?
osumnjiceni = pd.read_csv("osumnjiceni.csv")
print(osumnjiceni[(osumnjiceni["visina_cm"] > 180) &
                   (osumnjiceni["boja_kose"] == "crna")]
      [["ime_prezime", "visina_cm", "boja_kose"]].to_string(index=False))