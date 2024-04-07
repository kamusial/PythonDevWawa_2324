import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn.datasets import make_circles
X, y = make_circles(n_samples=5000, factor=0.4, noise=0.2)
print(X)
print(y)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)
# kernel{‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’}


print('\nSVC')
model = SVC(kernel='rbf', degree=2)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))
