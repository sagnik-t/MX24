import streamlit as st
import pickle as pk
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=416ea103ba95d98d64c5188e40b50f07&&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/original/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies_dict = pk.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pk.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'Select a movie',
    movies['title'].values)

import streamlit as st

# Assuming you have your data in 'names' and 'posters' lists

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    
    col1, spacer1, col2, spacer2, col3, spacer3, col4, spacer4, col5 = st.columns(9)
    
    with col1:
        st.header(names[0])
        st.image(posters[0])
    
    with spacer1:
        pass  # Spacer, adds space between columns
    
    with col2:
        st.header(names[1])
        st.image(posters[1])
    
    with spacer2:
        pass  # Spacer
    
    with col3:
        st.header(names[2])
        st.image(posters[2])
    
    with spacer3:
        pass  # Spacer
    
    with col4:
        st.header(names[3])
        st.image(posters[3])
    
    with spacer4:
        pass  # Spacer
    
    with col5:
        st.header(names[4])
        st.image(posters[4])
