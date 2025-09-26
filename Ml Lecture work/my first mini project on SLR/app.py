import pandas as pd 
import numpy as np
import joblib
import streamlit as st

model = joblib.load("student_perfoemance_predictor.joblib")

st.title("Students Performace Predictor")

hours = st.number_input("Enter Number of Hours You Study")

btn = st.button("Predict Score")

if btn:
    m = model.coef_[0]
    b = model.intercept_

    y = m * hours + b

    st.success(f"Your score will be : {str(y)[:4]} Score")

    st.balloons()