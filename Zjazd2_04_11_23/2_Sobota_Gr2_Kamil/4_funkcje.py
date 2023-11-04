import random

def przywitanie():
    print('Witam, jest ładnyt dzień')

def przywitanie_zlozone(imie, wiek):
    if wiek >= 18:
        if imie[-1] == 'a':
            print(f'Dzień dobry Pani {imie}')
        else:
            print(f'Dzień dobry Panu {imie}')
    else:
        print(f'Czesc {imie}, masz {wiek} lat')

# funkcja rozpoznaje, czy facet, czy kobieta
# jesli pełnoletni - print: Dzień dobry Panu / pani
# jeśli młody - print: Cześć 'imie'

def dodawanie(a, b):
#    print(f'Wynik dodawania to {a+b}')
    return a + b


print('Start programu')
przywitanie()
przywitanie_zlozone('Kamil', 35)
print(f'Wynik dodawania to {dodawanie(5, 7)}')

for i in range(3, dodawanie(3, 6), 2):
    print(i)

tmp_list = [5, 6, 23, 3, 6]
for i in range(3, dodawanie(tmp_list[2], random.randint(3, 30))):
    print(i)

print(dodawanie(tmp_list[3], 5) + 6)