
class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
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

        return f"{self.title} | {self.author} | {status}"


class Library:

    def __init__(self, library_name):
        self.library_name = library_name
        self.list_of_books = []

    def add_book(self, book):

        self.list_of_books.append(book)
        print(f'"{book.title}" added successfully.')

    def show_books(self):

        print(f"\n===== {self.library_name} =====")

        if len(self.list_of_books) == 0:
            print("No books available.")
            return

        for book in self.list_of_books:
            print(book)

    def borrow_book(self, title):

        for book in self.list_of_books:

            if book.title.lower() == title.lower():

                book.borrow_book()
                return

        print("Book not found.")

    def return_book(self, title):

        for book in self.list_of_books:

            if book.title.lower() == title.lower():

                book.return_book()
                return

        print("Book not found.")


book1 = Book("Python Crash Course", "Eric Matthes")
book2 = Book("Atomic Habits", "James Clear")
book3 = Book("Hands-On Machine Learning", "Aurelien Geron")

library = Library("Samarth Library")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.show_books()

print()

library.borrow_book("Atomic Habits")

print()

library.show_books()

print()

library.return_book("Atomic Habits")

print()

library.show_books()