#Python program to sort a list of elements using the bubble sort algorithm.

num = int(input("Enter the count of elements to be added to the list:\n"))
ele_list=[]
print("Enter the elements into the list:\n")
for i in range(0, num):
    ele=int(input(f"Enter element\n"))
    ele_list.append(ele)
print(f"Original List: {ele_list}")

for i in range(0,num-1):
    for j in range(0,num-i-1):
        if int(ele_list[j])>int(ele_list[j+1]):
            temp = ele_list[j+1]
            ele_list[j+1] = ele_list[j]
            ele_list[j] = temp


print(f"Sorted List: {ele_list}")