# 14 // 4 = 3   # część calkowita z dzielenia
# 14 % 4 = 2    # reszta z dzielenia z dzielenia

# x = 5
# napiszmy, czy liczba parzysta, czy nie
# if x % 2 == 0:
#     print('parzysta')
# else:
#     print('nieparzysta')

# pomidory kosztują 3zł sztuka. Ale w 3-paku, 3 pomidory razem kosztują 80% ceny
# program pyta ile pomidorów chcemy kupić i zwraca najniższą cenę

# wersja 1:
price_per_tomato = 3
no_of_tomatos = int(input('Ile pomidorów chcesz kupić? '))
no_of_3packs = no_of_tomatos // 3
no_of_single_tomatos = no_of_tomatos % 3
total_price = price_per_tomato * (no_of_3packs * 3 * 0.8 + no_of_single_tomatos)
total_price = round(total_price, 2)   #zaokrąglij do groszy
print(f'zaplacisz {total_price}zł')

# wersja 2:
print(round(price_per_tomato * (no_of_tomatos // 3 * 3 * 0.8 + no_of_tomatos % 3)), 2)