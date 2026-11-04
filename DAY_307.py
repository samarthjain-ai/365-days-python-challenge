import streamlit as st 
st.title("Welcome to GitHub Clone")

st.write("THIS IS THE PROJECT I WAS MAKEING IN MY 365 DAY OF PYTHON CHALLANGE")


st.header("Registration")

username = st.text_input("Enter you username here")
st.caption("This will show as you profile or main name ")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password") 

if  st.button("Register"):
    if not username:
        st.error("Errorr")
    elif password != confirm_password:
        st.error("Incorrect password")

    elif len(password) <= 7:
        st.write("Too short")

    else:
        st.success("done")


st.header("Information")
st.write(username)
st.write(email)


