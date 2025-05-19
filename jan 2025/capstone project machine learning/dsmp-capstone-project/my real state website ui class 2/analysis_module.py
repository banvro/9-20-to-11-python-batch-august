import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st 


st.set_page_config(page_title = "Analysis")

st.sidebar.title("Analysis Module")

data = pd.read_csv("data_viz1.csv")

# print(data.columns)


# grooup_df = data.groupby("sector")


# new_df = st.dataframe(grooup_df.mean("bedRoom"))

# print(new_df)

# group_df = data.groupby('sector').mean()[['price','price_per_sqft','built_up_area','latitude','longitude']]


numeric_cols = ['price','price_per_sqft','built_up_area','latitude','longitude']
group_df = data[numeric_cols + ['sector']].groupby('sector').mean()

st.header('Sector Price per Sqft Geomap')
fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)
st.plotly_chart(fig,use_container_width=True)