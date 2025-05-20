import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st 


st.set_page_config(page_title = "Analysis")

st.sidebar.title("Analysis Module")

data = pd.read_csv("datasets/data_viz1.csv")

st.header('Sector Price per Sqft Geomap')


choice = st.selectbox("Choose a Option", ["Select any one","Flat", "House"])

if choice == "Flat":
    data = data[data["property_type"] == "flat"]

    numeric_cols = ['price','price_per_sqft','built_up_area','latitude','longitude']
    group_df = data[numeric_cols + ['sector']].groupby('sector').mean()

    fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                    color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                    mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)
    st.plotly_chart(fig,use_container_width=True)

elif choice == "House":
    data = data[data["property_type"] == "house"]

    numeric_cols = ['price','price_per_sqft','built_up_area','latitude','longitude']
    group_df = data[numeric_cols + ['sector']].groupby('sector').mean()

    fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                    color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                    mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)
    st.plotly_chart(fig,use_container_width=True)

else:
    numeric_cols = ['price','price_per_sqft','built_up_area','latitude','longitude']
    group_df = data[numeric_cols + ['sector']].groupby('sector').mean()

    fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                    color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                    mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)
    st.plotly_chart(fig,use_container_width=True)




st.header("Features Wordclode")

forword = pd.read_csv("datasets/for_wordclode.csv")

import ast
import matplotlib.pyplot as plt
from wordcloud import WordCloud

main = []

for item in forword["features"].dropna().apply(ast.literal_eval):
    # print(item)
    main.extend(item)

features_text = ' '.join(main)

wordclodee = WordCloud(width = 1000, height = 800,
                       background_color = "white",
                       stopwords = set(['s']),
                       min_font_size = 5).generate(features_text)

plt.figure(figsize=  (8, 8))
plt.imshow(wordclodee)
plt.axis("off")
plt.tight_layout(pad = 0)
# plt.show()
st.pyplot()