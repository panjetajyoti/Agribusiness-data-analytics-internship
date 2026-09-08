"""
Week 4: Performance Evaluation and Strategic Agribusiness KPI Matrix.
Benchmarking Production, Economics, and Post-Harvest Losses against Industry Standards.
"""

import numpy as np
import pandas as pd


def generate_kpi_evaluation_matrix():
    kpi_records = {
        "Metric": [
            "Crop Yield (MT/Ha)",
            "Operating Cost per Quintal (INR/q)",
            "Net Profit Margin (%)",
            "Water Use Efficiency (m3/MT)",
            "Post-Harvest Loss (%)",
        ],
        "Enterprise_Actual": [3.85, 1850.0, 16.8, 1420.0, 14.2],
        "Benchmark_Baseline": [4.20, 1650.0, 20.0, 1150.0, 8.5],
        "Operational_Target": [4.50, 1500.0, 23.5, 950.0, 5.0],
    }

    df = pd.DataFrame(kpi_records)
    df["Variance_vs_Benchmark"] = df["Enterprise_Actual"] - df["Benchmark_Baseline"]

    # Normalize performance ratio (higher is better; inverse for costs and losses)
    df["Performance_Ratio"] = [
        df.loc[0, "Enterprise_Actual"] / df.loc[0, "Benchmark_Baseline"],
        df.loc[1, "Benchmark_Baseline"] / df.loc[1, "Enterprise_Actual"],
        df.loc[2, "Enterprise_Actual"] / df.loc[2, "Benchmark_Baseline"],
        df.loc[3, "Benchmark_Baseline"] / df.loc[3, "Enterprise_Actual"],
        df.loc[4, "Benchmark_Baseline"] / df.loc[4, "Enterprise_Actual"],
    ]

    weights = [0.25, 0.20, 0.25, 0.15, 0.15]
    composite_index = np.dot(df["Performance_Ratio"], weights) * 100

    print("==========================================================")
    print("        AGRIBUSINESS ENTERPRISE KPI EVALUATION            ")
    print("==========================================================")
    print(df.to_string(index=False))
    print("----------------------------------------------------------")
    print(f"Overall Enterprise Efficiency Index: {composite_index:.2f}%")
    print("==========================================================")


if __name__ == "__main__":
    generate_kpi_evaluation_matrix()
