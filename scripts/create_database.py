import pandas as pd
import sqlite3
from pathlib import Path

# Project location
BASE_DIR = Path(__file__).resolve().parent.parent

# Input Excel file
INPUT_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "ApexPlanet_Cleaned_Sales.xlsx"
)

# Database location
DATABASE_DIR = BASE_DIR / "database"
DATABASE_DIR.mkdir(
    parents=True,
    exist_ok=True
)

DATABASE_FILE = DATABASE_DIR / "apexplanet_sales.db"

# Load Excel
df = pd.read_excel(INPUT_FILE)

# Convert date
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)

# Connect to SQLite
connection = sqlite3.connect(DATABASE_FILE)

# Create sales table
df.to_sql(
    "sales",
    connection,
    if_exists="replace",
    index=False
)

connection.close()

print("=" * 60)
print("SQLITE DATABASE CREATED SUCCESSFULLY")
print("=" * 60)

print("Database:")
print(DATABASE_FILE)

print("\nTable:")
print("sales")

print("\nRows:")
print(len(df))