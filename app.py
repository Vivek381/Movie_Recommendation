'''import streamlit as st
import pickle
import pandas as pd

movies_dict=pickle.load(open('movies_dict.pkl','rb'))


# Create a DataFrame from the dictionary
movies = pd.DataFrame(movies_dict)

movies = pd.DataFrame(movies_dict)

st.title('Movie_Recommendation')

option = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)'''
import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = new_df[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = {
    'Title': ['Movie 1', 'Movie 2', 'Movie 3'],
    'Rating': [4.5, 3.8, 4.2],
    'Genre': ['Action', 'Drama', 'Comedy']
}
#movies_dict=pickle.load(open('movies_dict.pkl','rb'))
# Create a DataFrame from the dictionary
movies=pd.DataFrame(movies_dict)

similarity= pickle.load(open('similarity.pkl','rb'))
st.title('Movie_Recommendation')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['Title'].values)  # Use 'Title' instead of 'title'

if st.button('Recommend'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(selected_movie_name)
