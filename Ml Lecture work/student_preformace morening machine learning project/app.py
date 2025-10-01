import streamlit as st 
import joblib

model = joblib.load("student_performance_predictor.joblib")


st.header("Student Performance Predictor")

hour_study = st.number_input("Enter your number of Hours Studied")

pre = st.number_input("Enter your Previous Scores")

extra_cl_ec = st.selectbox("Choose Extracurricular Activities", ["Yes", "No"])

sleeping_hours = st.number_input("Enter your Sleep Hours")

solved_paper = st.number_input("How many Sample Question Papers Practiced")

if st.button("Predict My Score"):

    if extra_cl_ec == "Yes":
        num_ex = 1
    else:
        num_ex = 0

    student_performace = model.predict([[hour_study, pre, num_ex, sleeping_hours, solved_paper]])

    st.success(f"Your Performance Score will be : {str(student_performace[0])[: 4]} Percent.")

    st.balloons()