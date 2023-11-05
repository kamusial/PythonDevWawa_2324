def user_add(username):
    user_dict[username] = input('Podaj haslo: ')
    print(f'uzytkownik {username} dodany do listy uzytkowników')


def is_username_available(username):
    if username not in user_dict:
        print(f'Nazwa {username} dozwolona')
        return True
    else:
        print(f'Nazwa {username} NIEdozwolona')
        return False


def suggest_username(username):
    return username + '1'


def find_available_name(username):
    while not is_username_available(suggest_username(username)):
        username = suggest_username(username)
    username = suggest_username(username)
    print(f'Dostępna nazwa {username}')
    return username


user_dict = {
    'majki': '123',
    'Kamil': '124',
    'Kamil1': '234',
    'Kamil11': '765',
    'Kamil111': 'mama',
    'Kamil001': 'eee',
    'Rafcio': '876',
    'Betty': 'betty'
}
