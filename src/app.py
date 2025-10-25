import streamlit as st
import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(BASE_DIR, ".."))
model_path = os.path.join(project_root, "models", "savings_model_compressed.pkl")
model = joblib.load(model_path)

st.title("💰 Personal Finance Predictor App")

st.write("Predict your monthly savings based on your income, expenses, and spending habits")

income = st.number_input("1. Monthly Income", min_value=0, value=3000, step=500)
expense = st.number_input("2. Monthly Expense", min_value=0, value=2000, step=500)
scenario = st.selectbox("3. Economic Condition", options=['normal', 'inflation', 'recession',])
credit = st.number_input("4. Credit Score", min_value=300, max_value=850, value=500, step=50)
loan = st.number_input("5. Loan Payment", min_value=0, value=0, step=500)
investment = st.number_input("6. Investment Amount", min_value=0, value=0, step=500)
subscriptions = st.slider("7. No. of Subscriptions", min_value=0, max_value=30, value=0, step=1)
emergency = st.number_input("8. Emergency Fund", min_value=0, value=0, step=500)
income_type = st.selectbox("9. Income Type", options=['Freelance', 'Salary', 'Mixed'])
rent = st.number_input("10. Rent or Mortgage Price", min_value=0, value=2000, step=500)

if st.button("Predict Savings"):
    data = pd.DataFrame([{
        "monthly_income": income,
        "monthly_expense_total": expense,
        "financial_scenario": scenario,
        "credit_score": credit,
        "loan_payment": loan,
        "investment_amount": investment,
        "subscription_services": subscriptions,
        "emergency_fund": emergency,
        "income_type": income_type,
        "rent_or_mortgage": rent
    }])

    prediction = model.predict(data)[0]

    st.success(f"Estimated Savings: ${prediction:,.2f}")

