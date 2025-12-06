import streamlit as st
from database_manager import DatabaseManager
import pandas as pd

db = DatabaseManager()

def main():
    st.title("Main Dashboard")

    incidents = db.fetch_incidents()
    if incidents:
        df = pd.DataFrame(incidents)
        st.dataframe(df)
    else:
        st.warning("No incident records found")
