# hasło do systemu: 1234
# użytkownik podaje hasło
# program wpuszcza uzytkownika bądź nie

system_password = '1234'   # 1234 - str
user_password = input('Wpisz haslo: ')

if system_password == user_password:
    print('dobre haslo')
else:
    print('Zle haslo')