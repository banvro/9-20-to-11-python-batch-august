import pandas as pd
import streamlit as st 
import pickle

cosine_sim1 = pickle.load(open("cosine_sim1.pkl", "rb"))
cosine_sim2 = pickle.load(open("cosine_sim2.pkl", "rb"))
cosine_sim3 = pickle.load(open("cosine_sim3.pkl", "rb"))
df = pickle.load(open("location_dff.pkl", "rb"))
location_df_normalized = pickle.load(open("location_df_normalized.pkl", "rb"))

st.set_page_config(page_title = "Recamended Aparments")

st.header("Get Appartminets Recmendation")

appartment_chocie = st.selectbox("Choose an Appartment", sorted(location_df_normalized.index.tolist()))




def recommend_properties_with_scores(property_name, top_n=5):
    
    cosine_sim_matrix = 30*cosine_sim1 + 20*cosine_sim2 + 8*cosine_sim3
    # cosine_sim_matrix = cosine_sim3
    
    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[location_df_normalized.index.get_loc(property_name)]))
    
    # Sort properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n+1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n+1]]
    
    # Retrieve the names of the top properties using the indices
    top_properties = location_df_normalized.index[top_indices].tolist()
    
    # Create a dataframe with the results
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })
    
    return recommendations_df

# # Test the recommender function using a property name
# recommend_properties_with_scores('Ireo Victory Valley')



if st.button("Recmeendd"):
    appartmes = recommend_properties_with_scores(appartment_chocie)

    st.dataframe(appartmes)
