# %% Importing the libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %% Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
# %% Training on Decision Regression Tree
from sklearn.tree import DecisionTreeRegressor

decision_tree_regressor = DecisionTreeRegressor(random_state=0)
decision_tree_regressor.fit(X, y)
# %% Prediction
print(decision_tree_regressor.predict([[6.5]]))
# %% High Visualization
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color='red')
plt.plot(X_grid, decision_tree_regressor.predict(X_grid), color='blue')
plt.title('Salary vs experience (DecisionTreeRegression)')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()
