import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn.datasets import make_circles
X, y = make_circles(n_samples=50, factor=0.6, noise=0.2)
print(X)
print(y)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()