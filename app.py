import streamlit as st
import pandas as pd
from datetime import datetime

st.title("TLC Fare Estimator")

distance = st.number_input("Trip Distance (miles)", min_value=0.1, value=2.0, step=0.1)
pickup_time = st.text_input("Pickup Time (YYYY-MM-DD HH:MM:SS)", "2025-06-03 10:00:00")
rate_code = st.selectbox("Rate Type", [1, 2], format_func=lambda x: "Standard" if x == 1 else "Airport",
                         help="1 = Standard rate, 2 = Airport rate (includes additional fee)")

try:
    pickup_dt = pd.to_datetime(pickup_time)
    hour = pickup_dt.hour
    dayofweek = pickup_dt.dayofweek
except ValueError:
    st.error("Invalid datetime format. Use YYYY-MM-DD HH:MM:SS.")
    st.stop()

duration = distance * 2
congestion = 2.5
improvement = 0.3
extra = 0.5
airport_fee = 1.25 if rate_code == 2 else 0
tolls = 0

if st.button("Estimate Fare"):
    base_fare = distance * 2.5 + duration * 0.5 + congestion + improvement + extra + airport_fee + tolls
    st.success(f"Estimated Fare: ${round(base_fare, 2)}")
