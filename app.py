import streamlit as st
import pickle
import pandas as pd
import requests
import time

def fetch_movie_details(movie_id):
    api_key = "f519d92f69196fdc35f9eb2f48b92b36"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        poster = "https://image.tmdb.org/t/p/w500/" + data['poster_path'] if data.get('poster_path') else "https://via.placeholder.com/500x750?text=No+Poster"
        return poster, data.get('vote_average', 'N/A'), data.get('overview', 'No overview.')
    except:
        return "https://via.placeholder.com/500x750?text=Error", "N/A", "Error"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity_indices[index]
    
    rec_data = []
    for i in distances:
        time.sleep(0.1)
        m_id = movies.iloc[i].movie_id
        details = fetch_movie_details(m_id)
        rec_data.append({
            "name": movies.iloc[i].title,
            "poster": details[0],
            "rating": details[1],
            "overview": details[2]
        })
    return rec_data

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity_indices = pickle.load(open('similarity_indices.pkl', 'rb'))

st.set_page_config(layout="wide")
st.title('🎬 Movie Recommender System')

selected_movie = st.selectbox('Search for a movie:', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    cols = st.columns(5)
    
    for i in range(5):
        with cols[i]:
            st.image(recommendations[i]['poster'])
            st.subheader(recommendations[i]['name'])
            st.write(f"⭐ {recommendations[i]['rating']}/10")
        
            with st.expander("Read Overview"):
                st.write(recommendations[i]['overview'])