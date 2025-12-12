import pandas as pd

# Ghana bounding box (lat, lon)
LAT_MIN, LON_MIN = 4.739167, -3.257679
LAT_MAX, LON_MAX = 11.172774, 1.197338

in_parquet  = "2025-04-01_performance_mobile_tiles.parquet"
out_parquet = "Q2_2025_ghana_fixed_mobile.parquet"

df = pd.read_parquet(in_parquet)

# Treat tiles as GPS directly
df["lat"] = df["tile_y"]
df["lon"] = df["tile_x"]

# Filter Ghana
ghana_df = df[
    (df["lat"] >= LAT_MIN) & (df["lat"] <= LAT_MAX) &
    (df["lon"] >= LON_MIN) & (df["lon"] <= LON_MAX)
]

ghana_df.to_parquet(out_parquet, index=False)

print(f"Saved {len(ghana_df)} Ghana rows to {out_parquet}")
