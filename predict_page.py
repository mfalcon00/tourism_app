import streamlit as st
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
#import seaborn as sns

top_five = pd.read_csv('top_five.csv')
top_five = top_five.set_index('Unnamed: 0')
top_five.index.names = ['year']

def load_model_fce():
    
    with open('arima_model_fce.pkl', 'rb') as file:
        m_fce = pickle.load(file)
    return m_fce

def load_model_us():
    with open('arima_model_us.pkl', 'rb') as file:
        m_us= pickle.load(file)
    return m_us

def load_model_mx():
    with open('arima_model_mx.pkl', 'rb') as file:
        m_mx = pickle.load(file)
    return m_mx

def load_model_pol():
    with open('arima_model_pol.pkl', 'rb') as file:
        m_pol = pickle.load(file)
    return m_pol

def load_model_sp():
    with open('arima_model_sp.pkl', 'rb') as file:
        m_sp = pickle.load(file)
    return m_sp


def plot_series(country):
        
        plt.figure(figsize=(15,4))
        country = str(country)
        df = top_five[country]

        st.line_chart(df)


def show_predict_page():
    st.title('Prediction of the number of visitors')
    st.subheader('Top 5 countries having most visitors overall')

    st.empty()
    countries = ('FRANCE', 
                'UNITED STATES OF AMERICA', 
                'POLAND',
                'SPAIN',
                'MEXICO'
    )

    country = st.selectbox('Select a year',countries, placeholder='Select a country', key = 'country1')
    #st.write("You selected:", country)

    country = str(country)
    

    if country == 'FRANCE':
        st.empty()
        plot_series('FRANCE')
        data = load_model_fce()
    if country == 'UNITED STATES OF AMERICA':
        st.empty()
        plot_series('UNITED STATES OF AMERICA')
        data = load_model_us()
    if country == 'POLAND':
        st.empty()
        plot_series('POLAND')
        data = load_model_pol()
    if country == 'SPAIN':
        st.empty()
        plot_series('SPAIN')
        data = load_model_sp()
    if country == 'MEXICO':
        st.empty()
        plot_series('MEXICO')
        data = load_model_mx()

    years_to_predict = st.slider('Years to predict', 0, 3)

    start = len(top_five)-1
    end = start + years_to_predict
    forecast = data.predict(start=start,end = end)
    st.write(forecast)


show_predict_page()
