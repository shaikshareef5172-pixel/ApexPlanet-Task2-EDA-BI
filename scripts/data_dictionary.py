import pandas as pd

data = {
    "Column": [
        "Order_ID",
        "Order_Date",
        "Customer_ID",
        "Customer_Name",
        "Age",
        "Gender",
        "City",
        "Product",
        "Category",
        "Quantity",
        "Unit_Price",
        "Total_Sales"
    ],

    "Description": [
        "Unique order identifier",
        "Date of order",
        "Customer identifier",
        "Customer name",
        "Customer age",
        "Customer gender",
        "Customer city",
        "Product purchased",
        "Product category",
        "Number of units purchased",
        "Price per unit",
        "Total sales amount"
    ],

    "Data_Type": [
        "Text",
        "Date",
        "Text",
        "Text",
        "Numeric",
        "Categorical",
        "Categorical",
        "Categorical",
        "Categorical",
        "Numeric",
        "Numeric",
        "Numeric"
    ]
}

dictionary = pd.DataFrame(data)

dictionary.to_excel(
    "data/processed/data_dictionary.xlsx",
    index=False
)

print("Data dictionary created successfully.")