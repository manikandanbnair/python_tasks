import library_module as lb

book_id_unique = 1
user_id_unique = 1

def main():
    global book_id_unique, user_id_unique
    lib = lb.Library()
    while True:
        print("Menu:")
        print("1.Add books to library.\n2.Remove a book.\n3.Search for a book\n4.Create a user\n5.Borrow a book\n6.Return a borrowed book.\n7.Track your borrowed book list.\n8.List of all available book in library")
        choice = int(input("Enter your choice\n"))
        try:
            match choice:
                case 1:
                    book_name = input("Enter the title of the book:\n")
                    book_author = input("Enter the name of author\n")
                    book_id = book_id_unique
                    book =lb.Book(book_id,book_name,book_author)
                    lib.add_book(book)
                    book_id_unique += 1

                case 2:
                    try:
                        book_id = int(input("Enter the ID of book to be removed:\n"))
                        book = lib.get_book_by_id(book_id)
                        if book is not None:
                            book.remove_book(book_id)
                        else:
                            print("Invalid Book ID\n")
                    except ValueError:
                        print("Book ID must be of type integer\n")
                case 3:
                    book_name = input("Enter the name of the book to be searched for:\n")
                    lb.Library().search_for_book(book_name)
                case 4:
                    user_id = user_id_unique
                    user_name = input("Enter your name\n")
                    user_id_unique += 1

                    user = lb.LibraryUser(user_id,user_name)
                    lb.LibraryUser(user_id,user_name).add_user(user)

                case 5:
                    try:
                        user_id = int(input("Enter your user ID:\n"))
                        user = lb.LibraryUser.get_user_by_id(user_id)
                        if user is not None:
                            book_id = int(input("Enter the book ID you want to borrow\n"))
                            book = lb.Library.get_book_by_id(book_id)
                            if book is not None:
                                user.borrow_book(user_id,book_id)
                            else:
                                print("Invalid Book ID\n")
                        else:
                            print("Invalid User\n")
                    except ValueError:
                        print("IDs must be of type integer")

                case 6:
                    try:

                        user_id = int(input("Enter your user ID:\n"))
                        user = lb.LibraryUser.get_user_by_id(user_id)
                        if user is not None:
                            book_id = int(input("Enter the book ID you want to return\n"))
                            book = lib.get_book_by_id(book_id)
                            if book is not None:
                                user.return_borrowed_book(user_id, book_id)
                            else:
                                print("Invalid Book ID\n")
                        else:
                            print("Invalid User\n")
                    except ValueError:
                        print("IDs must be of type integer")

                case 7:
                    try:
                        user_id = int(input("Enter your user ID:\n"))
                        user = lb.LibraryUser.get_user_by_id(user_id)
                        if user is not None:
                            user.get_all_borrowed_books(user_id)
                        else:
                            print("Invalid User\n")

                    except ValueError:
                        print("ID must be of type integer")
                case 8:
                    book = lib.get_all_books()
                    current_book = None
                    while True:
                        choice = int(input("Enter 1 to show next book:\n"))
                        if choice == 1:
                            try:
                                if current_book is None:
                                    current_book = next(book)
                                else:
                                    try:
                                        current_book = next(book)
                                    except StopIteration:
                                        print("No more books to be shown")
                                        current_book = None
                                        break
                            except StopIteration:
                                print("No more books")
                                current_book = None
                        else:
                            break
                        if current_book is not None:
                            current_book.book_details()


        except Exception as e:
            print(f"{e}")



if __name__ == "__main__":
    main()