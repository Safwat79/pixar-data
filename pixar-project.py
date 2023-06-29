import streamlit as st  
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# App configuration
st.set_page_config(page_title="Pixar data analysis", page_icon= "pixar-icon.jpg", layout="wide", menu_items={
    'About': "This is a cool app for close understanding of Pixar movies data"
})

# Remove the hamburger button on the page of streamlit
st.markdown("""
<style> 
.css-nqowgj.e1ewe7hr3
{
    visibility: hidden;
}
</ style>
""", unsafe_allow_html=True)

# Remove the footer on the page of streamlit
st.markdown("""
<style> 
.css-h5rgaw.e1g8pov61
{
    visibility: hidden;
}
</ style>
""", unsafe_allow_html=True)


# Adding data of Pixar Movies
df=pd.read_csv('PixarMovies.csv')


#  Creat side bar fetures
opt = st.sidebar.radio(">Please Select Graph Type", options=("Choose me", "Movie length Chart", "Comparing Chart"))

# Visualize data with fetures of (Choose me - Bar - Comparing-Plot)
if opt == "Choose me":
    st.title("We have chosen some questions to be answered by this app about Pixar")

elif opt == "Movie length Chart":
# To make picture on the right and paragraph on left
    col1, col2 = st.columns(2)
    with col1:
        st.image("pixar-1.jpg", width=300)
    with col2:
        st.title('**what is the descending movies length in minutes for pixar**??')

# Creating the Bar Chart
    bar = plt.figure(figsize=(10,4))
    width = 0.40
    plt.title('Movies Length in Minutes')
    plt.xlabel('Movie')
    plt.ylabel('Length')
    plt.bar(df['Movie'],  df['Length'].sort_values(ascending=False), width, color = "green")
    plt.xticks(df['Movie'], rotation='vertical')
    st.write(bar)


else:
    # To make picture on the right and paragraph on left
    col1, col2 = st.columns(2)
    with col1:
        st.title('**How does the critics evaluate Pixar Movies??**')
    with col2:
        st.image("pixar-2.jpg", width=300)

# Creating the comparing subplots Chart
    fig, ax1 = plt.subplots(figsize=(10,4))
    plt.title('Comparing between MS critics & RT Critics')

    # ax1 character
    ax1.set_xlabel('Movies_names')
    color = 'green'
    ax1.set_ylabel('Metacritic Score', color= color)
    ax1.plot(df['Movie'], df['Metacritic Score'], color= color)
    ax1.tick_params(axis='y', labelcolor= color)
    plt.xticks(df['Movie'], rotation='vertical')

    # instantiate a second axes that shares the same x-axis
    ax2 = ax1.twinx()  

    # ax2 character
    color = 'red'
    ax2.set_ylabel('RT_score', color= color)  # we already handled the x-label with ax1
    ax2.plot(df['Movie'], df['RT Score'], color= color)
    ax2.tick_params(axis='y', labelcolor= color)
    plt.xticks(df['Movie'], rotation='vertical')

    st.write(fig, ax1)
  
