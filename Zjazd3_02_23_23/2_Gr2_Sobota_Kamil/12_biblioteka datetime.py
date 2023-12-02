from datetime import datetime as dt

today = dt.now()
print(today)
print(type(today))
today = str(today)
# print('Logi_' + today[11:13] + today[14:16] + '.txt')

timestamp1 = today.strftime('Moja zmiena to: %d/%m/%y/%Y.txt')
print(timestamp1)

timestamp2 = today.strftime('Moja zmiena to: %H--%M--%S.txt')
print(timestamp2)