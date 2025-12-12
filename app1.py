import streamlit as st
import pandas as pd
import pickle

# Load trained model pipeline
model = pickle.load(open("model.pkl", "rb"))

st.title("🎓 Student Performance Predictor")
st.write("Fill in the details below to predict the student's final grade (G3).")

# Collect inputs for ALL features used during training
school = st.selectbox("School", ["GP", "MS"])
sex = st.selectbox("Sex", ["M", "F"])
age = st.number_input("Age", min_value=15, max_value=22, step=1)
address = st.selectbox("Address", ["U", "R"])
famsize = st.selectbox("Family Size", ["LE3", "GT3"])
Pstatus = st.selectbox("Parent's Cohabitation Status", ["T", "A"])
Medu = st.number_input("Mother's Education (0-4)", min_value=0, max_value=4, step=1)
Fedu = st.number_input("Father's Education (0-4)", min_value=0, max_value=4, step=1)
Mjob = st.selectbox("Mother's Job", ["teacher", "health", "services", "at_home", "other"])
Fjob = st.selectbox("Father's Job", ["teacher", "health", "services", "at_home", "other"])
reason = st.selectbox("Reason to Choose School", ["home", "reputation", "course", "other"])
guardian = st.selectbox("Guardian", ["mother", "father", "other"])
traveltime = st.number_input("Travel Time to School (1-4)", min_value=1, max_value=4, step=1)
studytime = st.number_input("Study Time (1-4)", min_value=1, max_value=4, step=1)
failures = st.number_input("Number of Failures", min_value=0, max_value=3, step=1)
schoolsup = st.selectbox("School Support", ["yes", "no"])
famsup = st.selectbox("Family Support", ["yes", "no"])
paid = st.selectbox("Extra Paid Classes", ["yes", "no"])
activities = st.selectbox("Extra-curricular Activities", ["yes", "no"])
nursery = st.selectbox("Attended Nursery School", ["yes", "no"])
higher = st.selectbox("Wants Higher Education", ["yes", "no"])
internet = st.selectbox("Internet Access", ["yes", "no"])
romantic = st.selectbox("In a Romantic Relationship", ["yes", "no"])
famrel = st.number_input("Family Relationship Quality (1-5)", min_value=1, max_value=5, step=1)
freetime = st.number_input("Free Time (1-5)", min_value=1, max_value=5, step=1)
goout = st.number_input("Going Out with Friends (1-5)", min_value=1, max_value=5, step=1)
Dalc = st.number_input("Workday Alcohol Consumption (1-5)", min_value=1, max_value=5, step=1)
Walc = st.number_input("Weekend Alcohol Consumption (1-5)", min_value=1, max_value=5, step=1)
health = st.number_input("Health (1-5)", min_value=1, max_value=5, step=1)
absences = st.number_input("Absences", min_value=0, max_value=100, step=1)
G1 = st.number_input("Grade 1", min_value=0, max_value=20, step=1)
G2 = st.number_input("Grade 2", min_value=0, max_value=20, step=1)

# Prepare input data as DataFrame
input_df = pd.DataFrame([{
    'school': school,
    'sex': sex,
    'age': age,
    'address': address,
    'famsize': famsize,
    'Pstatus': Pstatus,
    'Medu': Medu,
    'Fedu': Fedu,
    'Mjob': Mjob,
    'Fjob': Fjob,
    'reason': reason,
    'guardian': guardian,
    'traveltime': traveltime,
    'studytime': studytime,
    'failures': failures,
    'schoolsup': schoolsup,
    'famsup': famsup,
    'paid': paid,
    'activities': activities,
    'nursery': nursery,
    'higher': higher,
    'internet': internet,
    'romantic': romantic,
    'famrel': famrel,
    'freetime': freetime,
    'goout': goout,
    'Dalc': Dalc,
    'Walc': Walc,
    'health': health,
    'absences': absences,
    'G1': G1,
    'G2': G2
}])

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    st.success(f"🎯 Predicted Final Grade (G3): {prediction}")
