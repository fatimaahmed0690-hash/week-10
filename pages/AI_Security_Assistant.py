import streamlit as st
from ai_helper import ask_ai

def main():
    st.title("AI Security Assistant")

    question = st.text_area("Ask a cybersecurity question:")

    if st.button("Ask AI"):
        if question.strip():
            answer = ask_ai(question)
            st.success(answer)
        else:
            st.warning("Please enter a question.")
