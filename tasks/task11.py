# Python program to remove duplicates from a list.
num = int(input("Enter the count of elements to be added to the list:\n"))
ele_list=[]
print("Enter the elements into the list:\n")
for i in range(0, num):
    ele=input(f"Enter element\n")
    ele_list.append(ele)
print(f"Original List: {ele_list}")

freq = []

for item in ele_list:
    if item not in freq:
        freq.append(item)
print(f"List with duplicates removed: {freq}")