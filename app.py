import streamlit as st
import PIL
import pandas as pd
import plotly.express as px

# global vars
height = 0
weight = 0
gender = ''
age = 0



# Title
st.title("Fitness Trainer")




st.header('Goals')
st.write('Fitness has never been so much fun!')
goal = st.selectbox(" ", ["Select an option ", 'Weight loss', 'General Fitness', 'Endurance', 'Bulking'])
st.header('Your Stats')


# Inputting user stacks
height, weight = st.columns(2)
with height:
    height = st.number_input(label= 'Height (cm)', value = 0)
    gender = st.selectbox("Gender", ['Male', 'Female'])

with weight:
    weight = st.number_input(label= 'Weight (kg)', value = 0)
    age= st.number_input(label= 'Age', value = 18)
diet, excercies = st.columns(2)
nav = 'None'


# Navigation after diet
if goal != "Select an option ":
    with diet:
        nav_d = st.button('Diet')

    with excercies:
        nav_w = st.button('Workout')

# if nav_d==True:
