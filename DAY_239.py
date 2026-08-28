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


