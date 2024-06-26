import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = pd.read_csv('weight-height.csv', delimiter=';')
print(df)
print(type(df))

df.Height *= 2.54
df.Weight /= 2.2
print(df.head(3)) #pierwsze 3 wiersze

# # wykresy
# plt.hist(df.query('Gender=="Male"').Weight)
# #plt.show()
# plt.hist(df.query('Gender=="Female"').Weight)
# plt.show()
#
# sns.histplot(df.query('Gender=="Male"').Weight)
# sns.histplot(df.query('Gender=="Female"').Weight)
# plt.show()

# zamiana gender na dane numeryczne
df = pd.get_dummies(df)
del (df['Gender_Male'])
df = df.rename(columns={'Gender_Female': 'Gender'})
print(df.head())
# False - facet,  True - kobieta

model = LinearRegression()
model.fit(df[['Height', 'Gender']]    ,   df['Weight'])    #dane wejściowe i wyjściowe
print(f'Wspolczynnik kierunkowy: {model.coef_}\nWyraz wolny: {model.intercept_}')

print(f'Weight = Height * {model.coef_[0]} + Gender * {model.coef_[1]} + {model.intercept_}')

#sprawdźmy coś
print(model.predict([[160, 0]]))
print(model.predict([[160, 1], [180, 0], [167, 1]]))