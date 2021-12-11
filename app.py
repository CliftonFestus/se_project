import streamlit as st
from PIL import Image
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


# Login
logins= pd.read_excel('logins.xlsx', index_col= 'user')
# if st.sidebar.button('New User'):
#     new_username = st.sidebar.text_input('New Username')
#     new_password = st.sidebar.text_input('New Password')
#     st.write("Thank you for resgistering. We will send you you a verification email.")

logins_dict = logins.to_dict()
username = st.sidebar.text_input('Username')
if username != '':
    if username in logins.index:
        st.sidebar.write('Valid username')
    else:
        st.sidebar.write('Invalid username')

    password = st.sidebar.text_input('Password')
    if password == str(logins_dict['password'][username]):
        st.sidebar.write("Successful login")
        navigator = st.sidebar.selectbox('Take me to', ['Overview', 'Your Stats', 'Goals', 'Resources', 'Credits' ])




        if navigator == 'Overview':
            st.subheader("""Welcome to your new Fitness buddy. Enter your stats to proceed with the recommended training regime. Select a Goal for us to help you work towards a healthy routine. Get your personalised diet to see effective results. """)



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
            goal = st.selectbox(" ", ["Select an option ", 'Weight Loss', 'General Fitness', 'Bulking'])
            # Navigation after diet

            df = pd.read_csv('Exercise Final.csv')
            new = df[['Exercise', 'Equipment', 'Exercise Type', 'Major Muscle', 'Goal ']]
            df2 = new[new['Goal ']==goal]

            muscle = st.selectbox('Muscle', ['Arms', 'Core', 'Full Body' ,'Legs' ])

            if goal!= "Select an option ":
                st.write(df2[df2['Major Muscle']==muscle])



        if navigator == 'Credits':
            st.subheader('This app has been made by Arslan Mansoor, Aditya Narayan Singh, Clifton Festus Malvea and Rohan Rajput')

            st.write("To add register yourself as a new user, please send your email and age to:")
            st.write(" **new_user@fitnessAmigos.com**")
        if navigator == 'Resources':
            image= st.image(Image.open('diet2.png'), caption='diet')
