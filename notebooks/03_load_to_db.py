import pandas as pd
from sqlalchemy import create_engine
import time

# ── Database Connection ────────────────────────────────
engine = create_engine('postgresql://postgres:12345@localhost:5432/property_pulse')

# ── Load Cleaned Data ──────────────────────────────────
print("Loading cleaned CSV...")
df = pd.read_csv('data/cleaned/sydney_property_cleaned.csv')
print(f"Rows to load: {len(df):,}")

# ── Fix Data Types ─────────────────────────────────────
df['contract_date'] = pd.to_datetime(df['contract_date'], errors='coerce')
df['settlement_date'] = pd.to_datetime(df['settlement_date'], errors='coerce')
df['post_code'] = pd.to_numeric(df['post_code'], errors='coerce').astype('Int64')
df['year'] = pd.to_numeric(df['year'], errors='coerce').astype('Int64')
df['month'] = pd.to_numeric(df['month'], errors='coerce').astype('Int64')
df['quarter'] = pd.to_numeric(df['quarter'], errors='coerce').astype('Int64')
df['property_id'] = pd.to_numeric(df['property_id'], errors='coerce').astype('Int64')

# ── Load in Chunks (4.7M rows — do it in batches) ──────
print("Loading to PostgreSQL in chunks...")
start = time.time()

df.to_sql(
    'sydney_properties',
    engine,
    if_exists='append',
    index=False,
    chunksize=50000,
    method='multi'
)

end = time.time()
print(f"✅ Done! Loaded {len(df):,} rows in {round(end - start, 1)} seconds")