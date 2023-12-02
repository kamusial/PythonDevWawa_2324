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

def how_many_cakes(available_ingredients: dict, necessary_ingredients: dict):

    results = {}
    for key in cake.keys():
        results[key] = available[key] / cake[key]
    sorted_available = sorted(results.items(), key=lambda x: x[1])

#    print(f'Zrobimy {int(sorted_available[0][1])} ciast. Najszybciej braknie {sorted_available[0][0]}')
    return int(sorted_available[0][1])

how_many_cakes(available, cake)

