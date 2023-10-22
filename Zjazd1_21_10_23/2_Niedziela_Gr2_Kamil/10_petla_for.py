# program pyta, ile osób dodać do systemu
# program pozwala dodać tyle osób, zapisuje je w liście

names = []
no_of_reps = int(input('Ile osób chcesz dodać? '))
for i in range(no_of_reps):
    name = input('Podaj nazwe: ')
    names.append(name)
print('koniec petli1')

# program pyta za każdym razem, czy chcesz dodać koleją osobę
while True:
    name = input('Podaj nazwe: ')
    names.append(name)
    _next = input('Czy chcesz dodać kolejna osobę? T/N: ')
    if _next.upper() != 'T':    #małe t i duże T  spełni warunek
        break
print(names, end=' ')
