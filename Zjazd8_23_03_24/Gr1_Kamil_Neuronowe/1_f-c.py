import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(1, activation='linear'))  # warstwa wejściowa
model.add(Dense(2, activation='linear'))
model.add(Dense(1, activation='linear'))  # warstwa wyjściowa
model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

df = pd.read_csv('f-c.csv', usecols=[1, 2])
print(df.head())
plt.scatter(df.F, df.C)
plt.show()

result = model.fit(df.F, df.C, epochs=10, verbose=2)
# print(result)
# print(type(result))
print(result.history)
df1 = pd.DataFrame(result.)