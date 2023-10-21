# print('Hej')
# input()          # poczekaj na 'enter'
# print('Milego dnia')

imie = input('Jak masz na imie?   ')   # wypisz treść, zapisz zmienną i poczekaj na enter
# wiek = int(input('Ile masz lat?   '))  #zapisz wiek, jako liczbę
wiek = input('Ile masz lat?   ')

print('Cześć', imie, '. Masz', wiek, 'lat.')
print(f'Cześć {imie}. Masz {wiek} lat.')

print(f'Przejdziesz na emerytuję za {65 - int(wiek)} lat')