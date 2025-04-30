import streamlit as st
import pandas as pd
import io
from  word2number import w2n
import matplotlib.pyplot as plt
import numpy as np

st.title("Retail_sale site")

df = pd.read_csv("./retail_sales.csv")

st.write("fetching the dataset", df)
df.columns = df.columns.str.strip()

st.write("column", df['Price'])
df['Price'] = df['Price'].str.replace('$', '')
st.write("price", df['Price'])
df['Price'] = df['Price'].str.replace('USD', '')
st.write("New_price", df['Price'])
df = df.dropna()
st.write("existing_price", df['Price'])
df['Quantity Sold'].values
st.write("Quantity_sold", df['Quantity Sold'])
df['Quantity Sold'] = df['Quantity Sold'].str.replace('five', '')
st.write("old_Quantity_sold", df['Quantity Sold'])
df['Quantity Sold']
st.write("New_Quantity_sold", df['Quantity Sold'])
df['Sale Date'] = pd.to_datetime(df['Sale Date'], errors='coerce', infer_datetime_format=True).dt.strftime('%m/%d/%Y')
st.write("old Date", df['Sale Date'])
df = df.dropna()
st.write("Date", df['Sale Date'])
df = df.dropna(ignore_index=True)
st.write("Date", df['Sale Date'])
df = df.drop_duplicates(ignore_index=True)
st.write("Date", df)
df['Total Sale'] = pd.to_numeric(df['Price']) * pd.to_numeric(df['Quantity Sold'])
st.write("Total Sale", df['Total Sale'])
df.count()
st.write("count", df)
df['month'] = pd.DatetimeIndex(df['Sale Date']).month
st.write("month", df['month'])
revenue_per_store = df.groupby('Store')['Total Sale'].sum().sort_values 
print(revenue_per_store)
st.write("store", df)
most_sold_product = df.groupby('Product')['Quantity Sold'].sum().sort_values
print(most_sold_product)
st.write("product", df)
df
st.write("df", df)
df["Product"].values
st.write("product", df)
df["Total Sale"].values
st.write("Total Sale", df)
df = df.dropna()
st.write("product", df["Product"])
df
st.write("df", df)
df["Total Sale"].values
st.write("Total Sale", df["Total Sale"])
df["Product"].values
st.write("Product", df["Product"])

uniqueProduct = df["Product"].unique()
uniqueProductDict = { y: x for x, y in enumerate(uniqueProduct)}
uniqueProductDict
st.write("unique", df["Product"])

st.title("Visualizations")
x = [ uniqueProductDict[x] for x in  df["Product"].values ]
y = df["Total Sale"].values

st.write("\n\n\n")
fig, ax = plt.subplots()
# fig, ax.(figsize=(20, 10))
ax.scatter(x, y)
ax.set_xlabel("Product")
ax.set_ylabel("Total sale", loc="center")
st.pyplot(fig)
