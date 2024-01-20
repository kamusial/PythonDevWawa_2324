class Dog:
    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner

    def __str__(self):
        return f"I am Rex, my owner is Tim who says: I think therefore I am."

    def think(self):
        return "Hau hau"


class Human:
    species = "Homo sapiens"

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

"""
Cwiczenie
Wypisac na konsole
Wynik metody think u Rexa
Wynik metody think u Tima
Wynik metody think u Tima, odwolujac sie przez bazowy obiekt Rex 
"""
print(rex.think())
print(tim.think())
print(tim.species)
print(rex.owner.think())

print(rex)