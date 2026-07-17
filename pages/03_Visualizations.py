import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.title("📈 Interactive Data Visualizations")

if "data" not in st.session_state:
    st.warning("Please upload a dataset first.")
    st.stop()

df = st.session_state["data"]

numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

# ====================================================
# Sidebar
# ====================================================

st.sidebar.header("Visualization Settings")

chart_type = st.sidebar.selectbox(
    "Select Chart",
    [
        "Histogram",
        "Bar Chart",
        "Line Chart",
        "Scatter Plot",
        "Box Plot",
        "Pie Chart",
        "Area Chart",
        "Violin Plot",
        "Correlation Heatmap"
    ]
)

# ====================================================
# Histogram
# ====================================================

if chart_type == "Histogram":

    column = st.selectbox(
        "Numeric Column",
        numeric_cols
    )

    bins = st.slider(
        "Number of Bins",
        5,
        100,
        30
    )

    fig = px.histogram(
        df,
        x=column,
        nbins=bins,
        marginal="box",
        title=f"Distribution of {column}"
    )

    st.plotly_chart(fig, use_container_width=True)

# ====================================================
# Bar Chart
# ====================================================

elif chart_type == "Bar Chart":

    x = st.selectbox("Category", categorical_cols)

    y = st.selectbox("Numeric Value", numeric_cols)

    fig = px.bar(
        df,
        x=x,
        y=y,
        color=x,
        title=f"{y} by {x}"
    )

    st.plotly_chart(fig, use_container_width=True)

# ====================================================
# Line Chart
# ====================================================

elif chart_type == "Line Chart":

    x = st.selectbox("X Axis", df.columns)

    y = st.selectbox("Y Axis", numeric_cols)

    fig = px.line(
        df,
        x=x,
        y=y,
        markers=True,
        title=f"{y} over {x}"
    )

    st.plotly_chart(fig, use_container_width=True)

# ====================================================
# Scatter Plot
# ====================================================

elif chart_type == "Scatter Plot":

    x = st.selectbox(
        "X Axis",
        numeric_cols,
        key="scatter_x"
    )

    y = st.selectbox(
        "Y Axis",
        numeric_cols,
        key="scatter_y"
    )

    color = st.selectbox(
        "Color",
        ["None"] + categorical_cols
    )

    if color == "None":

        fig = px.scatter(
            df,
            x=x,
            y=y,
            title=f"{x} vs {y}"
        )

    else:

        fig = px.scatter(
            df,
            x=x,
            y=y,
            color=color,
            title=f"{x} vs {y}"
        )

    st.plotly_chart(fig, use_container_width=True)

# ====================================================
# Box Plot
# ====================================================

elif chart_type == "Box Plot":

    y = st.selectbox(
        "Numeric Column",
        numeric_cols
    )

    fig = px.box(
        df,
        y=y,
        points="all",
        title=f"Box Plot of {y}"
    )

    st.plotly_chart(fig, use_container_width=True)

# ====================================================
# Pie Chart
# ====================================================

elif chart_type == "Pie Chart":

    column = st.selectbox(
        "Categorical Column",
        categorical_cols
    )

    pie = (
        df[column]
        .value_counts()
        .reset_index()
    )

    pie.columns = [
        column,
        "Count"
    ]

    fig = px.pie(
        pie,
        names=column,
        values="Count",
        hole=0.4,
        title=f"{column} Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

# ====================================================
# Area Chart
# ====================================================

elif chart_type == "Area Chart":

    x = st.selectbox(
        "X Axis",
        df.columns
    )

    y = st.selectbox(
        "Y Axis",
        numeric_cols
    )

    fig = px.area(
        df,
        x=x,
        y=y,
        title=f"{y} over {x}"
    )

    st.plotly_chart(fig, use_container_width=True)

# ====================================================
# Violin Plot
# ====================================================

elif chart_type == "Violin Plot":

    y = st.selectbox(
        "Numeric Column",
        numeric_cols
    )

    fig = px.violin(
        df,
        y=y,
        box=True,
        points="all",
        title=f"Violin Plot of {y}"
    )

    st.plotly_chart(fig, use_container_width=True)

# ====================================================
# Correlation Heatmap
# ====================================================

elif chart_type == "Correlation Heatmap":

    # Filter columns that are not entirely null and have more than one unique value (non-constant)
    corr_cols = [col for col in numeric_cols if df[col].notnull().any() and df[col].nunique() > 1]

    if len(corr_cols) > 1:
        corr = df[corr_cols].corr()

        fig = px.imshow(
            corr,
            text_auto=".2f",
            aspect="auto",
            color_continuous_scale="RdBu_r",
            title="Correlation Heatmap"
        )

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Not enough numeric columns with variance to show correlation heatmap.")

# ====================================================
# Raw Data
# ====================================================

with st.expander("View Dataset"):

    st.dataframe(
        df,
        use_container_width=True
    )

# ====================================================
# Download Dataset
# ====================================================

csv = df.to_csv(index=False).encode()

st.download_button(
    "⬇ Download Dataset",
    csv,
    "dataset.csv",
    "text/csv"
)