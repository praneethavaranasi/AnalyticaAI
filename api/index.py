from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def root():
    return "<html><body><h1>AnalyticaAI</h1><p>This repo hosts a Streamlit app. To run locally, use <code>streamlit run app.py</code>.</p></body></html>"
