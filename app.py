import pandas as pd
import streamlit as st
import pickle
import requests

def fetch_poster(id):
    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMDk2NTM2OWVkZTZlZDdhYjUxNzUwOGM5NDU5OWZlNyIsInN1YiI6IjY2MGQzZmU3MTQ5NTY1MDE0YWI5ZTY4YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.y6UcQ43MC3lmoTqdMKHNzXU1EoOaCIW4KS1N0vRBmWM"
    }
    response = requests.get(url, headers=headers)
    data = response.text

    image_path = "https://image.tmdb.org/t/p/w500" + data['poster_path']

    return(image_path)


similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")

df = pd.read_csv("PreprocessedData/train_data.csv")
movie_list = tuple(df['title'].values)

def recommend(movie):
    movie_index = df[df['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x:x[1])[1:6]

    r = []
    for i in movie_list:
        index = i[0]
        r.append(df.iloc[index, 1])
    return(r)

option = st.selectbox(
    'What Movies would you like to watch?',
    movie_list)

if st.button("Recommend"):
    recommended = recommend(option)
    id_list = []
    for i in recommended:
        id_temp = list(df.loc[df['title'] == i, 'movie_id'])
        id = id_temp[0]
        id_list.append(id)
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.write(id_list[0], recommended[0])
    with col2:
        st.write(id_list[1], recommended[1])
    with col3:
        st.write(id_list[2], recommended[2])
    with col4:
        st.write(id_list[3], recommended[3])
    with col5:
        st.write(id_list[4], recommended[4])