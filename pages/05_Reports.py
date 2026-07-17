import streamlit as st

st.title("📄 Reports")

if "data" not in st.session_state:

    st.warning(
        "Upload dataset first."
    )

else:

    df = st.session_state["data"]

    report = f"""
ANALYTICAAI REPORT

Rows: {df.shape[0]}
Columns: {df.shape[1]}
Missing Values: {df.isnull().sum().sum()}
Duplicates: {df.duplicated().sum()}

Dataset Summary

{df.describe()}
"""

    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name="analytics_report.txt",
        mime="text/plain"
    )