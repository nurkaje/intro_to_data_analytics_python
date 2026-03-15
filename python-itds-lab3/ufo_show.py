import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("ufo_sightings.csv",low_memory=False)

df["datetime"]=pd.to_datetime(df["datetime"],errors="coerce")
df=df.dropna(subset=["datetime"])

df["year"]=df["datetime"].dt.year
df["month"]=df["datetime"].dt.month
df["hour"]=df["datetime"].dt.hour

if "country" in df.columns:
    df["country"]=df["country"].astype(str).str.strip().str.upper()

if "shape" in df.columns:
    df["shape"]=df["shape"].astype(str).str.strip().str.lower()

df.to_csv("ufo_cleaned.csv",index=False)

year_counts=df["year"].value_counts().sort_index()

plt.figure(figsize=(12,6))
year_counts.plot(kind="line",marker="o")
plt.title("UFO Sightings per Year")
plt.xlabel("Year")
plt.ylabel("Number of Sightings")
plt.grid(True)
plt.tight_layout()
plt.show()

if "country" in df.columns:
    country_counts=df["country"].value_counts().head(15)

    plt.figure(figsize=(12,6))
    country_counts.plot(kind="bar")
    plt.title("UFO Sightings by Country")
    plt.xlabel("Country")
    plt.ylabel("Number of Sightings")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if "shape" in df.columns:
    shape_counts=df["shape"].value_counts().head(10)

    plt.figure(figsize=(12,6))
    shape_counts.plot(kind="bar")
    plt.title("Most Common UFO Sightings")
    plt.xlabel("Shape")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

print("Broj redova nakon ciscenja:",len(df))
print("Godine izdvojene uspjesno.")
print("Mjeseci izdvojeni uspjesno.")
print("Sati izdvojeni uspjesno.")

print("\nTop 10 godina sa najvise vidjenja:")
print(df["year"].value_counts().head(10))

if "country" in df.columns:
    print("\nTop 10 drzava sa najvise vidjenja:")
    print(df["country"].value_counts().head(10))

if "shape" in df.columns:
    print("\nTop 10 najcescih vidjenja:")
    print(df["shape"].value_counts().head(10))