import streamlit as st
from auth import authenticate, register_user

def main():
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        success, msg = authenticate(username, password)
        if success:
            st.success(msg)
        else:
            st.error(msg)

    if st.button("Register"):
        if username.strip() and password.strip():
            success, msg = register_user(username, password)
            if success:
                st.success(msg)
            else:
                st.warning(msg)
