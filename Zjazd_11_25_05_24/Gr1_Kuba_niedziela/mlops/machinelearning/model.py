import random

from sklearn.datasets import make_circles
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from .models import MLModel
from django.core.files import File
import joblib
import os


def train_model_and_save_model(user, factor, noise):
    X , y = make_circles(n_samples=1000, factor=factor, noise=noise)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print('\n')
    print(f'Got model with score: {score}.')
    print(f'Using parameters: factor: {factor}, noise: {noise}.')
    model_name = 'model_' + str(random.randint(0,1000))
    joblib.dump(model, model_name)
    with open(model_name, 'rb') as model_file:
        m = MLModel(
            upload=File(model_file),
            accuracy=score,
            factor=factor,
            noise=noise,
            author=user
        )
        m.save()
    os.remove(model_name)
    print(f'Saved model: {model_name}')