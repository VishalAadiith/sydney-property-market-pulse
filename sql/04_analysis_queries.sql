-- ── 1. Yearly Median Price Trend ──────────────────────
SELECT
    year,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY purchase_price)) AS median_price,
    ROUND(AVG(purchase_price)) AS avg_price,
    COUNT(*) AS total_transactions
FROM sydney_properties
GROUP BY year
ORDER BY year;

-- ── 2. Top 10 Councils by Median Price (Last 5 Years) ──
SELECT
    council_name,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY purchase_price)) AS median_price,
    COUNT(*) AS transactions
FROM sydney_properties
WHERE year >= 2018
GROUP BY council_name
ORDER BY median_price DESC
LIMIT 10;

-- ── 3. Price Growth Rate by Council (2013 vs 2023) ────
SELECT
    a.council_name,
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
ORDER BY growth_pct DESC
LIMIT 15;

-- ── 4. Transaction Volume by Quarter ──────────────────
SELECT
    year,
    quarter,
    COUNT(*) AS transactions,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY purchase_price)) AS median_price
FROM sydney_properties
GROUP BY year, quarter
ORDER BY year, quarter;

-- ── 5. House vs Unit Price Comparison by Year ─────────
SELECT
    year,
    property_type,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY purchase_price)) AS median_price,
    COUNT(*) AS transactions
FROM sydney_properties
GROUP BY year, property_type
ORDER BY year, property_type;

-- ── 6. Postcode Level Median Price (Top 20) ───────────
SELECT
    post_code,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY purchase_price)) AS median_price,
    COUNT(*) AS transactions
FROM sydney_properties
WHERE year >= 2018
GROUP BY post_code
HAVING COUNT(*) >= 50
ORDER BY median_price DESC
LIMIT 20;

-- ── 7. Seasonal Analysis ──────────────────────────────
SELECT
    month,
    ROUND(AVG(purchase_price)) AS avg_price,
    COUNT(*) AS transactions
FROM sydney_properties
GROUP BY month
ORDER BY month;