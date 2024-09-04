
from abc import ABC , abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def get_fuel_efficiency(self):
        pass

    def describe(self):
        print(f"This is the description of type: {self.__class__.__name__}")

    @staticmethod
    def from_name(name):
        if name.lower() == "car":
            return Car()
        elif name.lower() == "truck":
            return Truck()
        else:
            raise ValueError("Invalid input")


class Car(Vehicle):
    def get_fuel_efficiency(self):
        print("Fuel efficiency of car: 25 miles per gallon")


class Truck(Vehicle):

    def get_fuel_efficiency(self):
        print("Fuel efficiency of truck: 15 miles per gallon")



def main():
    try:
        vehicle_name1 = Vehicle.from_name("Car")
        vehicle_name1.get_fuel_efficiency()

        vehicle_name2 = Vehicle.from_name("Truck")
        vehicle_name2.get_fuel_efficiency()

        car = Car()
        truck = Truck()

        car.describe()
        truck.describe()

    except ValueError as e:
        print(f"Error: {e}")
        exit(0)


if __name__ == "__main__":
    main()