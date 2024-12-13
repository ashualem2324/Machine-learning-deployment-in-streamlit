import streamlit as st
def show_about_us():
    st.markdown("<h4 style='text-align:center'>IOT based data inroom Occupancy Detection using Machine learning\n</h4>", unsafe_allow_html=True)
    st.markdown("""Person detection in an embedded IoT device without the use of a computer vision solution refers to the ability to detect the presence of a person in a given environment using sensors and signal processing techniques instead of relying on visual image analysis.
Typically, this type of person detection solution is achieved by leveraging various types of sensors, such as passive infrared (PIR) sensors, ultrasonic sensors, and radar sensors, which can detect physical changes in the environment caused by the presence of a person, such as body heat or movement.
Signal processing techniques are then applied to the sensor data to detect and differentiate the signal patterns associated with a person's presence from other environmental noise. Machine learning algorithms may also be used to improve the accuracy of the person detection system.
By using sensors and signal processing techniques, this type of person detection system can be implemented in an embedded IoT device with limited computing resources, making it suitable for a wide range of applications, such as home automation, security systems, and smart buildings.
""")
 
         