def user_add(username):
    while True:
        passwd1 = input('Podaj haslo: ')
        passwd2 = input('Podaj jeszcze raz haslo: ')

        if passwd1 == passwd2 and is_passwd_correct(passwd1):
            user_dict[username] = passwd1
            print(f'uzytkownik {username} dodany do listy uzytkowników')
            break

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

def passwd_has_cap_and_small_letter(password):
    if password.upper() != password and password.lower() != password:
        return True
    else:
        print(f'nie znaleziono duzej badz malej litery')
        return False

def pass_has_digit(password):
    if len(set(password) & digits) > 0:
        return True
    else:
        print(f'nie znaleziono cyfry')
        return False


def passwd_has_special_character(password):
    if len(set(password) & special_characters) > 0:
        return True
    else:
        print(f'nie znaleziono znaku specjalnego')
        return False

def is_passwd_correct(password):
    if passwd_has_special_character(password) and passwd_has_cap_and_small_letter(password) and pass_has_digit(password):
        return True
    return False


special_characters = set('.,/;!@#$%\'\"\\')
digits = set('0123456789')

# set2 = set[1, 2, 3, 5]
# set1 | set2 -> suma
# set1 & set2 -> część wspólna


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