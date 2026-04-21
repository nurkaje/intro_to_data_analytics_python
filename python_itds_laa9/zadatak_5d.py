import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

df = pd.read_csv("imdb_top_1000.csv")

img = np.asarray(Image.open("python.jpg"))
gray = img.mean(axis=2)

cmaps = ["gray", "viridis", "hot", "cool", "nipy_spectral", "terrain"]

fig, axes = plt.subplots(2, 3, figsize=(15, 9))

for ax, cmap_name in zip(axes.ravel(), cmaps):
    ax.imshow(gray, cmap=cmap_name)
    ax.set_title(f'cmap="{cmap_name}"', fontsize=12)
    ax.axis("off")

plt.suptitle("python.jpg — 6 različitih colormap-a", fontsize=16, y=0.98)
plt.tight_layout()
plt.show()