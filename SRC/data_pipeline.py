import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Load CSV into a DataFrame."""
    return pd.read_csv(path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing values in numeric columns with the column median."""
    # 1) compute medians only for numeric columns
    medians = df.median(numeric_only=True)
    # 2) fillna using that medians Series (pandas will only apply to matching columns)
    return df.fillna(medians)

def save_data(df: pd.DataFrame, path: str):
    """Save cleaned DataFrame to CSV."""
    df.to_csv(path, index=False)

def main():
    raw_path   = "Data/synthetic_retail_sales_data.csv"
    clean_path = "Data/cleaned_sales.csv"

    df       = load_data(raw_path)
    df_clean = clean_data(df)
    save_data(df_clean, clean_path)
    print(f"Saved cleaned data to {clean_path}")

if __name__ == "__main__":
    main()
