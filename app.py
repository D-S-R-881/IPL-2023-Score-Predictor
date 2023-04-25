import streamlit as st
import pickle
import pandas as pd
import numpy as np
import xgboost
from xgboost import XGBRegressor
import os

# Get the absolute file path of the model.pkl file
model_file_path = os.path.join(os.path.dirname(__file__), "model.pkl")

# Load the model from the file
with open(model_file_path, 'rb') as f:
    model = pickle.load(f)

# model = pickle.load(open('model.pkl','rb'))

teams = ['Chennai Super Kings',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Rajasthan Royals',
 'Sunrisers Hyderabad',
 'Mumbai Indians',
 'Punjab Kings',
 'Delhi Capitals',
 'Lucknow Super Giants',
 'Gujarat Titans']

venues = ['Wankhede Stadium',
 'Eden Gardens',
 'Arun Jaitley Stadium',
 'M.Chinnaswamy Stadium',
 'MA Chidambaram Stadium',
 'Rajiv Gandhi International Stadium',
 'Punjab Cricket Association IS Bindra Stadium',
 'Sawai Mansingh Stadium',
 'Narendra Modi Stadium',
 'Himachal Pradesh Cricket Association Stadium',
 'Barsapara Cricket Stadium',
 'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium']

st.set_page_config(page_title = "Score Predictor", initial_sidebar_state="collapsed")
st.title('IPL 2023 1st Innings Score Predictor')


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1554034483-04fda0d3507b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjJ8fHBsYWluJTIwYmFja2dyb3VuZHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=600&q=60");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select Batting Team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select Bowling Team', sorted(teams))

venue = st.selectbox('Select Venue',sorted(venues))

col3,col4,col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs Done(Works for over>5)')
with col5:
    wickets = st.number_input('Wickets Left')

last_five = st.number_input('Runs scored in last 5 overs')

if st.button('Predict Score'):
    balls_left = 120 - (overs*6)
    wickets_left = wickets
    current_run_rate = current_score/overs

    input_df = pd.DataFrame(
     {'batting_team': [batting_team], 'bowling_team': [bowling_team],'venue':venue, 'current_score': [current_score],'balls_left': [balls_left], 'wickets_left': [wickets], 'current_run_rate': [current_run_rate], 'last_five': [last_five]})
    result = model.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))