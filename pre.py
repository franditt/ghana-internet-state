import pandas as pd

file_path = "2025-07-01_performance_mobile_tiles.parquet"

# Read parquet with pandas
df = pd.read_parquet(file_path)

# Dataset size
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

# Column names
print("Column names:")
for col in df.columns:
    print(col)

# First 5 rows
print("\nFirst 5 rows:")
print(df.head(5))
