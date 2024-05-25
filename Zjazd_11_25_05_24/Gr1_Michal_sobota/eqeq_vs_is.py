print(id(3))
print(id(1+2))
print(3 == 1+2)
print(3 is 1+2)


a = [1, 2, 3]
print(id(a))
b = [1, 2, 3]
print(id(b))
print(a == b)
print(a is b)

b = a
print(a == b)
print(a is b)
