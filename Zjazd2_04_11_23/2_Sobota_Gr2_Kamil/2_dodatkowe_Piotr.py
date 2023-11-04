user_list = ['majki', 'Kamil001', 'Rafcio', 'Betty']
password_list = ['haslo1', 'haslo2', 'haslo3', 'haslo4']
user_password_list = dict(zip(user_list, password_list))


def check_username(username):
    # zmieniam wszystkie znaki z username na małe, dodatkowo zmieniam na małe każdy znak w
    # w każdym kluczu, który jest w liście user_password_list.keys(to słownik{} username:password )
    return username.lower() in [key.lower() for key in user_password_list.keys()]


def suggest_username(username):
    counter = 1
    suggest_name = username
    while check_username(suggest_name):
        suggest_name = username + str(counter)
        counter += 1
    return suggest_name


def check_exit(string):
    if ";" in string:
        exit()


while True:
    _next = input('Czy chcesz dodać nowego użytkownika ? T/N')
    check_exit(_next)
    if _next != 't':
        break
    print(f'Nacisnij ";" w dowolnej chwili-> żeby wyjść :)')
    while True:
        user_name = input('Podaj nazwe użytkownika')
        check_exit(user_name)
        if check_username(user_name):
            sug_username = suggest_username(user_name)
            print(f'Nazwa użytkownika jest już zajęta, proponuje {sug_username}\n')
        elif user_name == ';':
            exit()
        else:
            break
    while True:
        password1 = input('Podaj hasło : ')
        check_exit(password1)
        print()
        password2 = input('Powtórz hasło: ')
        check_exit(password2)
        if password1 != password2:
            print('Hasła są różne !! Podaj ponownie \n')
        elif password1 == ';' or password2 == ';':
            exit()
        else:
            password = password1
            break
    user_password_list[user_name] = password
    print()
    for index, (key, value) in enumerate(user_password_list.items()):
        print('Index = {:<3} Username = {:<12} Password = {}'.format(index + 1, key, value))