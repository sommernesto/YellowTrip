# TLC Fare Estimator

This project predicts NYC taxi fares using 3M+ TLC trip records. I built a LinearRegression model (MSE: 32.29, R²: 0.892) and created a Streamlit app for user estimates. A rule-based model (`estimate_fare`) was also tested but underperformed (R²: 0.073).

## Key Files
- `Yellow_Trip_DataAnalysis.ipynb`: Main notebook with code, analysis, and visualizations.
- `linear_fare_plot_dayofweek.png`: LinearRegression predicted vs. actual fares plot.
- `trip_distance_histogram.png`: Trip distance distribution.
- `fare_model.pkl`: Trained LinearRegression model (to be uploaded).
- `app.py`: Streamlit app for fare predictions (to be uploaded).

## How to View
- Open `Yellow_Trip_DataAnalysis.ipynb` to see the full code and analysis.
- Check the plots for visualizations of the results.

## Next Steps
I plan to explore geospatial features (e.g., PULocationID, DOLocationID), test non-linear models like RandomForest, and deploy the app on Streamlit Community Cloud.
