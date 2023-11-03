#  Powtórka 2
#  Pomidory kosztują 3 zł za sztukę. Jeśli kupisz 3 pomidory, to jest 20% taniej.
#  Program pyta ile pomidorów chcesz kupić i wylicza najniższą cenę.

# liczba wszystkich pomidorów
no_of_tomatoes = int(input("Ile pomidorów chcesz kupić?"))

# liczba 3-paków
no_of_3_packs = no_of_tomatoes // 3

# liczba pojedynczych pomidorów
no_of_single_tomatoes = no_of_tomatoes % 3

# wyliczenie ceny w zaleznosci od promocji
price = no_of_3_packs * 3 * 0.8 * 3 + no_of_single_tomatoes * 3

# wypisanie ceny na ekran
print("Zapłacisz: ", round(price), "zł za ", no_of_tomatoes, "pomidorów")