import streamlit as st
import pandas as pd

from utils.insights import generate_insights

st.set_page_config(
    page_title="Business Insights",
    page_icon="💡",
    layout="wide"
)

st.title("💡 AI Business Insights")

if "data" not in st.session_state:
    st.warning("Please upload a dataset first.")
    st.stop()

df = st.session_state["data"]

with st.spinner("Generating insights..."):
    insights = generate_insights(df)

# ====================================================
# Dataset Overview
# ====================================================

st.subheader("Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Rows", f"{len(df):,}")
col2.metric("Columns", df.shape[1])
col3.metric("Missing Values", int(df.isnull().sum().sum()))
col4.metric("Duplicate Rows", int(df.duplicated().sum()))

st.divider()

# ====================================================
# Executive Summary
# ====================================================

st.subheader("Executive Summary")

st.info(insights["summary"])

st.divider()

# ====================================================
# Key Insights
# ====================================================

st.subheader("Key Business Insights")

for item in insights["insights"]:
    st.success(f"✅ {item}")

st.divider()

# ====================================================
# Opportunities
# ====================================================

st.subheader("Business Opportunities")

for item in insights["opportunities"]:
    st.info(f"📈 {item}")

st.divider()

# ====================================================
# Risks
# ====================================================

st.subheader("Potential Risks")

for item in insights["risks"]:
    st.warning(f"⚠️ {item}")

st.divider()

# ====================================================
# Recommendations
# ====================================================

st.subheader("Recommendations")

for item in insights["recommendations"]:
    st.success(f"🚀 {item}")

st.divider()

# ====================================================
# Data Quality
# ====================================================

st.subheader("Data Quality Report")

quality = pd.DataFrame({

    "Metric":[
        "Rows",
        "Columns",
        "Missing Values",
        "Duplicate Rows",
        "Missing Percentage"
    ],

    "Value":[

        len(df),

        df.shape[1],

        df.isnull().sum().sum(),

        df.duplicated().sum(),

        round(
            (
                df.isnull().sum().sum()
                /
                (len(df)*len(df.columns))
            )*100,
            2
        )

    ]

})

st.dataframe(
    quality,
    use_container_width=True
)

st.divider()

# ====================================================
# Column Summary
# ====================================================

st.subheader("Column Analysis")

column_info = pd.DataFrame({

    "Column":df.columns,

    "Data Type":df.dtypes.astype(str),

    "Unique Values":df.nunique(),

    "Missing":df.isnull().sum()

})

st.dataframe(
    column_info,
    use_container_width=True
)

st.divider()

# ====================================================
# Download Report
# ====================================================

report = f"""
BUSINESS INSIGHTS REPORT

Executive Summary
-----------------
{insights["summary"]}

Key Insights
------------
"""

for item in insights["insights"]:
    report += f"- {item}\n"

report += "\nOpportunities\n--------------\n"

for item in insights["opportunities"]:
    report += f"- {item}\n"

report += "\nRisks\n------\n"

for item in insights["risks"]:
    report += f"- {item}\n"

report += "\nRecommendations\n----------------\n"

for item in insights["recommendations"]:
    report += f"- {item}\n"

st.download_button(

    "📥 Download Business Insights",

    report,

    file_name="Business_Insights_Report.txt",

    mime="text/plain"

)