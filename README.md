# YellowTrip — NYC Taxi Fare Estimator

This project analyzes over 3 million New York City Yellow Taxi trips from January 2024 to build a machine learning model that accurately predicts taxi fares. It includes a full end-to-end data analysis pipeline — data cleaning, exploratory analysis, modeling, evaluation, and an interactive Streamlit app for fare estimation.

## Project Highlights

- **Modeling:** Ensemble model (XGBoost + LightGBM) with strong performance
  - R²: 0.892
  - MSE: 32.29
  - Kaggle Top 15%
- **Baseline Comparison:** Rule-based fare estimation function (R²: 0.073) — confirms the advantage of data-driven estimation
- **Exploratory Data Analysis:** Visualized fare distributions, trip distances, and outlier patterns
- **Feature Engineering:** Trip distance, time of day, day of week, and NYC-specific surcharges
- **App:** Streamlit app for real-time fare estimation based on user input → [Live Demo ↗](https://yellowtrip-fyhkcrqpnatnqtbu4gk7du.streamlit.app)

## Key Files

| File | Description |
|---|---|
| `Yellow_Trip_DataAnalysis.ipynb` | Main notebook: data cleaning, EDA, modeling, evaluation |
| `fare_model.pkl` | Trained ensemble model (XGBoost + LightGBM) |
| `app.py` | Streamlit app for interactive fare prediction |
| `linear_fare_plot_dayofweek.png` | Predicted vs. actual fare plot |
| `trip_distance_histogram.png` | Histogram of trip distances |

## Results

- Most predictions fall within ±5 USD of the actual fare
- Ensemble model significantly outperforms the rule-based baseline (R² 0.892 vs 0.073)
- Model accounts for base fare, per-mile charges, peak hour multipliers, and NYC-specific surcharges

## Data Sources

- NYC Taxi & Limousine Commission (TLC) Trip Record Data:
  https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
  Dataset used: Yellow Taxi Trip Data for January 2024 (Parquet format)
- TLC Rate Card: https://www.nyc.gov/assets/tlc/downloads/pdf/taxi_rate_card.pdf
- NYC Congestion Pricing Info: https://www.nyc.gov/html/tlc/html/passenger/taxicab_rate.shtml

## Tools Used

- Python (Pandas, NumPy, scikit-learn, XGBoost, LightGBM, Matplotlib, Seaborn)
- Jupyter Notebook
- Streamlit
- Git and GitHub

## Contact

LinkedIn: [linkedin.com/in/sommer-vargas](https://www.linkedin.com/in/sommer-vargas)
