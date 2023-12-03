import argparse
from funckje_do_4 import *

parser = argparse.ArgumentParser(description='opis')
parser.add_argument('-f', '--filename', help='bez rozszerzenia. Akceptowalne pliki .txt',
                    default='U2', required=False, type=str)
parser.add_argument('-m','--mode', help='Tryb w, r, x',
                    default='r', required=False)
parser.add_argument('-now', '--number_of_words', type=int, default=0, required=False)
parser.add_argument('-uw', '--unique_words', type=int, default=0, required=False)
parser.add_argument('-d', '--duplicates', type=int, default=0, required=False)
parser.add_argument('-o', '--operations', type=str, default='111', required=False)
args = parser.parse_args()

file = args.filename + '.txt'
with open(file, 'r') as u2:
    content = u2.read()
content = clear_text(content)
content = make_split(content)
print(args.number_of_words)
print(args.unique_words)
print(args.duplicates)

if args.operations[0] != '0':
    print(f'Liczba slow: {no_of_words(content)}')
if args.operations[1] != '0':
    print(f'Liczba unikalnych slow: {no_of_unique_elements(content)}')
if args.operations[2] != '0':
    print(f'Powtorzenia\n{reps_of_words(content)}')


if args.number_of_words == 1:
    print(f'Liczba slow: {no_of_words(content)}')
if args.unique_words == 1:
    print(f'Liczba unikalnych slow: {no_of_unique_elements(content)}')
if args.duplicates == 1:
    print(f'Powtorzenia\n{reps_of_words(content)}')
