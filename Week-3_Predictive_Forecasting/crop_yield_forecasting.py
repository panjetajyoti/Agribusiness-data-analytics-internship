"""
Week 3: Time-Series Trend Modeling & Predictive Regression for Agribusiness.
Simulating ARIMA/SARIMAX & Linear Trend Evaluation for Commodity Yields.
"""

import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, root_mean_squared_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing


def run_predictive_yield_model():
    np.random.seed(42)
    years = pd.date_range(start="2010", periods=16, freq="YE")

    # Upward technology trend + weather fluctuations
    trend = np.linspace(3.0, 4.3, 16)
    noise = np.random.normal(0, 0.15, 16)
    yield_series = pd.Series(trend + noise, index=years)

    train_data = yield_series.iloc[:-3]
    test_data = yield_series.iloc[-3:]

    # Holt's Exponential Smoothing (Additive Trend)
    model = ExponentialSmoothing(
        train_data, trend="add", seasonal=None
    ).fit()
    forecast = model.forecast(steps=3)

    mae = mean_absolute_error(test_data, forecast)
    rmse = root_mean_squared_error(test_data, forecast)

    print("--- CROP YIELD FORECAST VALIDATION RESULTS ---")
    print(f"Test Actuals:\n{test_data.to_dict()}")
    print(f"Model Forecast:\n{forecast.to_dict()}")
    print(f"\nMean Absolute Error (MAE): {mae:.4f} MT/Ha")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f} MT/Ha")


if __name__ == "__main__":
    run_predictive_yield_model()
