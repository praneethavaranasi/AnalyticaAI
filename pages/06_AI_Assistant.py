import streamlit as st
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")

st.title("🤖 AI Data Assistant")

if not api_key:
    st.error(
        "Gemini API Key not found. Create a .env file and add GEMINI_API_KEY."
    )
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-2.0-flash")

def safe_generate_content(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "quota" in error_msg.lower() or "limit" in error_msg.lower():
            st.error(
                "⚠️ **Gemini API Quota Exceeded (Error 429)**: You have exceeded the free tier quota for this API key. "
                "Please wait a few seconds/minutes and try again, or check your billing plan/create a new key "
                "in [Google AI Studio](https://aistudio.google.com/)."
            )
        else:
            st.error(f"Error calling Gemini API: {error_msg}")
        return None

# Check dataset
if "data" not in st.session_state:

    st.warning(
        "Please upload a dataset first."
    )

else:

    df = st.session_state["data"]

    st.success(
        f"Dataset Loaded: {df.shape[0]} rows × {df.shape[1]} columns"
    )

    st.subheader("Ask Questions About Your Dataset")

    question = st.text_input(
        "Example: Give me key insights from this dataset"
    )

    if st.button("Analyze"):

        if question.strip() == "":
            st.warning(
                "Please enter a question."
            )

        else:

            with st.spinner(
                "Analyzing dataset..."
            ):

                try:

                    dataset_info = f"""
                    Dataset Shape:
                    {df.shape}

                    Columns:
                    {list(df.columns)}

                    Data Types:
                    {df.dtypes.to_string()}

                    Missing Values:
                    {df.isnull().sum().to_string()}

                    Statistical Summary:
                    {df.describe(include='all').to_string()}

                    First 50 Rows:
                    {df.head(50).to_string()}
                    """

                    prompt = f"""
                    You are a professional Senior Data Analyst.

                    Analyze the dataset below.

                    {dataset_info}

                    User Question:
                    {question}

                    Instructions:
                    - Answer based only on the dataset.
                    - Give clear business insights.
                    - Use bullet points when appropriate.
                    - Mention trends, anomalies, opportunities, and risks.
                    - If information is unavailable, say so.
                    """

                    res_text = safe_generate_content(prompt)
                    if res_text:
                        st.subheader(
                            "🤖 AI Response"
                        )
                        st.write(res_text)

                except Exception as e:

                    st.error(
                        f"Error: {str(e)}"
                    )

    st.divider()

    st.subheader("Quick Questions")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Dataset Summary"):

            prompt = f"""
            Summarize this dataset.

            Columns:
            {list(df.columns)}

            Summary:
            {df.describe(include='all').to_string()}
            """

            res_text = safe_generate_content(prompt)
            if res_text:
                st.write(res_text)

        if st.button("Business Insights"):

            prompt = f"""
            Give 10 important business insights from this dataset.

            Dataset:
            {df.head(200).to_string()}
            """

            res_text = safe_generate_content(prompt)
            if res_text:
                st.write(res_text)

    with col2:

        if st.button("Recommendations"):

            prompt = f"""
            Provide actionable business recommendations.

            Dataset:
            {df.head().to_string()}
            """

            res_text = safe_generate_content(prompt)
            if res_text:
                st.write(res_text)

        if st.button("Find Anomalies"):

            prompt = f"""
            Identify unusual patterns or anomalies.

            Dataset:
            {df.head(200).to_string()}
            """

            res_text = safe_generate_content(prompt)
            if res_text:
                st.write(res_text)