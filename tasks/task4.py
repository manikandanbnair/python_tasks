# Python program to find the largest element in a list.
def main():
    num = int(input("Enter the count of numbers to be added to the list:\n"))
    num_list=[]
    print("Enter the numbers into list:\n")
    for i in range(0, num):
        ele=input(f"Enter number\n")
        num_list.append(ele)
    print(f"List: {num_list}")
    largest = int(num_list[0])
    for j in range(1,num):
        try:
            if int(num_list[j]) > largest:
                largest = num_list[j]
        except Exception as e:
            print(f"Error occurred:{e}")
            exit(0)
    print(f"Largest element:{largest}")

if __name__ =="__main__":
    main()