"""
Week 2: Data Visualization and Multi-Panel Executive Reporting.
Visualizing Price Spread, Yield Variance, and Production Correlation.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def plot_agribusiness_dashboard():
    np.random.seed(101)
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]

    paddy_prices = [2150 + np.sin(i / 2) * 180 + i * 15 for i in range(12)]
    wheat_prices = [2275 + np.cos(i / 2) * 120 + i * 10 for i in range(12)]

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(
        "Agribusiness Executive Intelligence Dashboard",
        fontsize=16,
        fontweight="bold",
    )

    # Subplot 1: Price Trends
    axes[0, 0].plot(
        months,
        paddy_prices,
        marker="o",
        color="#2ca02c",
        linewidth=2,
        label="Paddy (Basmati)",
    )
    axes[0, 0].plot(
        months,
        wheat_prices,
        marker="s",
        color="#d62728",
        linewidth=2,
        label="Wheat (Kalyan Sona)",
    )
    axes[0, 0].set_title("Wholesale Mandi Commodity Price Trends (INR/q)")
    axes[0, 0].set_ylabel("Price (INR/q)")
    axes[0, 0].grid(True, linestyle="--", alpha=0.6)
    axes[0, 0].legend()

    # Subplot 2: Crop Yield Distribution
    crops = ["Wheat", "Paddy", "Mustard", "Sugarcane"]
    yields = [
        np.random.normal(4.2, 0.4, 100),
        np.random.normal(3.8, 0.6, 100),
        np.random.normal(1.9, 0.2, 100),
        np.random.normal(72.0, 5.0, 100),
    ]
    axes[0, 1].boxplot(yields[:3], labels=crops[:3], patch_artist=True)
    axes[0, 1].set_title("Yield Variance per Hectare (Grain Crops)")
    axes[0, 1].set_ylabel("Yield (MT/Ha)")
    axes[0, 1].grid(True, linestyle="--", alpha=0.5)

    # Subplot 3: Rainfall vs Yield Scatter
    rain = np.random.uniform(400, 950, 80)
    wheat_yield = 2.5 + (rain * 0.0022) + np.random.normal(0, 0.25, 80)
    axes[1, 0].scatter(rain, wheat_yield, color="#1f77b4", alpha=0.7)
    axes[1, 0].set_title("Impact of Seasonal Rainfall on Yield")
    axes[1, 0].set_xlabel("Seasonal Precipitation (mm)")
    axes[1, 0].set_ylabel("Yield (MT/Ha)")
    axes[1, 0].grid(True, linestyle="--", alpha=0.6)

    # Subplot 4: Storage Breakdown
    labels = ["Cold Storage", "Silos", "Covered Sheds", "Open Storage (High Risk)"]
    shares = [35, 25, 28, 12]
    colors = ["#2b5c8f", "#418ab3", "#8ec6c5", "#e76f51"]
    axes[1, 1].pie(
        shares,
        labels=labels,
        autopct="%1.1f%%",
        startangle=140,
        colors=colors,
    )
    axes[1, 1].set_title("Regional Agri-Warehouse Capacity Distribution")

    plt.tight_layout()
    plt.savefig("agribusiness_dashboard.png", dpi=300)
    print("[+] Dashboard generated and saved as 'agribusiness_dashboard.png'")


if __name__ == "__main__":
    plot_agribusiness_dashboard()
