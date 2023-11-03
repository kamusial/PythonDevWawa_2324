result = 0
i = 0

# while i < 3:
#     number = int(input("Podaj dodatnią liczbę "))
#     if number > 0:
#         result += number
#     else:
#         print("Miała być dodatnia")
#         #break
#         continue
#     print("Aktualny wynik to: ", result)
#     i += 1

for i in range(3):
    number = int(input("Podaj dodatnią liczbę "))
    if number > 0:
        result += number
    else:
        print("Miała być dodatnia")
        # break
        continue
    print("Aktualny wynik to: ", result)

a = True
b = False
result = a and b

