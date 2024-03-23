import matplotlib.pyplot as plt
import numpy as np
from numpy.random import seed
import pandas as pd
from sklearn.datasets import load_breast_cancer  #, load_wine
from sklearn.neural_network import MLPClassifier
from collections import Counter
from sklearn.model_selection import train_test_split, RepeatedStratifiedKFold
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

X, y = load_breast_cancer(return_X_y=True, as_frame=True)

### wersja 1 ###
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# model = MLPClassifier(hidden_layer_sizes=(100, 100, 100), max_iter=10000, activation='relu')
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print(confusion_matrix(y_test, y_pred))
# print(accuracy_score(y_test, y_pred))

### wersja 2 ###
score = []
kfold = RepeatedStratifiedKFold(n_splits=10, n_repeats=30)
for train, test in kfold.split(X,y):
    model = MLPClassifier(hidden_layer_sizes=(10, 10, 10, 10, 10), max_iter=5000, activation='relu')
    X_train, X_test = X.iloc[train,:], X.iloc[test,:]
    y_train, y_test = y.iloc[train], y.iloc[test]
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    score.append(accuracy_score(y_test, y_pred))
print(score)

plt.plot(score)
plt.grid()
plt.show()
