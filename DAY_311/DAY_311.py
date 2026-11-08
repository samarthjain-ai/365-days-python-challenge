import streamlit as st

st.set_page_config(
    page_title="🪔 Light Up Your Coding Journey",
    page_icon="🪔",
    layout="centered"
)

with open("style311.css", "r", encoding="utf-8") as file:
    content = file.read()

st.markdown(
    f"""
    <style>
    {content}
    </style>
    """,
    unsafe_allow_html=True
)

# Registration Card
st.markdown(
    """
    <div class="registration-card">
        <h3>Create Your Account</h3>
    </div>
    """,
    unsafe_allow_html=True
)

st.header("Your Year, Your Journey ✨")

st.subheader(
    "A new chapter. A new opportunity. A stronger you."
)

username = st.text_input("What should we call you?")

if st.button("Begin My Journey ✨"):

    if not username.strip():
        st.warning("Please enter your name first!")

    else:
        st.success(
            f"Welcome, {username.strip()}! "
            "Your journey starts here. 🪔"
        )
