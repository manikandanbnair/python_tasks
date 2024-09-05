#Python program to find the second-largest number in a list.
from operator import index
def main():
    num = int(input("Enter the count of numbers to be added to the list:\n"))
    num_list=[]
    print("Enter the numbers into list:\n")
    for i in range(0, num):
        ele=int(input(f"Enter number\n"))
        num_list.append(ele)
    print(f"List: {num_list}")
    largest = num_list[0]
    second_largest = -100000000

    for j in range(1,num):
        if num_list[j] > largest:
            second_largest = largest
            largest = num_list[j]

        elif num_list[j] > second_largest and num_list[j]!= largest:
            second_largest = num_list[j]


    print(f"Second Largest element:{second_largest}")

if __name__ =="__main__":
    main()