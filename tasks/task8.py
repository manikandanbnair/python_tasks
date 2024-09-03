#Python program to find the common elements between two lists.
num1 = int(input("Enter the count of elements to be added to the list 1:\n"))
ele_list1=[]
print("Enter the elements into the list:\n")
for i in range(0, num1):
    ele=input(f"Enter element\n")
    ele_list1.append(ele)

num2 = int(input("Enter the count of elements to be added to the list 2:\n"))
ele_list2=[]
print("Enter the elements into the list:\n")
for i in range(0, num2):
    ele=input(f"Enter element\n")
    ele_list2.append(ele)

print(f"List 1: {ele_list1}")
print(f"List 2: {ele_list2}")

common_list = []
for item in ele_list1:
    if item in ele_list2:
        common_list.append(item)
if len(common_list) != 0:
    print(f"The elements common in both the lists:\n{common_list}")
else:
    print("No common elements present")
