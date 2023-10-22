sample_list = [5, 7, 12, 14, 23, 36, 45, 3535, 34, 76]
even_list = []
odd_list = []
# program, który weźmie listę "sample_list" i zapisze liczby parzyste i nieparzyste
# osobno w noywhc listach

x = 0
while x < len(sample_list):
    print(f'element {x} ma wartosc {sample_list[x]}')
    if sample_list[x] % 2 == 0:
        even_list.append(sample_list[x])
    else:
        odd_list.append(sample_list[x])
    x += 1
print(f'parzyste to: {even_list}')
print(f'nieparzyste to: {odd_list}')