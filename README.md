# NYC TLC Fare Estimator

This project analyzes over 3 million New York City Yellow Taxi trips from January 2024 to build a machine learning model that accurately predicts taxi fares. It includes a full end-to-end data analysis pipeline — data cleaning, exploratory analysis, feature engineering, ensemble modeling, evaluation, and an interactive Streamlit app for fare estimation.

## Project Highlights

- **Modeling:** Ensemble model (XGBoost + LightGBM) with strong performance
  - R²: 0.892
  - MSE: 32.29
  - Kaggle Top 15%
- **Baseline Comparison:** Rule-based fare estimation function (R²: 0.073) used as a benchmark, confirming the advantage of data-driven approaches
- **Exploratory Data Analysis:** Fare distributions, trip distances, outlier patterns, and geospatial pickup/dropoff zones
- **Feature Engineering:** Trip distance, time of day, day of week, NYC-specific surcharges, congestion pricing, and geospatial zone features
- **Deployed App:** Streamlit app for real-time fare estimation based on user input

## Live Demo

[yellowtrip-fyhkcrqpnatnqtbu4gk7du.streamlit.app](https://yellowtrip-fyhkcrqpnatnqtbu4gk7du.streamlit.app)

## Key Files

| File                              | Description                                                  |
|-----------------------------------|--------------------------------------------------------------|
| `Yellow_Trip_DataAnalysis.ipynb`  | Main notebook: data cleaning, EDA, modeling, evaluation      |
| `linear_fare_plot_dayofweek.png`  | Predicted vs. actual fare plot                               |
| `trip_distance_histogram.png`     | Histogram of trip distances                                  |
| `fare_model.pkl`                  | Trained ensemble model                                       |
| `app.py`                          | Streamlit app for interactive fare prediction                |

## Results

- Most model predictions fall within ±5 USD of the actual fare
- Model accounts for base fare, per-mile charges, peak hour multipliers, and NYC surcharges
- Ensemble approach (XGBoost + LightGBM) significantly outperformed both the rule-based baseline and single-model approaches

## Data Sources

- NYC Taxi & Limousine Commission (TLC) Trip Record Data:  
  https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page  
  Dataset used: Yellow Taxi Trip Data for January 2024 (Parquet format)

Additional references:
- TLC Rate Card: https://www.nyc.gov/assets/tlc/downloads/pdf/taxi_rate_card.pdf
- NYC Congestion Pricing Info: https://www.nyc.gov/html/tlc/html/passenger/taxicab_rate.shtml

## Tools Used

- Python (pandas, numpy, scikit-learn, xgboost, lightgbm, matplotlib, seaborn)
- Jupyter Notebook
- Streamlit
- Git and GitHub

## Contact

LinkedIn: [linkedin.com/in/sommer-vargas](https://www.linkedin.com/in/sommer-vargas/)
