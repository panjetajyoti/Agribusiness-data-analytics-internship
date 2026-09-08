# Agribusiness Data Analytics & Strategic Advisory

A comprehensive 4-week end-to-end data analytics and quantitative evaluation suite designed for the Indian agribusiness domain. This project bridges public empirical data ingestion, exploratory sanitization, executive visual storytelling, predictive time-series modeling, and strategic KPI benchmarking.

---

## 📌 Project Architecture & Weekly Milestones

### Week 1: Data Collection, Exploration, and Cleaning
* **Core Objective:** Ingestion and cleaning of public agricultural data from sources such as the Directorate of Economics and Statistics (DES), Agmarknet, and the Indian Meteorological Department (IMD).
* **Key Implementations:**
  * Handled missing spatial data using group-median imputations across district clusters.
  * Interquartile Range (IQR) outlier filtering and automatic correction of mixed metric units (Quintals vs. Metric Tons).
  * Automated data-quality checks.

### Week 2: Data Visualization and Reporting
* **Core Objective:** Executive reporting and visual pattern analysis across commodity prices, yield distributions, and storage infrastructure.
* **Key Implementations:**
  * 4-panel executive dashboard built with Matplotlib and Seaborn.
  * Multi-year seasonal mandi price trends across grain varieties (Wheat vs. Paddy).
  * Regional warehousing capacity distribution analysis highlighting post-harvest exposure risks.

### Week 3: Predictive Analysis and Trend Forecasting
* **Core Objective:** Time-series forecasting and regression modeling to predict seasonal crop yields.
* **Key Implementations:**
  * Built Holt’s Linear Exponential Smoothing and rolling autoregressive models.
  * Out-of-sample backtesting across historical multi-year harvest data.
  * Evaluated performance using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).

### Week 4: Performance Evaluation and Strategic Recommendations
* **Core Objective:** Enterprise-level performance benchmarking across five mission-critical agribusiness KPIs.
* **Key Implementations:**
  * Evaluated Yield/Ha, Operating Cost/Quintal, Net Margin %, Water Use Efficiency, and Post-Harvest Loss %.
  * Benchmarked enterprise actuals against empirical CACP and DES standards.
  * Delivered actionable operational interventions (IoT drip irrigation, solar farm-gate cold storage, and direct e-NAM market integration).

---

## 🚀 Setup and Execution Instructions

**1. Clone the Repository**
```bash
git clone https://github.com/panjetajyoti/agribusiness-data-analytics-internship.git
cd agribusiness-data-analytics-internship
```
**2. Environment Configuration**
```Bash
pip install -r requirements.txt
```
**3. Run Pipeline Modules**
```Bash
# Week 1 Data Cleaning
python Week-1_Data_Collection_Cleaning/data_pipeline_cleaning.py

# Week 2 Visualization Dashboard
python Week-2_Visualization_Reporting/agribusiness_visualization.py

# Week 3 Forecasting Engine
python Week-3_Predictive_Forecasting/crop_yield_forecasting.py

# Week 4 Strategic KPI Evaluation
python Week-4_Performance_KPI_Evaluation/agribusiness_kpi_eval.py
```
 **📊 Key Analytical Findings**
* KPI Metric      | Enterprise Actual | Industry Benchmark | Strategic  Deviation
* Crop Yield        |  3.85MT/Ha        |  4.20MT/Ha         | -8.3%
* Operating Cost    |  INR 1,850/q      | INR 1,650/q        | +12.1% (Adverse)
* Net Profit Margin |  16.8%            | 20.0%              |   -320 bps
* Water Efficiency  | 1,420 m³/MT       | 1,150 m³/MT        | +23.5% (Excessive)
* Post-Harvest Loss |14.2%              |8.5%                | +570bps (Critical)

 **Composite Enterprise Operational Index: 88.54%**

 **🛠 Tech Stack**
* Language: Python 3.10+
* Data Manipulation: Pandas, NumPy
* Visualization: Matplotlib, Seaborn
* Statistical Modeling & Forecasting: Statsmodels, Scikit-Learn
* Domain Datasets: DES, CACP, Agmarknet, CGWB
