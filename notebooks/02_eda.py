import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('reports/figures', exist_ok=True)

# ── Load Cleaned Data ──────────────────────────────────
print("Loading cleaned data...")
df = pd.read_csv('data/cleaned/sydney_property_cleaned.csv')
print(f"Shape: {df.shape}")

# ── 1. Yearly Median Price Trend ───────────────────────
yearly = df.groupby('year')['purchase_price'].median().reset_index()
yearly.columns = ['year', 'median_price']

plt.figure(figsize=(12, 5))
sns.lineplot(data=yearly, x='year', y='median_price', marker='o', color='steelblue')
plt.title('Sydney Median Property Price Trend (2001–2023)')
plt.xlabel('Year')
plt.ylabel('Median Price (AUD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('reports/figures/01_yearly_price_trend.png')
plt.close()
print("✅ Saved: 01_yearly_price_trend.png")

# ── 2. Top 15 Councils by Median Price ────────────────
council_price = df.groupby('council_name')['purchase_price'].median().reset_index()
council_price = council_price.sort_values('purchase_price', ascending=False).head(15)

plt.figure(figsize=(12, 6))
sns.barplot(data=council_price, x='purchase_price', y='council_name', palette='Blues_r')
plt.title('Top 15 Sydney Councils by Median Property Price')
plt.xlabel('Median Price (AUD)')
plt.ylabel('Council')
plt.tight_layout()
plt.savefig('reports/figures/02_top_councils_price.png')
plt.close()
print("✅ Saved: 02_top_councils_price.png")

# ── 3. Transaction Volume by Year ──────────────────────
vol = df.groupby('year')['property_id'].count().reset_index()
vol.columns = ['year', 'transaction_count']

plt.figure(figsize=(12, 5))
sns.barplot(data=vol, x='year', y='transaction_count', color='coral')
plt.title('Sydney Property Transaction Volume by Year')
plt.xlabel('Year')
plt.ylabel('Number of Transactions')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('reports/figures/03_transaction_volume.png')
plt.close()
print("✅ Saved: 03_transaction_volume.png")

# ── 4. Property Type Distribution ─────────────────────
ptype = df['property_type'].value_counts().reset_index()
ptype.columns = ['property_type', 'count']

plt.figure(figsize=(8, 5))
sns.barplot(data=ptype, x='property_type', y='count', palette='Set2')
plt.title('Property Type Distribution')
plt.xlabel('Property Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('reports/figures/04_property_type.png')
plt.close()
print("✅ Saved: 04_property_type.png")

# ── 5. Price Distribution (capped at 5M) ──────────────
df_cap = df[df['purchase_price'] <= 5000000]

plt.figure(figsize=(12, 5))
sns.histplot(df_cap['purchase_price'], bins=50, color='steelblue', kde=True)
plt.title('Sydney Property Price Distribution (Up to $5M)')
plt.xlabel('Price (AUD)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('reports/figures/05_price_distribution.png')
plt.close()
print("✅ Saved: 05_price_distribution.png")

print("\n✅ All EDA charts saved to reports/figures/")
print("\nKey Stats:")
print(f"Total Transactions: {len(df):,}")
print(f"Median Price Overall: ${df['purchase_price'].median():,.0f}")
print(f"Mean Price Overall: ${df['purchase_price'].mean():,.0f}")
print(f"Most Common Property Type: {df['property_type'].mode()[0]}")
print(f"Top Council by Volume: {df['council_name'].value_counts().index[0]}")