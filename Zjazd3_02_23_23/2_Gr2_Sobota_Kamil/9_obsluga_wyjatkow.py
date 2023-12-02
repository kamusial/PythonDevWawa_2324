def convert(data):
    try:
        data = int(data)
        print('Skowertowano do int')
        return data
    except ValueError:
        try:
            data = float(data)
            print('Skowertowano do float')
            return data
        except ValueError:
            print('Zostaje string')
            return data


x = input('Podaj dane: ')
x = convert(x)

print('dalsza czesc kodu')