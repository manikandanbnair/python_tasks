import library_module as lb

# - Add books to the library.
#  - Create a user.
#  - Allow the user to borrow a book and return it.


def main():
    print("Menu:")
    print("1.Add books to library.\n2.Create a user\n3.Borrow a book\n4.Return a borrowed book")
    choice = int(input("Enter your choice"))

    match choice:
        case 1:
            book_name = input("Enter the title of the book:\n")
            book_author = input("Enter the name of author\n")
            lb.Library.add_book(book_name,book_author)

if __name__ == "__main__":
    main()