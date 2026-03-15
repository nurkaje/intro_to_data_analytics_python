import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt

df=pd.read_csv('ufo_sightings.csv')

shape_counts=df['shape'].value_counts().head(10)

shape_counts.plot(kind="bar")
plt.title("UFO sightings")
plt.xlabel("Shape")
plt.ylabel("Count")

plt.show()