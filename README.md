# 🏠 Sydney Property Market Pulse

## Overview
End-to-end data analytics project analysing **4.7 million NSW property transactions** 
spanning 22 years (2001–2023) using Python, PostgreSQL, and Power BI.

## Business Questions Answered
- How have Sydney property prices trended over 22 years?
- Which councils have the highest median prices?
- Which councils saw the highest price growth (2013–2023)?
- How do house and unit prices compare over time?
- Which postcodes are the most expensive in Sydney?
- What seasonal patterns exist in the property market?

## Tech Stack
| Tool | Purpose |
|---|---|
| Python (Pandas, NumPy, Seaborn) | Data cleaning, EDA, exports |
| PostgreSQL | Data storage, analytical queries |
| Power BI | Interactive dashboard (5 pages) |
| Git | Version control |

## Dataset
- **Source:** NSW Valuer General via Kaggle
- **Size:** 4.7M+ transactions
- **Period:** 2001–2023
- **Coverage:** Greater Sydney, NSW

## Key Insights
- Sydney median property price grew **247%** from $244K (2001) to $850K (2023)
- **Woollahra** is Sydney's most expensive council at $2.55M median
- **2021 COVID surge** drove the sharpest single-year price jump (+$101K)
- Houses overtook units in price premium post-2021 lifestyle shift
- **December** consistently records the highest average transaction prices
- **Blacktown** leads in transaction volume — most active market

## Dashboard Pages
| Page | Content |
|---|---|
| 1 | Market Overview — price trend + volume |
| 2 | Council Analysis — top councils + growth |
| 3 | Property Type — house vs unit comparison |
| 4 | Postcode Heatmap — geographic price map |
| 5 | Seasonality — monthly and quarterly trends |

## How to Run
1. Clone the repo
2. Install dependencies: `pip install pandas numpy psycopg2-binary sqlalchemy matplotlib seaborn`
3. Set up PostgreSQL database named `property_pulse`
4. Run notebooks in order: 01 → 02 → 03 → 04
5. Open Power BI and connect to `reports/powerbi_data/` CSVs

## Author
**Vishal Aadiith Gunashekar**  
Master of Information Technology (AI) — UNSW Sydney  
[LinkedIn](https://linkedin.com/in/vishal-aadiith-gunshekar-38601323a) | [GitHub](https://github.com/VishalAadiith)
