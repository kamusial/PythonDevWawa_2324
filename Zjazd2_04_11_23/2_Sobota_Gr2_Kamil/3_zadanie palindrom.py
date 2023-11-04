sentence = input('Podaj wyrazenie: ')

print(f'prowadzono {sentence}')
sentence = sentence.replace(' ','')
print(f'bez spacji wygląda tak: {sentence}')
sentence = sentence.lower()
print(f'bez duzych liter wygląda tak: {sentence}')

#print(sentence[3:6:-2])
print(sentence[::-1])  #wypisz od końca

if sentence == sentence[::-1]:
    print(f'tak, wyrażenie {sentence} jest palindromem')



