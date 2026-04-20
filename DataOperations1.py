import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
data = pd.read_csv("spx.csv", index_col=0, parse_dates=True)

data.dtypes

Then type:
data.describe()
