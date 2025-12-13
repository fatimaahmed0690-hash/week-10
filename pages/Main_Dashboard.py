import streamlit as st
import pandas as pd
from database_manager import DatabaseManager

db = DatabaseManager()

def main():
    st.title("Main Dashboard")

    incidents = db.fetch_incidents()
    if incidents:
        df = pd.DataFrame(incidents)
        st.dataframe(df)
    else:
        st.warning("No incident records found")
