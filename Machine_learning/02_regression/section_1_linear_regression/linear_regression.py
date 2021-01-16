# %% Importing the libraries
#
import matplotlib.pyplot as plt
import pandas as pd

# %% Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# %% Split to train,test dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.2)

# %% LinearRegression
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, y_train)

# %% training
# y_pred = regression.predict(X_test)

# %% Visualization train set
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regression.predict(X_train), color='blue')
plt.title('Salary vs experience (Training set)')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()

# %% Visualization Test set
plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regression.predict(X_train), color='blue')
plt.title('Salary vs experience (Test set)')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()
