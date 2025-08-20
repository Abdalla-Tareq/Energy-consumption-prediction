import streamlit as st
import joblib
import numpy as np

# Load models
models = {
    "Linear Regression": joblib.load("model_lr.plt"),
    "Random Forest": joblib.load("model_rf.plt"),
    "Decision Tree": joblib.load("model_dt.plt"),
    "Gradient Boosting": joblib.load("model_gbr.plt"),
}

st.title("Energy Consumption Prediction App")

# Model selection
model_name = st.selectbox("Choose a model", list(models.keys()))
model = models[model_name]

# User input
st.header("Enter the features:")

square_footage = st.number_input("Square Footage", min_value=0.0)
num_occupants = st.number_input("Number of Occupants", min_value=0)
appliances_used = st.number_input("Appliances Used", min_value=0)
avg_temp = st.number_input("Average Temperature", min_value=-50.0, max_value=60.0)
building_type = st.selectbox("Building Type", ["Residential", "Commercial", "Industrial"])
day_of_week = st.selectbox("Day of Week", ["Weekday", "Weekend"])

# Map categorical to numeric (same as training)
building_map = {'Residential': 1, 'Commercial': 2, 'Industrial': 3}
week_map = {'Weekday': 1, 'Weekend': 2}

input_data = np.array([[
    square_footage,
    num_occupants,
    appliances_used,
    avg_temp,
    building_map[building_type],
    week_map[day_of_week]
]])

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Energy Consumption: {prediction:.2f}")