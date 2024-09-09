# Python program to find the largest element in a list.
def largest_element(num_list,num):
    try:
        print(f"List: {num_list}")
        largest = int(num_list[0])
        for j in range(1,num):
            if int(num_list[j]) > largest:
                largest = int(num_list[j])
        print(f"Largest element:{largest}")
    except ValueError:
        print("Error:Input valid number")

def main():
    try:
        num = int(input("Enter the count of numbers to be added to the list:\n"))
        num_list=[]
        print("Enter the numbers into list:\n")
        for i in range(0, num):
            ele=input(f"Enter number\n")
            num_list.append(ele)
        largest_element(num_list,num)
    except ValueError:
        print("Enter a valid number")
if __name__ =="__main__":
    main()