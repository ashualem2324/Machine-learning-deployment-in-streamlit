import streamlit as st
import pickle
import pandas as pd
import numpy as np 
def load_model():
    with open('saved_pikle.pkl','rb') as file:
     data=pickle.load(file)
    return data

data=load_model()
model_loaded=data['model']
def show_predict_page():
 st.markdown("<h4 style='text-align:center'>IOT based data inroom Occupancy Detection using Machine learning\n</h4>", unsafe_allow_html=True)
 Temp = st.text_input('Temperature')
 humidity = st.text_input('Humidity')
 light = st.text_input('Light')
 co2 = st.text_input('CO2')
 humr = st.text_input('HumidityRatio')
 ok = st.button('Submit')
 if ok:
     X=np.array([[Temp,humidity,light,co2,humr]])
     X = X.astype(float)
     occu=model_loaded.predict(X)
     if occu== 1:
        st.subheader(f" The room is Occupied")

     else:
         st.subheader(f" The room is Not Occupied")
         
         
