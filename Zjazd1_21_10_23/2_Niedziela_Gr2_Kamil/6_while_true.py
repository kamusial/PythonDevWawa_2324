# program losuje liczbę 1-100
# uzytkownik zgaduje liczbe
# program mówi, czy liczba uzytkownika jest ok, większa bądź mniejsza od wylosowanej liczby
import random
random_number = random.randint(1, 100)
while True:
    user_number = int(input('Podaj liczbę: '))
    if user_number > random_number:
        print('Za duzo')
    elif user_number < random_number:
        print('Za malo')
    else:
        print('Super')
        break