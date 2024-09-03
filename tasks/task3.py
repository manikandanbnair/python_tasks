#Python program to find the factorial of a number
def fact(n):
    if n==1 or n==0:
        return  1
    else:
        return n * fact(n-1)

number = int(input("Enter the number whose factorial is to be found:\n"))
if number < 0:
    print("Please enter a positive number\n")
else:
    factorial_of_number= fact(number)
    print(f"Factorial of {number}: {factorial_of_number}")