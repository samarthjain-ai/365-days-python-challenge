class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
        pass

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author
    
    def is_long_book(self):
        if self.pages>300:
            return True
        else:
            return False
        
book1=Book("Hands-on-Machine-Learning","Aurélien Géron",484)
book2=Book("Machine Learning For Absolute Beginners","Oliver Theobal",290)
book3=Book("Grokking_Algorithms20191211-5332-1c8w1se","Aditya Y. Bhargava",235)

for book in [book1, book2, book3]:

    if book.is_long_book():
        print(f"{book.get_title()} is a long book")

    else:
        print(f"{book.get_title()} is a short book")

