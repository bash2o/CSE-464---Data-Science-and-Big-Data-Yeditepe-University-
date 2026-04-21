import pandas as pd
names1880 = pd.read_csv("babynames/yob1880.txt",names=["name", "sex", "births"])
names1880.dtypes
