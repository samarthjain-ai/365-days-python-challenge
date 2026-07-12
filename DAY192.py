class Book:
    def __init__(self,title,author,book_id):
        self.title=title
        self.author=author
        self.book_id=book_id
        self.available=True
        pass

    def borrow_book(self):
        if self.available: 
            self.available=False
            print("Book borrowed")
        else:
            print("book was not avalable")
    
    def return_book(self):
        if not self.available:
            self.available=True
            print("Book retuned")
        else:
            print("Book is already Avalable")


    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return (
            f"Book ID : {self.book_id}\n"
            f"Title   : {self.title}\n"
            f"Author  : {self.author}\n"
            f"Status  : {status}"
        )
    
book1 = Book("Atomic Habits", "James Clear", 101)

print(book1)
 
book1.borrow_book()
print(book1)

book1.return_book()
print(book1)

 