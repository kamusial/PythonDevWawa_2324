# zgadnij liczbę wylosowaną przez program. 2 punkty / 1 punkt.
# trzeba zdobyć 5 punktów

import random

points = 0
counter = 0
while points < 5:
    counter += 1
    random_number = random.randrange(1, 5)
    user_guess = int(input('Zgadnij liczbę od 1 do 4:   '))
    if user_guess == random_number:
        points += 2
    else:
        points += 1
    print(f'Podejscie nr {counter}. Obecnie masz {points} punktów')
print(f'gratulacje, finalnie zdobyles {points} punktów')
