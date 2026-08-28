import streamlit as st
import requests


st.title("📚 BOOK SYSTEM")


st.write("Add a new book")

Book = st.text_input("BOOK NAME")

Title = st.text_input("Title")

Author = st.text_input("Author name")

price = st.number_input("Price", min_value=0)


if st.button("ADD BOOK"):

    book_data = {
        "Book": Book,
        "title": Title,
        "author": Author,
        "price": price
    }

    response = requests.post(
        "http://127.0.0.1:8000/book",
        json=book_data
    )

    if response.status_code == 200:

        st.success("Book added successfully!")

        st.write(response.json())

    else:

        st.error("Something went wrong")


if st.button("Show Books"):

    response = requests.get(
        "http://127.0.0.1:8000/show_book"
    )

    if response.status_code == 200:

        st.success("ALL BOOKS")

        st.write(response.json())

    else:

        st.error("Something went wrong")


st.write("Find Book by ID")

id = st.number_input(
    "ID number",
    min_value=1,
    step=1
)


if st.button("Book by ID"):

    response = requests.get(
        f"http://127.0.0.1:8000/book/{id}"
    )

    if response.status_code == 200:

        st.success("BOOK")

        st.write(response.json())

    else:

        st.error("Something went wrong")


st.write("Update Book")

update_id = st.number_input(
    "Update ID",
    min_value=1,
    step=1
)

update_book = st.text_input("New Book Name")

update_title = st.text_input("New Title")

update_author = st.text_input("New Author")

update_price = st.number_input(
    "New Price",
    min_value=0
)


if st.button("Update Book"):

    book_data = {
        "Book": update_book,
        "title": update_title,
        "author": update_author,
        "price": update_price
    }

    response = requests.put(
        f"http://127.0.0.1:8000/update_book/{update_id}",
        json=book_data
    )

    if response.status_code == 200:

        st.success("BOOK UPDATED")

        st.write(response.json())

    else:

        st.error("Something went wrong")