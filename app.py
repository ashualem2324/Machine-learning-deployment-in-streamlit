import streamlit as st 
from predict_page import show_predict_page
from data_visual import show_explore_page
from about import show_about_us
from home import show_home_page
from contact import show_contact_us
from algorithem import show_algorithm
contianer=st.container()
selected_page = st.sidebar.radio('Navigations', ['Home','Predict' ,'About', 'Contact','Algorithms','Visualize'])
if selected_page == "Home":
    show_home_page()
elif selected_page=="Predict":
  show_predict_page()
elif selected_page=="About":
    show_about_us()
elif selected_page=="Contact":
    show_contact_us()
elif selected_page=="Algorithms":
    show_algorithm()
elif selected_page=="Visualize":
    show_explore_page()


