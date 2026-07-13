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

        # Check if the book already exists
        if book in self.books:
            print("Book already exists.")

        else:
            self.books.append(book)
            print(f'"{book.title}" added successfully.')

    def show_all_books(self):

        print(f"\n===== {self.library_name} =====")

        if len(self.books) == 0:
            print("No books available.")
            return

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



book1 = Book("Atomic Habits", "James Clear", 101)
book2 = Book("Python Crash Course", "Eric Matthes", 102)
book3 = Book("Hands-On Machine Learning", "Aurelien Geron", 103)

library = Library("Samarth Library")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print()

library.show_all_books()

print()

library.search_book("Atomic Habits")

print()

library.search_book("Harry Potter")