from abc import ABC, abstractmethod


class ElectronicDevice(ABC):

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def power_usage(self):
        pass

    def describe(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

    @staticmethod
    def from_type(device):
        if device.lower() == "laptop":
            return Laptop("HP","Elite")
        elif device.lower() == "smartphone":
            return SmartPhone("Oppo","Reno")
        else:
            raise ValueError("Invalid Input")



class Laptop(ElectronicDevice):

    def power_usage(self):
        return 50

class SmartPhone(ElectronicDevice):
    def power_usage(self):
        return 10

def main():
    laptop = Laptop("HP","Elite book")
    smart_phone = SmartPhone("Oppo","Reno")

    print(f"Description of Laptop->")
    laptop.describe()
    smart_phone.describe()

    try:
        device1 = ElectronicDevice.from_type("Laptop")
        device1_type = device1.power_usage()
        print(f"Power usage of {device1.__class__.__name__}: {device1_type} watts per hour")

        device2 = ElectronicDevice.from_type("SmartPhone")
        device2_type = device2.power_usage()
        print(f"Power usage of {device2.__class__.__name__}: {device2_type} watts per hour")
    except ValueError as e:
        print(f"Error :{e}")
        exit(0)
if __name__ == "__main__":
    main()