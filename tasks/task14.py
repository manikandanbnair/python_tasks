#Python program to find all prime numbers between 1 and 100 using nested loops and calculates their sum
def main():
    def check_prime(n):
        flag = True
        for j in range(2,int(n/2)+1):
            if n % j ==0:
                flag = False
                break
            else:
                flag = True

        if flag:
            return True
        else:
            return False

    list1 = []
    sum_of_prime_numbers = 0
    for i in range(1,101):
        if check_prime(i):
            list1.append(i)
            sum_of_prime_numbers += i

    print(list1)
    print(f"Sum of prime numbers between 1 and 100: {sum_of_prime_numbers}")

if __name__ =="__main__":
    main()