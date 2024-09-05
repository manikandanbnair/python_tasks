#Python program to print a diamond pattern using nested loops.
def main():
    rows = int(input("Enter number of rows:\n"))

    #upper half
    for i in range(0,rows):
        for j in range(0,rows-i-1):
            print(" ",end="")
        for j in range(0,i+1):
            print("* ",end="")
        print()

    #lower half
    for i in range(0,rows-1):
        for j in range(0,i+1):
            print(" ",end="")
        for j in range(0, rows - i - 1):
            print("* ", end="")
        print()

if __name__ =="__main__":
    main()