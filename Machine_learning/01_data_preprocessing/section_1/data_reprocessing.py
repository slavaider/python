# dataset2 = pd.read_excel('C:\\Users\\User\\Downloads\\table_dataset8_data.xls')
# %% Importing the libraries
import numpy as np
import pandas as pd

# %% Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# %% Taking care of missing data
from sklearn.impute import SimpleImputer

impute = SimpleImputer()
X[:, 1:3] = impute.fit_transform(X[:, 1:3])

# %% Encoding Categorical Data
# Encoding Independent Variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])],
                       remainder='passthrough')
X = np.array(ct.fit_transform(X))
# Encoding Dependent Variable
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
y = le.fit_transform(y)

# %% Splitting Dataset to TrainSet and TestSet
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# %% Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.transform(X_test[:, 3:])
