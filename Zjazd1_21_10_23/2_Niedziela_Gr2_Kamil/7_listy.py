my_list = [5, 7.5, 12, 14, 'mama', 'piesek']

print(my_list)
print(my_list[5])
#print(my_list[6])  # za daleko
print(my_list[2:5])
my_list[1] = 'siedem i pol'
print(my_list)
print(my_list[2])
my_list[2] += 4.4
print(my_list[2])

print(f'dlugosc listy wynosi {len(my_list)}')

#print(my_list[len(my_list) - 1])    #ostatni element listy
print(my_list[-1])   # ostatni element
print(my_list[-2])   # przedostatni element

print(my_list[1:5:2])
print(my_list[:2])   #od początku do danego indeksu
print(my_list[2:])   #od danego inteksu do końca
print(my_list[::-2]) #od początku do końca, skok o -2

