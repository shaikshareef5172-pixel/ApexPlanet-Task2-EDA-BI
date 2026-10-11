import sqlite3
import pandas as pd
import os

database = "database/apexplanet_sales.db"

os.makedirs("outputs/sql_results", exist_ok=True)

connection = sqlite3.connect(database)

print("Connected to SQLite database successfully!\n")


# ==================================================
# Q1 - TOP 5 PRODUCTS
# ==================================================

q1 = """
SELECT
    Product,
    SUM(Quantity) AS Total_Quantity,
    ROUND(SUM(Total_Sales), 2) AS Revenue
FROM sales
GROUP BY Product
ORDER BY Revenue DESC
LIMIT 5;
"""

result1 = pd.read_sql_query(q1, connection)

print("========== Q1: TOP 5 PRODUCTS ==========")
print(result1)

result1.to_csv(
    "outputs/sql_results/q1_top_products.csv",
    index=False
)


# ==================================================
# Q2 - MONTHLY REVENUE
# ==================================================

q2 = """
SELECT
    strftime('%Y-%m', Order_Date) AS Month,
    COUNT(*) AS Orders,
    ROUND(SUM(Total_Sales), 2) AS Revenue
FROM sales
GROUP BY Month
ORDER BY Month;
"""

result2 = pd.read_sql_query(q2, connection)

print("\n========== Q2: MONTHLY REVENUE ==========")
print(result2)

result2.to_csv(
    "outputs/sql_results/q2_monthly_revenue.csv",
    index=False
)


# ==================================================
# Q3 - REVENUE BY CATEGORY
# ==================================================

q3 = """
SELECT
    Category,
    SUM(Quantity) AS Units_Sold,
    ROUND(SUM(Total_Sales), 2) AS Revenue
FROM sales
GROUP BY Category
ORDER BY Revenue DESC;
"""

result3 = pd.read_sql_query(q3, connection)

print("\n========== Q3: REVENUE BY CATEGORY ==========")
print(result3)

result3.to_csv(
    "outputs/sql_results/q3_category_revenue.csv",
    index=False
)


# ==================================================
# Q4 - REVENUE BY CITY
# ==================================================

q4 = """
SELECT
    COALESCE(City, 'Unknown') AS City,
    COUNT(*) AS Orders,
    ROUND(SUM(Total_Sales), 2) AS Revenue
FROM sales
GROUP BY City
ORDER BY Revenue DESC;
"""

result4 = pd.read_sql_query(q4, connection)

print("\n========== Q4: REVENUE BY CITY ==========")
print(result4)

result4.to_csv(
    "outputs/sql_results/q4_city_revenue.csv",
    index=False
)


# ==================================================
# Q5 - TOP 10 CUSTOMERS
# ==================================================

q5 = """
SELECT
    Customer_ID,
    Customer_Name,
    COUNT(*) AS Orders,
    ROUND(SUM(Total_Sales), 2) AS Revenue
FROM sales
GROUP BY Customer_ID, Customer_Name
ORDER BY Revenue DESC
LIMIT 10;
"""

result5 = pd.read_sql_query(q5, connection)

print("\n========== Q5: TOP 10 CUSTOMERS ==========")
print(result5)

result5.to_csv(
    "outputs/sql_results/q5_top_customers.csv",
    index=False
)


# ==================================================
# Q6 - REVENUE BY GENDER
# ==================================================

q6 = """
SELECT
    Gender,
    COUNT(*) AS Orders,
    SUM(Quantity) AS Units_Sold,
    ROUND(SUM(Total_Sales), 2) AS Revenue,
    ROUND(AVG(Total_Sales), 2) AS Average_Order_Value
FROM sales
GROUP BY Gender
ORDER BY Revenue DESC;
"""

result6 = pd.read_sql_query(q6, connection)

print("\n========== Q6: REVENUE BY GENDER ==========")
print(result6)

result6.to_csv(
    "outputs/sql_results/q6_gender_revenue.csv",
    index=False
)


# ==================================================
# Q7 - CATEGORY QUANTITY VS REVENUE
# ==================================================

q7 = """
SELECT
    Category,
    SUM(Quantity) AS Units_Sold,
    ROUND(SUM(Total_Sales), 2) AS Revenue,
    ROUND(AVG(Total_Sales), 2) AS Average_Order_Value
FROM sales
GROUP BY Category
ORDER BY Revenue DESC;
"""

result7 = pd.read_sql_query(q7, connection)

print("\n========== Q7: CATEGORY ANALYSIS ==========")
print(result7)

result7.to_csv(
    "outputs/sql_results/q7_category_analysis.csv",
    index=False
)


connection.close()

print("\n==========================================")
print("ALL 7 SQL QUERIES COMPLETED SUCCESSFULLY")
print("==========================================")
print("Results saved inside:")
print("outputs/sql_results/")