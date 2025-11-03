import pandas as pd
import glob
import os

# Path to your data folder
data_folder = "data"

# Read all CSV files in the folder
all_files = glob.glob(os.path.join(data_folder, "*.csv"))

# Combine all CSVs into one DataFrame
df_list = [pd.read_csv(file) for file in all_files]
df = pd.concat(df_list)

# Filter only 'Pink Morsel' products
df = df[df['product'] == 'pink morsel']

# Create sales column
df['sales'] = df['quantity'] * df['price']

# Keep only the required columns
df = df[['sales', 'date', 'region']]

# Save to processed_data.csv
os.makedirs(data_folder, exist_ok=True)
df.to_csv(os.path.join(data_folder, "processed_data.csv"), index=False)

print("✅ processed_data.csv created successfully!")
