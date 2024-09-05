#Python program to reverse a string
def main():
    word = input("Enter the string to be reversed:\n")

    char_count = 0
    for n in word:
        char_count+=1
    j=0
    rev = ""
    for i in range(char_count-1,-1,-1):
        rev += word[i]

    print(f"Original String: {word}")
    print(f"Reversed String: {rev}")

if __name__ =="__main__":
    main()