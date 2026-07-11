def analyze_data(df):
    """Perform basic analytics on the dataset."""
    return {
        "rows": len(df),
        "columns": len(df.columns) if hasattr(df, "columns") else 0,
    }
