import random

from sklearn.datasets import make_circles
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib


def train_model(factor, noise):
    X , y = make_circles(n_samples=1000, factor=factor, noise=noise)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print('\n')
    print(f'Got model with score: {score}.')
    print(f'Using parameters: factor: {factor}, noise: {noise}.')
    model_name = 'model_' + str(random.randint(0,1000)) + '_with_score_' + str(score)
    joblib.dump(model, model_name)
    print(f'Saved model: {model_name}')