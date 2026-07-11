import pandas as pd


def generate_insights(df):

    summary = (
        f"The dataset contains {len(df):,} rows and "
        f"{df.shape[1]} columns."
    )

    insights = [

        f"{df.select_dtypes('number').shape[1]} numeric columns detected.",

        f"{df.select_dtypes('object').shape[1]} categorical columns detected.",

        f"{df.isnull().sum().sum()} missing values found.",

        f"{df.duplicated().sum()} duplicate rows identified."

    ]

    opportunities = [

        "Clean missing values to improve analysis accuracy.",

        "Use correlation analysis to identify strong relationships.",

        "Build predictive models using the numeric features.",

        "Create dashboards for real-time monitoring."

    ]

    risks = []

    if df.isnull().sum().sum() > 0:
        risks.append("Dataset contains missing values.")

    if df.duplicated().sum() > 0:
        risks.append("Duplicate records may impact analysis.")

    if len(risks) == 0:
        risks.append("No major data quality risks detected.")

    recommendations = [

        "Handle missing values before modeling.",

        "Remove duplicate records.",

        "Standardize categorical values.",

        "Detect and treat outliers.",

        "Perform feature engineering for better predictions."

    ]

    return {

        "summary": summary,

        "insights": insights,

        "opportunities": opportunities,

        "risks": risks,

        "recommendations": recommendations

    }