# RSFIA

## Project Summary
This project leverages machine learning, specifically a Random Forest model, to generate accurate sales forecasts and proactively identify inventory risks across 50 products and 10 stores over two years. We ensure data consistency and quality throughout the process using a synthetic dataset and a robust batch ingestion pipeline. Our end-to-end system supports reliable model development and includes data validation, feature engineering, and experiment tracking. By capturing complex retail dynamics such as seasonality and promotions, our ML-driven forecasts help reduce stockouts and overstocking, lower holding costs, and improve overall customer satisfaction through smarter inventory management.

**RSFIA** (Retail Sales Forecasting & Inventory Analytics) is an AI‑powered toolkit designed to streamline inventory management and sharpen retail sales forecasts.  
Developed by **Group IV**, RSFIA provides:

- **Data Ingestion Pipeline**: Automatically load and clean raw sales data  
- **Exploratory Data Analysis**: Visualize trends by date, category, and region  
- **Feature Engineering**: Generate predictive features for modeling  
- **Forecasting Models**: Plug‑and‑play algorithms (e.g. ARIMA, Prophet, LSTM)  
- **Deployment Guide**: Dockerized examples for production

---

## Table of Contents

1. [Getting Started](#getting-started)  
2. [Usage](#usage)  
3. [Repository Structure](#repository-structure)  
4. [Contributors](#contributors)  
5. [License](#license)

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/Somar894/RSFIA.git
cd RSFIA

# Install dependencies
pip install -r requirements.txt

# Run the data ingestion pipeline
python SRC/data_pipeline.py

# Perform EDA
python SRC/eda.py
```

## Contributors
1. Sharif Abouomar 
2. Randy Mercado Candia
3. Prisha Srivastava
4. Shivani Yadav
5. Zekeriya Karatas
