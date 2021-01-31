# %% Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd

# %% Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, -2:-1].values
y = dataset.iloc[:, -1].values
# %% LinearRegression
from sklearn.linear_model import LinearRegression

lin_regression = LinearRegression()
lin_regression.fit(X, y)
# %% Visualization LinearRegression
plt.scatter(X, y, color='red')
plt.plot(X, lin_regression.predict(X), color='blue')
plt.title('Level vs Salary (LinearRegression)')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()
# %% PolynomialLinearRegression
from sklearn.preprocessing import PolynomialFeatures

pf = PolynomialFeatures(degree=4)
X_poly = pf.fit_transform(X)
pol_lin_regression = LinearRegression()
pol_lin_regression.fit(X_poly, y)
# %% Visualization PolynomialLinearRegression
plt.scatter(X, y, color='red')
plt.plot(X, pol_lin_regression.predict(X_poly), color='blue')
plt.title('Level vs Salary (PolynomialLinearRegression)')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()
# %% LinearRegression Prediction
print(lin_regression.predict([[6.5]]))
# %% PolynomialLinearRegression Prediction
print(pol_lin_regression.predict(pf.fit_transform([[6.5]])))
