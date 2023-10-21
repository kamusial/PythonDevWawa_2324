wyplata = int(input("Ile zarabiasz? "))
print(f'Zarabiasz {wyplata}zł miesiecznie')

# jeżeli zarabiasz więcej 15k, placisz 20% podatku. Jeśli mniej - 10% podatku.

if wyplata > 15000:
    print('Zarabiasz duzo')
    print(f'Na czysto zarobisz {wyplata * 0.8}, a podatek {wyplata * 0.2}')
else:
    print('zarabiasz mało')
    print(f'Na czysto zarobisz {wyplata * 0.9}, a podatek {wyplata * 0.1}')
print('Dalsza czesc programu')
print('koniec programu')


