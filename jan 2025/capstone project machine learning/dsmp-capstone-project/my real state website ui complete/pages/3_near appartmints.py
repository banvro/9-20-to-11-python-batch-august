import pandas as pd
import streamlit as st 
import pickle

df = pickle.load(open("location_dff.pkl", "rb"))


st.set_page_config(page_title = "Near By Appartmints")

st.header("Find Near By Appartmints..")

appartment_choosoe = st.selectbox("Select a appartmint", sorted(df.columns.tolist()))

radios = st.number_input("Choose a range in km")

if st.button("Check Near Appartmints"):

    nearloc = df[appartment_choosoe][df[appartment_choosoe] < radios * 1000]

    # st.dataframe(nearloc)

    for key, value in nearloc.items():
        st.text(key + "  ------------> " + str(value/1000) + "Km.")
