import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from database_manager import DatabaseManager

def main():  
    st.title("Main Security Dashboard")

    db = DatabaseManager()
    severity_data = pd.DataFrame(db.incident_by_severity())
    category_data = pd.DataFrame(db.incident_by_category())
    trend_data = pd.DataFrame(db.incident_status_trend())

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Incidents by Severity")
        if not severity_data.empty:
            fig, ax = plt.subplots()
            ax.bar(severity_data["severity"], severity_data["count"])
            st.pyplot(fig)

    with col2:
        st.subheader("Incidents by Category")
        if not category_data.empty:
            fig2, ax2 = plt.subplots()
            ax2.pie(category_data["count"], labels=category_data["category"], autopct="%1.1f%%")
            ax2.axis("equal")
            st.pyplot(fig2)

    trend_data = pd.DataFrame(db.incident_status_trend())

    if trend_data.empty:
        st.warning("No trend data available")
    else:
        fig3, ax3 = plt.subplots()
        ax3.plot(trend_data["incident_date"].values, trend_data["count"].values, marker="o")
        ax3.set_xlabel("Date")
        ax3.set_ylabel("Incidents")
        plt.xticks(rotation=45)
        st.pyplot(fig3)


    st.info("""
    🔹 High severity incidents require immediate attention  
    🔹 Categories with repeated incidents indicate vulnerable areas  
    🔹 Rising trend may indicate increasing threat activity
    """)
