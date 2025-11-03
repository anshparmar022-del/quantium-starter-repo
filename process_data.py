import pandas as pd
import os

# Path to your data folder
data_folder = "data"

# List of all CSV files inside the folder
csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

# List to hold all filtered DataFrames
filtered_dfs = []

for file in csv_files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path)
    
    # Filter only pink morsels (case-insensitive just in case)
    df = df[df["product"].str.lower() == "pink morsel"]
    
    # Create the sales column
    df["sales"] = df["quantity"] * df["price"]
    
    # Keep only the required columns
    df = df[["sales", "date", "region"]]
    
    # Add to list
    filtered_dfs.append(df)

# Combine all filtered data
final_df = pd.concat(filtered_dfs)

# Save to a new CSV file
final_df.to_csv("formatted_output.csv", index=False)

print("✅ Data processing complete! File saved as formatted_output.csv")
