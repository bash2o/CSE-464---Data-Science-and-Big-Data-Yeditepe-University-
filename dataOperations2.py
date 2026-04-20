import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

fig, ax = plt.subplots()
data = pd.read_csv("spx.csv", index_col=0, parse_dates=True)
spx = data["SPX"]
spx.plot(ax=ax, color="black")
ax.set_title("US Stock Market SPX Index from 1990 to 2011")
