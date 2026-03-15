import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("ufo_sightings.csv",low_memory=False)

df=df.dropna(subset=["city"])
df["city"]=df["city"].astype(str).str.strip().str.lower()

top_10_cities=df["city"].value_counts().head(10)

print("Top 10 gradova s najvecim brojem prijavljenih viđenja NLO-a:\n")
for city,count in top_10_cities.items():
    print(f"{city.title()}: {count}")

plt.figure(figsize=(12,6))
top_10_cities.sort_values().plot(kind="barh")
plt.title("Top 10 gradova s najvecim brojem viđenja NLO-a")
plt.xlabel("Broj viđenja")
plt.ylabel("Grad")
plt.grid(axis="x",linestyle="--",alpha=0.7)
plt.tight_layout()
plt.show()