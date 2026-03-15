import pandas as pd
import plotly.graph_objects as go
# Load dataset
df = pd.read_csv("ufo_sightings.csv", low_memory=False)
# Clean coordinates
df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
df = df.dropna(subset=["latitude", "longitude"])
# Optional: speed improvement
df = df.sample(15000)
fig = go.Figure()
fig.add_trace(go.Scattergeo(
    lon=df["longitude"],
    lat=df["latitude"],
    text=df["city"],
    mode="markers",
    marker=dict(
        size=4,
        color="cyan",
        opacity=0.7
   )
))

fig.update_layout(
    title="Global UFO Signal Activity",
    template="plotly_dark",
    geo=dict(
        projection_type="orthographic",
        showland=True,
        landcolor="rgb(30,30,30)",
        showcountries=True,
        showocean=True,
        oceancolor="rgb(10,10,30)",
        showlakes=True,
        lakecolor="rgb(10,10,30)",
        bgcolor="black"
    )
)
fig.show()