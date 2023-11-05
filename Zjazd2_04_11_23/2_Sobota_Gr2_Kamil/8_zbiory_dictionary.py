# produkty = ['mleko', 'ser', 'olej']
# ceny = [4, 67, 12]
#
# lista_zakupow = [
#     ['mleko', 4],
#     ['ser', 12],
#     ['olej', 12]
# ]

dict1 = {'mleko': 4, 'ser': 12, 'olej': 11}
dict1['masło'] = 6
dict1['mleko'] = 1
dict1['mleko'] = dict1['mleko'] * 1.5
# print(f'cena mleka: {dict1['mleko']}')
# print(dict1)
# print(dict1['masło'] + dict1['mleko'])

while True:
    nazwa = input("Jaki produkt chcesz sprawdzić:  ")
    if nazwa in dict1.keys():
        print(f'Cena produktu {nazwa} wynosi {dict1[nazwa]}')
    else:
        print(f"Nie mam w bazie produktu {nazwa}")
        decyzja = input(f"Czy chcesz dodać {nazwa} do listy produktów? t/n: ")
        if decyzja == 't':
            cena = float(input('Podaj cenę: '))
            dict1[nazwa] = cena
        nastepny = input(f'Czy chcesz sprawdzic/dodać kolejny produkt? t/n: ')
        if nastepny == 'n':
            break
#sprawdzam czy produkt jest, jeśli nie to proponuje dodanie i ponownie pytam czy chce coś sprawdzić