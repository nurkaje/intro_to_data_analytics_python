import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('ufo_sightings.csv',low_memory=False)

df["datetime"]=pd.to_datetime(df["datetime"],errors="coerce")

df["year"]=df["datetime"].dt.year
year_count=df["year"].value_counts().sort_index()

plt.figure()
year_count.plot()

plt.title("UFO Sightings per Year")
plt.xlabel("Year")
plt.ylabel("Number of sightings")

plt.show()