# Jaime S.
# 11/9/2021
# This is a program that will print a car's specifications or attributes that are assigned as (car1 & car2)
# (These attributes can be modified and you can add more than 1 car)
# Helpful information: The code works by simply by running it or modifying its car specifications.

class car:  # defines a car's class specifications (through the entire section)
    def __init__(self, model, year, color, type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacturer = manufacturer

    # Entire section  defines & returns/stops iterations/repetitions
    def get_type(self):
        return self.type

    def get_manufacturer(self):
        return self.manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def fullspecs(self):
        return self.model + ' ' + str(self.year) + ' ' + self.color + ' ' + self.type + ' ' + self.manufacturer


# These can be modified.
car1 = car("Sports", 2021, "Blue", "limited", "Honda")  # Car specifications
car2 = car("Civic", 2020, "Black", "Sedan", "Honda")  # Car specifications

print(car1.get_color())  # Will print car1 color
print(car2.get_color())  # Will print car2 color
print(car1.fullspecs())  # Will print car1 full specifications
print(car1.fullspecs())  # Will print car2 full specifications
