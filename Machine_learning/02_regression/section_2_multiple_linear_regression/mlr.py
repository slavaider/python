# Importing the libraries
import pandas as pd

# %% Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
# %% Encoding to dummy variables
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
X[:, -1] = le.fit_transform(X[:, -1])
# %% Split in train,test data sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.2)

# %%
# prepare to exam...
