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

                    response = model.generate_content(
                        prompt
                    )

                    st.subheader(
                        "🤖 AI Response"
                    )

                    st.write(
                        response.text
                    )

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

            response = model.generate_content(
                prompt
            )

            st.write(response.text)

        if st.button("Business Insights"):

            prompt = f"""
            Give 10 important business insights from this dataset.

            Dataset:
            {df.head(200).to_string()}
            """

            response = model.generate_content(
                prompt
            )

            st.write(response.text)

    with col2:

        if st.button("Recommendations"):

            prompt = f"""
            Provide actionable business recommendations.

            Dataset:
            {df.head().to_string()}
            """

            response = model.generate_content(
                prompt
            )

            st.write(response.text)

        if st.button("Find Anomalies"):

            prompt = f"""
            Identify unusual patterns or anomalies.

            Dataset:
            {df.head(200).to_string()}
            """

            response = model.generate_content(
                prompt
            )

            st.write(response.text)