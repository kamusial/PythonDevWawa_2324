a = 5
b = 7.4
c = 'mama'

print(a * b)
print(c)
print('c')

wiek = int(input('Ile masz lat? '))
if wiek > 65:
    print('juz czas na emeryture')
elif wiek > 30:
    print('Jeszcze dużo życia przed tobą')
else:
    print('Jesteś mlody')

print(f'na emeryture przejdziesz za {65 - wiek} lat')

for i in range(5):
    print(i)

for i in range(30, 5, -3):
    print(i)

products = ['kawa', 'herbata', 'cola', 'kefir']

for product in products:
    print(product)

x = 10
while x > 5:
    print(f'moje {x}')
    x -= 2

while True:
    if x > 8:
        break


