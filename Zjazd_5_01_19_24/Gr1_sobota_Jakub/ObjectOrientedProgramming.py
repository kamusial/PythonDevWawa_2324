class Dog:
    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner

    def think(self):
        return "Hau hau"


class Human:
    def think(self):
        return "I think therefore I am."


class Owner(Human):
    def __init__(self, name, age):
        self.name = name
        self.age = age


tim = Owner("Tim", 10)
rex = Dog("Rex", 1, tim)

print(rex.name)
print(tim.name)
print(rex.owner.name)