import pickle
import streamlit as st 
import pandas as pd
import numpy as np

with open("df.pkl", "rb") as file:
    df = pickle.load(file)

with open("pipeline.pkl", "rb") as file:
    pipeline = pickle.load(file)


st.set_page_config(page_title = "Price Predictor")

st.sidebar.title("Predict Price")

st.header("Enter your requirenments for price..")

col1, col2 = st.columns(2)

with col1:
    propery_type = st.selectbox("Property Type", ["flat", "house"])

with col2:
    sector = st.selectbox("Sector", df["sector"].unique())

x, y, z = st.columns(3)

with x:
    bedroom = float(st.selectbox("Select number of Bedrooms", sorted(df["bedRoom"].unique())))

with y:
    bathroom = float(st.selectbox("Select number of bathroom", df["bathroom"].unique()))

with z:
    balcony = st.selectbox("Select number of balcony", df["balcony"].unique())


p, q = st.columns(2)

with p:
    agePossession = st.selectbox("Choose Propery Age", df["agePossession"].unique())

with q:
    furnishing_type = st.selectbox("Choose furnishing Cat", df["furnishing_type"].unique())


p, q = st.columns(2)

with p:
    luxury = st.selectbox("Choose luxury", df["luxury_category"].unique())

with q:
    floor = st.selectbox("Choose Floor Req", df["floor_category"].unique())

p, q = st.columns(2)

with p:
    servant_room = st.selectbox("Need servant room", df["servant room"].unique())

with q:
    store_room = st.selectbox("Need Store Room", df["store room"].unique())

area = float(st.number_input("Enter house/flat area"))


columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony','agePossession', 'built_up_area',
           'servant room', 'store room','furnishing_type', 'luxury_category', 'floor_category']

data = [propery_type, sector, bedroom, bathroom, balcony, agePossession, area, float(servant_room), float(store_room), furnishing_type, luxury, floor]

inp_df = pd.DataFrame([data], columns = columns)


if st.button("Predict Price"):

    st.text("Your Inputs Preview")
    st.dataframe(inp_df)
    
    predicted_price = np.expm1(pipeline.predict(inp_df))[0]

    max_price = predicted_price + 0.25

    low_price = predicted_price - 0.25

    st.header("Your output Summery")

    st.text(f"The Price lies between the range of {round(low_price, 2)} crore to {round(max_price, 2)} crore according to your property requiremtns.")