# data_cleaning.py
import pandas as pd

def load_data():
    try:
        # Try Excel
        df = pd.read_excel("dataset.xlsx", engine="openpyxl")
    except Exception:
        # Fallback to CSV
        df = pd.read_csv("ottdata2.csv")

    df.columns = df.columns.str.strip()  # Clean column names
    return df

df = load_data()
