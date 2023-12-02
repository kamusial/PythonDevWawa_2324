# 1. Rozwinąć program tworzony na zajęciach.
# Chcemy, aby system podpowiadał ładną, podobną nazwę użytkownika, jeśli dana nazwa jest zajęta.
# Chcemy, aby haśło nie mogło zawierać ciągu znaków '12345'   bądź, aby nie mogło zawierać załego zestawu takich słabych wzorów.

# 2.
# Dany jest słownik, wskazujący ile mamy produktów:
# available = {'mleko': 3, 'jajko': 25, 'maka': 7, 'cukier': 4, 'maliny': 3}

# Dany jest również słownik wskazując ile jakich produktów potrzebujemy, aby zrobić ciasto:
# cake = {'mleko': 1, 'jajko': 8, 'maka': 0.5, 'cukier': 0.3}
# Zadanie, napisać program liczący, ile ciast możemy upiec z posiadanych produktów.

available = {'mleko': 3, 'jajko': 25, 'maka': 7, 'cukier': 4, 'maliny': 3}
cake = {'mleko': 1.1, 'jajko': 8, 'maka': 0.5, 'cukier': 0.3}

minimum = 1000000
critical_ingredient = ''
results = {}

for key in cake.keys():
    print(f'Bierzemy {key}')
    print(f'zrobimy {available[key] / cake[key]} ciast')
    if available[key] / cake[key] < minimum:
        minimum = available[key] / cake[key]
        critical_ingredient = key
    results[key] = available[key] / cake[key]
print(f'Zrobimy {int(minimum)} ciast. Najszybciej braknie {critical_ingredient}')
print('\n', results, '\n')

sorted_available = sorted(results.items(), key=lambda x: x[1])
print(sorted_available)

