# uzytkownik prowadza osoby
# każda wprowadzona osoba ma imie, nazwisko, mail
# program pyta czy wprowadzić koleją osobę
# po zakończeniu wprowadzania, program wypisuje
#  - ile jest kobiet
#  - ile osób ma maila w domenie gmail
# dla chętnych: program usuwa tych, których imion nie ma w bazie

data = []
while True:
    person = input('Wprowadź dane: Imie, nazwisko, mail - oddziel spacją ').split()
    data.append(person)
    decission = input('Czy chcesz dodać kolejną osobę? T/N ')
    if decission.upper() != 'T':
        break
no_of_women = 0
no_of_gmail = 0
for person in data:
    if person[0][-1] == 'a':
        no_of_women += 1
    if '@gmail.' in person[2]:
        no_of_gmail += 1
print(f' Liczba kobiet: {no_of_women}, a liczba uzytkowników gmail: {no_of_gmail}')
print(f'Lista osób: {data}')
#print(data[0][2][7:10])   # wyciągnicie kawałka maila
# usuwanie niepasujących imion
names = ['Kamil', 'Marek', 'Basia', 'Kasia', 'Gustaw', 'Mietek']
for person in data:
    if person[0] not in names:
        data.remove(person)
print(f'Końcowa lista wygląda tak: {data}\n, jest {len(data)} osób')
