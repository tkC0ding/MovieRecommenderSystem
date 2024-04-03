import pandas as pd
import streamlit as st

st.title("Movie Recommender System")

df = pd.read_csv("PreprocessedData/train_data.csv")
movie_list = tuple(df['title'].values)

option = st.selectbox(
    'What Movies would you like to watch?',
    movie_list)