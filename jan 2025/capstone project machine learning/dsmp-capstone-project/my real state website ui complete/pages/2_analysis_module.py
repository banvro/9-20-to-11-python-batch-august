import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st 
import seaborn as sn


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



st.header("Area vs price relationship")

fig3 = px.scatter(data, x = "built_up_area", y = "price", color = "bedRoom")
st.plotly_chart(fig3)


st.header("BHK's Pie Chart")

sector_data = data["sector"].unique().tolist()
sector_data.sort()
sector_data.insert(0, "All Sectors")

sector_choice = st.selectbox("Choose your sector nunmber", sector_data)

if sector_choice == "All Sectors":
    fig4 = px.pie(data, names = "bedRoom")
    st.plotly_chart(fig4)
else:
    query = data[data["sector"] == sector_choice]
    fig4 = px.pie(query, names = "bedRoom")
    st.plotly_chart(fig4)



st.header("Box plot on price and bedrooms")

room_data = data[data["bedRoom"] <= 4]
fig5 = px.box(room_data, x = "bedRoom", y = "price")
st.plotly_chart(fig5)


st.header("Distrbution plot of house and flats")

fig6 = plt.figure(figsize = (10, 4))
sn.distplot(data[data["property_type"] == "house"]["price"])
sn.distplot(data[data["property_type"] == "flat"]["price"])
plt.legend()
st.pyplot(fig6)