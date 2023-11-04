

with open('rollin_stones.txt', 'r') as file1:
    content = file1.read()

print('dalsza czesc programu, plik zamknięty')
print(content)

content = content.split()
print(content)
print(f'liczba slow: {len(content)}')