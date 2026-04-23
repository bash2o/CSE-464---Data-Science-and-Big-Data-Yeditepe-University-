import pandas as pd  

import numpy as np 

df = pd.read_csv('output.csv')  

df.head() 

headers = ["symboling", "normalized-losses", "make",  

           "fuel-type", "aspiration","num-of-doors", 

           "body-style","drive-wheels", "engine-location", 

           "wheel-base","length", "width","height", "curb-weight", 

           "engine-type","num-of-cylinders", "engine-size",  

           "fuel-system","bore","stroke", "compression-ratio", 

           "horsepower", "peak-rpm","city-mpg","highway-mpg","price"] 

df.columns=headers 

df.head()
