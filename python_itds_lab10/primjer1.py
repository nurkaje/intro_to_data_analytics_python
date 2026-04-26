import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

sns.set_theme(style="whitegrid", palette="muted")

df = pd.read_csv("imdb_top_1000.csv")

sns.scatterplot(data=df, x="IMDB_Rating", y="Meta_score", alpha=0.5)
plt.title("IMDB Rating vs Metascore")
plt.show()
