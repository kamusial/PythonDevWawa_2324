class Engineer:

    def __init__(self, name):
        self.name = name
        self.salary = 10000


    def build(self):
        ...

    @property   # dla niewymagających obliczeniowo dynamicznych atrybutów
    def tax(self):
        return self.salary * 0.2

    def calculate_taxes(self):
        return self.salary * 0.2

    @staticmethod   # kiedy nie potrzebujemy self w metodzie
    def calculate_taxes_static(salary):
        return salary * 0.2

    def __str__(self):
        return self.name


michal = Engineer("Michal")
print(Engineer.calculate_taxes(michal))
print(michal.calculate_taxes())

print(michal.calculate_taxes_static(6000))

print(michal.tax)