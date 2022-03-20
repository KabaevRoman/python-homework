"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, new_cargo):
        if self.cargo + new_cargo > self.max_cargo:
            raise CargoOverload
        self.cargo += new_cargo

    def remove_all_cargo(self):
        temp = self.cargo
        self.cargo = 0
        return temp
