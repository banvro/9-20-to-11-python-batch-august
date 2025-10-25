import streamlit as st
import joblib

model = joblib.load("student_placement_predictor.joblib")

st.subheader("Student Placement Predictor")

iq = st.number_input("Please Enter your IQ")
previous_result = st.number_input("Please Enter your previous score")
CGPA = st.number_input("Please Enter your CGPA ")
Academic_Performance = st.number_input("Please Enter your Academic Performance ")

Internship_Experience = st.selectbox("Please Choose your Internship Experience", ["Yes", "No"])

Extra_Curricular_Score = st.number_input("Please Enter your Extra Curricular Score")
Communication_Skills = st.number_input("Please Enter your Communication Skills Points")
Projects_Completed = st.number_input("Please Enter Complted Projects")

if Internship_Experience == "Yes":
    Internship_Experience = 1
else:
    Internship_Experience = 0

btn = st.button("Predcit My Placement")

if btn:
    pred = model.predict([[iq, previous_result, CGPA, Academic_Performance, Internship_Experience, Extra_Curricular_Score, Communication_Skills, Projects_Completed]])

    if pred == 1:
        st.success("Congratulations! You are going to be placed...")
        st.balloons()
    else:
        st.warning("Hope! you will do better next time...!")
        st.snow()