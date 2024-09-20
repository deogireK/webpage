import streamlit as st
import numpy as np

# Configure the page
st.set_page_config(page_title="Loan Prediction", page_icon=":moneybag:", layout="wide")

# Add title
st.markdown(
    "<h1 style='text-align: center; margin-top: -30px; margin-bottom: 30px;'>Loan Approval Prediction</h1>",
    unsafe_allow_html=True,
)

# Helper functions for encoding (simplified for static demo)
def encode_property_area(area):
    if area.lower() == 'urban':
        return np.array([1, 0, 0])
    elif area.lower() == 'semiurban':
        return np.array([0, 1, 0])
    else:
        return np.array([0, 0, 1])

def encode_credit_history(ch):
    return 1 if ch.lower() == 'yes' else 0

# ------------------inputs--------------------- #
# Form inputs for the loan prediction
gender = st.radio("Select Gender", ["Male", "Female"])
married = st.radio("Are you married?", ["Yes", "No"])
dependents = st.number_input("Number of dependents", min_value=0)
education = st.radio("Education", ["Graduate", "Not Graduate"])
self_employed = st.radio("Are you self-employed?", ["Yes", "No"])
applicant_income = st.number_input('Applicant Income in INR', min_value=0)
coapplicant_income = st.number_input("Co-Applicant Income in INR", min_value=0)
loan_amount = st.number_input("Loan Amount in INR", min_value=0)
loan_amount_term = st.selectbox("Loan Amount Term", [60, 90, 120, 180, 240, 360, 480])
credit_history = st.radio("Credit History (Previously taken loan?)", ['Yes', 'No'])
property_area = st.selectbox("Select Property Area", ["Urban", "Semiurban", "Rural"])

# ---------------------------------------------------- #

# Simulate a simple loan approval check based on some input logic
if st.button("Submit"):
    # Static output logic based on credit history and loan amount
    if credit_history == "Yes" and loan_amount <= 500000:
        st.success("Congratulations! Your loan can be approved.")
    else:
        st.error("Sorry, your loan application may not be approved.")
