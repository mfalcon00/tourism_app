import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
import pandas as pd


df_in_peryear = pd.read_csv('/Users/marjoriefalcon/Desktop/Bootcamp DS-22/M4P3-Final_Project-main/Tourism/Out/inbound_per_year.csv')
df_in_peryear = df_in_peryear.drop('Unnamed: 0', axis=1)


# Plot - total volume inbound per year
def show_volume_year():
  st.text('\n')
  st.text('\n')
  st.subheader('Inbound volume per year worlwide')
  st.text('\n')
  st.text('\n')
  st.bar_chart(df_in_peryear, x ='index', x_label = '', y_label = 'Thousands')
  st.text('\n')
  st.text('\n')
  


def show_home_page():
    st.title('Tourism in the World')
    st.write('Tourism plays a vital role in the global economy, contributing to employment, cultural exchange, and the development of infrastructure. Tourism statistics are essential for understanding the patterns and dynamics of travel and tourism, helping stakeholders such as governments, businesses, and policymakers make informed decisions.')
    st.write('These statistics encompass a wide range of data, including the number of visitors to a destination, their spending and the impacts of tourism on local economy.')
    st.write('In the "Explore" page it is possible to explore tourism data to uncover insights')
    st.write('In the "Predict" page it is possible to forecast the inbound volume for the top 5 countries')
    st.write('The data used for this project has been extracted from UN Tourism: https://www.unwto.org/')
    st.write('\n')

    
    show_volume_year()




show_home_page()

