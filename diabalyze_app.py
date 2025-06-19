
import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('Diabalyze.pkl', 'rb') as file:
    model = pickle.load(file)

# Page config
st.set_page_config(page_title="Diabalyze", page_icon="🩺", layout="centered")

# Title and description
st.title("🩺 Diabalyze - Diabetes Prediction App")
st.write("""
Enter the details below to predict if the person is likely to have diabetes.
This prediction is based on a machine learning model trained with health data.
""")

# User input fields
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, step=1)
glucose = st.number_input("Glucose Level", min_value=0, max_value=300)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100)
insulin = st.number_input("Insulin Level", min_value=0, max_value=1000)
bmi = st.number_input("BMI", min_value=0.0, max_value=80.0, format="%.1f")
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=5.0, format="%.3f")
age = st.number_input("Age", min_value=1, max_value=120, step=1)

# Predict button
if st.button("Predict"):
    # Prepare input
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                            insulin, bmi, dpf, age]])

    # Get prediction
    prediction = model.predict(input_data)[0]

    # Show result
    if prediction == 1:
        st.error("🚨 The model predicts this person is **likely diabetic**.")
    else:
        st.success("✅ The model predicts this person is **not diabetic**.")
