import pandas as pd

df = pd.read_excel(
    "Data/processed/ApexPlanet_Cleaned_Sales.xlsx"
)

columns = [
    "Age",
    "Quantity",
    "Unit_Price",
    "Total_Sales"
]

correlation = df[columns].corr()

print("Correlation Matrix:")
print(correlation)

correlation.to_csv(
    "outputs/correlation_matrix.csv"
)

print("\nCorrelation matrix saved successfully.")