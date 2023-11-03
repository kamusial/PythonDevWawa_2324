# for i in range(50, 101):
#     print("Kolejna liczba to:", i)


names = ["Natalia", "Ania", "Barbara", "Dorota", "Rafał", "Michał", "Kamil", "Mateusz", "Rafał"]
#            0           1       2           3       4       5           6       7       8
#            -9          -8      -7        -6       -5      -4          -3       -2       -1

print("Dlugość listy names to: ", len(names))
print("Zawartość listy names to: ", names)

# for i in range(len(names)):
#     print("Kolejne imie z listy to: ", names[i])
#     if len(names[i]) <= 4:
#         print("Znalazłam krótkie imię")

word = "Ania"
# counter = 0
#
# for name in names:
#     if name == word:
#         print("Znalazłem!", name)
#         counter += 1
#
# print("Znalazłem słowo ", word, counter, " razy")

if word in names:
    print("Zalazałem!")

# numbers = ["dwa", [1, 3, 5, 8], "6", 8.5, 10]
# print(numbers[1][1])

text = """dsdfsd fliflkahdal ashd ahd ad adcC dsdfsd fliflkahdal ashd ahd ad adcCdsdfsd fliflkahdal ashd ahd ad
        adcCdsdfsd fliflkahdal ashd ahd ad adcCdsdfsd fliflkahdal ashd ahd ad adcCdsdfsd fliflkahdal ashd ahd ad
        AdcCdsdfsd fliflkahdal ashd ahd ad adcCdsdfsd fliflkahdal ashd ahd ad adcCdsdfsd fliflkahdal ashd ahd 
        ad adcC"""

print(names[-1])
names2 = names[:]
print("Kopia listy to:", names2)