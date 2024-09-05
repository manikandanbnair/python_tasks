#Python program to count the frequency of each element in a list.
def main():
    num = int(input("Enter the count of elements to be added to the list:\n"))
    ele_list=[]
    print("Enter the elements into the list:\n")
    for i in range(0, num):
        ele=input(f"Enter element\n")
        ele_list.append(ele)
    print(f"List: {ele_list}")

    freq = {}
    for element in ele_list:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1


    for key in freq:
        print(f"{key}: {freq[key]}")

if __name__ =="__main__":
    main()