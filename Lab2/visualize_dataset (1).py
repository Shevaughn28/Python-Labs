# %% Import excel to dataframe
import pandas as pd

df = pd.read_excel("Online Retail.xlsx")


# %%  Show the first 10 rows



# %% Generate descriptive statistics regardless the datatypes



# %% Remove all the rows with null value and generate stats again



# %% Remove rows with invalid Quantity (Quantity being less than 0)



# %% Remove rows with invalid UnitPrice (UnitPrice being less than 0)



# %% Only Retain rows with 5-digit StockCode



# %% strip all description



# %% Generate stats again and check the number of rows



# %% Plot top 5 selling countries
import matplotlib.pyplot as plt
import seaborn as sns

top5_selling_countries = df["Country"].value_counts()[:5]
sns.barplot(x=top5_selling_countries.index, y=top5_selling_countries.values)
plt.xlabel("Country")
plt.ylabel("Amount")
plt.title("Top 5 Selling Countries")


# %% Plot top 20 selling products, drawing the bars vertically to save room for product description



# %% Focus on sales in UK



#%% Show gross revenue by year-month
from datetime import datetime

df["YearMonth"] = df["InvoiceDate"].apply(
    lambda dt: datetime(year=dt.year, month=dt.month, day=1)
)



# %% save df in pickle format with name "UK.pkl" for next lab activity
# we are only interested in InvoiceNo, StockCode, Description columns
