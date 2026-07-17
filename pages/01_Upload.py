import streamlit as st
import pandas as pd
import numpy as np


st.title("📂 Dataset Upload")
st.markdown("Upload your dataset to begin analysis.")

uploaded_file = st.file_uploader(
    "Choose a CSV or Excel file",
    type=["csv", "xlsx", "xls"]
)

if uploaded_file:

    # Read file
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)

        else:
            df = pd.read_excel(uploaded_file)

    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        st.stop()

    st.session_state["data"] = df

    st.success("✅ Dataset Uploaded Successfully")

    st.divider()

    # -----------------------------
    # Dataset Overview
    # -----------------------------

    total_rows = df.shape[0]
    total_columns = df.shape[1]

    missing = df.isnull().sum().sum()

    duplicates = df.duplicated().sum()

    memory = round(df.memory_usage(deep=True).sum() / (1024 * 1024), 2)

    quality = round(
        (
            1
            - (
                (missing + duplicates)
                / max(total_rows * total_columns, 1)
            )
        )
        * 100,
        2,
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Rows", f"{total_rows:,}")

    col2.metric("Columns", total_columns)

    col3.metric("Missing Values", missing)

    col4.metric("Duplicates", duplicates)

    col5.metric("Quality Score", f"{quality}%")

    st.divider()

    # -----------------------------
    # Data Types
    # -----------------------------

    st.subheader("Dataset Structure")

    numeric = len(df.select_dtypes(include=np.number).columns)

    categorical = len(
        df.select_dtypes(include="object").columns
    )

    datetime = len(
        df.select_dtypes(include="datetime").columns
    )

    boolean = len(
        df.select_dtypes(include="bool").columns
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Numeric", numeric)

    c2.metric("Categorical", categorical)

    c3.metric("Datetime", datetime)

    c4.metric("Boolean", boolean)

    st.divider()

    # -----------------------------
    # Dataset Preview
    # -----------------------------

    st.subheader("Dataset Preview")

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

    st.divider()

    # -----------------------------
    # Column Details
    # -----------------------------

    st.subheader("Column Information")

    info = pd.DataFrame(
        {
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str),
            "Missing": df.isnull().sum().values,
            "Unique Values": df.nunique().values,
        }
    )

    st.dataframe(
        info,
        use_container_width=True
    )

    st.divider()

    # -----------------------------
    # Missing Values
    # -----------------------------

    st.subheader("Missing Value Analysis")

    missing_df = (
        df.isnull()
        .sum()
        .reset_index()
    )

    missing_df.columns = [
        "Column",
        "Missing Values",
    ]

    missing_df["Missing %"] = (
        missing_df["Missing Values"]
        / len(df)
        * 100
    ).round(2)

    st.dataframe(
        missing_df,
        use_container_width=True
    )

    st.divider()

    # -----------------------------
    # Statistical Summary
    # -----------------------------

    st.subheader("Statistical Summary")

    st.dataframe(
        df.describe(include="all").fillna("-"),
        use_container_width=True
    )

    st.divider()

    # -----------------------------
    # Download Clean Dataset
    # -----------------------------

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Download Dataset",
        csv,
        file_name="dataset.csv",
        mime="text/csv",
    )

else:
    st.info("Please upload a CSV or Excel file.")