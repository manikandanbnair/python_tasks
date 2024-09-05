#Python program to calculate the sum of each row in a 2D and 3D list
# 2D
def main():
    row = int(input("Enter the number of rows:\n"))
    col = int(input("Enter the number of columns:\n"))

    arr1 =[]
    arr2 =[]
    print("Enter the elements:\n")
    for i in range(0, row):
        for j in range(0, col):
            arr2.append(int(input()))
        arr1.append(arr2)
        arr2 = []

    print(f"2D List:\n{arr1}")

    for i in arr1:
        sum_of_elements = 0
        for j in i:
            sum_of_elements += j
        print(f"Sum of row {i}:{sum_of_elements}")


    #3D
    print("Enter the dimensions of the 3D list to be  created:\n")
    n1 = int(input("Enter dimension number 1:\n"))
    n2 = int(input("Enter dimension number 2:\n"))
    n3 = int(input("Enter dimension number 3:\n"))

    arr1 = []
    arr2 = []
    arr3 = []
    print("Enter the elements:\n")
    for i in range(0, n3):
        for j in range(0, n2):
            for k in range(0,n1):
                print(f"{i}{j}{k}:")
                arr3.append(int(input()))
            arr2.append(arr3)
            arr3 = []
        arr1.append(arr2)
        arr2 = []

    for i in arr1:
        total_sum =0
        for j in i:
            sum_of_elements = 0
            for k in j:
                sum_of_elements += k
            total_sum =total_sum + sum_of_elements
        print(f"Sum of row {i}:{total_sum}")

    print(arr1)

if __name__ =="__main__":
    main()