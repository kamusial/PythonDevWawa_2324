import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df = pd.read_csv('diabetes.csv')

print(f'ile danych: {df.shape}')
print(df.describe().T.to_string())
print(df.isna().sum())    # suma pustych pól
# wszędzie, gdzie są zera lub brak wartości - przypiszmy średnią

for col in ['glucose', 'bloodpressure', 'skinthickness', 'insulin',
       'bmi', 'diabetespedigreefunction', 'age']:
    df[col].replace(0, np.NaN, inplace=True)   # usuwamy zera
    mean_ = df[col].mean()    #liczymy średnią
    df[col].replace(np.NaN, mean_, inplace=True)   # wpisujemy srednią tam, gdzie puste pola

print('Po czyszczeniu danych')
print(df.describe().T.to_string())

print(df.isna().sum())    # suma pustych pól

df.to_csv('cukrzyca.csv', sep=';', index=False)

X = df.iloc[:, :-1]
y = df.outcome
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))

print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))
