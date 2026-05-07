#PLOTTING ALL VARIABLES

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
# Loading pre-defined Diabetes Dataset
diabetes_dataset = load_diabetes()
# Create a scatter plot with variable names (feature names) displayed
plt.style.use('ggplot')
fig = plt.figure(figsize=(24, 24))

for index, feature_name in enumerate(diabetes_dataset.feature_names):
    ax = fig.add_subplot(4, 4, index + 1)
    X = diabetes_dataset.data[:, index].reshape(-1, 1)
    y = diabetes_dataset.target
    ax.scatter(X, y, label='Data Points')

    # Adding the feature name on the plot
    ax.set_ylabel('Disease Progression', size=10)
    ax.set_xlabel(feature_name, size=24)
   
    # Display the feature name inside the plot
    ax.text(0.5, 0.9, feature_name, transform=ax.transAxes, ha='center', va='center', fontsize=12, color='blue')

    ax.legend()
plt.tight_layout()
plt.show()
print(diabetes_dataset.DESCR)
