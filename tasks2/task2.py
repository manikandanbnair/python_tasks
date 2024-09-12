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

    @classmethod
    def from_type(cls,device):
        if device.lower() == "laptop":
            brand_name = input("Enter the brand:\n")
            model_name = input("Enter the model:\n")
            battery_life = int(input("Enter the battery_life:\n"))
            print("Created instance of class Laptop:")
            print("---------------------------------")
            return Laptop(brand_name,model_name , battery_life)
        elif device.lower() == "smartphone":
            brand_name = input("Enter the brand:\n")
            model_name = input("Enter the model:\n")
            screen_size = int(input("Enter the screen_size:\n"))
            print("Created instance of class SmartPhone:")
            print("-------------------------------------")
            return Laptop(brand_name,model_name , screen_size)
        else:
            raise ValueError("Invalid Input")



class Laptop(ElectronicDevice):
    def __init__(self,  brand, model,battery_life: int):
        super().__init__(brand, model)
        self.battery_life = battery_life

    def power_usage(self):
        return 50

class SmartPhone(ElectronicDevice):
    def __init__(self, brand, model, screen_size : int):
        super().__init__(brand, model)
        self.screen_size = screen_size

    def power_usage(self):
        return 10

def main():
    try:

        laptop = Laptop("HP", "Elite book", "10")
        smart_phone = SmartPhone("Oppo", "Reno", 14)

        print(f"Laptop:")
        laptop.describe()
        print(f"Power usage: {laptop.power_usage()}")
        print()

        print(f"Smart Phone:")
        smart_phone.describe()
        print(f"Power usage: {smart_phone.power_usage()}")
        print()

        device = input("Enter Laptop or SmartPhone:\n")
        device_type = ElectronicDevice.from_type(device)

        device_power = device_type.power_usage()
        device_type.describe()
        print(f"Power usage of {device_type.__class__.__name__}: {device_power} watts per hour")

    except ValueError as e:
        print(f"Error :{e}")
        exit(0)

    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()