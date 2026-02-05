import pandas as pd
import json

# Read the Excel file
df = pd.read_excel('Energy use of products.xlsx')

# Display the data
print("Column names:")
print(df.columns.tolist())
print("\nFirst few rows:")
print(df.head(10))
print("\nAll data:")
print(df.to_string())
