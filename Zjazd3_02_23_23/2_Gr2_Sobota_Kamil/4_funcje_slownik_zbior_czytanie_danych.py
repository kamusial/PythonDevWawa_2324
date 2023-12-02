# przeczytać plik
# wyczyścić dane
# znaleźć liczbę słów
# znaleźć liczbę różnych słów
# zapisać ilosć powórzeń każdego słowa

from funckje_do_4 import *

with open('U2.txt', 'r') as u2:
    content = u2.read()
print(content)
content = clear_text(content)
content = make_split(content)
print(content)
print(f'Liczba slow: {no_of_words(content)}')
print(f'Liczba unikalnych slow: {no_of_unique_elements(content)}')
print(f'Powtorzenia\n{reps_of_words(content)}')
