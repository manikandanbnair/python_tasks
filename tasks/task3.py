#Python program to find the factorial of a number

def fact(n):
    if n==1 or n==0:
        return  1
    else:
        return n * fact(n-1)

def main():
    try:
        number = int(input("Enter the number whose factorial is to be found:\n"))
        factorial_of_number = fact(number)
        print(f"Factorial of {number}: {factorial_of_number}")
    except ValueError:
        print("Error:Enter a valid number")
    except RecursionError:
        print("Error: Enter a positive number")

if __name__ =="__main__":
    main()