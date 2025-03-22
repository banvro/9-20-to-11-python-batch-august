
# stremit

# pip install streamlit
# pip install plotly
# pip install pandas 
# pip intsall numpy

import streamlit as st 
import pandas as pd 
import numpy as np 
import plotly.express as px

st.set_page_config(layout = "wide")

df = pd.read_csv("india_info.csv")

states = list(df["State"].unique())
states.insert(0, "India")

st.sidebar.title("About India")

slected_state = st.sidebar.selectbox("State", states)

first_option = st.sidebar.selectbox("choose options", ["Hindus","Households_with_Internet", "Male", "Female", "State name"])

second_option = st.sidebar.selectbox("choose more options", df.columns[5 : ])

plot = st.sidebar.button("Plot Graph")

if plot:
    
    if slected_state == "India":
        fig = px.scatter_map(df, lat="Latitude", lon="Longitude", size_max=15, zoom=3, size = second_option, color = first_option)
        st.plotly_chart(fig, use_container_width = True)

    else:
        pass