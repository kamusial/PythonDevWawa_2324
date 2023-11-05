# załóżmy, że pesel ma 4 cyfry
# stwórzmy zbiór NFZ – ludzie, w bazie pacjentów NFZ
# stwórzmy zbiór chorzy_rok – ludzie chorzy w ostatnim roku
# stwórzmy zbiór chorzy_miesiac – ludzie chorzy w ostatnim miesiącu
# stwórzmy zbiór bemowo – wszystkich ludzi mieszkających na bemowie
# stwórzmy zbiór zoliborz – wszystkich ludzi mieszkających na zoliborzu

NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
bemowo = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
zoliborz = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

# set1 | set2 -> suma
# set1 & set2 -> część spólna
# set1 - set2 -> różnica
# set ^ set2 -> różnica symetryczna  (bez części wpsólnej)

# sprawdźmy, ile osób chorowało w ostatnim roku na bemowie
print(f'Chorzy w ostatnim roku na bemowie to {chorzy_rok & bemowo}')
print(f'Liczba osób {len(chorzy_rok & bemowo)}')

# sprawdźmy ile osób z Bemowa chorowało w ostatnim roku
print(f'Chorzy w ostatnim roku na bemowie to {bemowo & chorzy_rok}')
print(f'Liczba osób {len(bemowo & chorzy_rok)}')

# sprawdźmy, ile osób chorowało w ostatnim miesiącu na żoliborzu
print(f'Chorzy w ostatnim roku na bemowie to {zoliborz & chorzy_miesiac}')
print(f'Liczba osób {len(zoliborz & chorzy_miesiac)}')

                # sprawdźmy poprawność danych:

# każdy, kto chorował w ostatnim miesiącu, powinien jednocześnie chorować w ostatnim roku
# czy są ludzie, którzy chorowali w ostatnim miesiącu, a nie chorowali w ostatnim roku?
print(f'Ludzie chorujący w ostatniem miesiącu i NIE chorujący w ostatnim roku: {chorzy_miesiac - chorzy_rok}')

# nikt nie powinien mieszkać jendocześnie na żoliborzu i na bemowie – jeśli tak, trzeba usunąć
