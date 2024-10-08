#Python program to check if a string is a palindrome without using an inbuilt string functions.
from distutils.command.check import check
def check_palindrome(word : str):
    try:
        char_count = 0

        for n in word:
            char_count+=1

        length_of_word = char_count

        j = length_of_word-1
        flag = False
        for i in range(int(length_of_word/2)):
            if word[i] == word[j]:
                flag = True
                j-=1
                i+=1
            else:
                flag = False
                break

        if flag:
            print(f"The string {word} is a valid palindrome.")
        else:
            print(f"The string {word} is not a valid palindrome.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    word = input("Enter the word to be checked if it is a palindrome or not:\n")
    check_palindrome(word)
if __name__ =="__main__":
    main()