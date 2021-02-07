# Importing the libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %% Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
y = y.reshape(len(y), 1)
# %% Feature Scaling
from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)
# %% Training
from sklearn.svm import SVR

svr_regressor = SVR(kernel='rbf')
svr_regressor.fit(X, np.ravel(y))
# %% Prediction
y_prediction = svr_regressor.predict(sc_X.transform([[6.5]]))
print(sc_y.inverse_transform(y_prediction))
# %% Visualization
plt.scatter(sc_X.inverse_transform(X), sc_y.inverse_transform(y), color='red')
plt.plot(sc_X.inverse_transform(X), sc_y.inverse_transform(svr_regressor.predict(X)), color='blue')
plt.title('Level vs Salary (Support Vector Regression)')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()
# %% High Visualization
X_grid = np.arange(min(sc_X.inverse_transform(X)), max(sc_X.inverse_transform(X)), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(sc_X.inverse_transform(X), sc_y.inverse_transform(y), color='red')
plt.plot(X_grid, sc_y.inverse_transform(svr_regressor.predict(sc_X.transform(X_grid))), color='blue')
plt.title('(HR) Level vs Salary (Support Vector Regression)')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()
