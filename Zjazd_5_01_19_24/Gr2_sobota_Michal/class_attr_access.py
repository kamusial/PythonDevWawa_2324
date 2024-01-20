class Animal:
    amount_of_heads = 1

    def __init__(self, species: str, name: str):
        self.species = species
        self.name = name
        self._calories_left = 4000

    def eat(self):
        self._calories_left += 1000


    def __convert_calories_to_joule(self):
        ...

    def print_calories_left(self):
        print(self._calories_left)


class Crocodile(Animal):
    def eat(self):
        self._calories_left += 2000

    def dive(self):
        ...


andrew = Crocodile("crocodile", "Ania")
miau = Animal("cat", "Nyanko")
print(Animal.amount_of_heads)
# andrew._Animal__calories_left += 6000  # name mangling, tak nie robimy!! :<
andrew.print_calories_left()



andrew.eat()

"""
Podsumowanie:
.public - można wszędzie
._protected - można w Animal oraz w Crocodile
.__private - można TYLKO w Animal
"""