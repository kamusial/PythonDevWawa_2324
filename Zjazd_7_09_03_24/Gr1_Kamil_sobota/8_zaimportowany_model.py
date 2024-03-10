import joblib

model_new = joblib.load('Kamil_random_forest.model')

print(model_new.predict([[3, 4, 1, 1], [3, 1, 2, 3], [5, 4, 3 , 2]]))
print(model_new.n_features_in_, model_new.feature_names_in_)
print(model_new.feature_importances_)