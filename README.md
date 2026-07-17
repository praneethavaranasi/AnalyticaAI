# AnalyticaAI

A starter analytics application scaffold with pages for upload, dashboard, visualizations, AI assistant, and reporting.

## Structure

- `App.py` - main application entrypoint
- `database/analytics.db` - local analytics database file
- `pages/` - UI page modules
- `utils/` - data cleaning, analysis, visualization, and reporting utilities
- `models/` - saved machine learning or anomaly detection models
- `data/` - input datasets and exports
- `assets/` - static assets such as images or styles

## Getting Started

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements-app.txt
   ```
3. Run the app:
   ```bash
   streamlit run App.py
   ```

### Deployment note
- Vercel's serverless API uses [requirements.txt](requirements.txt) with a lightweight FastAPI stack for the health endpoint in [api/index.py](api/index.py).
- The full Streamlit app remains in [requirements-app.txt](requirements-app.txt) for local development.
