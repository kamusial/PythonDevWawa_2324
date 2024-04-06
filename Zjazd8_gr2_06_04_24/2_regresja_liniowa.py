import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('otodom.csv')
print(df)
#print(df.describe())
print(df.describe().T.to_string())

# print(df.iloc[3:8, 1:3])   # wiersze i kolumny
print(df.iloc[:, 1:].corr())
sns.heatmap(df.iloc[:, 1:].corr(), annot=True)
plt.show()

sns.histplot(df.price)
plt.show()
q1 = df.describe().T.loc['price', '25%']
q3 = df.describe().T.loc['price', '75%']
print(f'cena na koncu q1 to: {q1}')
print(f'cena na koncu q3 to: {q3}')

df1 = df[(df.price >= q1) & (df.price <= q3)]
sns.histplot(df1.price)
plt.show()

X = df1.iloc[:, 2:]   # bez id i bez ceny
y = df1.price
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))