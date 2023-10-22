sample_list = [12, 15, 24, 54, 32, 12, 53, 46]
cars = ['audi', 'polonez', 'multipla', 'chevrolet']

# 2 pętle robią to samo
for i in range(len(sample_list)):
    print(sample_list[i], end=' ')
print('\n')

for i in sample_list:
    print(i, end=' ')
print()

for car in cars:
    print(car, end=' ')
print()

for name in ['Marysia', 'Kasia', 'Augusto', 'Kamil']:
    if len(name) > 5:
        print(f'{name} to długie imie jest')
    if name[-1] == 'a':
        print(f'{name} to żenskie imie jest')