from abc import ABC,abstractmethod
from traceback import print_tb


class Employee(ABC):

    def __init__(self,employee_name : str):
        self.employee_name = employee_name

    @abstractmethod
    def calculate_salary(self):
        pass

    def describe(self):
        print(f"Employee:\nName: {self.employee_name}\nType:{self.__class__.__name__}")


class FullTimeEmployee(Employee):

    def __init__(self, employee_name: str):
        super().__init__(employee_name)

    def calculate_salary(self):
        return 3000

class PartTimeEmployee(Employee):

    def __init__(self, employee_name: str,hours_worked : int, hourly_rate : int):
        super().__init__(employee_name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

def main():

    full_time_employee = FullTimeEmployee("Jon")
    full_time_employee.describe()
    full_time_employee_salary = full_time_employee.calculate_salary()
    print(f"Salary:{full_time_employee_salary}\n")
    print()

    part_time_employee = PartTimeEmployee("Snow",10,250)
    part_time_employee.describe()
    part_time_employee_salary = part_time_employee.calculate_salary()
    print(f"Salary:{part_time_employee_salary}")


if __name__ == "__main__":
    main()