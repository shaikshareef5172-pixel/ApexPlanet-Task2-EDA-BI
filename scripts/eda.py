import pandas as pd
from pathlib import Path

# ---------------------------------------
# Project paths
# ---------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "ApexPlanet_Cleaned_Sales.xlsx"
)

OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

# ---------------------------------------
# Load dataset
# ---------------------------------------

df = pd.read_excel(INPUT_FILE)

# Convert date
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# ---------------------------------------
# Dataset Shape
# ---------------------------------------

print("\nDATASET SHAPE")

print(df.shape)

# ---------------------------------------
# Numerical Columns
# ---------------------------------------

numeric_columns = [
    "Age",
    "Quantity",
    "Unit_Price",
    "Total_Sales"
]

# ---------------------------------------
# Numerical Statistics
# ---------------------------------------

print("\nNUMERICAL STATISTICS")

print(
    df[numeric_columns].describe()
)

# ---------------------------------------
# Median
# ---------------------------------------

print("\nMEDIAN")

print(
    df[numeric_columns].median()
)

# ---------------------------------------
# Mode
# ---------------------------------------

print("\nMODE")

for column in numeric_columns:

    mode_values = df[column].mode()

    if len(mode_values) > 0:

        print(
            f"{column}: {mode_values.iloc[0]}"
        )

# ---------------------------------------
# Gender Distribution
# ---------------------------------------

print("\nGENDER DISTRIBUTION")

print(
    df["Gender"].value_counts()
)

# ---------------------------------------
# City Distribution
# ---------------------------------------

print("\nCITY DISTRIBUTION")

print(
    df["City"].value_counts()
)

# ---------------------------------------
# Product Distribution
# ---------------------------------------

print("\nPRODUCT DISTRIBUTION")

print(
    df["Product"].value_counts()
)

# ---------------------------------------
# Category Distribution
# ---------------------------------------

print("\nCATEGORY DISTRIBUTION")

print(
    df["Category"].value_counts()
)

# ---------------------------------------
# Save numerical summary
# ---------------------------------------

summary = df[numeric_columns].describe()

summary.to_csv(
    OUTPUT_DIR / "eda_summary.csv"
)

print("\nEDA summary saved successfully.")

print(
    "File:",
    OUTPUT_DIR / "eda_summary.csv"
)

print("\nEDA ANALYSIS COMPLETED SUCCESSFULLY.")