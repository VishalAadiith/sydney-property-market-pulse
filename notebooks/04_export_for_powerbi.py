import pandas as pd
from sqlalchemy import create_engine
import os

os.makedirs('reports/powerbi_data', exist_ok=True)

engine = create_engine('postgresql://postgres:12345@localhost:5432/property_pulse')

# ── 1. Yearly Trend ────────────────────────────────────
q1 = """
SELECT year,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY purchase_price)) AS median_price,
    ROUND(AVG(purchase_price)) AS avg_price,
    COUNT(*) AS total_transactions
FROM sydney_properties
GROUP BY year ORDER BY year;
"""

# ── 2. Council Median Price (2018–2023) ────────────────
q2 = """
SELECT council_name,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY purchase_price)) AS median_price,
    COUNT(*) AS transactions
FROM sydney_properties
WHERE year >= 2018
GROUP BY council_name
ORDER BY median_price DESC;
"""

# ── 3. Price Growth 2013 vs 2023 ──────────────────────
q3 = """
SELECT a.council_name,
    ROUND(a.median_price) AS price_2013,
    ROUND(b.median_price) AS price_2023,
    ROUND(((b.median_price - a.median_price) / a.median_price) * 100) AS growth_pct
FROM
    (SELECT council_name,
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY purchase_price) AS median_price
     FROM sydney_properties WHERE year = 2013
     GROUP BY council_name) a
JOIN
    (SELECT council_name,
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY purchase_price) AS median_price
     FROM sydney_properties WHERE year = 2023
     GROUP BY council_name) b
ON a.council_name = b.council_name
WHERE a.median_price > 100000
ORDER BY growth_pct DESC;
"""

# ── 4. Quarterly Trend ─────────────────────────────────
q4 = """
SELECT year, quarter,
    COUNT(*) AS transactions,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY purchase_price)) AS median_price
FROM sydney_properties
GROUP BY year, quarter
ORDER BY year, quarter;
"""

# ── 5. House vs Unit ───────────────────────────────────
q5 = """
SELECT year, property_type,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY purchase_price)) AS median_price,
    COUNT(*) AS transactions
FROM sydney_properties
GROUP BY year, property_type
ORDER BY year, property_type;
"""

# ── 6. Postcode Heatmap ───────────────────────────────
q6 = """
SELECT post_code,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY purchase_price)) AS median_price,
    COUNT(*) AS transactions
FROM sydney_properties
WHERE year >= 2018
GROUP BY post_code
HAVING COUNT(*) >= 50
ORDER BY median_price DESC;
"""

# ── 7. Seasonal Analysis ──────────────────────────────
q7 = """
SELECT month,
    ROUND(AVG(purchase_price)) AS avg_price,
    COUNT(*) AS transactions
FROM sydney_properties
GROUP BY month
ORDER BY month;
"""

queries = {
    '01_yearly_trend': q1,
    '02_council_prices': q2,
    '03_price_growth': q3,
    '04_quarterly_trend': q4,
    '05_house_vs_unit': q5,
    '06_postcode_heatmap': q6,
    '07_seasonal': q7
}

for name, query in queries.items():
    print(f"Exporting {name}...")
    df = pd.read_sql(query, engine)
    df.to_csv(f'reports/powerbi_data/{name}.csv', index=False)
    print(f"✅ {name}.csv — {len(df)} rows")

print("\n✅ All exports done. Ready for Power BI!")