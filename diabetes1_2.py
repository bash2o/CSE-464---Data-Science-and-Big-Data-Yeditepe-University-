#PLOTTING THE HISTOGRAM OF TARGET VARIABLE

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_diabetes

# Load the dataset by calling the function
diabetes_data = load_diabetes()
df = pd.DataFrame(data=diabetes_data.data, columns=diabetes_data.feature_names)

# Add the target variable to the DataFrame
df['target'] = diabetes_data.target # This line adds the 'target' column

# Plotting the histogram of the target variable (diabetes progression)
plt.figure(figsize=(8, 6))
sns.histplot(df['target'], bins=30, kde=True)  # `kde=True` adds a Kernel Density Estimate
plt.title('Distribution of Diabetes Progression (Target Variable)')
plt.xlabel('Diabetes Progression')
plt.ylabel('Frequency')
plt.show()
