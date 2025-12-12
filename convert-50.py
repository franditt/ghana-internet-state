import pandas as pd

file_path = "2025-07-01_performance_mobile_tiles.parquet"
out_csv = "performance_mobile_tiles_first50.csv"

df = pd.read_parquet(file_path)

# Take first 50 rows and save to CSV
df.head(50).to_csv(out_csv, index=False)

print(f"Saved first 50 rows to {out_csv}")
