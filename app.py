import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Load model
try:
    model = joblib.load('fare_model.pkl')
except FileNotFoundError:
    st.error("Model file 'fare_model.pkl' not found. Please upload it to the same directory.")
    st.stop()

st.title("TLC Fare Estimator")

# Input fields with validation
distance = st.number_input("Trip Distance (miles)", min_value=0.1, value=2.0, step=0.1)
pickup_time = st.text_input("Pickup Time (YYYY-MM-DD HH:MM:SS)", "2025-05-30 17:00:00")
rate_code = st.selectbox("Rate Type", [1, 2], format_func=lambda x: "Standard" if x == 1 else "Airport",
                         help="1 = Standard rate, 2 = Airport rate (includes additional fee)")

# Validate and process pickup time
try:
    pickup_dt = pd.to_datetime(pickup_time)
    hour = pickup_dt.hour
    dayofweek = pickup_dt.dayofweek
except ValueError:
    st.error("Invalid datetime format. Use YYYY-MM-DD HH:MM:SS.")
    st.stop()

# Estimate duration and surcharges
duration = distance * 2  # 2 min/mile heuristic
congestion = 2.5  # Average from your data
improvement = 0.3
extra = 0.5
airport_fee = 1.25 if rate_code == 2 else 0
tolls = 0

if st.button("Estimate Fare"):
    try:
        # Prepare features with column names matching the trained model
        feature_names = ['trip_distance', 'trip_duration', 'pickup_hour', 'pickup_dayofweek',
                         'congestion_surcharge', 'improvement_surcharge', 'extra', 'Airport_fee', 'tolls_amount']
        features = pd.DataFrame([[distance, duration, hour, dayofweek, congestion, improvement, extra, airport_fee, tolls]],
                                columns=feature_names)
        fare = model.predict(features)[0]
        st.success(f"Estimated Fare: ${round(fare, 2)}")
    except Exception as e:
        st.error(f"Prediction failed: {str(e)}")

st.write("Note: This estimator uses a LinearRegression model trained on 2024 TLC data with an R² of 0.892.")
