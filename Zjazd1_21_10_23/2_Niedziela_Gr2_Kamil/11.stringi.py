word1 = 'akbrakadabra'
word2 = 'file.txt'
print(word1[2:5])
print(word2[:4] + '_' + word1 + word2[4:])

word1 = word1.replace('a', 'A', 2)  #zamień a, na A, 2 pierwsze
print(word1)

word3 = 'mama.tata.pies'
word3 = word3.split('.')
print(word3)

people = input('Wprowadź imiona ludzi, oddziel spacją: ').split()
print(people)