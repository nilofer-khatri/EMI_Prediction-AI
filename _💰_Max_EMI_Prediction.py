import streamlit as st
import joblib
import pandas as pd
import numpy as np

st.title("💰 Maximum EMI Prediction")

# Load trained regression model
model = joblib.load("best_regression_model_xgb.pkl")

st.sidebar.header("Enter Financial Details")

# User inputs
age = st.sidebar.number_input("Age", 18, 70, 30)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
marital_status = st.sidebar.selectbox("Marital Status", ["Single", "Married"])
education = st.sidebar.selectbox("Education", ["High School", "Graduate", "Professional"])
monthly_salary = st.sidebar.number_input("Monthly Salary", 0, 200000, 50000)
employment_type = st.sidebar.selectbox("Employment Type", ["Private", "Government", "Self-Employed"])
years_of_employment = st.sidebar.number_input("Years of Employment", 0.0, 40.0, 5.0)
company_type = st.sidebar.selectbox("Company Type", ["Startup", "Mid-size", "MNC"])
house_type = st.sidebar.selectbox("House Type", ["Own", "Family", "Rented"])
monthly_rent = st.sidebar.number_input("Monthly Rent", 0, 100000, 10000)
family_size = st.sidebar.slider("Family Size", 1, 10, 4)
dependents = st.sidebar.slider("Dependents", 0, 5, 1)
school_fees = st.sidebar.number_input("School Fees", 0, 20000, 2000)
college_fees = st.sidebar.number_input("College Fees", 0, 20000, 2000)
travel_expenses = st.sidebar.number_input("Travel Expenses", 0, 20000, 1500)
groceries_utilities = st.sidebar.number_input("Groceries & Utilities", 0, 30000, 5000)
other_monthly_expenses = st.sidebar.number_input("Other Monthly Expenses", 0, 10000, 2500)
existing_loans = st.sidebar.selectbox("Existing Loans", ["Yes", "No"])
current_emi_amount = st.sidebar.number_input("Current EMI Amount", 0, 50000, 2000)
credit_score = st.sidebar.number_input("Credit Score", 300, 900, 700)
bank_balance = st.sidebar.number_input("Bank Balance", 0, 1000000, 100000)
emergency_fund = st.sidebar.number_input("Emergency Fund", 0, 500000, 20000)
emi_scenario = st.sidebar.selectbox("EMI Scenario", [
    "Personal Loan EMI", "Education EMI", "Vehicle EMI",
    "Home Appliances EMI", "E-commerce Shopping EMI"
])
requested_amount = st.sidebar.number_input("Requested Loan Amount", 10000, 2000000, 500000)
requested_tenure = st.sidebar.slider("Requested Tenure (months)", 6, 84, 24)

if st.button("💡 Estimate Max EMI"):

    # Step 1: Create DataFrame with all required columns
    input_data = pd.DataFrame([{
        "age": age,
        "gender": gender,
        "marital_status": marital_status,
        "education": education,
        "monthly_salary": monthly_salary,
        "employment_type": employment_type,
        "years_of_employment": years_of_employment,
        "company_type": company_type,
        "house_type": house_type,
        "monthly_rent": monthly_rent,
        "family_size": family_size,
        "dependents": dependents,
        "school_fees": school_fees,
        "college_fees": college_fees,
        "travel_expenses": travel_expenses,
        "groceries_utilities": groceries_utilities,
        "other_monthly_expenses": other_monthly_expenses,
        "existing_loans": existing_loans,
        "current_emi_amount": current_emi_amount,
        "credit_score": credit_score,
        "bank_balance": bank_balance,
        "emergency_fund": emergency_fund,
        "emi_scenario": emi_scenario,
        "requested_amount": requested_amount,
        "requested_tenure": requested_tenure
    }])

    # Step 2: Add engineered columns (same as training phase)
    eps = 1e-6
    input_data["total_expenses"] = (
        input_data["monthly_rent"] + input_data["school_fees"] + input_data["college_fees"] +
        input_data["travel_expenses"] + input_data["groceries_utilities"] + input_data["other_monthly_expenses"]
    )
    input_data["debt_to_income"] = input_data["total_expenses"] / (input_data["monthly_salary"] + eps)
    input_data["savings_to_income"] = input_data["bank_balance"] / (input_data["monthly_salary"] + eps)
    input_data["emergency_to_salary"] = input_data["emergency_fund"] / (input_data["monthly_salary"] + eps)
    input_data["affordability_ratio"] = input_data["bank_balance"] / (input_data["requested_amount"] + eps)

    # Step 3: Ensure every expected column exists
    expected_cols = list(input_data.columns)
    for col in expected_cols:
        if col not in input_data.columns:
            input_data[col] = 0

    # Step 4: Predict
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Maximum EMI: ₹ {prediction:,.2f}")
