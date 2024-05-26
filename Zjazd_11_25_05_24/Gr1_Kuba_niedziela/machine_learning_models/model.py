import random

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
    print('\n')
    print(f'Got model with score: {score}.')
    print(f'Using parameters: factor: {factor}, noise: {noise}, test_size: {test_size}.')
    if score >= 0.68:
        model_name = 'model_' + str(random.randint(0,1000)) + '_with_score_' + str(score)
        joblib.dump(model, model_name)
        print(f'Saved model: {model_name}')
    else:
        print('Model was not good enough!')


def rand_float(a, b):
    return random.randint(a, b) * 0.01


def model_generator(x):
    for i in range(x):
        train_model(n_samples=1000,
                    factor=rand_float(0,80),
                    noise=rand_float(0,5),
                    test_size=rand_float(1,20)
                    )

model_generator(1000)