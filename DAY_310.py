import streamlit as st

with open("style.css", "r") as file:
    content = file.read()

st.markdown(f"""
<style>
{content}
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="Github Clone",
    page_icon="🤍",
    layout="centered"
    )

st.header("Github Clone")
st.subheader("Build. Collaborate. Create.")
