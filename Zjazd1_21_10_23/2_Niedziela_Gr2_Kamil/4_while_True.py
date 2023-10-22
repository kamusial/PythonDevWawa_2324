age = int(input('Ile masz lat? '))

while True:
    if age >= 18:
        break
    else:
        print('Zły wiek, jeszcze raz')
        age = int(input('Ile masz lat? '))
print('Witamy')