class Book:
    def __init__(self,book_id,book_title,book_author):
        self.book_id = book_id
        self.book_title = book_title
        self.book_author = book_author

    def book_details(self):
        print(f"Book_id: {self.book_id}")
        print(f"Book_Title:{self.book_title}")
        print(f"Book_Author: {self.book_author}")

class Library:

    book_list ={}
    borrowed_book_list = []
    #use generator function to yield each book's details
    @classmethod
    def get_book_by_id(cls,book_id):
        if book_id in cls.book_list:
            return cls.book_list[book_id]
        else:
            return None

    def add_book(self,book):
        self.book_list[book.book_id] = book
        print(self.book_list)



    def remove_book(self,book_id):
       if book_id in self.book_list.keys():
            book_info = self.book_list[book_id]
            del self.book_list[book_id]
            print(f"Successfully removed book titled {book_info.book_title} from Library\n")
       else:
           print("Invalid Book ID\n")


    def search_for_book(self,book_name):
        book_flag = False
        for book_info in self.book_list.values():
            if book_name.lower() in book_info.book_title.lower():
                print(f"Book Name: {book_info.book_title}, Author: {book_info.book_author}")
                book_flag = True
        if not book_flag:
            print("Cannot find book with the given input\n")


    def get_all_books(self):
        for book in self.book_list.values():
            yield book


class User:

    def __init__(self,user_id,user_name):
        self.user_id = user_id
        self.user_name = user_name

    def display_user(self):
        print(f"User_id:{self.user_id }")
        print(f"User_name:{self.user_name}")

class LibraryUser(User):
    user_list = {}
    user_borrowed_list = {}

    def __init__(self, user_id, user_name):
        super().__init__(user_id, user_name)

    @classmethod
    def get_user_by_id(cls,user_id):
        if user_id in cls.user_list:
            return cls.user_list[user_id]
        else:
            return None

    def add_user(self,user):
        self.user_list[user.user_id] = user

        print(f"User created:\n User ID: {user.user_id} \n Username:{user.user_name}")


    def borrow_book(self,user_id,book_id):

        if book_id not in Library.borrowed_book_list:
            Library.borrowed_book_list.append(book_id)
            if user_id not in self.user_borrowed_list:
                self.user_borrowed_list[user_id] = []
            self.user_borrowed_list[user_id].append(book_id)
            print(f"Successfully borrowed book with ID {book_id}")
        else:
            print("The book is currently unavailable.")


    def return_borrowed_book(self,user_id,book_id):

        if user_id in self.user_borrowed_list and book_id not in self.user_borrowed_list[user_id]:
            print(f"You have not borrowed the book with ID {book_id}.\n")
        else:
            Library.borrowed_book_list.remove(book_id)
            self.user_borrowed_list[user_id].remove(book_id)
            print("Successfully returned book")

    def get_all_borrowed_books(self,user_id):

        if user_id not in self.user_borrowed_list or  self.user_borrowed_list[user_id] == []:
            user = self.user_list[user_id]
            user.display_user()
            print("You borrowed list is empty")
        else:
            user = self.user_list[user_id]
            user.display_user()
            print(f"Borrowed List:\nBook IDs: {self.user_borrowed_list[user_id]}")


    def get_all_users(self):
        for user in self.user_list.values():
            user.display_user()





