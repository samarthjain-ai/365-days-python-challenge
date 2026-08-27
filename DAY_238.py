from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class BOOK(BaseModel):
    Book:str
    title:str
    author:str
    price:int

class BOOK_ID(BaseModel):
    Book:str
    title:str
    author:str
    price:int
    id:int
class BOOKUpdate(BaseModel):
    Book: Optional[str] = None
    title: Optional[str] = None
    author: Optional[str] = None
    price: Optional[int] = None
    
books =[]
next_id = 1
@app.post("/book")
def add_book(book:BOOK):
    global next_id

    new_book=BOOK_ID(
        id=next_id,
        Book=book.Book,
        title=book.title,
        author=book.author,
        price=book.price
    )

    books.append(new_book)
    next_id+=1

    return "BOOK Added"


@app.get("/show_book")
def show_book():
    return books

@app.get("/book/{id}")
def book_id(id:int):
    for book in books:
        if book.id == id:
            return book
    else:
        return "BOOK NOT FOUND"

@app.put("/update_book/{id}")
def update_book(id:int,Book:BOOK):
    for book in books:
        if book.id==id:

            book.Book   = Book.Book
            book.title  = Book.title
            book.author = Book.author
            book.price  = Book.price

            return "BOOK UPDATED"

    else:
        return "BOOK NOT FOUND"


@app.patch("/patch_book/{id}")
def patch_book(id:int,BOok:BOOKUpdate):
    for book in books:
        if book.id == id:

            if BOok.Book is not None:
                book.Book = BOok.Book

            if BOok.title is not None:
                book.title = BOok.title

            if BOok.author is not None:
                book.author = BOok.author

            if BOok.price is not None:
                book.price = BOok.price

            return "BOOK partially updated successfully"

    else:
        return "Book not found"


@app.delete("/delete_book/{id}")
def delete_book(id:int,Book:BOOK):
    for book in books:
        if book.id==id:
            books.remove(book) 

    else : 
        return("BOOK NOT FOUND")



