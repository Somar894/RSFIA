# SRC/eda.py

import pandas as pd
import matplotlib.pyplot as plt

def main():
    # 1) Load cleaned data (use the exact “Date” header)
    df = pd.read_csv('Data/cleaned_sales.csv', parse_dates=['Date'])

    # 2) Daily sales
    daily = df.groupby('Date')['Sales_Volume'].sum()
    plt.figure()
    daily.plot(title='Daily Sales')
    plt.tight_layout()
    plt.savefig('Data/daily_sales.png')
    plt.close()

    # 3) Category breakdown
    cat = df.groupby('Category')['Sales_Volume'].sum()
    plt.figure()
    cat.plot(kind='bar', title='Sales by Category')
    plt.tight_layout()
    plt.savefig('Data/category_sales.png')
    plt.close()

    # 4) Regional trends
    reg = df.pivot_table(index='Date', columns='Region', values='Sales_Volume', aggfunc='sum')
    plt.figure()
    reg.plot(title='Sales by Region Over Time')
    plt.tight_layout()
    plt.savefig('Data/region_trends.png')
    plt.close()

    print("✅ EDA complete, figures saved to Data/*.png")

if __name__ == '__main__':
    main()
