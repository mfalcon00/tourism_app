import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from home_page import show_home_page
import pandas as pd

page = st.sidebar.selectbox("Explore or Predict", ("Home", "Explore","Predict"), key ='sb1')

st.empty()
if page == "Home":
    show_home_page()
if page == "Explore":
    show_explore_page()
if page == "Predict":
    show_predict_page()
