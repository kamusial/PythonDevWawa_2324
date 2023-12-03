a = 0

for i in range(10):
    a += 1
    print(f'Iteracja {i+1}')
    print(f'a= {a}')
    if a ==3:
        continue
    if a == 5:
        break
    print('koniec iteracji')
print('koniec petli')