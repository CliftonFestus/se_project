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
st.title("Fitness Amigos!!")
st.write('Fitness has never been so much fun')

navigator = st.sidebar.selectbox('Take me to', ['Overview', 'Your Stats', 'Goals', 'Resources', 'Credits' ])





if navigator == 'Your Stats':
# Inputting user stacks
    bmi = 0
    height, weight = st.columns(2)
    with height:
        height = st.number_input(label= 'Height (cm)', value = 160)
        gender = st.selectbox("Gender", ['Male', 'Female'])

    with weight:
        weight = st.number_input(label= 'Weight (kg)', value = 60)
        age= st.number_input(label= 'Age', value = 18)

    # if st.button('Get BMI'):
    bmi = weight*10000/(height*height)

    st.write("Your Body Mass index is ", bmi)

    if st.button('Recomendation'):
        if bmi<18.5:
            st.write('You are underweight. \n You are recomended to follow follow a Bulking Plan.')
        elif bmi <24.9:
            st.write('You are Fit. \n You are recomended to follow a General fitness/Endurance Plan.')

        elif bmi >=25:
            st.write('You are **Overweight!!**. \n You are recomended to follow a Weight Loss plan.')





if navigator == 'Goals':

    st.header('Goals')
    st.write('Fitness has never been so much fun!')
    goal = st.selectbox(" ", ["Select an option ", 'Weight loss', 'General Fitness', 'Endurance', 'Bulking'])
    # Navigation after diet

    diet, excercies = st.columns(2)
    if goal != "Select an option ":
        with diet:
            nav_d = st.button('Diet')

        with excercies:
            nav_w = st.button('Workout')

    # if nav_d==True:
