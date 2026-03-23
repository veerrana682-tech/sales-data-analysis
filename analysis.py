import pandas as pd

df = pd.read_csv("sales_data.csv")

print("Dataset:")
print(df.head())

print("\nTotal Sales:", df['Sales'].sum())
print("Total Profit:", df['Profit'].sum())

print("\nSales by Region:")
print(df.groupby('Region')['Sales'].sum())

print("\nTop Product:")
print(df.groupby('Product')['Sales'].sum().idxmax())
