class Book:

    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
            print(f'"{self.title}" borrowed successfully.')
        else:
            print(f'"{self.title}" is already borrowed.')

    def return_book(self):
        if not self.available:
            self.available = True
            print(f'"{self.title}" returned successfully.')
        else:
            print(f'"{self.title}" is already available.')

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return (
            f"Book ID : {self.book_id}\n"
            f"Title   : {self.title}\n"
            f"Author  : {self.author}\n"
            f"Status  : {status}\n"
        )


class Library:

    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []

    def add_book(self, book):

        if book in self.books:
            print("Book already exists.")

        else:
            self.books.append(book)
            print(f'"{book.title}" added successfully.')

    def show_all_books(self):

        print(f"\n===== {self.library_name} =====")

        if len(self.books) == 0:
            print("No books available.")

        for book in self.books:
            print(book)

    def search_book(self, title):

        for book in self.books:

            if book.title.lower() == title.lower():

                print("Book Found\n")
                print(book)
                return book

        print("Book not found.")
        return None
    
    def borrow_book(self, title):
        book = self.search_book(title)

        if book:
            book.borrow_book()

    def return_book(self,title):
        book=self.search_book(title)

        if  book:
            book.return_book()

    def remove_book(self,title):
        book=self.search_book(title)

        if  book:
            self.books.remove(book)
            print(f"{title} removed successfully.")

    def total_books(self):
        print(f"Total Books: {len(self.books)}")

    def available_books(self):
        for book in self.books:
            if book.available:
                print(book)

    def borrowed_books(self):
        for book in self.books:
            if not book.available:
                print(book)
        
book1 = Book("Atomic Habits", "James Clear", 101)
book2 = Book("Python Crash Course", "Eric Matthes", 102)
book3 = Book("Hands-On Machine Learning", "Aurelien Geron", 103)

library = Library("Samarth Library")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)



while True:
    menu = """
    ========== Samarth Library ==========

    1. Add Book
    2. Search Book
    3. Return Book
    4. Borrow Book
    5. Remove Book
    6. Show All Books
    7. Available Books
    8. Borrowed Books
    9. Total Books
    10. Exit
    """
    print(menu)

    try :
        choice = int(input())

        if choice == 1:
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            book_id = int(input("Enter Book ID: "))

            new_book = Book(title, author, book_id)

            library.add_book(new_book)

        elif choice ==2:
            book=input("Enter book title : ")
            library.search_book(book)

        elif choice==3:
            book=input("Enter book title : ")
            library.return_book(book)

        elif choice == 4:
            book=input("Enter book title : ")
            library.borrow_book(book)

        elif choice == 5:
            book=input("Enter book title : ")
            library.remove_book(book)

        elif choice == 6:
            library.show_all_books()

        elif choice == 7:
            library.available_books()

        elif choice == 8:
            library.borrowed_books()

        elif choice == 9:
            library.total_books()

        elif choice == 10:
            break
        else:
            print("Invalid Choice!")
    except ValueError:
        print("Plz Enter a number") 