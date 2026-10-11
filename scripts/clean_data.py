import pandas as pd

input_file = "data/raw/ApexPlanet_DataAnalytics_Dataset.xlsx"
output_file = "data/processed/ApexPlanet_Cleaned_Sales.xlsx"

df = pd.read_excel(input_file)

# Convert date column
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# Fill missing Age with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing City
df["City"] = df["City"].fillna("Unknown")

# Remove completely duplicated rows
df = df.drop_duplicates()

# Save cleaned dataset
df.to_excel(output_file, index=False)

print("Cleaning completed.")
print("Cleaned dataset shape:", df.shape)
print("Saved to:", output_file)