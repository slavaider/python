import pandas as pd

# %% Importing the dataset
dataset = pd.read_csv('train.csv')
dataset_test = pd.read_csv('test.csv')
X_test = dataset_test.iloc[:, :1].values
X_train = dataset.iloc[:, :1].values
y_train = dataset.iloc[:, 1:2].values
# %% Train LinearRegression
from sklearn.linear_model import LinearRegression

regression = LinearRegression()
regression.fit(X_train, y_train)
print(regression.predict(X_test))
