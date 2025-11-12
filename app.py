import streamlit as st

st.set_page_config(
    page_title="EMI Prediction Platform",
    page_icon="💳",
    layout="wide"
)

st.title("💳 EMI Prediction and Analysis Platform")
st.markdown("""
Welcome to the **AI-powered EMI Prediction Platform**.  
This app helps users:
- Predict EMI **Eligibility** (Classification)
- Estimate **Maximum EMI Amount** (Regression)
- Explore **ML model performance** using MLflow tracking
""")

st.sidebar.success("Select a page from the sidebar 👈")
