import streamlit as st

st.set_page_config(
    page_title="GitHub Clone | Sign Up",
    page_icon="🩵",
    layout="centered")

with open("style.css", "r", encoding="utf-8") as file:
    css = file.read()

st.markdown(
    f"<style>{css}</style>",
    unsafe_allow_html=True)

st.title("Create your account")
st.write("Join our developer community.")


import streamlit as st

st.set_page_config(
    page_title="GitHub Clone | Sign Up",
    page_icon="🩵",
    layout="centered")

with open("style.css", "r", encoding="utf-8") as file:
    css = file.read()

st.markdown(
    f"<style>{css}</style>",
    unsafe_allow_html=True)

st.title("Create your account")
st.write("Join our developer community.")

with st.form("registration_form"):

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm password", type="password")

    submit = st.form_submit_button("Sign Up")

if submit:
    if not username or not email or not password or not confirm_password:
        st.error("All fields are required.")

    elif password != confirm_password:
        st.error("Passwords do not match.")

    else:
        st.success("Account created!")

