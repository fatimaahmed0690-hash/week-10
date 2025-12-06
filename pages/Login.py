import streamlit as st
from database_manager import DatabaseManager
import hashlib

db = DatabaseManager()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = db.get_user(username)
        if user and hash_password(password) == user["password_hash"]:
            st.success("Login successful")
        else:
            st.error(" Invalid username or password")

    if st.button("Register"):
        if username.strip() and password.strip():
            if not db.get_user(username):
                db.add_user(username, hash_password(password))
                st.success("Registered successfully")
            else:
                st.warning("User already exists")
