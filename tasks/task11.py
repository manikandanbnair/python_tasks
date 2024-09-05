# Python program to remove duplicates from a list.
def main():
    num = int(input("Enter the count of elements to be added to the list:\n"))
    ele_list=[]
    print("Enter the elements into the list:\n")
    for i in range(0, num):
        ele=input(f"Enter element\n")
        ele_list.append(ele)
    print(f"Original List: {ele_list}")
    print(f"List with duplicates removed: {set(ele_list)}")

if __name__ =="__main__":
    main()