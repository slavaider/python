# %% Importing the libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %% Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, -2:-1].values
y = dataset.iloc[:, -1].values
# %% LinearRegression
from sklearn.linear_model import LinearRegression

lin_regressor = LinearRegression()
lin_regressor.fit(X, y)
# %% Visualization LinearRegression
plt.scatter(X, y, color='red')
plt.plot(X, lin_regressor.predict(X), color='blue')
plt.title('Level vs Salary (LinearRegression)')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()
# %% PolynomialLinearRegression
from sklearn.preprocessing import PolynomialFeatures

pf = PolynomialFeatures(degree=4)
X_poly = pf.fit_transform(X)
pol_lin_regressor = LinearRegression()
pol_lin_regressor.fit(X_poly, y)
# %% Visualization PolynomialLinearRegression
plt.scatter(X, y, color='red')
plt.plot(X, pol_lin_regressor.predict(X_poly), color='blue')
plt.title('Level vs Salary (PolynomialLinearRegression)')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()
# %% High Visualization PolynomialLinearRegression
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color='red')
plt.plot(X_grid, pol_lin_regressor.predict(pf.transform(X_grid)), color='blue')
plt.title('(HR) Level vs Salary (PolynomialLinearRegression)')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()
# %% LinearRegression Prediction
print(lin_regressor.predict([[6.5]]))
# %% PolynomialLinearRegression Prediction
print(pol_lin_regressor.predict(pf.fit_transform([[6.5]])))
