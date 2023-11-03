#  Powtórka z 'if'
#  Program, który pyta, czy jesteśmy głodni
#  Dodatkowo, program sprawdza, czy mamy alergie

status = input("Czy jestes glodny? T/N ")
allergies = input("Czy masz alergie? T/N ")

if (status == "T") or (status == "t"):
    print("Rozumiem, zaproponuję coś pysznego!")
    if allergies == "T":
        print("Proponuję danie dla alergików")
    elif allergies == "N":
        print("rzepraszam, nie rozumiem tej komendy")
    else:
        print("Sam nie wiem, co zrobic")
elif status == "N":
    print("Aha, czyli nic nie jemy")
else:
    print("Przepraszam, nie rozumiem tej komendy")


if "jeden :)":
    print("prawda")

# # or jest prawdziwy >> 1
# 1 or 1
# 1 or 0
# 0 or 1
#
# # or nie jest prawdziwy (fałsz) >> 0
# 0 or 0