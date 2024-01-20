"""Zadania są mniej więcej w kolejności od najłatwiejszego do najtrudniejszego"""
# zad 1: wyprintuj sumę największej i najmniejszej liczby w liście:
a = [2, 52, 5, 7, 12, 67, 22, 31]

# zad 2: wyprintuj ile razy w tekście poniżej występuje litera 'e'
# zad 3: wyprintuj która litera występuje najczęściej
b = "pip! dwudziestu uzurpatorow dusi padalcem dwa pudle"

# zad 4: zamień pary elementów w liście 'a' miejscami, czyli powinno wyjść: [52, 2, 7, 5, 67, 12, 31, 22]

# zad 5: zasymuluj dużego lotka - wylosuj 6 NIEPOWTARZAJĄCYCH SIĘ liczb od 1 do 49
import random

# zad 6: wyprintuj 4 najczęściej występujące litery w zmiennej 'b' jako 4-literowe słowo
from collections import Counter


counter = Counter(b.replace(" ", ""))
most_common = counter.most_common(4)

result = ""
for letter, _ in most_common:
    result += letter
print(result)

result = "".join([letter for letter, _ in most_common])
print(result)
