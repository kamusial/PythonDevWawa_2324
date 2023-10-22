# program pyta uzytniwnika o haslo
# jesli hasło poprawne - wchodzimy
# jesli wprowadzono hasło serwisowe, progrma pyta o wiek i jesli pełnoetni to wchodzimy

password = '1234'
service_password = 'service'

while True:
    user_password = input('Podaj haslo: ')
    if user_password == password:
        break
    elif user_password == service_password:
        age = input('Podaj wiek: ')
        if int(age) >= 18:
            break
    else:
        print('Złe dane, jeszcze raz')
#        exit()   #wyjście z programu
print('Witamy w programie')