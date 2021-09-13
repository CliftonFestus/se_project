import streamlit as st
import PIL
import pandas as pd
import plotly.express as px


st.title("Mental Health Chatbot+ app")

df = pd.read_csv("gantt.csv", index_col="Unnamed: 0")
fig = px.timeline(df, x_start="Start", x_end="Finish",
                  y="Task", color='Category')
fig.update_yaxes(tickfont=dict(size=12))
fig.update_xaxes(tickfont=dict(size=12))

fig.update_layout({'height': 500, 'width': 1200})


st.plotly_chart(fig, height=200)
