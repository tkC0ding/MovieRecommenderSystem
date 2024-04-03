import pandas as pd
import streamlit as st
import pickle

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