from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def get_fuel_efficiency(self):
        pass

    def describe(self):
        print(f"This is the description of type:{self.__class__.__name__}")

    @classmethod
    def from_name(cls, name):
        if name.lower() == "car":
            print("Created instance of class: Car")
            return Car()
        elif name.lower() == "truck":
            print("Created instance of class: Truck")
            return Truck()
        else:
            raise ValueError(f"Invalid input '{name}'")


class Car(Vehicle):
    def get_fuel_efficiency(self):
        return 25


class Truck(Vehicle):

    def get_fuel_efficiency(self):
        return 15


def main():
    try:
        print()
        car = Car()
        car.describe()

        print()
        truck = Truck()
        truck.describe()

        print()

        vehicle_name = Vehicle.from_name(input("Enter Car or Truck:\n"))
        vehicle_name.describe()
        print(f"Fuel efficiency :{vehicle_name.get_fuel_efficiency()} miles per gallon")



    except ValueError as e:
        print(f"Error: {e}")
        exit(0)


if __name__ == "__main__":
    main()
