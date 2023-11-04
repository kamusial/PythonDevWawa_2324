print(10 * 10 * 1.1)
print(10 * 1.1 * 10)

def mnozenie(a, b):
    return round(a * b, 2)

my_list = [23.4, 100, 45, 21321, 54.43943]

print(mnozenie(100, my_list[-1]))

#funkcja, która wykonuje dzielenie - uwzględnia dzielenie przez 0
def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        return 0

def f2(a, b, c):
    return a + b, b + c, c * 2

print(f2(3, 4, 5))
print(f2(4, 5, 6)[1])

print(f2('mama', 'tata', 'siostra'))


# funkcja, zarobki, wiek, stan zdrowia
# zwraca informacje o max kredycie, jaki można dostać

def max_kredyt(zarobki, wiek, stan_zdrowia):
    if stan_zdrowia < 3:
        print(f'zly stan zdrowia')
        return 0
    else:
        liczba_rat = (65 - wiek) * 12
        max_rata = zarobki - 1500
        if wiek >= 18 and liczba_rat > 0 and max_rata > 0:
            return liczba_rat * max_rata
        else:
            return 0

print(f'max kredyt: {max_kredyt(1000, 75, 5)}')
