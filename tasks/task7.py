#Python program to check if a number is prime.
num = int(input("Enter a number to check if it is prime or not:\n"))

flag =True

for i in range(2,int(num/2)+1):
    if num % i == 0:
        flag = False
        break
    else:
        flag = True

if flag:
    print(f"The number {num} is a prime number")
else:
    print(f"The number {num} is not a prime number")