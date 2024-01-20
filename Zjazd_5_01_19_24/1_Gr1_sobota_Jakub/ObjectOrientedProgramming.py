class Dog:
    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner

    def __str__(self):
        return f"I am {self.name}, my owner is {self.owner} who is {self.owner.age} years old and says: {self.owner.think()}"

    def think(self):
        return "Hau hau"


class Human:
    species = "Homo sapiens"

    def think(self):
        return "I think therefore I am"


class Owner(Human):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name


tim = Owner("Tim", 10)
jim = Owner("Jim", 30)
rex = Dog("Rex", 1, tim)
dex = Dog("Dex", 3, jim)

print(rex)
tim.__setattr__("age",11)
print(dex)

#print(rex.name)
#print(tim.name)
#print(rex.owner.name)

"""
Cwiczenie
Wypisac na konsole
Wynik metody think u Rexa
Wynik metody think u Tima
Wynik metody think u Tima, odwolujac sie przez bazowy obiekt Rex 
"""
#print(rex.think())
#print(tim.think())
#print(tim.species)
#print(rex.owner.think())
#print(rex)