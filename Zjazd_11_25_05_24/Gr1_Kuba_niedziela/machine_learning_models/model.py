import random

import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib


def train_model(n_samples, factor, noise, test_size):
    X , y = make_circles(n_samples=n_samples, factor=factor, noise=noise)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print(f'Got model with score: {score}.')
    if score > 0.45:
        model_name = 'my_model_' + str(random.randint(0,1000))
        joblib.dump(model, model_name)
        print(f'Saved model: {model_name}')
    else:
        print('Model was not good enough!')

for i in range(10):
    train_model(1000, 0.9, 0.1, 0.2)

random.randint(0,99) * 0.01