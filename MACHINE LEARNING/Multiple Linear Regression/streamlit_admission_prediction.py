import streamlit as st
import pickle
import numpy as np

# Load Model
model = pickle.load(open("admission_model.pkl", "rb"))

# Title
st.title("Graduate Admission Predictor")
st.write("Enter your profile details from the sidebar.")

# Sidebar Inputs
st.sidebar.header("Student Profile")

gre = st.sidebar.number_input(
    "GRE Score",
    min_value=260,
    max_value=340,
    value=320
)

toefl = st.sidebar.number_input(
    "TOEFL Score",
    min_value=0,
    max_value=120,
    value=100
)

rating = st.sidebar.slider(
    "University Rating",
    min_value=1,
    max_value=5,
    value=3
)

sop = st.sidebar.slider(
    "SOP Strength",
    min_value=1.0,
    max_value=5.0,
    value=3.0
)

lor = st.sidebar.slider(
    "LOR Strength",
    min_value=1.0,
    max_value=5.0,
    value=3.0
)

cgpa = st.sidebar.number_input(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    value=8.0
)

research = st.sidebar.selectbox(
    "Research Experience",
    ["No", "Yes"]
)

# Convert Research to Numeric
research = 1 if research == "Yes" else 0

# Prediction
if st.sidebar.button("Predict Admission Chance"):

    student = np.array([
        [gre, toefl, rating, sop, lor, cgpa, research]
    ])

    prediction = model.predict(student)

    st.success(
        f"Admission Chance: {prediction[0]*100:.2f}%"
    )