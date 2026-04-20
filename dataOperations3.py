import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
fig, ax = plt.subplots()
data = pd.read_csv("spx.csv", index_col=0, parse_dates=True)
spx = data["SPX"]
spx.plot(ax=ax, color="black")
crisis_data = [
(datetime(2007, 10, 11), "Peak of bull market"),
(datetime(2008, 3, 12), "Bear Stearns Fails"),
(datetime(2008, 9, 15), "Lehman Bankruptcy")
]
or date, label in crisis_data:
  ax.annotate(label, xy=(date, spx.asof(date) + 75),
  xytext=(date, spx.asof(date) + 225),
  arrowprops=dict(facecolor="red", headwidth=8, width=4, headlength=8),
  horizontalalignment="left", verticalalignment="top")
# Zoom in on 2007-2010
ax.set_xlim(["1/1/2007", "1/1/2011"])
ax.set_ylim([600, 1800])
ax.set_title("Important dates in the 2008-2009 financial crisis")
