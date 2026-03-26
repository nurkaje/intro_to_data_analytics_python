import pandas as pd

df=pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

stressed=df[df["Stress Level"]>7]
not_stressed=df[df["Stress Level"]<=7]

avg_sleep_stressed=stressed["Sleep Duration"].mean()
avg_sleep_not_stressed=not_stressed["Sleep Duration"].mean()

median_sleep_stressed=stressed["Sleep Duration"].median()
median_sleep_not_stressed=not_stressed["Sleep Duration"].median()

correlation=df["Stress Level"].corr(df["Sleep Duration"])

print("=== ANALIZA STRESA I SPAVANJA ===")
print(f"Broj osoba sa stress level >7: {len(stressed)}")
print(f"Broj ostalih osoba: {len(not_stressed)}")

print("\n=== PROSJEČNO SPAVANJE ===")
print(f"Prosječno spavanje kod osoba sa stress level >7: {avg_sleep_stressed:.2f} sati")
print(f"Prosječno spavanje kod osoba sa stress level <=7: {avg_sleep_not_stressed:.2f} sati")

print("\n=== MEDIJALNO SPAVANJE ===")
print(f"Medijalno spavanje kod osoba sa stress level >7: {median_sleep_stressed:.2f} sati")
print(f"Medijalno spavanje kod osoba sa stress level <=7: {median_sleep_not_stressed:.2f} sati")

print("\n=== KORELACIJA ===")
print(f"Korelacija između Stress Level i Sleep Duration: {correlation:.3f}")

print("\n=== ZAKLJUČAK ===")
if avg_sleep_stressed<avg_sleep_not_stressed:
    print("Da, osobe sa većim stresom uglavnom manje spavaju.")
else:
    print("Ne, iz ovih podataka se ne vidi da osobe sa većim stresom manje spavaju.")

if correlation<0:
    print("Negativna korelacija znači: kako stres raste, trajanje sna opada.")
elif correlation>0:
    print("Pozitivna korelacija znači: kako stres raste, trajanje sna raste.")
else:
    print("Nema jasne linearne povezanosti između stresa i trajanja sna.")