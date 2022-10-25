import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
from pandas import read_csv
import numpy as np


# Display matrix
dfClasses = read_csv("./xlabels.csv", header=None)
xlabels = dfClasses.values.ravel()	

resultMatrix = read_csv("./data.csv", header=None)	
dfData=(resultMatrix)

ylabels = read_csv("./ylabels.csv", header=None)
ylabels = ylabels.values.ravel()	

f, ax = plt.subplots(figsize=(20,5))
#ax = sn.heatmap(dfData, annot=True, fmt="d", cmap=sn.color_palette("Blues"),  cbar=False)
#palette = sn.color_palette("GnBu_d",30)
palette = sn.color_palette("Blues",30)
#palette.reverse()
sn.set(font_scale = 1)
ax = sn.heatmap(dfData, annot=True, annot_kws={"size": 10}, fmt=".2f", cmap=palette,    
#cbar_kws={'label': 'Accuracy 'orientation': 'horizontal'},
cbar_kws={'label': 'Accuracy' },
cbar=True, xticklabels=xlabels, yticklabels=ylabels)
ax.tick_params(axis='both', which='major', labelsize=12)
ax.set_xlabel('Lineage', fontsize=12)
ax.set_ylabel("Primer Sequence", fontsize=12)
plt.show()
plt.savefig("test")



