"""
Week 1: Data Ingestion, Profiling, Outlier Removal, and Unit Normalization.
Data Sources: Directorate of Economics and Statistics (DES), Agmarknet, IMD.
"""

import numpy as np
import pandas as pd


def generate_raw_agri_data(n_records=500):
    np.random.seed(42)
    districts = ["Karnal", "Kurukshetra", "Ambala", "Ludhiana", "Patiala"]
    crops = ["Wheat", "Paddy", "Mustard"]

    data = {
        "District": np.random.choice(districts, n_records),
        "Crop": np.random.choice(crops, n_records),
        "Reported_Yield_Raw": np.random.normal(38.0, 6.5, n_records),
        "Rainfall_mm": np.random.normal(650, 120, n_records),
        "Mandi_Price_Quintal": np.random.normal(2250, 250, n_records),
    }
    df = pd.DataFrame(data)

    # Inconsistent units and missing data simulation
    df.loc[10:25, "Reported_Yield_Raw"] = np.nan
    df.loc[30:35, "Reported_Yield_Raw"] = df.loc[
        30:35, "Reported_Yield_Raw"
    ] * 10  # quintals instead of MT
    return df


def clean_agri_pipeline(df):
    print(f"[*] Ingested raw records: {len(df)}")

    # 1. Imputation
    df["Reported_Yield_Raw"] = df.groupby(["District", "Crop"])[
        "Reported_Yield_Raw"
    ].transform(lambda x: x.fillna(x.median()))

    # 2. IQR Outlier Filtering & Unit Normalization (Target: MT/Hectare)
    Q1 = df["Reported_Yield_Raw"].quantile(0.25)
    Q3 = df["Reported_Yield_Raw"].quantile(0.75)
    IQR = Q3 - Q1
    upper_bound = Q3 + 2.5 * IQR

    # Normalize anomalous quintal values back to MT
    df["Cleaned_Yield_MT_Ha"] = np.where(
        df["Reported_Yield_Raw"] > upper_bound,
        df["Reported_Yield_Raw"] / 10.0,
        df["Reported_Yield_Raw"],
    )

    # Standardize Pricing
    df["Mandi_Price_Cleaned"] = df["Mandi_Price_Quintal"].clip(
        lower=1500, upper=3500
    )

    print(f"[+] Cleaned dataset ready with shape: {df.shape}")
    print(
        df[["Crop", "Cleaned_Yield_MT_Ha", "Mandi_Price_Cleaned"]].describe()
    )
    return df


if __name__ == "__main__":
    raw_data = generate_raw_agri_data()
    clean_data = clean_agri_pipeline(raw_data)
