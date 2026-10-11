import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel(
    "data/processed/ApexPlanet_Cleaned_Sales.xlsx"
)

columns = [
    "Age",
    "Quantity",
    "Unit_Price",
    "Total_Sales"
]

sns.pairplot(
    df[columns]
)

plt.savefig(
    "outputs/plots/pair_plot.png"
)

plt.close()

print("Pair plot created.")