import streamlit as st 
def show_home_page():
    st.title("Room occupancy detection based on IOT dataset using Machine learning")
    st.image('iot.png',width=None)
    st.markdown("""This dataset is used for binary classification and contains experimental data related to the likelihood of a room being occupied based on five environmental factors: temperature, humidity, light, and carbon dioxide (CO2) and humidity ratio levels.

The dataset consists of five features and a target variable. The features are temperature, humidity, light,humidity ratio and CO2 levels, while the target variable indicates the likelihood of room occupancy. 

A target value of 1 indicates that the room is likely to be occupied, while a target value of 0 indicates that the room is not likely to be occupied.""")