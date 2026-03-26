import pandas as pd

df=pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

# Ko najmanje spava
min_sleep=df["Sleep Duration"].min()
najmanje_spava=df[df["Sleep Duration"]==min_sleep]

# Ko najviše spava
max_sleep=df["Sleep Duration"].max()
najvise_spava=df[df["Sleep Duration"]==max_sleep]

# Najveći heart rate
max_hr=df["Heart Rate"].max()
najveci_hr=df[df["Heart Rate"]==max_hr]

# Najniži daily steps
min_steps=df["Daily Steps"].min()
najnizi_steps=df[df["Daily Steps"]==min_steps]

print("=== KO NAJMANJE SPAVA ===")
print(najmanje_spava[["Person ID","Gender","Age","Occupation","Sleep Duration"]])

print("\n=== KO NAJVIŠE SPAVA ===")
print(najvise_spava[["Person ID","Gender","Age","Occupation","Sleep Duration"]])

print("\n=== OSOBA SA NAJVEĆIM HEART RATE ===")
print(najveci_hr[["Person ID","Gender","Age","Occupation","Heart Rate"]])

print("\n=== OSOBA SA NAJNIŽIM DAILY STEPS ===")
print(najnizi_steps[["Person ID","Gender","Age","Occupation","Daily Steps"]])