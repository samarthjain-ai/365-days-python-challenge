import streamlit as st 

st.set_page_config(
    page_title="GitHub Clone",
    page_icon="💻",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background-color: #0d1117;
}

h1, h2, h3, p, label {
    color: white !important;
}

.stButton > button {
    background-color: #238636;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 10px 25px;
}

.stButton > button:hover {
    background-color: #2ea043;
    color: white;
}

[data-testid="stFormSubmitButton"] button {
    background-color: #238636;
    color: white;
    border: none;
    border-radius: 8px;
    width: 100%;
    height: 45px;
    font-weight: bold;
}

[data-testid="stFormSubmitButton"] button:hover {
    background-color: #2ea043;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.header("GitHub Clone")


with st.form("Registation fome"):

    username = st.text_input("Username")
    email = st.text_input("Email",type="email")
    password = st.text_input("Password",type="password")
    confirm_password = st.text_input("confirm_password",type="password")

    if st.form_submit_button("Create Account",type="primary"):

        if not username or not email or not password or not confirm_password:
            st.error("All fields are required")

        elif password != confirm_password:
            st.error("Incorrect password")

        elif len(password) < 8:
            st.error("Password must be at least 8 characters long.")

        else:
            st.success("Access given.")



# import streamlit as st

# if "count" not in st.session_state:
#     st.session_state.count = 0

# if st.button("Click me"):
#     st.session_state.count += 90

# st.write("Button clicked:", st.session_state.count)