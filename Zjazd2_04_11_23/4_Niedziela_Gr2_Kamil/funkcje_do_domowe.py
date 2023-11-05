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
