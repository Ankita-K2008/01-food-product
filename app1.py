import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open('delivery_model.pkl', 'rb'))

# App title
st.title("Delivery Time Prediction")

# User inputs
Distance_km = st.number_input("Distance (km)", min_value=0.0)

Weather = st.selectbox("Weather", [0, 1, 2])

Traffic_Level = st.selectbox("Traffic Level", [0, 1, 2])

Time_of_Day = st.selectbox("Time of Day", [0, 1, 2])

Vehicle_Type = st.selectbox("Vehicle Type", [0, 1, 2])

Preparation_Time_min = st.number_input("Preparation Time (min)", min_value=0)

Courier_Experience_yrs = st.number_input("Courier Experience (years)", min_value=0.0)


# Prediction button
if st.button("Predict Delivery Time"):

    data = pd.DataFrame({
        'Distance_km': [Distance_km],
        'Weather': [Weather],
        'Traffic_Level': [Traffic_Level],
        'Time_of_Day': [Time_of_Day],
        'Vehicle_Type': [Vehicle_Type],
        'Preparation_Time_min': [Preparation_Time_min],
        'Courier_Experience_yrs': [Courier_Experience_yrs]
    })

    prediction = model.predict(data)

    st.success(f"Estimated Delivery Time: {prediction[0]:.2f} minutes")