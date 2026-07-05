class Library:

    def __init__(self,books):
        self.books=books
        pass

    def __len__(self):
        return len(self.books)
    
library = Library(["Python","AI","ML","DSA"])

print(len(library))