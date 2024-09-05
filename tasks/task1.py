# Python program to convert Fahrenheit to Celsius and back, or inches to centimeters and back
def main():
    option = 0
    while option != 5:
        print()
        print("Menu\n1.Convert Fahrenheit to Celsius\n"
              "2.Convert Celsius to Fahrenheit\n"
              "3.Convert Inches to Centimeters\n"
              "4.Convert Centimeters to Inches\n"
              "5.Exit\n")
        option = int(input("Enter your option\n"))
        if option == 1:
            temp = float(input("Enter the temperature in Fahrenheit:\n"))
            print(f"Temperature in Fahrenheit: {temp}\nTemperature in Celsius: {round((temp - 32)/1.8,2)}")
        elif option == 2:
            temp =float(input("Enter the temperature in Celsius:\n"))
            print(f"Temperature in Celsius: {temp}\nTemperature in Fahrenheit: {temp * 1.8 +32}")
        elif option == 3:
            temp = float(input("Enter the length in Inches:\n"))
            print(f"Length in Inches: {temp}\nLength in Centimeters: {temp * 2.54}")
        elif option == 4:
            temp = float(input("Enter the length in Centimeters:\n"))
            print(f"Length in Centimeters: {temp}\nLength in Inches: {temp / 2.54}")
        elif option == 5:
            print("Exiting")
            break
        else:
            print("Invalid option. Enter a valid option")

if __name__=="__main__":
    main()