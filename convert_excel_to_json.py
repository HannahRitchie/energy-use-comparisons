import pandas as pd
import json
import numpy as np

# Read the Excel file
df = pd.read_excel('Energy use of products.xlsx')

# Convert to the format needed for the visualization
products = []

for idx, row in df.iterrows():
    product = {
        "name": row['Product'],
        "wattage": None if pd.isna(row['Energy rating (W)']) else float(row['Energy rating (W)']),
        "fixed_wh": None if pd.isna(row['Energy used (Wh)']) else float(row['Energy used (Wh)']),
        "input_type": None,
        "default_value": None
    }

    # Determine input type based on 'User selection' column
    user_selection = row['User selection']
    hours_per_day = row['Hours per day']

    if pd.isna(user_selection):
        product['input_type'] = 'fixed'
        product['default_value'] = None
    elif user_selection == 'Hours':
        product['input_type'] = 'hours'
        product['default_value'] = float(hours_per_day) if not pd.isna(hours_per_day) else 1.0
        # Recalculate fixed_wh for hours-based items
        if product['wattage'] is not None and product['default_value'] is not None:
            product['fixed_wh'] = product['wattage'] * product['default_value']
    elif user_selection == 'Number of cycles':
        product['input_type'] = 'cycles'
        product['default_value'] = 1
    elif user_selection == 'Number of full boils':
        product['input_type'] = 'boils'
        product['default_value'] = 1
    elif user_selection == 'Number of queries':
        product['input_type'] = 'queries'
        product['default_value'] = 1
    elif user_selection == 'Miles driven':
        product['input_type'] = 'miles'
        product['default_value'] = 10

    products.append(product)

# Save to JSON file
with open('products_data.json', 'w') as f:
    json.dump(products, f, indent=2)

print(f"Converted {len(products)} products to JSON")
print("\nFirst 3 products:")
for p in products[:3]:
    print(json.dumps(p, indent=2))
