import streamlit as st
import pandas as pd
import mlflow

st.title("🏠 Dashboard Overview")

st.write("### Dataset Overview")
df = pd.read_csv("emi_dataset_ready_for_model.csv")
st.dataframe(df.head())

st.write("### Basic Statistics")
st.write(df.describe())

st.write("### Model Tracking (MLflow)")
st.info("To view MLflow dashboard, open terminal and run:")
st.code("mlflow ui --backend-store-uri file:./mlruns", language="bash")
st.write("Then open: [http://localhost:5000](http://localhost:5000)")
