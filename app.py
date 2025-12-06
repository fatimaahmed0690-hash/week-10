import streamlit as st

st.set_page_config(layout="wide")

page = st.sidebar.radio("Navigation", [
    "Login",
    "Main Dashboard",
    "Threat Intelligence",
    "AI Security Assistant"
])

if page == "Login":
    from pages.Login import main
elif page == "Main Dashboard":
    from pages.Main_Dashboard import main
elif page == "Threat Intelligence":
    from pages.Threat_Intelligence import main
elif page == "AI Security Assistant":
    from pages.AI_Security_Assistant import main

main()
