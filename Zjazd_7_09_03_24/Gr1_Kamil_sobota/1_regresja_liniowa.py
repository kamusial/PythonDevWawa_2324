import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = pd.read_csv('weight-height.csv')
print(df)
print(type(df))

print(df.head(3))   # wyświetl 3 pierwsze wiersze
print(f'\nzliczanie wartosci kolumny Gender\n{df.Gender.value_counts()}')

#zmiana jednostek
df.Height *= 2.54
df.Weight /= 2.2
print(df.head(3))

#wykresy
# plt.hist(df.Weight)
# plt.show()

sns.histplot(df.query("Gender=='Male'").Weight)
sns.histplot(df.query("Gender=='Female'").Weight)
plt.show()

# zamiana gender na dane numeryczne
df = pd.get_dummies(df)
print(df)