x = int(input('Podaj 1sza liczbe: '))
y = int(input('Podaj 2ga liczbe: '))


try:
    result = x / y
except ZeroDivisionError:
    print('Wyskoczyl blad')
    raise
except ValueError:
    print('value error')
else:
    print('Udalo sie')
finally:
    print('Zbieram logi')
