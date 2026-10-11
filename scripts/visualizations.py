import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "ApexPlanet_Cleaned_Sales.xlsx"
)

PLOTS_DIR = (
    BASE_DIR
    / "outputs"
    / "plots"
)

# Automatically create the plots folder
PLOTS_DIR.mkdir(
    parents=True,
    exist_ok=True
)

# ============================================================
# LOAD DATA
# ============================================================

df = pd.read_excel(INPUT_FILE)

# Make sure Order_Date is a date
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)

print("=" * 60)
print("DATA VISUALIZATION")
print("=" * 60)

# ============================================================
# 1. AGE HISTOGRAM
# ============================================================

plt.figure(figsize=(8, 5))

plt.hist(
    df["Age"],
    bins=10,
    edgecolor="black"
)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(
    PLOTS_DIR / "age_histogram.png",
    dpi=300
)

plt.close()

print("1. Age histogram created")


# ============================================================
# 2. REVENUE BY CATEGORY
# ============================================================

category_sales = (
    df.groupby("Category")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

plt.bar(
    category_sales.index,
    category_sales.values
)

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Total Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    PLOTS_DIR / "category_revenue.png",
    dpi=300
)

plt.close()

print("2. Category revenue chart created")


# ============================================================
# 3. REVENUE BY PRODUCT
# ============================================================

product_sales = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

plt.bar(
    product_sales.index,
    product_sales.values
)

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Total Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    PLOTS_DIR / "product_revenue.png",
    dpi=300
)

plt.close()

print("3. Product revenue chart created")


# ============================================================
# 4. MONTHLY REVENUE TREND
# ============================================================

df["Month"] = (
    df["Order_Date"]
    .dt.to_period("M")
    .astype(str)
)

monthly_sales = (
    df.groupby("Month")["Total_Sales"]
    .sum()
)

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    PLOTS_DIR / "monthly_revenue.png",
    dpi=300
)

plt.close()

print("4. Monthly revenue chart created")


# ============================================================
# 5. QUANTITY VS TOTAL SALES
# ============================================================

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Quantity",
    y="Total_Sales"
)

plt.title("Quantity vs Total Sales")
plt.xlabel("Quantity")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig(
    PLOTS_DIR / "quantity_vs_sales.png",
    dpi=300
)

plt.close()

print("5. Quantity vs sales scatter plot created")


# ============================================================
# 6. CORRELATION HEATMAP
# ============================================================

numeric_columns = [
    "Age",
    "Quantity",
    "Unit_Price",
    "Total_Sales"
]

correlation = df[numeric_columns].corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig(
    PLOTS_DIR / "correlation_heatmap.png",
    dpi=300
)

plt.close()

print("6. Correlation heatmap created")


# ============================================================
# FINAL MESSAGE
# ============================================================

print("\n" + "=" * 60)
print("ALL VISUALIZATIONS CREATED SUCCESSFULLY")
print("=" * 60)

print("\nCharts saved in:")

print(PLOTS_DIR)