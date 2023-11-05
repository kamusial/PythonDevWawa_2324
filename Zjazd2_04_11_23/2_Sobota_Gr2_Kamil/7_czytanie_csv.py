#1 czytanie pliku csv

# with open('rozliczenie.csv', 'r') as file1:
#     for line in file1:
#         content = file1.readline()
#         print(content)

# with open('rozliczenie.csv', 'r') as file1:
#     content = file1.readlines()
# print(f'{content}\n')
# for i in range(len(content)):
#     content[i] = content[i].split(',')
# # print(content)
# print(content[3]) #dana linia
# print(content[3][2]) #dane pole
# print(content[0][2][7:10]) #kawałek stringa


# with open('rozliczenie.csv', 'r') as file1:
#     content = file1.readlines()
#     for i in range(len(content)):
#         content[i] = content[i].split(',')
#         print(content[i])
# #2. średnia wypłata
# lista_wyplat = []
# suma = 0
# for i in range(1,len(content)):
#     print(content[i][1])
#     suma += int(content[i][1])
#     lista_wyplat.append(int(content[i][1]))
#     #srednia = suma / (len(content)-1)
# print(suma)
# print(srednia)
# print(f'lista wypłat: {lista_wyplat}')
# print(f'średnia wypłąta wynosi: {suma/len(content) - 1}), 2')
# print(max(f'maksymalna wypłata: {lista_wyplat}'))
# print(min(f'minimalna wypłata: {lista_wyplat}'))
from statistics import mean
#print(f'średnia wypłata {mean(lista_wyplat)}')

# 3. ile kobiet na macierzyńskim
liczba_na_macierz = 0
with open('rozliczenie.csv', 'r') as file1:
    content = file1.readlines()
    print(content)
    for i in range(1, len(content)):
        content[i] = content[i].split(',')
        content[i][4] = content[i][4].replace('"\n', '')
        print(content[i][4])
        #if content[i][4] == 't\n' or content[i][4] == 't':
        if content[i][4] == 't' and content[i][3] == 'k':
            liczba_na_macierz +=1
    print(f'Liczba kobiet na macierzyńskim: {liczba_na_macierz}')
