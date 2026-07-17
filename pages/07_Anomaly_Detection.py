import streamlit as st
from utils.anomaly import detect_anomalies

st.title("🚨 Anomaly Detection")

if "data" not in st.session_state:

    st.warning(
        "Upload dataset first."
    )

else:

    df = st.session_state["data"]

    anomalies = detect_anomalies(df)

    st.subheader(
        "Detected Anomalies"
    )

    st.dataframe(anomalies)