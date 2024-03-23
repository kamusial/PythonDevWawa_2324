import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
penguins = sns.load_dataset('penguins')

# print(penguins.to_string())
# sns.pairplot(penguins, hue='species')
# plt.show()

penguins_filtered = penguins.drop(columns=['island', 'sex']).dropna()
print(penguins_filtered.to_string())

penguins_features = penguins_filtered.drop(columns=['species'])
target = pd.get_dummies(penguins_filtered['species'])
print(target)

from sklearn.model_selection import train_test_split
from tensorflow import keras

X_train, X_test, y_train, y_test = train_test_split(penguins_features, target, test_size=0.2)
inputs = keras.Input(4)
hidden_layer1 = keras.layers.Dense(5, activation='relu')(inputs)
hidden_layer2 = keras.layers.Dense(5, activation='relu')(hidden_layer1)
output_layer = keras.layers.Dense(5, activation='relu')(hidden_layer2)

model = keras.Model(inputs=inputs, outputs=output_layer)