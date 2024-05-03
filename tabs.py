import streamlit as st

tab1, tab2, tab3 = st.tabs(["Data Sources", "Streamlit", "Snowflake"])

with tab1:
   st.header("Transactional Data")

with tab2:
   st.header("GUI")

with tab3:
   st.header("EDW")