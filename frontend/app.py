import streamlit as st
import requests

st.title("💳 Credit Card Fraud Detection")

st.write("Enter transaction details (30 values separated by commas):")

# Input
user_input = st.text_area("Transaction Features")

# Button
if st.button("Predict"):
    try:
        # Convert input string → list of floats
        features = [float(x.strip()) for x in user_input.split(",")]

        # API call
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json={"features": features}
        )

        data = response.json()

        # Handle response
        if response.status_code == 200:
            st.success(f"Prediction: {data['result']}")
        else:
            st.error(data.get("detail", "Something went wrong"))

    except ValueError:
        st.error("Please enter valid numeric values separated by commas.")