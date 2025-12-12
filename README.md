# ghana-internet-state

OOKLA Dataset

Steps to obtain

Install AWS Command Line Interface
-https://awscli.amazonaws.com/AWSCLIV2.msi

Download latest mobile data (3rd Quarter of 2025)
-aws s3 cp s3://ookla-open-data/parquet/performance/type=mobile/year=2025/quarter=3/ . --no-sign-request --recursive

Download latest fixed data (3rd Quarter of 2025)
-aws s3 cp s3://ookla-open-data/parquet/performance/type=fixed/year=2025/quarter=3/ . --no-sign-request --recursive

Inspect data file (pre.py script)
Rows: 3409380 (mobile)/ 6936126 (fixed)
Columns: 11
Column names:
quadkey
tile
tile_x
tile_y
avg_d_kbps
avg_u_kbps
avg_lat_ms
avg_lat_down_ms
avg_lat_up_ms
tests
devices
