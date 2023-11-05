# Zadanie 1:dana jest lista użytkowników
# User_list = ['majki', 'Kamil001', 'Rafcio', 'Betty']- program pyta o wprowadzenie nowego użytkownika-
# jeśli nazwa użytkownika jest zajęta program prosi o ponowne wprowadzenie nazwy bądź proponuje swoją podobną nazwę
# po wprowadzeniu uzytkownika, program 2 razy prosi o hasło
# po dwukrotnie wprowadzonym takim samym haśle, uzytkownikzostaje dodany do listy użytkowników, a jego hasło jest zapisane w drugiej liście

def user_add(username):
    user_list.append(username)
    print(f'uzytkownik {username} dodany do listy uzytkowników')


def is_username_available(username):
    if username not in user_list:
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

user_list = ['majki', 'Kamil', 'Kamil1', 'Kamil11', 'Kamil111', 'Kamil001', 'Rafcio', 'Betty']


username = input('Podaj nazwe uzytkownika: ')
if is_username_available(username):
    user_add(username)
else:
    username = find_available_name(username)









