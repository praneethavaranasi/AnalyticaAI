import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Executive Analytics Dashboard")

if "data" not in st.session_state:
    st.warning("Please upload a dataset first.")
    st.stop()

df = st.session_state["data"]

# ---------------------------------------------------
# Sidebar Filters
# ---------------------------------------------------

st.sidebar.header("Dashboard Filters")

show_rows = st.sidebar.slider(
    "Rows to Preview",
    5,
    100,
    10
)

numeric_columns = df.select_dtypes(include=np.number).columns.tolist()

# ---------------------------------------------------
# KPI CARDS
# ---------------------------------------------------

rows = df.shape[0]
columns = df.shape[1]
missing = int(df.isnull().sum().sum())
duplicates = int(df.duplicated().sum())

memory = round(
    df.memory_usage(deep=True).sum() / 1024**2,
    2
)

quality = round(
    (
        1 -
        ((missing + duplicates) /
        max(rows * columns, 1))
    ) * 100,
    2
)

st.subheader("Dataset Overview")

c1, c2, c3, c4, c5, c6 = st.columns(6)

c1.metric("Rows", f"{rows:,}")
c2.metric("Columns", columns)
c3.metric("Missing", missing)
c4.metric("Duplicates", duplicates)
c5.metric("Memory", f"{memory} MB")
c6.metric("Quality", f"{quality}%")

st.divider()

# ---------------------------------------------------
# Dataset Preview
# ---------------------------------------------------

st.subheader("Dataset Preview")

st.dataframe(
    df.head(show_rows),
    use_container_width=True
)

st.divider()

# ---------------------------------------------------
# Data Types
# ---------------------------------------------------

st.subheader("Column Summary")

summary = pd.DataFrame({

    "Column": df.columns,

    "Data Type": df.dtypes.astype(str),

    "Missing Values": df.isnull().sum(),

    "Unique Values": df.nunique()

})

st.dataframe(
    summary,
    use_container_width=True
)

st.divider()

# ---------------------------------------------------
# Numeric Summary
# ---------------------------------------------------

if len(numeric_columns):

    st.subheader("Statistical Summary")

    st.dataframe(
        df[numeric_columns].describe().T,
        use_container_width=True
    )

st.divider()

# ---------------------------------------------------
# Missing Values Chart
# ---------------------------------------------------

st.subheader("Missing Value Analysis")

missing_df = pd.DataFrame({

    "Column": df.columns,

    "Missing": df.isnull().sum()

})

fig = px.bar(

    missing_df,

    x="Column",

    y="Missing",

    color="Missing",

    title="Missing Values by Column"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ---------------------------------------------------
# Data Type Distribution
# ---------------------------------------------------

st.subheader("Data Type Distribution")

dtype_df = pd.DataFrame(

    df.dtypes.astype(str)

    .value_counts()

).reset_index()

dtype_df.columns = [

    "Data Type",

    "Count"

]

fig = px.pie(

    dtype_df,

    names="Data Type",

    values="Count",

    hole=0.5,

    title="Column Data Types"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ---------------------------------------------------
# Correlation Heatmap
# ---------------------------------------------------

if len(numeric_columns) > 1:

    st.subheader("Correlation Heatmap")

    corr = df[numeric_columns].corr()

    fig = px.imshow(

        corr,

        text_auto=".2f",

        color_continuous_scale="RdBu_r",

        aspect="auto"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ---------------------------------------------------
# Distribution Analysis
# ---------------------------------------------------

if len(numeric_columns):

    st.subheader("Distribution Analysis")

    selected = st.selectbox(

        "Select Numeric Column",

        numeric_columns

    )

    fig = px.histogram(

        df,

        x=selected,

        nbins=30,

        marginal="box",

        title=f"Distribution of {selected}"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ---------------------------------------------------
# Duplicate Records
# ---------------------------------------------------

st.subheader("Duplicate Records")

duplicate_df = df[df.duplicated()]

st.write(f"Duplicate Rows Found: **{len(duplicate_df)}**")

if len(duplicate_df):

    st.dataframe(

        duplicate_df,

        use_container_width=True

    )

else:

    st.success("No duplicate records found.")

st.divider()

# ---------------------------------------------------
# Dataset Health
# ---------------------------------------------------

st.subheader("Dataset Health")

if quality >= 95:

    st.success("🟢 Excellent Dataset Quality")

elif quality >= 80:

    st.warning("🟡 Good Dataset Quality")

else:

    st.error("🔴 Dataset Requires Cleaning")

st.progress(int(quality))

st.divider()

# ---------------------------------------------------
# Download Summary
# ---------------------------------------------------

summary_csv = summary.to_csv(index=False).encode()

st.download_button(

    "⬇ Download Column Summary",

    summary_csv,

    "column_summary.csv",

    "text/csv"

)