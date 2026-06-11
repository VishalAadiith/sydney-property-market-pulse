import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ── Load Data ──────────────────────────────────────────
print("Loading data...")
df = pd.read_csv('data/raw/nsw_property_data.csv')
print(f"Raw shape: {df.shape}")

# ── Drop useless columns ───────────────────────────────
drop_cols = ['strata_lot_number', 'property_name', 'zoning',
             'legal_description', 'download_date', 'area_type']
df.drop(columns=drop_cols, inplace=True)
print(f"After dropping columns: {df.shape}")

# ── Filter Sydney postcodes only (2000–2999) ───────────
df = df[df['post_code'].between(2000, 2999)]
print(f"After Sydney postcode filter: {df.shape}")

# ── Remove invalid prices ──────────────────────────────
df = df[df['purchase_price'] > 10000]
print(f"After price filter: {df.shape}")

# ── Convert dates ──────────────────────────────────────
df['contract_date'] = pd.to_datetime(df['contract_date'], errors='coerce')
df['settlement_date'] = pd.to_datetime(df['settlement_date'], errors='coerce')

# ── Extract year and month ─────────────────────────────
df['year'] = df['contract_date'].dt.year
df['month'] = df['contract_date'].dt.month
df['quarter'] = df['contract_date'].dt.quarter

# ── Filter valid years ─────────────────────────────────
df = df[df['year'].between(2001, 2023)]
print(f"After year filter: {df.shape}")

# ── Check result ───────────────────────────────────────
print("\nCleaned Data Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nSample:\n", df.head())

# ── Save cleaned data ──────────────────────────────────
df.to_csv('data/cleaned/sydney_property_cleaned.csv', index=False)
print("\n✅ Cleaned data saved to data/cleaned/sydney_property_cleaned.csv")