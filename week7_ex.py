import pandas as pd
import numpy as np from sklearn.model_selection
import train_test_split from sklearn.linear_model
import LinearRegression
d = {'x': [2,7,8, 10,15,17,30,41], 'y': [4,15,17,20,24,28,41,56], 'z': [8,15,np.nan,20,np.nan,np.nan,35,np.nan]}
df = pd.DataFrame(data=d)
print(df)
df_m=df.dropna()X = df_m.loc[:, df_m.columns != 'z']y=df_m['z']
X_train, X_test, y_train, y_test = train_test_split(X, y)
LR=LinearRegression()LR.fit(X_train,y_train)
to_predict = df[df['z'].isna()]print('Predict:')print(to_predict)
print('\nGet Predictions:')predictions = LR.predict(np.array(to_predict[['x','y']]))
print(predictions)
print('\nMerge it back:')to_predict['z'] = predictions
print(to_predict)
