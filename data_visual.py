import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv("Occupancy.csv")
    df=df[['Temperature','Humidity','Light','CO2','HumidityRatio','Occupancy']]
  
    return df

df = load_data()

def show_explore_page():
    st.title("Explore Indoor Occupancy classification")
    data = df["Occupancy"].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)
    st.bar_chart(data)

    
    
    
