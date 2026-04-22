import pandas as pd
pieces = []
for year in range(1880, 2011):
  path = f"datasets/yob{year}.txt"
  frame = pd.read_csv(path, names=["name", "sex", "births"])
# Add a column for the year
  frame["year"] = year
  pieces.append(frame)
# Concatenate everything into a single DataFrame
names = pd.concat(pieces, ignore_index=True)
print (names.dtypes)
print(names)
