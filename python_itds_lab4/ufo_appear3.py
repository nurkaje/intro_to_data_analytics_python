#heatmap
import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_csv("ufo_sightings.csv", low_memory=False)
# Clean coordinates
df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
df = df.dropna(subset=["latitude", "longitude"])
# Optional: reduce dataset for faster plotting
df = df.sample(15000)
plt.figure(figsize=(12, 6))
plt.hexbin(
    df["longitude"],
    df["latitude"],
    gridsize=60,
    cmap="inferno"
)
plt.colorbar(label="Sightings density")
plt.title("UFO Sightings Density Heatmap")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()