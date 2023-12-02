x = int(input('Podaj 1sza liczbe: '))
y = int(input('Podaj 2ga liczbe: '))

try:
    result = x / y
    print('dzelenie ok')
except:
    result = x
    print('Blad, zwracam pierwsza liczbe')

print(f'Wynik to: {result}')

