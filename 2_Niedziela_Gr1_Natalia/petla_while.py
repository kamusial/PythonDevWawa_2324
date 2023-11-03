# Pętla while
result = 0

# pętla nieskończona
# while True:
#     result += int(input("Podaj liczbę do dodania: "))
#     print("Wynik dodawania to: ", result)

counter = 0

while counter <= 100:
    print("Kolejna liczba to:", counter)
    if counter % 2 == 0:
        print(counter, " to liczba parzysta")
    else:
        print(counter, " to liczba nieparzysta")
    counter += 1

# Program, który sprawdza, czy możesz zakupić alkohol
age = 18
user_age = int(input('Podaj wiek:'))

while user_age < age:
    user_age = int(input('Podaj wiek:'))
    if age == 18:
        print('Mozesz kupić alkohol')
    else:
        print('Nie możesz kupić alkoholu!')
