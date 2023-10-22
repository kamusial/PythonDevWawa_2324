# uzytkownik prowadza osoby
# każda wprowadzona osoba ma imie, nazwisko, mail
# program pyta czy wprowadzić koleją osobę
# po zakończeniu wprowadzania, program wypisuje
#  - ile jest kobiet
#  - ile osób ma maila w domenie gmail
# dla chętnych: program usuwa tych, których imion nie ma w bazie

data = []
while True:
    person = input('Wprowadź dane: Imie, nazwisko, mail - oddziel spacją').split()
    data.append(person)
    decission = input('Czy chcesz dodać kolejną osobę? T/N')
    if decission
