import pandas as pd

file_path = "data/raw/ApexPlanet_DataAnalytics_Dataset.xlsx"

df = pd.read_excel(file_path)

print("=" * 50)
print("DATA QUALITY REPORT")
print("=" * 50)

print("\n1. Dataset Shape")
print(df.shape)

print("\n2. Missing Values")
print(df.isnull().sum())

print("\n3. Duplicate Rows")
print(df.duplicated().sum())

print("\n4. Data Types")
print(df.dtypes)

print("\n5. Numerical Statistics")
print(df.describe())

print("\n6. Unique Values")
for column in df.columns:
    print(f"{column}: {df[column].nunique()} unique values")