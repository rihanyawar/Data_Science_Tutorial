import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Page configuration
st.set_page_config(
    page_title="Heart Disease Predictor",
    layout="centered"
)

# Title
st.title("Heart Disease Predictor")
st.write("Enter the patient's details below to predict the risk of heart disease.")

st.divider()

# -----------------------------
# User Inputs
# -----------------------------

age = st.number_input("Age", min_value=1, max_value=120, value=30)

sex = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

cp = st.selectbox(
    "Chest Pain Type",
    [
        "Typical Angina",
        "Atypical Angina",
        "Non-anginal Pain",
        "Asymptomatic"
    ]
)

trestbps = st.number_input(
    "Resting Blood Pressure",
    min_value=50,
    max_value=250,
    value=120
)

chol = st.number_input(
    "Cholesterol",
    min_value=100,
    max_value=600,
    value=200
)

fbs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dL",
    ["No", "Yes"]
)

restecg = st.selectbox(
    "Resting ECG",
    [
        "Normal",
        "ST-T Abnormality",
        "Left Ventricular Hypertrophy"
    ]
)

thalach = st.number_input(
    "Maximum Heart Rate",
    min_value=50,
    max_value=250,
    value=150
)

exang = st.selectbox(
    "Exercise-Induced Angina",
    ["No", "Yes"]
)

oldpeak = st.number_input(
    "ST Depression",
    min_value=0.0,
    max_value=10.0,
    value=1.0,
    step=0.1
)

slope = st.selectbox(
    "Slope of Peak Exercise ST Segment",
    [
        "Upsloping",
        "Flat",
        "Downsloping"
    ]
)

ca = st.selectbox(
    "Number of Major Vessels",
    [0, 1, 2, 3]
)

thal = st.selectbox(
    "Thalassemia",
    [
        "Normal",
        "Fixed Defect",
        "Reversible Defect"
    ]
)

# -----------------------------
# Convert Inputs
# -----------------------------

sex = 1 if sex == "Male" else 0

cp = {
    "Typical Angina": 0,
    "Atypical Angina": 1,
    "Non-anginal Pain": 2,
    "Asymptomatic": 3
}[cp]

fbs = 1 if fbs == "Yes" else 0

restecg = {
    "Normal": 0,
    "ST-T Abnormality": 1,
    "Left Ventricular Hypertrophy": 2
}[restecg]

exang = 1 if exang == "Yes" else 0

slope = {
    "Upsloping": 0,
    "Flat": 1,
    "Downsloping": 2
}[slope]

thal = {
    "Normal": 1,
    "Fixed Defect": 2,
    "Reversible Defect": 3
}[thal]

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict"):

    input_data = np.array([[
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]])

    prediction = model.predict(input_data)

    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(input_data)[0][1]
        risk = round(probability * 100, 2)
    else:
        risk = 50.0

    st.divider()

    if prediction[0] == 1:
        st.error("Prediction: High Risk of Heart Disease")
    else:
        st.success("Prediction: Low Risk of Heart Disease")

    st.progress(risk / 100)
    st.metric("Predicted Risk", f"{risk}%")