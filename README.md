# NYC TLC Fare Estimator

This project analyzes over 3 million New York City Yellow Taxi trips from January 2024 to build a machine learning model that accurately predicts taxi fares. It includes a full end-to-end data analysis pipeline—data cleaning, exploratory analysis, modeling, evaluation—and an interactive Streamlit app for fare estimation.

## Project Highlights

- Modeling: Built a Linear Regression model with strong performance  
  - R²: 0.892  
  - MSE: 32.29  
- Rule-Based Comparison: Created a hand-crafted fare estimation function (R²: 0.073) as a baseline.
- Exploratory Data Analysis: Visualized fare distributions, trip distances, and outlier patterns.
- Feature Engineering: Included trip distance, time of day, day of week, and NYC-specific surcharges.
- App Prototype: Developed a Streamlit app for real-time fare estimation based on user input.

## Key Files

| File                              | Description                                                  |
|-----------------------------------|--------------------------------------------------------------|
| `Yellow_Trip_DataAnalysis.ipynb`  | Main notebook: data cleaning, EDA, modeling, evaluation      |
| `linear_fare_plot_dayofweek.png`  | Predicted vs. actual fare plot (Linear Regression)           |
| `trip_distance_histogram.png`     | Histogram of trip distances                                  |
| `fare_model.pkl`                  | Trained Linear Regression model (to be uploaded)             |
| `app.py`                          | Streamlit app for interactive fare prediction (to be uploaded) |

## Results

- Most model predictions fall within ±5 USD of the actual fare.
- Model accounts for base fare, per-mile charges, peak hour multipliers (surge), and surcharges.
- Rule-based model underperformed the machine learning model, confirming the advantage of data-driven estimation.

## Next Steps

- Add geospatial features (pickup and drop-off zone IDs) for improved accuracy.
- Incorporate toll and airport flat fare handling.
- Test non-linear models such as Random Forest and XGBoost.
- Deploy the Streamlit app via Streamlit Community Cloud.
- Upload model and app files for full functionality.

## Tools Used

- Python (pandas, numpy, scikit-learn, matplotlib, seaborn)
- Jupyter Notebook
- Streamlit
- Git and GitHub

## Contact

For questions or feedback, please reach out via GitHub issues or connect on LinkedIn.
